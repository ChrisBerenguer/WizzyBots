# WizzyBots Landing Page

Site institucional da WizzyBots, agência de automação e IA para PMEs.

A copy segue o argumento do folder impresso (`harness/marketing/conteudo/2026-11-03-folder`): o estudo do MIT NANDA mostra que 95% dos projetos de IA não tiveram retorno mensurável, e a WizzyBots trabalha do lado oposto aos motivos que travaram esses projetos.

## Stack

Um único `index.html` estático, sem build e sem CDN:

- HTML e CSS escritos à mão, com tokens em variáveis CSS (`:root`)
- Fontes hospedadas no próprio site (`assets/fonts`): Outfit nos títulos e Plus Jakarta Sans no texto
- Ícones Lucide já embutidos como SVG
- JavaScript puro: IntersectionObserver para animações de entrada, abas com indicador deslizante, contagem do 95%, spotlight nos cards e o fluxo animado
- Vidro (glassmorphism) com fallback sólido em `prefers-reduced-transparency`; tudo fica estático em `prefers-reduced-motion`
- Chat Nino ligado ao webhook do n8n (`wizzy-bots-chat-bot-v2`)

## Estrutura da página

| Âncora | Seção |
|---|---|
| `#home` | Hero com vídeo do mago-robô |
| `#estudo` | Estudo MIT NANDA: 95% dos projetos de IA sem retorno e os 4 motivos (mesmo argumento do folder) |
| `#fluxo` | Fluxo de automação animado em loop (SVG + JS), com câmera que acompanha o pacote no celular |
| `#automacoes` | 6 automações do catálogo (bento) |
| `#servicos` | As 5 frentes de serviço (abas) |
| `#como-funciona` | O método do lado oposto: tarefa que mais custa, IA dentro do processo, número combinado antes, acompanhamento até se pagar |
| `#bastidor` | Bastidor de um projeto: a IA que aprende com quem usa |
| `#quem-somos` | História do nome e fundador |
| `#tecnologia` | Faixa de logos do stack (Simple Icons) |
| `#contato` | "O seu pode estar nos outros 5%": Agendar diagnóstico (Calendly) ou WhatsApp |

## Assets

```text
assets/
├── fonts/               # woff2 latin + latin-ext
├── hero.mp4             # vídeo desktop (~620 KB)
├── hero-mobile.mp4      # vídeo recortado para celular (~410 KB)
├── hero-poster*.jpg     # quadro inicial do vídeo
├── og.jpg               # imagem de compartilhamento 1200x630
├── foto-*.webp          # fotos do Unsplash (licença gratuita) dos cards
└── *.webp               # render do mago (saudação), foto do fundador, fundo
```

Os arquivos originais (vídeos em alta, renders, referências) continuam em `Site References/`.

`exports/` (fora do git) guarda o GIF e o MP4 do fluxo animado para uso em redes sociais.

## Rodar localmente

Abra o `index.html` no navegador ou use a extensão Live Server do VS Code.

O chat só responde se o n8n aceitar a origem da página (CORS). Abrindo direto do disco, ele cai na mensagem de erro com o botão de WhatsApp.

## Pendências

- Adicionar no rodapé as URLs reais de YouTube e TikTok
- Confirmar o domínio wizzybots.com.br (usado em canonical, og:image e dados estruturados)
- Liberar o domínio do site no CORS do webhook do n8n

---

*"Tarefas tediosas nunca mais."*
