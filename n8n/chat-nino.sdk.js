import { workflow, node, trigger, ifElse, languageModel, memory, tool, fromAi } from '@n8n/workflow-sdk';

const LEADS = { __rl: true, mode: 'id', value: 'Hlo5V8tGzyZYaYn6', cachedResultName: 'Leads do site' };
const CONVERSAS = { __rl: true, mode: 'id', value: '76QAys8CSjMqdiHz', cachedResultName: 'Conversas do chat' };
const SESSAO = "={{ $('Code - Normalizar Entrada').first().json.session_id }}";

const webhook = trigger({
  type: 'n8n-nodes-base.webhook',
  version: 2.1,
  config: {
    name: 'Webhook - WizzyBots Chat',
    parameters: {
      httpMethod: 'POST',
      path: 'wizzy-bots-chat-bot-v2',
      responseMode: 'responseNode',
      options: { allowedOrigins: 'https://wizzybots.com.br, http://localhost:3000, http://127.0.0.1:3000, http://localhost:5173, http://127.0.0.1:5173' }
    },
    position: [0, 300]
  }
});

const normaliza = node({
  type: 'n8n-nodes-base.code',
  version: 2,
  config: {
    name: 'Code - Normalizar Entrada',
    parameters: {
      mode: 'runOnceForEachItem',
      language: 'javaScript',
      jsCode: `const body = $json.body || {};
const root = $json || {};
const message = body.message ?? body.user_message ?? body.text ?? body.chatInput ?? body.input ?? root.message ?? root.user_message ?? root.text ?? root.chatInput ?? root.input ?? '';
const session = body.sessionId ?? body.session_id ?? root.sessionId ?? root.session_id ?? ('session-' + Date.now());
return { json: {
  user_message: String(message).trim().slice(0, 1500),
  page: String(body.page || root.page || 'site-wizzybots').slice(0, 300),
  source: body.source || root.source || 'webchat',
  session_id: String(session).slice(0, 120),
  created_at: new Date().toISOString()
} };`
    },
    position: [220, 300]
  }
});

const temMensagem = ifElse({
  version: 2.3,
  config: {
    name: 'IF - Mensagem existe?',
    parameters: {
      conditions: {
        combinator: 'and',
        options: { caseSensitive: true, leftValue: '', typeValidation: 'strict', version: 2 },
        conditions: [{ leftValue: '={{ $json.user_message }}', rightValue: '', operator: { type: 'string', operation: 'notEmpty', singleValue: true } }]
      }
    },
    position: [440, 300]
  }
});

const vazia = node({
  type: 'n8n-nodes-base.set',
  version: 3.4,
  config: {
    name: 'Set - Resposta Mensagem Vazia',
    parameters: {
      assignments: { assignments: [
        { id: 'r1', name: 'reply', value: 'Oi! Parece que sua mensagem veio vazia. Me conta rapidamente: qual processo você gostaria de automatizar?', type: 'string' },
        { id: 'r2', name: 'status', value: 'empty_message', type: 'string' },
        { id: 'r3', name: 'agent', value: 'wizzybots-ai', type: 'string' },
        { id: 'r4', name: 'session_id', value: '={{ $json.session_id }}', type: 'string' }
      ] },
      options: {}
    },
    position: [700, 560]
  }
});

const moderacao = node({
  type: 'n8n-nodes-base.code',
  version: 2,
  config: {
    name: 'Code - Moderação Simples',
    parameters: {
      mode: 'runOnceForEachItem',
      language: 'javaScript',
      jsCode: `const message = String($json.user_message || '').toLowerCase();
const blockedTerms = ['senha','cartão de crédito','cartao de credito','cpf','cnpj','dados bancários','dados bancarios','token secreto','api key','apikey','chave privada'];
const hasSensitiveData = blockedTerms.some(term => message.includes(term));
return { json: { ...$json, blocked: hasSensitiveData, block_reason: hasSensitiveData ? 'possible_sensitive_data' : null } };`
    },
    position: [700, 200]
  }
});

const sensivel = ifElse({
  version: 2.3,
  config: {
    name: 'IF - Conteúdo Sensível?',
    parameters: {
      conditions: {
        combinator: 'and',
        options: { caseSensitive: true, leftValue: '', typeValidation: 'strict', version: 2 },
        conditions: [{ leftValue: '={{ $json.blocked }}', rightValue: true, operator: { type: 'boolean', operation: 'true', singleValue: true } }]
      }
    },
    position: [920, 200]
  }
});

