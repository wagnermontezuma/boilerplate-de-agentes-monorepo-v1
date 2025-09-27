"""Backend application conforming to the documented API contract."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Dict, List, Literal, Optional, TypedDict
from uuid import uuid4

from litestar import Litestar, get, post
from litestar.datastructures import UploadFile
from litestar.exceptions import HTTPException
from litestar.params import Body

Timestamp = str


class ConversationPayload(TypedDict, total=False):
    """Payload accepted when creating a conversation."""

    agentType: Literal["chat_agent", "doc_agent"]
    title: Optional[str]


class ConversationResponse(TypedDict, total=False):
    """Response schema for a conversation."""

    id: str
    createdAt: Timestamp
    updatedAt: Timestamp
    agentType: Literal["chat_agent", "doc_agent"]
    title: Optional[str]


class NewMessagePayload(TypedDict):
    """Payload for sending a message to a conversation."""

    content: str


class MessageResponse(TypedDict, total=False):
    """Response schema for a message."""

    id: str
    conversationId: str
    role: Literal["human", "ai"]
    content: str
    createdAt: Timestamp
    metadata: Dict[str, object]


class DocumentResponse(TypedDict):
    """Response schema for an uploaded document."""

    id: str
    filename: str
    status: Literal["uploaded", "processing", "completed", "error"]
    createdAt: Timestamp


def _utcnow() -> datetime:
    return datetime.now(tz=timezone.utc)


def _iso_now() -> str:
    return _utcnow().isoformat()


conversations: Dict[str, ConversationResponse] = {}
conversation_messages: Dict[str, List[MessageResponse]] = {}
documents: Dict[str, DocumentResponse] = {}


@get("/health")
def health_check() -> dict[str, str]:
    """Health check endpoint required by the documentation."""

    return {"status": "ok"}


@post("/conversations")
def create_conversation(
    payload: Optional[ConversationPayload] = Body(default=None),
) -> ConversationResponse:
    """Create a new conversation with default metadata."""

    conversation_id = str(uuid4())
    now = _iso_now()
    agent_type = (payload or {}).get("agentType", "chat_agent")
    conversation: ConversationResponse = {
        "id": conversation_id,
        "createdAt": now,
        "updatedAt": now,
        "agentType": agent_type,
    }

    title = (payload or {}).get("title")
    if title:
        conversation["title"] = title

    conversations[conversation_id] = conversation
    conversation_messages[conversation_id] = []
    return conversation


@post("/conversations/{conversation_id}/messages")
def send_message(
    conversation_id: str,
    payload: NewMessagePayload,
) -> MessageResponse:
    """Accept a new user message and echo a simple AI response."""

    if conversation_id not in conversations:
        raise HTTPException(status_code=404, detail="Conversation not found.")

    now = _iso_now()
    human_message: MessageResponse = {
        "id": str(uuid4()),
        "conversationId": conversation_id,
        "role": "human",
        "content": payload["content"],
        "createdAt": now,
        "metadata": {},
    }
    conversation_messages[conversation_id].append(human_message)

    ai_message: MessageResponse = {
        "id": str(uuid4()),
        "conversationId": conversation_id,
        "role": "ai",
        "content": payload["content"],
        "createdAt": _iso_now(),
        "metadata": {"responseType": "echo"},
    }
    conversation_messages[conversation_id].append(ai_message)

    conversations[conversation_id]["updatedAt"] = now
    return ai_message


@post("/documents")
async def upload_document(file: UploadFile) -> DocumentResponse:
    """Register a document upload and return its metadata."""

    document_id = str(uuid4())
    document: DocumentResponse = {
        "id": document_id,
        "filename": file.filename or "untitled",
        "status": "uploaded",
        "createdAt": _iso_now(),
    }
    documents[document_id] = document
    return document


app = Litestar(route_handlers=[health_check, create_conversation, send_message, upload_document])
