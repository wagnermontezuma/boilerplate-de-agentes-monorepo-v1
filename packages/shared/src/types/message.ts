export interface Message {
  id: string;
  conversationId: string;
  role: 'human' | 'ai';
  content: string;
  createdAt: Date;
  metadata?: Record<string, any>;
}
