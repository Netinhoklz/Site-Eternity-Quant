# Criação do Meu Site

A seguir, um breve relato dos **principais passos** que segui para desenvolver meu site, desde a **definição de estrutura** até a **implementação de CSS** e **paginação**.

---

## 1. Estrutura de Pastas

Organizei meu projeto em algumas **pastas** principais:


- **`index.html`** é a página inicial (Home).
- **Páginas adicionais**, como `servicos.html`, `previsao-demanda.html` e `ia-para-atendimento.html`, ficam na raiz ou dentro de subpastas, dependendo da sua preferência de organização.
- **`style/`** contém os arquivos CSS que dão estilo ao meu site.
- **`static/imagens/`** (ou apenas `imagens/`) guarda todos os arquivos de mídia (logos, banners, ícones, etc.).

---

## 2. Layout HTML

O layout de cada página segue **uma estrutura semelhante**:

1. **`<!DOCTYPE html>`**, `<head>` e `<body>` com meta tags essenciais.
2. **Header fixo** com um menu de navegação, contendo links para as páginas principais (`Início`, `Serviços`, `Projetos`, etc.).
3. **Seções** (`<section>` ou `<main>`) dividem o conteúdo em blocos: **hero**, **serviços**, **depoimentos**, **CTA** de contato, etc.
4. **Footer** (rodapé) com informações de contato, redes sociais e direitos reservados.

**Exemplo** de uma seção de destaque (hero) em HTML:

```html
<section class="hero-servicos">
  <div class="container hero-content">
    <div class="hero-text">
      <h2>IA para Atendimento</h2>
      <p>Transforme a forma como seus clientes interagem com sua empresa...</p>
      <div class="hero-buttons">
        <a href="#beneficios" class="primary-btn">Saiba Mais</a>
      </div>
    </div>
    <img src="/static/imagens/ia_chatbot.png" alt="Chatbot Inteligente">
  </div>
</section>
