export interface Document {
  id: string;
  filename: string;
  status: 'uploaded' | 'processing' | 'completed' | 'error';
  createdAt: Date;
}