const respostaSensivel = node({
  type: 'n8n-nodes-base.set',
  version: 3.4,
  config: {
    name: 'Set - Resposta Conteúdo Sensível',
    parameters: {
      assignments: { assignments: [
        { id: 's1', name: 'reply', value: 'Para sua segurança, não envie senhas, documentos, dados bancários ou informações sensíveis por aqui. Posso te ajudar explicando o processo de automação de forma segura.', type: 'string' },
        { id: 's2', name: 'status', value: 'blocked_sensitive_data', type: 'string' },
        { id: 's3', name: 'agent', value: 'wizzybots-ai', type: 'string' },
        { id: 's4', name: 'session_id', value: '={{ $json.session_id }}', type: 'string' }
      ] },
      options: {}
    },
    position: [1180, 0]
  }
});

const logCliente = node({
  type: 'n8n-nodes-base.dataTable',
  version: 1.1,
  config: {
    name: 'Grava mensagem do cliente',
    onError: 'continueRegularOutput',
    parameters: {
      resource: 'row',
      operation: 'insert',
      dataTableId: CONVERSAS,
      columns: {
        mappingMode: 'defineBelow',
        value: {
          session_id: '={{ $json.session_id }}',
          papel: 'cliente',
          mensagem: '={{ $json.user_message }}',
          pagina: '={{ $json.page }}',
          criado_em: '={{ $json.created_at }}'
        },
        matchingColumns: [],
        schema: [
          { id: 'session_id', displayName: 'session_id', required: false, defaultMatch: false, display: true, type: 'string', canBeUsedToMatch: true },
          { id: 'papel', displayName: 'papel', required: false, defaultMatch: false, display: true, type: 'string', canBeUsedToMatch: true },
          { id: 'mensagem', displayName: 'mensagem', required: false, defaultMatch: false, display: true, type: 'string', canBeUsedToMatch: true },
          { id: 'pagina', displayName: 'pagina', required: false, defaultMatch: false, display: true, type: 'string', canBeUsedToMatch: true },
          { id: 'criado_em', displayName: 'criado_em', required: false, defaultMatch: false, display: true, type: 'dateTime', canBeUsedToMatch: true }
        ]
      }
    },
    position: [1180, 300]
  }
});

const deepseek = languageModel({
  type: '@n8n/n8n-nodes-langchain.lmChatDeepSeek',
  version: 1,
  config: { name: 'DeepSeek Chat Model1', parameters: { model: 'deepseek-v4-pro', options: {} }, position: [1300, 620] }
});

const openai = languageModel({
  type: '@n8n/n8n-nodes-langchain.lmChatOpenAi',
  version: 1.3,
  config: {
    name: 'OpenAI Chat Model1',
    parameters: { model: { __rl: true, value: 'gpt-5.5-pro-2026-04-23', mode: 'list', cachedResultName: 'gpt-5.5-pro-2026-04-23' }, builtInTools: {}, options: {} },
    position: [1440, 620]
  }
});

const memoria = memory({
  type: '@n8n/n8n-nodes-langchain.memoryPostgresChat',
  version: 1.3,
  config: {
    name: 'Postgres Chat Memory1',
    parameters: { sessionIdType: 'customKey', sessionKey: SESSAO, contextWindowLength: 20 },
    position: [1580, 620]
  }
});

