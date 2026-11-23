# Fluxos n8n do site

Código-fonte dos fluxos no formato do n8n Workflow SDK (`@n8n/workflow-sdk`), igual ao que está publicado em https://n8n.srv1632946.hstgr.cloud.

| Arquivo | Fluxo no n8n | Webhook |
|---|---|---|
| `cadastro-site.sdk.js` | WizzyBots \| Cadastro do site → Leads do site (`Qs91yTaPgEyigVBq`) | `POST /webhook/wizzybots-cadastro-site` |
| `chat-nino.sdk.js` | WizzyBots_chat_v2_FINAL (`PFEymwvHxr39C7Ge`) | `POST /webhook/wizzy-bots-chat-bot-v2` |

- Data Tables: **Leads do site** (`Hlo5V8tGzyZYaYn6`) e **Conversas do chat** (`76QAys8CSjMqdiHz`).
- Planilha espelho: Leads_Data_Table_Wizzybots. Alertas por Gmail para chrisberenguer300@gmail.com.
- `cadastro-site-wizzybots.json` é a primeira versão do cadastro (sem planilha e sem alerta), mantida só como histórico.

Para alterar: editar o `.sdk.js`, validar e publicar pelo MCP do n8n (`validate_workflow` → `update_workflow` → `publish_workflow`). Credenciais (Gmail, Google Sheets, DeepSeek, OpenAI, Postgres) ficam no n8n, não aqui.
