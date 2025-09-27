Product Requirements Document (PRD): Boilerplate de Agente de IA

1. Metas e Contexto
Metas:

Reduzir o tempo de setup inicial para novos projetos de agentes de IA em pelo menos 70%.

Tornar-se uma ferramenta open-source reconhecida e de alta qualidade na comunidade.

Fomentar uma comunidade de contribuidores e usuários.

Contexto:
A evolução acelerada do ecossistema de agentes de IA apresenta um desafio de engenharia significativo, e a complexidade na integração de ferramentas de ponta atrasa a inovação. Este boilerplate resolve esse problema fornecendo uma arquitetura padronizada e coesa que elimina o trabalho de configuração repetitivo, permitindo que as equipes se concentrem na construção de agentes de IA de alto valor.

2. Requisitos
Requisitos Funcionais (FR)

FR1: O boilerplate DEVE fornecer uma estrutura de monorepo executável contendo um frontend Next.js e um backend FastAPI.

FR2: O servidor backend DEVE expor um endpoint /health para verificação de status e um endpoint /chat para interação com o agente.

FR3: A aplicação frontend DEVE renderizar uma interface de chat capaz de enviar mensagens e exibir respostas do endpoint /chat.

FR4: O sistema DEVE incluir um agente de conversação básico e funcional (usando LangChain) que responde através do endpoint /chat.

FR5: O sistema DEVE incluir um "Agente de Documentação" pré-configurado, capaz de receber os documentos produzidos pelo método BMad (ex: prd.md, architecture.md) e, a partir deles, extrair e adicionar as regras de negócio e tecnologia do novo projeto ao arquivo agente.md, capacitando o desenvolvedor a continuar o desenvolvimento utilizando o método BMad.

FR6: O boilerplate DEVE fornecer um arquivo agente.md na raiz do projeto para servir como um repositório central de regras e padrões.

Requisitos Não-Funcionais (NFR)

NFR1: A aplicação full-stack completa DEVE ser executável localmente através de um único comando docker-compose up.

NFR2: Todas as interações com o agente de exemplo DEVEM ser rastreáveis no LangSmith, com a integração sendo configurável através de variáveis de ambiente (.env).

NFR3: O processo de setup inicial para um novo desenvolvedor, do git clone à aplicação em funcionamento, DEVE levar menos de 10 minutos.

NFR4: O boilerplate DEVE ser distribuído com um arquivo README.md abrangente, detalhando a configuração e o uso.

NFR5: O código do boilerplate DEVE seguir padrões de código limpo e moderno para Python e TypeScript, servindo como um exemplo de alta qualidade.

3. Metas de Design da Interface do Usuário
Visão Geral de UX:
A visão para a UX é uma interface limpa, minimalista e focada no desenvolvedor. Deve parecer uma ferramenta profissional, priorizando a clareza e a funcionalidade. A interface do MVP será focada em um paradigma de chat conversacional robusto. Contudo, a arquitetura do layout deve ser projetada de forma modular para acomodar futuros paradigmas de interação, como um visualizador de grafo ou uma interface de co-piloto, em versões futuras.

Paradigmas Chave de Interação:

Interface Conversacional: O paradigma principal é uma interface de chat para interação com os agentes.

Gerenciamento de Contexto: O usuário precisará de uma maneira clara de fornecer contexto aos agentes, como fazer o upload de documentos.

Feedback de Status: A interface deve fornecer feedback claro sobre o estado do agente.

Telas e Visões Principais:

Visão de Chat do Agente: A tela principal com o histórico da conversa e caixa de entrada.

Visão de Processamento de Documentos: Uma interface simples para carregar um documento e acionar o "Agente de Documentação".

Visão de Configurações: Uma tela mínima para ajudar o usuário a gerenciar as configurações do .env.

Acessibilidade:
O objetivo é a conformidade com o padrão WCAG AA.

Branding:
O branding será mínimo e neutro (temas claro/escuro simples) para facilitar a customização.

Plataformas-Alvo:
Web Responsivo, com foco principal na experiência em desktops.

4. Suposições Técnicas
Estrutura do Repositório: Monorepo, gerenciado com **Nx** para otimização de build e performance.

Justificativa: Um monorepo é a abordagem superior para simplificar o compartilhamento de código entre o frontend e o backend, proporcionando uma experiência de desenvolvimento unificada. **A migração para Nx garante um gerenciamento 7x mais rápido e DevTools superiores.**

Arquitetura de Serviço: Desacoplada com API REST

Justificativa: Uma arquitetura com um backend Python (**Litestar**) servindo uma API REST para um frontend (Next.js) desacoplado oferece máxima flexibilidade e uma clara separação de responsabilidades. **O uso do Litestar assegura performance 2x superior e melhor escalabilidade para serviços de IA.**

Stack de Tecnologia Principal:

Frontend: Next.js com TypeScript.

Backend: Python com **Litestar**.

Orquestração de IA: LangChain e LangGraph.

Observabilidade: LangSmith.

Data Fetching (Frontend): **TanStack Query** (em substituição ao SWR) para gerenciamento de estado de servidor.

Ambiente de Desenvolvimento: Docker.

Requisitos de Teste: Unidade + Integração

Justificativa: Para o MVP, focaremos em testes de unidade e integração para garantir uma base de qualidade sólida sem o custo de testes E2E completos na fase inicial.

## 5. Estrutura de Épicos
Épico 1: Fundação e Experiência Principal do Agente
Meta: Estabelecer a estrutura completa do monorepo, o ambiente Docker, e entregar a experiência de chat ponta-a-ponta com o agente de conversação básico, incluindo a integração de observabilidade com o LangSmith.

Estórias:

1.1: Configuração do Monorepo e Ambiente Docker: Como um Desenvolvedor, eu quero um monorepo pré-configurado com **Nx** e Docker Compose, para que eu possa configurar meu ambiente de desenvolvimento local completo com um único comando.

1.2: Backend API Mínimo com Health Check: Como um Desenvolvedor, eu quero um servidor backend **Litestar** mínimo com um endpoint /health, para que eu possa verificar que o backend está rodando corretamente.

1.3: Frontend Mínimo e Conexão com Backend: Como um Desenvolvedor, eu quero uma aplicação frontend Next.js mínima que consiga buscar dados do endpoint /health do backend, para que eu possa confirmar que a comunicação entre eles está funcionando.

1.4: Implementação da Interface de Chat: Como um Usuário, eu quero uma interface de chat básica com uma caixa de entrada e uma área de exibição de mensagens, para que eu possa interagir com o agente de IA.

1.5: Agente de Chat Básico e Endpoint /chat: Como um Usuário, eu quero que o backend tenha um endpoint /chat conectado a um agente "eco" simples da LangChain, para que minhas mensagens enviadas da UI recebam uma resposta básica.

1.6: Integração da Observabilidade com LangSmith: Como um Desenvolvedor, eu quero que todas as interações com o agente LangChain sejam automaticamente rastreadas no LangSmith, para que eu possa depurar e observar o comportamento do agente.

Épico 2: Agente de Documentação e Governança do Projeto
Meta: Implementar o "Agente de Documentação" avançado, que processa os artefatos do BMad para popular dinamicamente o arquivo agente.md. Isso cria a base de conhecimento fundamental para que, em versões futuras, o agente possa evoluir para também auxiliar na quebra de estórias e na geração de tarefas.

Estórias:

2.1: Estrutura do Arquivo agente.md e Parser Inicial: Como um Desenvolvedor, eu quero uma estrutura definida para o arquivo agente.md e um parser em Python que possa lê-lo, para que a aplicação tenha uma forma padronizada de entender as regras do projeto.

2.2: Interface e Endpoint para Upload de Documentos: Como um Usuário, eu quero um componente de UI e um endpoint no backend que me permitam fazer o upload de um documento, para que eu possa fornecer contexto para o Agente de Documentação.

2.3: Lógica do Agente para Extração de Regras: Como um Sistema, eu quero que o Agente de Documentação consiga ler um prd.md enviado e extrair dele as principais suposições técnicas e padrões, para que estas regras possam ser usadas para popular o arquivo de governança.

2.4: Atualização Dinâmica do agente.md: Como um Sistema, eu quero que o Agente de Documentação pegue as regras extraídas e atualize programaticamente o arquivo agente.md, para que a governança do projeto seja sincronizada com sua documentação.

Épico 3 (Pós-MVP): Ecossistema de Conectores
Meta: Expandir a utilidade e o valor do boilerplate implementando os conectores pré-configurados para as principais plataformas de chat e bancos de dados.

Estórias:

3.1: Criação de um Padrão de Conector Abstrato: Como um Desenvolvedor, eu quero um padrão de design claro e uma classe base para a criação de conectores, para que a adição de futuras integrações seja simples e consistente.

3.2: Implementação do Conector PostgreSQL: Como um Desenvolvedor, eu quero um conector pré-configurado para PostgreSQL, para que eu possa facilmente persistir dados para meu agente.

3.3: Implementação do Conector de Banco de Dados Vetorial: Como um Desenvolvedor, eu quero um conector pré-configurado para um banco de dados vetorial, para que eu possa começar a construir agentes com capacidades de RAG.

3.4: Implementação do Conector para Discord: Como um Desenvolvedor, eu quero um conector pré-configurado para bots do Discord, para que eu possa facilmente implantar meu agente em um servidor.

3.5: Implementação dos Conectores Adicionais: Como um Desenvolvedor, eu quero conectores pré-configurados para outras plataformas importantes como Slack, WhatsApp, Redis e MongoDB.