const salvarCadastro = tool({
  type: 'n8n-nodes-base.dataTableTool',
  version: 1.1,
  config: {
    name: 'salvar_cadastro',
    parameters: {
      resource: 'row',
      operation: 'upsert',
      dataTableId: LEADS,
      matchType: 'allConditions',
      filters: { conditions: [{ keyName: 'session_id', condition: 'eq', keyValue: SESSAO }] },
      columns: {
        mappingMode: 'defineBelow',
        value: {
          session_id: SESSAO,
          origem: 'chat',
          abertura: 'chat-nino',
          pagina: "={{ $('Code - Normalizar Entrada').first().json.page }}",
          recebido_em: '={{ $now.toISO() }}',
          nome: fromAi('nome', 'Nome do cliente. Vazio se ainda não informado.', 'string'),
          empresa: fromAi('empresa', 'Nome da empresa. Vazio se ainda não informado.', 'string'),
          segmento: fromAi('segmento', 'Tipo de negócio ou segmento. Vazio se ainda não informado.', 'string'),
          tamanho_empresa: fromAi('tamanho_empresa', 'Tamanho da empresa ou da operação (pessoas, unidades, volume). Vazio se ainda não informado.', 'string'),
          processos: fromAi('processos', 'Processos que tomam mais tempo da equipe, nas palavras do cliente. Vazio se ainda não informado.', 'string'),
          ferramentas: fromAi('ferramentas', 'IA, automação, CRM, ERP, chatbot ou ferramentas digitais que já usa. Vazio se ainda não informado.', 'string'),
          interesse: fromAi('interesse', 'Como a IA poderia ajudar o negócio a crescer, segundo o cliente. Vazio se ainda não informado.', 'string'),
          email: fromAi('email', 'E-mail do cliente. Vazio se ainda não informado.', 'string'),
          whatsapp: fromAi('whatsapp', 'WhatsApp do cliente com DDD. Vazio se ainda não informado.', 'string'),
          resumo: fromAi('resumo', 'Resumo curto da conversa até agora para a equipe de vendas: dor principal, contexto e oportunidade.', 'string')
        },
        matchingColumns: [],
        schema: [
          { id: 'session_id', displayName: 'session_id', required: false, defaultMatch: false, display: true, type: 'string', canBeUsedToMatch: true }, { id: 'origem', displayName: 'origem', required: false, defaultMatch: false, display: true, type: 'string', canBeUsedToMatch: true }, { id: 'abertura', displayName: 'abertura', required: false, defaultMatch: false, display: true, type: 'string', canBeUsedToMatch: true }, { id: 'pagina', displayName: 'pagina', required: false, defaultMatch: false, display: true, type: 'string', canBeUsedToMatch: true }, { id: 'recebido_em', displayName: 'recebido_em', required: false, defaultMatch: false, display: true, type: 'dateTime', canBeUsedToMatch: true },
          { id: 'nome', displayName: 'nome', required: false, defaultMatch: false, display: true, type: 'string', canBeUsedToMatch: true }, { id: 'empresa', displayName: 'empresa', required: false, defaultMatch: false, display: true, type: 'string', canBeUsedToMatch: true }, { id: 'segmento', displayName: 'segmento', required: false, defaultMatch: false, display: true, type: 'string', canBeUsedToMatch: true }, { id: 'tamanho_empresa', displayName: 'tamanho_empresa', required: false, defaultMatch: false, display: true, type: 'string', canBeUsedToMatch: true }, { id: 'processos', displayName: 'processos', required: false, defaultMatch: false, display: true, type: 'string', canBeUsedToMatch: true },
          { id: 'ferramentas', displayName: 'ferramentas', required: false, defaultMatch: false, display: true, type: 'string', canBeUsedToMatch: true }, { id: 'interesse', displayName: 'interesse', required: false, defaultMatch: false, display: true, type: 'string', canBeUsedToMatch: true }, { id: 'email', displayName: 'email', required: false, defaultMatch: false, display: true, type: 'string', canBeUsedToMatch: true }, { id: 'whatsapp', displayName: 'whatsapp', required: false, defaultMatch: false, display: true, type: 'string', canBeUsedToMatch: true }, { id: 'resumo', displayName: 'resumo', required: false, defaultMatch: false, display: true, type: 'string', canBeUsedToMatch: true }
        ]
      }
    },
    position: [1720, 620]
  }
});

