---
# GEMINI.md: Guia de Desenvolvimento e Regras do Agente de IA

## 1. Visão Geral do Projeto

**Objetivo:** Este projeto é um boilerplate full-stack projetado para acelerar o desenvolvimento de aplicações de agentes de IA. O objetivo é reduzir o tempo de setup inicial em mais de 70%, fornecendo uma arquitetura robusta, escalável e fácil de usar, permitindo que as equipes de desenvolvimento foquem na lógica de negócios e na inovação dos agentes.

**Componentes Principais:**
- **Frontend:** Uma interface de chat moderna e responsiva construída com Next.js.
- **Backend:** Uma API de alta performance em Python (Litestar) para servir os agentes de IA.
- **Agente de Conversação:** Um agente de chat básico e funcional para interação imediata.
- **Agente de Documentação:** Um agente especializado que lê os documentos do projeto (prd.md, architecture.md) e extrai regras de negócio e tecnologia para popular este arquivo (`GEMINI.md`), mantendo a governança do projeto sempre atualizada.

## 2. Stack de Tecnologia Principal

- **Monorepo:** Nx
- **Linguagens:** TypeScript (~5.3), Python (~3.11)
- **Frontend:** Next.js (~14.1), React, Tailwind CSS
- **UI Components:** shadcn/ui
- **Gerenciamento de Estado (Frontend):** TanStack Query
- **Backend:** Litestar (~2.9)
- **Orquestração de IA:** LangChain, LangGraph
- **Observabilidade:** LangSmith
- **Banco de Dados:** PostgreSQL (~16)
- **Containerização:** Docker

## 3. Arquitetura e Padrões

- **Estilo Arquitetural:** Arquitetura Desacoplada via API REST.
- **Organização do Backend:** Padrão de Repositório para abstração da camada de dados.
- **Infraestrutura:** Infraestrutura como Código (IaC) com `docker-compose.yml`.
- **Estrutura do Projeto:** Monorepo com a seguinte organização:
  ```
  /
  ├── apps/
  │   ├── backend/
  │   └── frontend/
  ├── packages/
  │   ├── shared/      # Código compartilhado (tipos, etc.)
  │   └── ui/          # Componentes de UI reutilizáveis
  ├── docs/
  ├── GEMINI.md        # Arquivo de governança do agente (este arquivo)
  └── docker-compose.yml
  ```

## 4. Regras para o Agente de IA (Gemini)

1.  **Sistema Operacional:** O ambiente de desenvolvimento primário é **Windows**. Todos os comandos de shell, scripts e ferramentas devem ser 100% compatíveis com o `cmd.exe` ou `PowerShell` no Windows.
2.  **Fonte da Verdade:** Os documentos na pasta `/docs` (`prd.md`, `architecture.md`, `front-end-spec.md`) e este arquivo `GEMINI.md` são a fonte da verdade para as regras do projeto.
3.  **Atualização de Regras:** Ao ser solicitado, você deve usar o "Agente de Documentação" para ler os documentos da pasta `/docs` e extrair novas regras de negócio, requisitos ou decisões arquiteturais, atualizando este arquivo `GEMINI.md` de acordo.
4.  **Consistência de Código:** Mantenha o estilo e os padrões de código existentes. Para o backend, siga o padrão `Litestar` e `Pytest`. Para o frontend, siga os padrões de `Next.js`, `TypeScript` e `TanStack Query`.
5.  **Comandos Críticos:** Antes de executar qualquer comando que modifique arquivos (`write_file`, `replace`) ou o sistema (`run_shell_command`), explique o que o comando fará e qual o impacto esperado.
6.  **Ambiente de Desenvolvimento:** O ambiente de desenvolvimento é totalmente containerizado. O comando principal para iniciar toda a aplicação é `docker-compose up`.

---
