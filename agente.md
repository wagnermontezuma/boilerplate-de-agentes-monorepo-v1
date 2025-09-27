# agente.md

## Visão Geral do Projeto
- Boilerplate de agentes de IA com arquitetura desacoplada entre frontend Next.js e backend Litestar.
- Monorepo gerenciado por Nx com compartilhamento de tipos entre apps e pacotes.
- Experiência do desenvolvedor priorizada com suporte a Docker e LangSmith para observabilidade.

## Regras de Negócio Essenciais
1. O sistema deve oferecer uma experiência de chat capaz de iniciar conversas, enviar mensagens e receber respostas automáticas.
2. O Agente de Documentação deve aceitar uploads de arquivos Markdown para atualização contínua das regras deste documento.
3. Todo projeto derivado deve manter os padrões de qualidade e extensibilidade descritos nos artefatos oficiais do método BMad.

## Padrões Técnicos
- **Frontend:** Next.js 14 com TypeScript, gerenciamento de dados via TanStack Query e componentes shadcn/ui.
- **Backend:** Python 3.11 com Litestar expondo endpoints `/health`, `/conversations`, `/conversations/{conversationId}/messages` e `/documents`.
- **Compartilhamento:** Tipos TypeScript publicados em `packages/shared` (`Conversation`, `Message`, `Document`).
- **Infraestrutura:** Docker e docker-compose com serviços individuais para frontend e backend.
- **Observabilidade:** Integração prevista com LangSmith via variáveis de ambiente.

## Estrutura do Monorepo
```
boilerplate-agente-ia/
├── apps/
│   ├── backend/
│   └── frontend/
├── packages/
│   ├── shared/
│   └── ui/
├── docs/
├── .docker/
├── docker-compose.yml
├── agente.md
└── nx.json
```

## Convenções de Desenvolvimento
- Seguir padrões de código limpo em Python e TypeScript, mantendo tipagem estrita.
- Reutilizar componentes de UI compartilhados via `packages/ui` sempre que possível.
- Toda funcionalidade nova deve preservar os contratos de API documentados.
- Atualizar este arquivo sempre que novas regras ou integrações forem introduzidas.