const SYSTEM = `Você é Nino, assistente virtual da WizzyBots, empresa de automação inteligente, RPAs e Inteligência Artificial aplicada ao crescimento de negócios.

Responda sempre em português do Brasil, com tom consultivo, acolhedor, tecnológico e levemente mágico. Cada resposta tem no máximo 600 caracteres.

REGRAS
- Nunca use placeholders como [nome], [empresa] ou {nome}.
- Use o nome do cliente só depois que ele informar, exatamente como informou.
- Nunca invente informação do cliente. Antes de personalizar, confira se a informação apareceu na conversa.
- Nunca peça senhas, documentos pessoais, CPF, CNPJ, dados bancários ou informações sigilosas.
- Não envie links. Não ofereça agendamento por link nem WhatsApp da WizzyBots.

SUA MISSÃO
Conduzir uma conversa consultiva e, ao longo dela, preencher o cadastro do cliente. Faça no máximo duas perguntas por mensagem, na ordem que soar natural, e demonstre que entendeu a dor antes de seguir. Informações a coletar:
1. Nome do cliente.
2. Nome da empresa e tipo de negócio ou segmento.
3. Tamanho da empresa ou da operação.
4. Processos que tomam mais tempo da equipe.
5. Se já usa IA, automação, CRM, ERP, chatbot ou outras ferramentas digitais.
6. Como a IA poderia ajudar o negócio a crescer.
7. E-mail e WhatsApp com DDD, para a equipe da WizzyBots entrar em contato. Peça por último, explicando que é para um especialista retornar.

Conecte as respostas a soluções da WizzyBots quando fizer sentido: automação de atendimento, integração entre sistemas, agentes de IA, fluxos com n8n, RPAs, dashboards, análise de dados e redução de tarefas manuais. Use metáforas leves de magia e tecnologia, como "Não é magia, é tecnologia bem orquestrada.", sem exagero.

FERRAMENTA salvar_cadastro
- Sempre que o cliente trouxer uma informação nova da lista acima, chame salvar_cadastro antes de responder.
- Em toda chamada, envie TODOS os campos já conhecidos na conversa, não só o novo. Campo ainda não informado vai vazio. Nunca apague um campo que já foi informado.
- Atualize o campo resumo em toda chamada com um resumo curto para a equipe de vendas.
- Não comente com o cliente que está salvando dados.

ENCERRAMENTO
Quando nome, segmento, tamanho, processos, ferramentas, e-mail e WhatsApp estiverem preenchidos, chame salvar_cadastro uma última vez e responda agradecendo pelo nome e dizendo que em breve alguém da WizzyBots vai entrar em contato. Não faça mais perguntas depois disso. Se o cliente voltar a escrever, responda com gentileza e reforce que a equipe vai entrar em contato em breve.
Se o cliente pedir para falar com uma pessoa antes de terminar, peça só nome, e-mail e WhatsApp, salve e encerre do mesmo jeito.
Se o cliente não quiser deixar contato, respeite, não insista e diga que ele pode usar o botão "Entre em contato" do site quando quiser.`;

const agente = node({
  type: '@n8n/n8n-nodes-langchain.agent',
  version: 3.1,
  config: {
    name: 'AI Agent - Nino',
    parameters: {
      promptType: 'define',
      text: "={{ $('Code - Normalizar Entrada').first().json.user_message }}",
      needsFallback: true,
      options: { systemMessage: SYSTEM, maxIterations: 6 }
    },
    subnodes: { model: [deepseek, openai], memory: memoria, tools: [salvarCadastro] },
    position: [1420, 300]
  }
});

const saida = node({
  type: 'n8n-nodes-base.code',
  version: 2,
  config: {
    name: 'Code - Estruturar Saída Final',
    parameters: {
      mode: 'runOnceForEachItem',
      language: 'javaScript',
      jsCode: `const raw = String($json.output || $json.text || $json.reply || $json.response || '').trim();
const reply = raw.replace(/https?:\\/\\/\\S+/g, '').replace(/\\s{2,}/g, ' ').trim() || 'Desculpe, não consegui responder agora. Pode repetir?';
return { json: {
  reply,
  status: 'success',
  agent: 'wizzybots-ai',
  session_id: $('Code - Normalizar Entrada').first().json.session_id,
  cta: null
} };`
    },
    position: [1800, 300]
  }
});

const responde = node({
  type: 'n8n-nodes-base.respondToWebhook',
  version: 1.5,
  config: {
    name: 'Respond to Webhook - JSON',
    parameters: {
      respondWith: 'json',
      responseBody: "={{ { reply: $json.reply || 'Não consegui gerar uma resposta agora.', status: $json.status || 'success', agent: $json.agent || 'wizzybots-ai', session_id: $json.session_id || 'default-session', cta: $json.cta || null } }}",
      options: {
        responseCode: 200,
        responseHeaders: { entries: [
          { name: 'Access-Control-Allow-Origin', value: '*' },
          { name: 'Access-Control-Allow-Methods', value: 'POST, OPTIONS' },
          { name: 'Access-Control-Allow-Headers', value: 'Content-Type' }
        ] }
      }
    },
    position: [2020, 300]
  }
});

