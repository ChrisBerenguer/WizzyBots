import { workflow, node, trigger, ifElse } from '@n8n/workflow-sdk';

const webhook = trigger({
  type: 'n8n-nodes-base.webhook',
  version: 2.1,
  config: {
    name: 'Webhook do site',
    parameters: {
      httpMethod: 'POST',
      path: 'wizzybots-cadastro-site',
      responseMode: 'responseNode',
      options: { allowedOrigins: '*' }
    },
    position: [0, 0]
  }
});

const valida = node({
  type: 'n8n-nodes-base.code',
  version: 2,
  config: {
    name: 'Valida e limpa',
    parameters: {
      mode: 'runOnceForAllItems',
      language: 'javaScript',
      jsCode: `const b = ($input.first().json.body) || {};
const txt = (v, max = 200) => String(v == null ? '' : v).replace(/[<>]/g, '').replace(/\\s+/g, ' ').trim().slice(0, max);
const nome = txt(b.nome, 120);
const email = txt(b.email, 160).toLowerCase();
let dig = String(b.whatsapp || '').replace(/\\D/g, '');
if (dig && !dig.startsWith('55')) dig = '55' + dig;
const whatsapp = dig ? '+' + dig : '';
const erros = [];
if (nome.length < 2) erros.push('nome');
if (!/^[^\\s@]+@[^\\s@]+\\.[^\\s@]{2,}$/.test(email)) erros.push('email');
if (dig.length < 12 || dig.length > 13) erros.push('whatsapp');
if (b.consentimento !== true) erros.push('consentimento');
if (txt(b.website)) erros.push('spam');
const agora = new Date().toISOString();
const env = new Date(b.enviado_em);
const enviado_em = isNaN(env.getTime()) ? agora : env.toISOString();
return [{ json: { valido: erros.length === 0, erros, linha: {
  nome, email, whatsapp,
  empresa: txt(b.empresa, 120),
  interesse: txt(b.interesse, 80),
  consentimento: b.consentimento === true,
  origem: txt(b.origem, 40) || 'site',
  abertura: txt(b.abertura, 40),
  pagina: txt(b.pagina, 300),
  utm_source: txt(b.utm_source, 100),
  utm_medium: txt(b.utm_medium, 100),
  utm_campaign: txt(b.utm_campaign, 100),
  enviado_em, recebido_em: agora, status: 'novo'
} } }];`
    },
    position: [220, 0]
  }
});

const checa = ifElse({
  version: 2.3,
  config: {
    name: 'Dados válidos?',
    parameters: {
      conditions: {
        combinator: 'and',
        options: { caseSensitive: true, leftValue: '', typeValidation: 'strict', version: 2 },
        conditions: [{
          leftValue: '={{ $json.valido }}',
          rightValue: true,
          operator: { type: 'boolean', operation: 'true', singleValue: true }
        }]
      }
    },
    position: [440, 0]
  }
});

const monta = node({
  type: 'n8n-nodes-base.code',
  version: 2,
  config: {
    name: 'Monta a linha',
    parameters: {
      mode: 'runOnceForAllItems',
      language: 'javaScript',
      jsCode: 'return [{ json: $input.first().json.linha }];'
    },
    position: [660, -100]
  }
});

const grava = node({
  type: 'n8n-nodes-base.dataTable',
  version: 1.1,
  config: {
    name: 'Grava em Leads do site',
    parameters: {
      resource: 'row',
      operation: 'insert',
      dataTableId: { __rl: true, mode: 'id', value: 'Hlo5V8tGzyZYaYn6', cachedResultName: 'Leads do site' },
      columns: { mappingMode: 'autoMapInputData', value: {}, matchingColumns: [], schema: [] }
    },
    position: [880, -100]
  }
});

const ok = node({
  type: 'n8n-nodes-base.respondToWebhook',
  version: 1.5,
  config: {
    name: 'Responde OK',
    parameters: {
      respondWith: 'json',
      responseBody: '={{ { ok: true } }}',
      options: { responseCode: 200 }
    },
    position: [1100, -100]
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
      jsCode: `const r = $('Grava em Leads do site').first().json;
const cols = ['id','nome','email','whatsapp','empresa','interesse','consentimento','origem','abertura','pagina','utm_source','utm_medium','utm_campaign','enviado_em','recebido_em','status'];
const o = {};
for (const c of cols) o[c] = r[c] == null ? '' : (c === 'consentimento' ? (r[c] ? 'sim' : 'não') : String(r[c]));
return [{ json: o }];`
    },
    position: [1320, -100]
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
    position: [1540, -100]
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
      subject: "={{ 'Novo lead no site: ' + $('Linha da planilha').first().json.nome }}",
      emailType: 'html',
      message: `={{ (() => { const l = $('Linha da planilha').first().json; const tel = l.whatsapp.replace(/\\D/g, ''); return '<div style="font-family:Arial,sans-serif;font-size:15px;color:#222;line-height:1.5"><h2 style="margin:0 0 12px;color:#fd8925">Novo lead no site da WizzyBots</h2><table cellpadding="6" style="border-collapse:collapse"><tr><td><b>Nome</b></td><td>' + l.nome + '</td></tr><tr><td><b>E-mail</b></td><td><a href="mailto:' + l.email + '">' + l.email + '</a></td></tr><tr><td><b>WhatsApp</b></td><td><a href="https://wa.me/' + tel + '">' + l.whatsapp + '</a></td></tr><tr><td><b>Empresa</b></td><td>' + (l.empresa || '-') + '</td></tr><tr><td><b>Interesse</b></td><td>' + (l.interesse || '-') + '</td></tr><tr><td><b>Botão</b></td><td>' + (l.abertura || '-') + '</td></tr><tr><td><b>UTM</b></td><td>' + ([l.utm_source, l.utm_medium, l.utm_campaign].filter(Boolean).join(' / ') || '-') + '</td></tr><tr><td><b>Recebido</b></td><td>' + new Date(l.recebido_em).toLocaleString('pt-BR', { timeZone: 'America/Fortaleza' }) + '</td></tr></table><p style="margin-top:16px"><a href="https://docs.google.com/spreadsheets/d/1Uc-aqaoFZQ41raKaMTq5n9XAO43K1zknS31hamKvwXE/edit">Abrir planilha de leads</a></p></div>'; })() }}`,
      options: { appendAttribution: false, senderName: 'Site WizzyBots', replyTo: "={{ $('Linha da planilha').first().json.email }}" }
    },
    position: [1760, -100]
  }
});

const erro = node({
  type: 'n8n-nodes-base.respondToWebhook',
  version: 1.5,
  config: {
    name: 'Responde erro',
    parameters: {
      respondWith: 'json',
      responseBody: '={{ { ok: false, erros: $json.erros } }}',
      options: { responseCode: 400 }
    },
    position: [660, 120]
  }
});

export default workflow('wizzybots-cadastro-site', 'WizzyBots | Cadastro do site → Leads do site')
  .add(webhook)
  .to(valida)
  .to(checa
    .onTrue(monta.to(grava).to(ok).to(linhaPlanilha).to(planilha).to(alerta))
    .onFalse(erro));
