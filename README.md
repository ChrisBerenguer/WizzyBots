# WizzyBots Landing Page

Site institucional da WizzyBots, agência de automação e IA para PMEs.

## Stack

Um único `index.html` estático, sem build e sem CDN:

- HTML e CSS escritos à mão, com tokens em variáveis CSS (`:root`)
- Fontes hospedadas no próprio site (`assets/fonts`): Outfit nos títulos e Plus Jakarta Sans no texto
- Ícones Lucide já embutidos como SVG
- JavaScript puro: IntersectionObserver para animações de entrada, abas acessíveis por teclado e menu mobile
- Chat Nino ligado ao webhook do n8n (`wizzy-bots-chat-bot-v2`)

## Estrutura da página

| Âncora | Seção |
|---|---|
| `#home` | Hero com vídeo do mago-robô |
| (sem âncora) | Dor: o desperdício está no operacional |
| `#automacoes` | 6 automações do catálogo (bento) |
| `#servicos` | As 5 frentes de serviço (abas) |
| `#como-funciona` | Diagnóstico, Arquitetura, Implementação, Evolução |
| `#quem-somos` | História do nome e fundador |
| `#tecnologia` | Faixa de logos do stack (Simple Icons) |
| `#contato` | Agendar diagnóstico (Calendly) ou WhatsApp |

## Assets

```text
assets/
├── fonts/               # woff2 latin + latin-ext
├── hero.mp4             # vídeo desktop (~620 KB)
├── hero-mobile.mp4      # vídeo recortado para celular (~410 KB)
├── hero-poster*.jpg     # quadro inicial do vídeo
├── og.jpg               # imagem de compartilhamento 1200x630
└── *.webp               # mago 3D, foto do fundador, fundos
```

Os arquivos originais (vídeos em alta, renders, referências) continuam em `Site References/`.

## Rodar localmente

Abra o `index.html` no navegador ou use a extensão Live Server do VS Code.

O chat só responde se o n8n aceitar a origem da página (CORS). Abrindo direto do disco, ele cai na mensagem de erro com o botão de WhatsApp.

## Pendências

- Adicionar no rodapé as URLs reais de Instagram, YouTube e TikTok
- Trocar `og:image` por URL absoluta quando o domínio estiver definido
- Liberar o domínio do site no CORS do webhook do n8n

---

*"Tarefas tediosas nunca mais."*