const logNino = node({
  type: 'n8n-nodes-base.dataTable',
  version: 1.1,
  config: {
    name: 'Grava resposta do Nino',
    onError: 'continueRegularOutput',
    parameters: {
      resource: 'row',
      operation: 'insert',
      dataTableId: CONVERSAS,
      columns: {
        mappingMode: 'defineBelow',
        value: {
          session_id: '={{ $json.session_id }}',
          papel: 'nino',
          mensagem: '={{ $json.reply }}',
          pagina: "={{ $('Code - Normalizar Entrada').first().json.page }}",
          criado_em: '={{ $now.toISO() }}'
        },
        matchingColumns: [],
        schema: [
          { id: 'session_id', displayName: 'session_id', required: false, defaultMatch: false, display: true, type: 'string', canBeUsedToMatch: true }, { id: 'papel', displayName: 'papel', required: false, defaultMatch: false, display: true, type: 'string', canBeUsedToMatch: true }, { id: 'mensagem', displayName: 'mensagem', required: false, defaultMatch: false, display: true, type: 'string', canBeUsedToMatch: true }, { id: 'pagina', displayName: 'pagina', required: false, defaultMatch: false, display: true, type: 'string', canBeUsedToMatch: true }, { id: 'criado_em', displayName: 'criado_em', required: false, defaultMatch: false, display: true, type: 'dateTime', canBeUsedToMatch: true }
        ]
      }
    },
    position: [2240, 300]
  }
});

const buscaLead = node({
  type: 'n8n-nodes-base.dataTable',
  version: 1.1,
  config: {
    name: 'Busca cadastro do chat',
    alwaysOutputData: true,
    onError: 'continueRegularOutput',
    parameters: {
      resource: 'row',
      operation: 'get',
      dataTableId: LEADS,
      matchType: 'allConditions',
      filters: { conditions: [{ keyName: 'session_id', condition: 'eq', keyValue: SESSAO }] },
      returnAll: false,
      limit: 1
    },
    position: [2460, 300]
  }
});

const avalia = node({
  type: 'n8n-nodes-base.code',
  version: 2,
  config: {
    name: 'Cadastro completo?',
    parameters: {
      mode: 'runOnceForAllItems',
      language: 'javaScript',
      jsCode: `const r = ($input.all().map(i => i.json).find(j => j && j.id)) || null;
if (!r) return [{ json: { alertar: false } }];
const t = v => String(v == null ? '' : v).replace(/[<>]/g, '').trim();
const email = t(r.email).toLowerCase();
let dig = t(r.whatsapp).replace(/\\D/g, '');
if (dig && !dig.startsWith('55') && dig.length <= 11) dig = '55' + dig;
const emailOk = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]{2,}$/.test(email);
const zapOk = dig.length >= 12 && dig.length <= 13;
const completo = !!(t(r.nome) && t(r.segmento) && t(r.tamanho_empresa) && t(r.processos) && t(r.ferramentas) && emailOk && zapOk);
return [{ json: { alertar: completo && r.alertado !== true, id: r.id, email, whatsapp: dig ? '+' + dig : '' } }];`
    },
    position: [2680, 300]
  }
});

const deveAlertar = ifElse({
  version: 2.3,
  config: {
    name: 'Alertar agora?',
    parameters: {
      conditions: {
        combinator: 'and',
        options: { caseSensitive: true, leftValue: '', typeValidation: 'strict', version: 2 },
        conditions: [{ leftValue: '={{ $json.alertar }}', rightValue: true, operator: { type: 'boolean', operation: 'true', singleValue: true } }]
      }
    },
    position: [2900, 300]
  }
});

const marca = node({
  type: 'n8n-nodes-base.dataTable',
  version: 1.1,
  config: {
    name: 'Marca lead como novo',
    parameters: {
      resource: 'row',
      operation: 'update',
      dataTableId: LEADS,
      matchType: 'allConditions',
      filters: { conditions: [{ keyName: 'id', condition: 'eq', keyValue: '={{ $json.id }}' }] },
      columns: {
        mappingMode: 'defineBelow',
        value: {
          status: 'novo',
          alertado: true,
          email: '={{ $json.email }}',
          whatsapp: '={{ $json.whatsapp }}'
        },
        matchingColumns: [],
        schema: [{ id: 'status', displayName: 'status', required: false, defaultMatch: false, display: true, type: 'string', canBeUsedToMatch: true }, { id: 'alertado', displayName: 'alertado', required: false, defaultMatch: false, display: true, type: 'boolean', canBeUsedToMatch: true }, { id: 'email', displayName: 'email', required: false, defaultMatch: false, display: true, type: 'string', canBeUsedToMatch: true }, { id: 'whatsapp', displayName: 'whatsapp', required: false, defaultMatch: false, display: true, type: 'string', canBeUsedToMatch: true }]
      }
    },
    position: [3120, 200]
  }
});

