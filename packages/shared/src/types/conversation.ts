export interface Conversation {
  id: string;
  createdAt: Date;
  updatedAt: Date;
  agentType: 'chat_agent' | 'doc_agent';
  title?: string;
}