const linhaPlanilha = node({
  type: 'n8n-nodes-base.code',
  version: 2,
  config: {
    name: 'Linha da planilha',
    parameters: {
      mode: 'runOnceForAllItems',
      language: 'javaScript',
      jsCode: `const r = $input.first().json;
const cols = ['id','nome','email','whatsapp','empresa','interesse','consentimento','origem','abertura','pagina','utm_source','utm_medium','utm_campaign','enviado_em','recebido_em','status','segmento','tamanho_empresa','processos','ferramentas','resumo','session_id'];
const o = {};
for (const c of cols) o[c] = r[c] == null ? '' : (c === 'consentimento' ? (r[c] ? 'sim' : 'não') : String(r[c]));
return [{ json: o }];`
    },
    position: [3340, 200]
  }
});

const planilha = node({
  type: 'n8n-nodes-base.googleSheets',
  version: 4.7,
  config: {
    name: 'Copia para a planilha',
    onError: 'continueRegularOutput',
    parameters: {
      resource: 'sheet',
      operation: 'append',
      authentication: 'oAuth2',
      documentId: { __rl: true, mode: 'id', value: '1Uc-aqaoFZQ41raKaMTq5n9XAO43K1zknS31hamKvwXE', cachedResultName: 'Leads_Data_Table_Wizzybots' },
      sheetName: { __rl: true, mode: 'id', value: '0', cachedResultName: 'Página1' },
      columns: { mappingMode: 'autoMapInputData', value: {}, matchingColumns: [], schema: [] },
      options: { cellFormat: 'RAW', handlingExtraData: 'insertInNewColumn' }
    },
    position: [3560, 200]
  }
});

const alerta = node({
  type: 'n8n-nodes-base.gmail',
  version: 2.2,
  config: {
    name: 'Alerta por e-mail',
    onError: 'continueRegularOutput',
    parameters: {
      resource: 'message',
      operation: 'send',
      authentication: 'oAuth2',
      sendTo: 'chrisberenguer300@gmail.com',
      subject: "={{ 'Novo lead no chat: ' + $('Linha da planilha').first().json.nome }}",
      emailType: 'html',
      message: `={{ (() => { const l = $('Linha da planilha').first().json; const tel = l.whatsapp.replace(/\\D/g, ''); const row = (k, v) => '<tr><td style="vertical-align:top"><b>' + k + '</b></td><td>' + (v || '-') + '</td></tr>'; return '<div style="font-family:Arial,sans-serif;font-size:15px;color:#222;line-height:1.5"><h2 style="margin:0 0 12px;color:#fd8925">Novo lead pelo chat Nino</h2><table cellpadding="6" style="border-collapse:collapse">' + row('Nome', l.nome) + row('E-mail', '<a href="mailto:' + l.email + '">' + l.email + '</a>') + row('WhatsApp', '<a href="https://wa.me/' + tel + '">' + l.whatsapp + '</a>') + row('Empresa', l.empresa) + row('Segmento', l.segmento) + row('Tamanho', l.tamanho_empresa) + row('Processos que tomam tempo', l.processos) + row('Ferramentas atuais', l.ferramentas) + row('Como a IA ajudaria', l.interesse) + row('Resumo do Nino', l.resumo) + row('Sessão', l.session_id) + '</table><p style="margin-top:16px">A conversa completa está na tabela <b>Conversas do chat</b> do n8n (filtre pela sessão). <a href="https://docs.google.com/spreadsheets/d/1Uc-aqaoFZQ41raKaMTq5n9XAO43K1zknS31hamKvwXE/edit">Abrir planilha de leads</a></p></div>'; })() }}`,
      options: { appendAttribution: false, senderName: 'Chat Nino - WizzyBots', replyTo: "={{ $('Linha da planilha').first().json.email }}" }
    },
    position: [3780, 200]
  }
});

export default workflow('wizzybots-chat-nino', 'WizzyBots_chat_v2_FINAL')
  .add(webhook)
  .to(normaliza)
  .to(temMensagem
    .onTrue(moderacao.to(sensivel
      .onTrue(respostaSensivel.to(responde))
      .onFalse(logCliente.to(agente).to(saida).to(responde))))
    .onFalse(vazia.to(responde)))
  .add(responde)
  .to(logNino)
  .to(buscaLead)
  .to(avalia)
  .to(deveAlertar.onTrue(marca.to(linhaPlanilha).to(planilha).to(alerta)));
