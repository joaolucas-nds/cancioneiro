# WO 0027 — Organizar (frente de interface, I3), DEC-032 e versao 0.16.0

## Cabecalho

> **Tipo:** mista — CODIGO (`app/index.html`, `scripts/validate.py`) e registro (CHANGELOG, README, DECISIONS, IDEAS, ROADMAP, STATUS inteiro).
> **Config sugerida:** Sonnet · `/effort medium`. 54 edicoes literais e o STATUS inteiro, aplicados e testados pelo chat num clone de `50dc707`; cada arquivo tem hash de chegada.
> **Pre-requisito:** commit `50dc707`, branch `main`, sincronizada com `origin/main`. O `git status` mostra **so** o que o chat gravou: `M logs/2026-11-06.md`, `M meta/CONTEXT.md`, `M meta/specs/261106-organizar.md` e esta WO (`?? meta/workorders/...wo0027...`).
> **Base:** spec `meta/specs/261106-organizar.md`, com os tres pontos decididos pelo dono em 2026-11-06 (viram a DEC-032 nesta WO); a frente e a DEC-030.
> **Depende de:** WO 0026, ja aplicada (`36596e2`, wrap `be28a23`).
>
> **Arquivos — partida e chegada, os dois medidos pelo chat** (em LF; chegada = aplicar literalmente as edicoes abaixo):
>
> | arquivo | partida (sha1) | chegada (sha1) |
> |---|---|---|
> | `app/index.html` | `556b5557f59e6c8935e8473aefbe5d1d8e84f74a` | `781f4997ce536e18dbefcac8e88433f9c6de59d4` |
> | `scripts/validate.py` | `0f5a5be23f02018df89b58da09419501311fc716` | `4105ec178c3405eacadcf3e0fc8b0763562e41fa` |
> | `README.md` | `457aba7429ac2608ee1d9946e1c5f99afca32e41` | `9bf1ea484306a9003690d066b501ec2694476f71` |
> | `meta/CHANGELOG.md` | `90571f8f2cea09e2dbec2697bdbc46f58db7e8fd` | `6d4d0e197f88263d37f32b6a6bb7de0f7ba8159b` |
> | `meta/DECISIONS.md` | `273cb57faa24d151c81b984af2a8ba7dd568f1ea` | `2cf7a23a9e23651da2fa847dc85b4a4145a661a3` |
> | `meta/IDEAS.md` | `134cdd655332936685f9e188597a63f61b39e63d` | `8b79aad07d745461d3b755d07d36aa98172f9202` |
> | `meta/ROADMAP.md` | `ed7e8295b4546e2066e1d30dca79bf5c4c59d063` | `337d94523982a90ebf10b10cca89f2e9fafbd0b1` |
> | `meta/STATUS.md` | `113a7bee5d4ac7911be3b74475bf753842135c5e` | `8c330ae7be3ab8620eb0b37cbda7203749fd6643` |
> | `meta/specs/261106-organizar.md` | `7f55605d5aa2cffc951a99a163e5a7805b74ccc2` | `7f55605d5aa2cffc951a99a163e5a7805b74ccc2` (gravado pelo chat; só versiona) |
> | `meta/CONTEXT.md` | `3fcfb3be6b92c65b1dd45652182fb16f98f67859` | `3fcfb3be6b92c65b1dd45652182fb16f98f67859` (gravado pelo chat; só versiona) |
> | `logs/2026-11-06.md` | `edb9019689e88d919f5654e4ca7fd534318d1c4a` | `edb9019689e88d919f5654e4ca7fd534318d1c4a` (gravado pelo chat; só versiona) |
>
> **Ancora semantica:** se um trecho-ancora nao bater EXATAMENTE, PARE e reporte.
> **Idempotencia:** antes de cada edicao, procure o texto NOVO INTEIRO; se ja estiver la, PULE e diga no relatorio. Arquivo inteiro (E55): se o hash ja for o de chegada, PULE.
> **Ancoras lidas em:** cada ancora foi recortada pelo chat do arquivo de partida (`git show 50dc707:<arquivo>`; os tres do chat, depois de gravados) e conferida como ocorrendo **exatamente 1 vez** no estado em que a edicao e aplicada, na ordem abaixo. Ancora sempre de linha inteira.
> **Remocoes:** algumas edicoes tiram codigo sem pôr outro no lugar (o interruptor «editar»). Nelas, a ancora leva as linhas vizinhas e o texto novo e so as vizinhas: o texto novo inteiro so existe depois da remocao, e a idempotencia vale igual.
> **Canal dos meta neste ciclo = CODE:** esta WO e o registro. A spec, o CONTEXT e o log ja estao gravados pelo chat (DEC-010); a WO so os versiona.

---

## 1. Por que

Terceira entrega da frente de interface (i-048), pela spec da I3:

- **Sem o interruptor «editar»:** organizar vale sempre que o acervo tem copia guardada no navegador.
- **Arrastar pela alca ⋮⋮** na Lista, no album ou para outro, e para a lateral (um album, ou «+ Novo album» durante o arrastar), com a **SortableJS 1.15.7 embutida** (o `Sortable.min.js` do npm, sem mudanca, com a licenca MIT acima). Com filtro ligado, a faixa cai antes da proxima visivel.
- **O «⋯» de cada faixa** (linha, detalhe e cartao): Mover para…, Subir, Descer, Exportar .md, Exportar .json, Excluir…; `Alt+↑`/`Alt+↓`.
- **Varias de uma vez:** caixas, `Shift`+clique, caixa do album e a barra de lote (Mover, Exportar .json, Marcar usei, Excluir).
- **«Desfazer»** no aviso e `Ctrl+Z`, da ultima operacao. **Soltar um `.json` sobre um album** importa faixas nele.
- **`validate.py`:** a oitava checagem, o sha256 da biblioteca embutida.
- **DEC-032** registra os tres pontos decididos pelo dono e a biblioteca com o hash.

O app de chegada foi executado pelo chat no Chromium headless (`file://`): **15 de 15** criterios; os testes das entregas 1 a 3, da I1 e da I2 seguem em **15 de 15**, **25 de 25**, **19 de 19**, **14 de 14** e **15 de 15**; prova de vida no app de partida (reprova). Abrir 205 faixas: de 148 a 159 ms, ate cerca de 30 ms a mais que a 0.15.0 (o limite era 100); a Lista de 300 com alcas, cerca de 60 ms. `validate.py` exit=0 com `jsonschema`, `test_convert_br.py` e `test_convert_guides.py` OK. O chat olhou a tela a 1366 e a 390 px (menu, lote, arrastar, folha de baixo, selecao).

**Versao 0.16.0 nesta WO.** A conferencia de tela e do dono, depois do push.

## Edicao 0 — Conferencia de hash e de arvore

```
sha1sum app/index.html scripts/validate.py README.md meta/CHANGELOG.md meta/DECISIONS.md meta/IDEAS.md meta/ROADMAP.md meta/STATUS.md meta/specs/261106-organizar.md meta/CONTEXT.md logs/2026-11-06.md
GIT_OPTIONAL_LOCKS=0 git status --short
```

Os onze batem com a coluna **partida**; o `git status` mostra exatamente as quatro linhas do Pre-requisito. Qualquer outra coisa: **PARE e reporte**.

## Edicoes E01 a E55

Na ordem. **Todas as secoes de edicao tem o mesmo titulo, `### Exx — ...`**, inclusive a de arquivo inteiro.
Copie o que esta ENTRE as linhas de quatro crases, sem elas. **O bloco termina na linha de quatro crases, nunca
num titulo:** o CHANGELOG, a DECISIONS, a IDEAS e o STATUS trazem `## ` e `### ` dentro do bloco.

### E01 — app: sai o CSS do lugar do «editar» na barra — `app/index.html`

**Ancora, literal:**

````
  .bar-edit { display: flex; gap: 6px; flex-shrink: 0; }
````

**Texto novo, literal:**

````
  /* I3: o «editar» saiu da barra (DEC-030); organizar vive no «⋯» de cada faixa. */
````

### E02 — app: o celular nao esconde mais um .bar-edit que nao existe — `app/index.html`

**Ancora, literal:**

````
    .brand, .bar-space, .bar-edit, .search-wrap kbd, .btn-label { display: none; }
````

**Texto novo, literal:**

````
    .brand, .bar-space, .search-wrap kbd, .btn-label { display: none; }
````

### E03 — app: sai o CSS dos botoes do modo «editar» — `app/index.html`

**Ancora, literal:**

````
  .card-foot .edit-btn { border-style: dashed; }
  [data-role="edit-btn"][aria-pressed="true"] { background: var(--ink); color: var(--paper); border-color: var(--ink); }
````

**Texto novo, literal:**

````
  .card-foot .card-more { min-width: 36px; font-size: 15px; }   /* I3: o «⋯» do cartao, no lugar de ↑ ↓ mover excluir */
````

### E04 — app: o CSS da alca, da selecao, do menu da faixa e do lote — `app/index.html`

**Ancora, literal:**

````
    body.detail-open .toast { bottom: 84px; }
  }
````

**Texto novo, literal:**

````
    body.detail-open .toast { bottom: 84px; }
  }

  /* ---- Organizar (I3, DEC-030, DEC-032 — spec meta/specs/261106-organizar.md) ---- */
  .row { padding: 0 8px 0 6px; }
  .row-grip { flex: none; width: 20px; height: 32px; padding: 0; border: 0; background: transparent;
    color: var(--ink-soft); cursor: grab; letter-spacing: -2px; font-size: 13px; touch-action: none; }
  .row-grip:hover { color: var(--ink); }
  .row-sel { flex: none; display: inline-flex; align-items: center; cursor: pointer; }
  .row-sel input, .album-sel { margin: 0; width: 16px; height: 16px; cursor: pointer; accent-color: var(--ink); }
  .row-more { flex: none; width: 28px; height: 28px; padding: 0; font-size: 15px; }
  .row.selected { background: var(--paper-2); }
  .row-ghost { opacity: .35; }
  .row-drag { background: var(--paper); box-shadow: 0 10px 28px rgba(35,32,27,.22); border-radius: 8px; }
  body.dragging-track, body.dragging-track * { cursor: grabbing !important; user-select: none; }
  body.view-list .album-head { padding-left: 8px; }
  .album-sel { margin-left: 26px; }
  /* As tres colunas novas (alca, caixa, «⋯») empurram os cortes: o titulo
     segue com pelo menos 160 px. Ordem de saida: Idioma, BPM, Estado e, por
     ultimo, o texto da saude (a marca fica). */
  @container lista (max-width: 840px) { .row-lang { display: none; } }
  @container lista (max-width: 740px) { .row-bpm { display: none; } }
  @container lista (max-width: 672px) { .row-state { display: none; } }
  @container lista (max-width: 600px) { .row-health { width: 18px; } .row-health .ht { display: none; } }

  .side-new-li { display: none; }
  body.dragging-track .side-new-li { display: list-item; }
  .side-new { margin-top: 4px; border: 1px dashed var(--line) !important; color: var(--ink-soft); }
  .drop-hover, .file-target { background: #e5c9ba !important; outline: 2px dashed var(--ember); outline-offset: -2px; }
  .detail-body .card-more { display: none; }

  #track-pop { position: fixed; z-index: 40; width: 240px; }
  #track-pop .tm-row { display: flex; gap: 4px; }
  #track-pop .tm-row button { flex: 1; }
  #track-pop .kbd-hint { color: var(--ink-soft); font-size: 11px; margin-left: 6px; }
  #track-pop button:disabled { opacity: .45; cursor: default; }
  #track-pop .tm-danger { color: var(--ember); }
  .sheet-backdrop { position: fixed; inset: 0; z-index: 39; background: rgba(35,32,27,.35); }

  .batch { position: fixed; left: 50%; bottom: 20px; transform: translateX(-50%); z-index: 30; display: flex;
    align-items: center; gap: 8px; padding: 8px 8px 8px 14px; border-radius: 12px; background: var(--ink); color: var(--paper);
    box-shadow: 0 10px 28px rgba(35,32,27,.3); white-space: nowrap; }
  .batch-count { font-weight: 600; margin-right: 4px; }
  .batch button { height: 30px; padding: 0 10px; border: 1px solid var(--ink-soft); background: transparent; color: var(--paper); font-size: 12px; }
  .batch button:hover:not(:disabled) { border-color: var(--paper); color: var(--paper); }
  .batch button:disabled { opacity: .4; cursor: default; }
  .batch .batch-danger { background: var(--ember); border-color: var(--ember); color: #fff; }
  .batch .batch-x { border: 0; width: 30px; padding: 0; font-size: 16px; }
  body.has-batch .toast { bottom: 84px; }
  body.has-batch main { padding-bottom: 88px; }   /* a barra de lote nao cobre as ultimas linhas */
  .toast.has-action { pointer-events: auto; display: flex; align-items: center; gap: 12px; }
  .toast-btn { height: 26px; padding: 0 10px; border: 1px solid #e0703f; background: transparent; color: #e0703f; font-weight: 600; font-size: 12px; }
  .toast-btn:hover { border-color: #f09060; color: #f09060; }

  @media (max-width: 719px) {
    .row { grid-template-columns: auto minmax(0, 1fr) 44px; grid-template-areas: "g t u" "g m u"; padding-left: 2px; }
    .row-grip, .row-sel { grid-area: g; }
    .row-grip { width: 32px; height: 44px; font-size: 14px; }
    .row-sel { display: none; width: 44px; height: 44px; justify-content: center; }
    .row-sel input { width: 20px; height: 20px; }
    body.selecting .row-sel { display: inline-flex; }
    body.selecting .row-grip { display: none; }
    .row-more { display: none; }
    .row-health { width: auto; }
    .row-meta .row-health .ht { display: inline !important; }
    .album-sel { display: none; margin-left: 12px; }
    body.selecting .album-sel { display: inline-block; }
    #track-pop { left: 0 !important; right: 0; top: auto !important; bottom: 0; width: auto; border-radius: 16px 16px 0 0;
      padding: 8px 8px 20px; max-height: 80vh; overflow: auto; }
    #track-pop [role="menuitem"] { min-height: 52px; font-size: 15px; }
    #track-pop .kbd-hint { display: none; }
    .batch { left: 8px; right: 8px; bottom: 16px; transform: none; flex-wrap: wrap; white-space: normal; gap: 6px; }
    .batch-count { flex: 1 1 calc(100% - 56px); }   /* contagem e × na primeira linha; acoes na segunda */
    .batch .batch-x { order: 1; }
    .batch button:not(.batch-x) { order: 2; }
    .batch button { flex: 1; height: 44px; padding: 0 6px; font-size: 12px; white-space: nowrap; }
    .batch .batch-x { flex: 0 0 44px; }
    body.has-draft .batch { bottom: 84px; }
    body.has-batch .toast { bottom: 150px; }
    body.has-batch main { padding-bottom: 150px; }
    body.has-draft.has-batch main { padding-bottom: 220px; }
  }
````

### E05 — app: versao 0.16.0 — `app/index.html`

**Ancora, literal:**

````
    <span class="version" data-role="app-version">v0.15.0</span>
````

**Texto novo, literal:**

````
    <span class="version" data-role="app-version">v0.16.0</span>
````

### E06 — app: sai o lugar do «editar» na barra — `app/index.html`

**Ancora, literal:**

````
  </div>
  <div class="bar-edit" id="bar-edit"></div>
  <div class="pop-wrap">
````

**Texto novo, literal:**

````
  </div>
  <div class="pop-wrap">
````

### E07 — app: «Importar faixas…» no «⋯» da barra, sem «Ligar editar» — `app/index.html`

**Ancora, literal:**

````
      <button type="button" role="menuitem" class="mobile-only" id="menu-edit" hidden>Ligar editar</button>
      <button type="button" role="menuitem" class="mobile-only" id="menu-import-tracks" hidden>Importar faixas…</button>
````

**Texto novo, literal:**

````
      <button type="button" role="menuitem" id="menu-import-tracks" hidden>Importar faixas…</button>
````

### E08 — app: o «⋯» no alto do detalhe — `app/index.html`

**Ancora, literal:**

````
    <button type="button" class="dbtn" id="detail-next" aria-label="Próxima faixa">›</button>
````

**Texto novo, literal:**

````
    <button type="button" class="dbtn" id="detail-next" aria-label="Próxima faixa">›</button>
    <button type="button" class="dbtn" id="detail-more" aria-label="Ações desta faixa" aria-haspopup="menu" aria-expanded="false" aria-controls="track-pop">⋯</button>
````

### E09 — app: o menu da faixa e a barra de lote — `app/index.html`

**Ancora, literal:**

````
<div class="toast" id="toast"></div>
````

**Texto novo, literal:**

````
<div class="sheet-backdrop" id="track-backdrop" hidden></div>
<div class="pop" id="track-pop" role="menu" aria-labelledby="track-pop-title" hidden>
  <div class="pop-head" id="track-pop-title"></div>
  <button type="button" role="menuitem" id="tm-move">Mover para…</button>
  <div class="tm-row">
    <button type="button" role="menuitem" id="tm-up">Subir<span class="kbd-hint">Alt+↑</span></button>
    <button type="button" role="menuitem" id="tm-down">Descer<span class="kbd-hint">Alt+↓</span></button>
  </div>
  <div class="pop-sep"></div>
  <button type="button" role="menuitem" id="tm-md">Exportar .md</button>
  <button type="button" role="menuitem" id="tm-json">Exportar .json</button>
  <div class="pop-sep"></div>
  <button type="button" role="menuitem" class="mobile-only" id="tm-select">Selecionar várias…</button>
  <button type="button" role="menuitem" class="tm-danger" id="tm-delete">Excluir…</button>
  <p class="pop-note" id="tm-note" hidden>Para organizar, importe o .json: a cópia guardada é o rascunho.</p>
  <button type="button" role="menuitem" class="mobile-only" id="tm-cancel">Cancelar</button>
</div>
<div class="batch" id="batch" role="toolbar" aria-label="Ações em lote" hidden>
  <span class="batch-count" id="batch-count"></span>
  <button type="button" id="batch-move">Mover para…</button>
  <button type="button" id="batch-export">Exportar .json</button>
  <button type="button" id="batch-used">Marcar usei</button>
  <button type="button" class="batch-danger" id="batch-delete">Excluir…</button>
  <button type="button" class="batch-x" id="batch-clear" aria-label="Tirar a seleção">×</button>
</div>
<div class="toast" id="toast"></div>
````

### E10 — app: a SortableJS 1.15.7 embutida, antes do codigo do app — `app/index.html`

**Ancora, literal:**

````
<script>
````

**Texto novo, literal:**

````
<script id="lib-sortable">
/* SortableJS 1.15.7 (https://github.com/SortableJS/Sortable), embutida pela I3 (DEC-030, DEC-032).
   E o arquivo Sortable.min.js do pacote npm sortablejs@1.15.7, sem mudanca: o scripts/validate.py
   confere o sha256 dele (bf4241bc...). Trocar de versao e decisao, nao acidente.

MIT License

Copyright (c) 2019 All contributors to Sortable

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
*/
/* ---- SortableJS 1.15.7: da linha seguinte ate o fim deste script, o Sortable.min.js do npm sem mudanca ---- */
/*! Sortable 1.15.7 - MIT | git://github.com/SortableJS/Sortable.git */
!function(t,e){"object"==typeof exports&&"undefined"!=typeof module?module.exports=e():"function"==typeof define&&define.amd?define(e):(t=t||self).Sortable=e()}(this,function(){"use strict";function o(t,e){(null==e||e>t.length)&&(e=t.length);for(var n=0,o=Array(e);n<e;n++)o[n]=t[n];return o}function i(t,e,n){return(e=function(t){t=function(t,e){if("object"!=typeof t||!t)return t;var n=t[Symbol.toPrimitive];if(void 0===n)return("string"===e?String:Number)(t);e=n.call(t,e||"default");if("object"!=typeof e)return e;throw new TypeError("@@toPrimitive must return a primitive value.")}(t,"string");return"symbol"==typeof t?t:t+""}(e))in t?Object.defineProperty(t,e,{value:n,enumerable:!0,configurable:!0,writable:!0}):t[e]=n,t}function a(){return(a=Object.assign?Object.assign.bind():function(t){for(var e=1;e<arguments.length;e++){var n,o=arguments[e];for(n in o)!{}.hasOwnProperty.call(o,n)||(t[n]=o[n])}return t}).apply(null,arguments)}function r(e,t){var n,o=Object.keys(e);return Object.getOwnPropertySymbols&&(n=Object.getOwnPropertySymbols(e),t&&(n=n.filter(function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable})),o.push.apply(o,n)),o}function I(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?r(Object(n),!0).forEach(function(t){i(e,t,n[t])}):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):r(Object(n)).forEach(function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))})}return e}function l(t,e){if(null==t)return{};var n,o=function(t,e){if(null==t)return{};var n,o={};for(n in t)if({}.hasOwnProperty.call(t,n)){if(-1!==e.indexOf(n))continue;o[n]=t[n]}return o}(t,e);if(Object.getOwnPropertySymbols)for(var i=Object.getOwnPropertySymbols(t),r=0;r<i.length;r++)n=i[r],-1===e.indexOf(n)&&{}.propertyIsEnumerable.call(t,n)&&(o[n]=t[n]);return o}function e(t){return function(t){if(Array.isArray(t))return o(t)}(t)||function(t){if("undefined"!=typeof Symbol&&null!=t[Symbol.iterator]||null!=t["@@iterator"])return Array.from(t)}(t)||function(t,e){if(t){if("string"==typeof t)return o(t,e);var n={}.toString.call(t).slice(8,-1);return"Map"===(n="Object"===n&&t.constructor?t.constructor.name:n)||"Set"===n?Array.from(t):"Arguments"===n||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)?o(t,e):void 0}}(t)||function(){throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()}function s(t){return(s="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(t){return typeof t}:function(t){return t&&"function"==typeof Symbol&&t.constructor===Symbol&&t!==Symbol.prototype?"symbol":typeof t})(t)}function t(t){if("undefined"!=typeof window&&window.navigator)return!!navigator.userAgent.match(t)}var y=t(/(?:Trident.*rv[ :]?11\.|msie|iemobile|Windows Phone)/i),w=t(/Edge/i),c=t(/firefox/i),u=t(/safari/i)&&!t(/chrome/i)&&!t(/android/i),d=t(/iP(ad|od|hone)/i),n=t(/chrome/i)&&t(/android/i),h={capture:!1,passive:!1};function f(t,e,n){t.addEventListener(e,n,!y&&h)}function p(t,e,n){t.removeEventListener(e,n,!y&&h)}function g(t,e){if(e&&(">"===e[0]&&(e=e.substring(1)),t))try{if(t.matches)return t.matches(e);if(t.msMatchesSelector)return t.msMatchesSelector(e);if(t.webkitMatchesSelector)return t.webkitMatchesSelector(e)}catch(t){return}}function m(t){return t.host&&t!==document&&t.host.nodeType&&t.host!==t?t.host:t.parentNode}function P(t,e,n,o){if(t){n=n||document;do{if(null!=e&&(">"!==e[0]||t.parentNode===n)&&g(t,e)||o&&t===n)return t}while(t!==n&&(t=m(t)))}return null}var v,b=/\s+/g;function k(t,e,n){var o;t&&e&&(t.classList?t.classList[n?"add":"remove"](e):(o=(" "+t.className+" ").replace(b," ").replace(" "+e+" "," "),t.className=(o+(n?" "+e:"")).replace(b," ")))}function R(t,e,n){var o=t&&t.style;if(o){if(void 0===n)return document.defaultView&&document.defaultView.getComputedStyle?n=document.defaultView.getComputedStyle(t,""):t.currentStyle&&(n=t.currentStyle),void 0===e?n:n[e];o[e=!(e in o||-1!==e.indexOf("webkit"))?"-webkit-"+e:e]=n+("string"==typeof n?"":"px")}}function D(t,e){var n="";if("string"==typeof t)n=t;else do{var o=R(t,"transform")}while(o&&"none"!==o&&(n=o+" "+n),!e&&(t=t.parentNode));var i=window.DOMMatrix||window.WebKitCSSMatrix||window.CSSMatrix||window.MSCSSMatrix;return i&&new i(n)}function E(t,e,n){if(t){var o=t.getElementsByTagName(e),i=0,r=o.length;if(n)for(;i<r;i++)n(o[i],i);return o}return[]}function O(){var t=document.scrollingElement;return t||document.documentElement}function X(t,e,n,o,i){if(t.getBoundingClientRect||t===window){var r,a,l,s,c,u,d=t!==window&&t.parentNode&&t!==O()?(a=(r=t.getBoundingClientRect()).top,l=r.left,s=r.bottom,c=r.right,u=r.height,r.width):(l=a=0,s=window.innerHeight,c=window.innerWidth,u=window.innerHeight,window.innerWidth);if((e||n)&&t!==window&&(i=i||t.parentNode,!y))do{if(i&&i.getBoundingClientRect&&("none"!==R(i,"transform")||n&&"static"!==R(i,"position"))){var h=i.getBoundingClientRect();a-=h.top+parseInt(R(i,"border-top-width")),l-=h.left+parseInt(R(i,"border-left-width")),s=a+r.height,c=l+r.width;break}}while(i=i.parentNode);return o&&t!==window&&(o=(e=D(i||t))&&e.a,t=e&&e.d,e&&(s=(a/=t)+(u/=t),c=(l/=o)+(d/=o))),{top:a,left:l,bottom:s,right:c,width:d,height:u}}}function Y(t,e,n){for(var o=M(t,!0),i=X(t)[e];o;){var r=X(o)[n];if(!("top"===n||"left"===n?r<=i:i<=r))return o;if(o===O())break;o=M(o,!1)}return!1}function B(t,e,n,o){for(var i=0,r=0,a=t.children;r<a.length;){if("none"!==a[r].style.display&&a[r]!==Ht.ghost&&(o||a[r]!==Ht.dragged)&&P(a[r],n.draggable,t,!1)){if(i===e)return a[r];i++}r++}return null}function F(t,e){for(var n=t.lastElementChild;n&&(n===Ht.ghost||"none"===R(n,"display")||e&&!g(n,e));)n=n.previousElementSibling;return n||null}function j(t,e){var n=0;if(!t||!t.parentNode)return-1;for(;t=t.previousElementSibling;)"TEMPLATE"===t.nodeName.toUpperCase()||t===Ht.clone||e&&!g(t,e)||n++;return n}function S(t){var e=0,n=0,o=O();if(t)do{var i=D(t),r=i.a,i=i.d}while(e+=t.scrollLeft*r,n+=t.scrollTop*i,t!==o&&(t=t.parentNode));return[e,n]}function M(t,e){if(!t||!t.getBoundingClientRect)return O();var n=t,o=!1;do{if(n.clientWidth<n.scrollWidth||n.clientHeight<n.scrollHeight){var i=R(n);if(n.clientWidth<n.scrollWidth&&("auto"==i.overflowX||"scroll"==i.overflowX)||n.clientHeight<n.scrollHeight&&("auto"==i.overflowY||"scroll"==i.overflowY)){if(!n.getBoundingClientRect||n===document.body)return O();if(o||e)return n;o=!0}}}while(n=n.parentNode);return O()}function _(t,e){return Math.round(t.top)===Math.round(e.top)&&Math.round(t.left)===Math.round(e.left)&&Math.round(t.height)===Math.round(e.height)&&Math.round(t.width)===Math.round(e.width)}function C(e,n){return function(){var t;v||(1===(t=arguments).length?e.call(this,t[0]):e.apply(this,t),v=setTimeout(function(){v=void 0},n))}}function H(t,e,n){t.scrollLeft+=e,t.scrollTop+=n}function T(t){var e=window.Polymer,n=window.jQuery||window.Zepto;return e&&e.dom?e.dom(t).cloneNode(!0):n?n(t).clone(!0)[0]:t.cloneNode(!0)}function x(t,e){R(t,"position","absolute"),R(t,"top",e.top),R(t,"left",e.left),R(t,"width",e.width),R(t,"height",e.height)}function A(t){R(t,"position",""),R(t,"top",""),R(t,"left",""),R(t,"width",""),R(t,"height","")}function L(n,o,i){var r={};return Array.from(n.children).forEach(function(t){var e;P(t,o.draggable,n,!1)&&!t.animated&&t!==i&&(e=X(t),r.left=Math.min(null!==(t=r.left)&&void 0!==t?t:1/0,e.left),r.top=Math.min(null!==(t=r.top)&&void 0!==t?t:1/0,e.top),r.right=Math.max(null!==(t=r.right)&&void 0!==t?t:-1/0,e.right),r.bottom=Math.max(null!==(t=r.bottom)&&void 0!==t?t:-1/0,e.bottom))}),r.width=r.right-r.left,r.height=r.bottom-r.top,r.x=r.left,r.y=r.top,r}var K="Sortable"+(new Date).getTime();function N(){var e,o=[];return{captureAnimationState:function(){o=[],this.options.animation&&[].slice.call(this.el.children).forEach(function(t){var e,n;"none"!==R(t,"display")&&t!==Ht.ghost&&(o.push({target:t,rect:X(t)}),e=I({},o[o.length-1].rect),!t.thisAnimationDuration||(n=D(t,!0))&&(e.top-=n.f,e.left-=n.e),t.fromRect=e)})},addAnimationState:function(t){o.push(t)},removeAnimationState:function(t){o.splice(function(t,e){for(var n in t)if(t.hasOwnProperty(n))for(var o in e)if(e.hasOwnProperty(o)&&e[o]===t[n][o])return Number(n);return-1}(o,{target:t}),1)},animateAll:function(t){var c=this;if(!this.options.animation)return clearTimeout(e),void("function"==typeof t&&t());var u=!1,d=0;o.forEach(function(t){var e=0,n=t.target,o=n.fromRect,i=X(n),r=n.prevFromRect,a=n.prevToRect,l=t.rect,s=D(n,!0);s&&(i.top-=s.f,i.left-=s.e),n.toRect=i,n.thisAnimationDuration&&_(r,i)&&!_(o,i)&&(l.top-i.top)/(l.left-i.left)==(o.top-i.top)/(o.left-i.left)&&(t=l,s=r,r=a,a=c.options,e=Math.sqrt(Math.pow(s.top-t.top,2)+Math.pow(s.left-t.left,2))/Math.sqrt(Math.pow(s.top-r.top,2)+Math.pow(s.left-r.left,2))*a.animation),_(i,o)||(n.prevFromRect=o,n.prevToRect=i,e=e||c.options.animation,c.animate(n,l,i,e)),e&&(u=!0,d=Math.max(d,e),clearTimeout(n.animationResetTimer),n.animationResetTimer=setTimeout(function(){n.animationTime=0,n.prevFromRect=null,n.fromRect=null,n.prevToRect=null,n.thisAnimationDuration=null},e),n.thisAnimationDuration=e)}),clearTimeout(e),u?e=setTimeout(function(){"function"==typeof t&&t()},d):"function"==typeof t&&t(),o=[]},animate:function(t,e,n,o){var i,r;o&&(R(t,"transition",""),R(t,"transform",""),i=(r=D(this.el))&&r.a,r=r&&r.d,i=(e.left-n.left)/(i||1),r=(e.top-n.top)/(r||1),t.animatingX=!!i,t.animatingY=!!r,R(t,"transform","translate3d("+i+"px,"+r+"px,0)"),this.forRepaintDummy=t.offsetWidth,R(t,"transition","transform "+o+"ms"+(this.options.easing?" "+this.options.easing:"")),R(t,"transform","translate3d(0,0,0)"),"number"==typeof t.animated&&clearTimeout(t.animated),t.animated=setTimeout(function(){R(t,"transition",""),R(t,"transform",""),t.animated=!1,t.animatingX=!1,t.animatingY=!1},o))}}}var W=[],z={initializeByDefault:!0},G={mount:function(e){for(var t in z)!z.hasOwnProperty(t)||t in e||(e[t]=z[t]);W.forEach(function(t){if(t.pluginName===e.pluginName)throw"Sortable: Cannot mount plugin ".concat(e.pluginName," more than once")}),W.push(e)},pluginEvent:function(e,n,o){var t=this;this.eventCanceled=!1,o.cancel=function(){t.eventCanceled=!0};var i=e+"Global";W.forEach(function(t){n[t.pluginName]&&(n[t.pluginName][i]&&n[t.pluginName][i](I({sortable:n},o)),n.options[t.pluginName]&&n[t.pluginName][e]&&n[t.pluginName][e](I({sortable:n},o)))})},initializePlugins:function(n,o,i,t){for(var e in W.forEach(function(t){var e=t.pluginName;(n.options[e]||t.initializeByDefault)&&((t=new t(n,o,n.options)).sortable=n,t.options=n.options,n[e]=t,a(i,t.defaults))}),n.options){var r;n.options.hasOwnProperty(e)&&(void 0!==(r=this.modifyOption(n,e,n.options[e]))&&(n.options[e]=r))}},getEventProperties:function(e,n){var o={};return W.forEach(function(t){"function"==typeof t.eventProperties&&a(o,t.eventProperties.call(n[t.pluginName],e))}),o},modifyOption:function(e,n,o){var i;return W.forEach(function(t){e[t.pluginName]&&t.optionListeners&&"function"==typeof t.optionListeners[n]&&(i=t.optionListeners[n].call(e[t.pluginName],o))}),i}};function U(t){var e=t.sortable,n=t.rootEl,o=t.name,i=t.targetEl,r=t.cloneEl,a=t.toEl,l=t.fromEl,s=t.oldIndex,c=t.newIndex,u=t.oldDraggableIndex,d=t.newDraggableIndex,h=t.originalEvent,f=t.putSortable,p=t.extraEventProperties;if(e=e||n&&n[K]){var g,m=e.options,t="on"+o.charAt(0).toUpperCase()+o.substr(1);!window.CustomEvent||y||w?(g=document.createEvent("Event")).initEvent(o,!0,!0):g=new CustomEvent(o,{bubbles:!0,cancelable:!0}),g.to=a||n,g.from=l||n,g.item=i||n,g.clone=r,g.oldIndex=s,g.newIndex=c,g.oldDraggableIndex=u,g.newDraggableIndex=d,g.originalEvent=h,g.pullMode=f?f.lastPutMode:void 0;var v,b=I(I({},p),G.getEventProperties(o,e));for(v in b)g[v]=b[v];n&&n.dispatchEvent(g),m[t]&&m[t].call(e,g)}}function q(t,e){var n=(o=2<arguments.length&&void 0!==arguments[2]?arguments[2]:{}).evt,o=l(o,V);G.pluginEvent.bind(Ht)(t,e,I({dragEl:$,parentEl:Q,ghostEl:J,rootEl:tt,nextEl:et,lastDownEl:nt,cloneEl:ot,cloneHidden:it,dragStarted:vt,putSortable:ut,activeSortable:Ht.active,originalEvent:n,oldIndex:rt,oldDraggableIndex:lt,newIndex:at,newDraggableIndex:st,hideGhostForTarget:Yt,unhideGhostForTarget:Bt,cloneNowHidden:function(){it=!0},cloneNowShown:function(){it=!1},dispatchSortableEvent:function(t){Z({sortable:e,name:t,originalEvent:n})}},o))}var V=["evt"];function Z(t){U(I({putSortable:ut,cloneEl:ot,targetEl:$,rootEl:tt,oldIndex:rt,oldDraggableIndex:lt,newIndex:at,newDraggableIndex:st},t))}var $,Q,J,tt,et,nt,ot,it,rt,at,lt,st,ct,ut,dt,ht,ft,pt,gt,mt,vt,bt,yt,wt,Dt,Et=!1,St=!1,_t=[],Ct=!1,Tt=!1,xt=[],Ot=!1,Mt=[],At="undefined"!=typeof document,Nt=d,It=w||y?"cssFloat":"float",Pt=At&&!n&&!d&&"draggable"in document.createElement("div"),kt=function(){if(At){if(y)return!1;var t=document.createElement("x");return t.style.cssText="pointer-events:auto","auto"===t.style.pointerEvents}}(),Rt=function(t,e){var n=R(t),o=parseInt(n.width)-parseInt(n.paddingLeft)-parseInt(n.paddingRight)-parseInt(n.borderLeftWidth)-parseInt(n.borderRightWidth),i=B(t,0,e),r=B(t,1,e),a=i&&R(i),l=r&&R(r),s=a&&parseInt(a.marginLeft)+parseInt(a.marginRight)+X(i).width,t=l&&parseInt(l.marginLeft)+parseInt(l.marginRight)+X(r).width;if("flex"===n.display)return"column"===n.flexDirection||"column-reverse"===n.flexDirection?"vertical":"horizontal";if("grid"===n.display)return n.gridTemplateColumns.split(" ").length<=1?"vertical":"horizontal";if(i&&a.float&&"none"!==a.float){e="left"===a.float?"left":"right";return!r||"both"!==l.clear&&l.clear!==e?"horizontal":"vertical"}return i&&("block"===a.display||"flex"===a.display||"table"===a.display||"grid"===a.display||o<=s&&"none"===n[It]||r&&"none"===n[It]&&o<s+t)?"vertical":"horizontal"},Xt=function(t){function l(r,a){return function(t,e,n,o){var i=t.options.group.name&&e.options.group.name&&t.options.group.name===e.options.group.name;if(null==r&&(a||i))return!0;if(null==r||!1===r)return!1;if(a&&"clone"===r)return r;if("function"==typeof r)return l(r(t,e,n,o),a)(t,e,n,o);e=(a?t:e).options.group.name;return!0===r||"string"==typeof r&&r===e||r.join&&-1<r.indexOf(e)}}var e={},n=t.group;n&&"object"==s(n)||(n={name:n}),e.name=n.name,e.checkPull=l(n.pull,!0),e.checkPut=l(n.put),e.revertClone=n.revertClone,t.group=e},Yt=function(){!kt&&J&&R(J,"display","none")},Bt=function(){!kt&&J&&R(J,"display","")};At&&!n&&document.addEventListener("click",function(t){if(St)return t.preventDefault(),t.stopPropagation&&t.stopPropagation(),t.stopImmediatePropagation&&t.stopImmediatePropagation(),St=!1},!0);function Ft(t){if($){t=t.touches?t.touches[0]:t;var e=(i=t.clientX,r=t.clientY,_t.some(function(t){var e=t[K].options.emptyInsertThreshold;if(e&&!F(t)){var n=X(t),o=i>=n.left-e&&i<=n.right+e,e=r>=n.top-e&&r<=n.bottom+e;return o&&e?a=t:void 0}}),a);if(e){var n,o={};for(n in t)t.hasOwnProperty(n)&&(o[n]=t[n]);o.target=o.rootEl=e,o.preventDefault=void 0,o.stopPropagation=void 0,e[K]._onDragOver(o)}}var i,r,a}function jt(t){$&&$.parentNode[K]._isOutsideThisEl(t.target)}function Ht(t,e){if(!t||!t.nodeType||1!==t.nodeType)throw"Sortable: `el` must be an HTMLElement, not ".concat({}.toString.call(t));this.el=t,this.options=e=a({},e),t[K]=this;var n,o,i={group:null,sort:!0,disabled:!1,store:null,handle:null,draggable:/^[uo]l$/i.test(t.nodeName)?">li":">*",swapThreshold:1,invertSwap:!1,invertedSwapThreshold:null,removeCloneOnHide:!0,direction:function(){return Rt(t,this.options)},ghostClass:"sortable-ghost",chosenClass:"sortable-chosen",dragClass:"sortable-drag",ignore:"a, img",filter:null,preventOnFilter:!0,animation:0,easing:null,setData:function(t,e){t.setData("Text",e.textContent)},dropBubble:!1,dragoverBubble:!1,dataIdAttr:"data-id",delay:0,delayOnTouchOnly:!1,touchStartThreshold:(Number.parseInt?Number:window).parseInt(window.devicePixelRatio,10)||1,forceFallback:!1,fallbackClass:"sortable-fallback",fallbackOnBody:!1,fallbackTolerance:0,fallbackOffset:{x:0,y:0},supportPointer:!1!==Ht.supportPointer&&"PointerEvent"in window&&(!u||d),emptyInsertThreshold:5};for(n in G.initializePlugins(this,t,i),i)n in e||(e[n]=i[n]);for(o in Xt(e),this)"_"===o.charAt(0)&&"function"==typeof this[o]&&(this[o]=this[o].bind(this));this.nativeDraggable=!e.forceFallback&&Pt,this.nativeDraggable&&(this.options.touchStartThreshold=1),e.supportPointer?f(t,"pointerdown",this._onTapStart):(f(t,"mousedown",this._onTapStart),f(t,"touchstart",this._onTapStart)),this.nativeDraggable&&(f(t,"dragover",this),f(t,"dragenter",this)),_t.push(this.el),e.store&&e.store.get&&this.sort(e.store.get(this)||[]),a(this,N())}function Lt(t,e,n,o,i,r,a,l){var s,c,u=t[K],d=u.options.onMove;return!window.CustomEvent||y||w?(s=document.createEvent("Event")).initEvent("move",!0,!0):s=new CustomEvent("move",{bubbles:!0,cancelable:!0}),s.to=e,s.from=t,s.dragged=n,s.draggedRect=o,s.related=i||e,s.relatedRect=r||X(e),s.willInsertAfter=l,s.originalEvent=a,t.dispatchEvent(s),c=d?d.call(u,s,a):c}function Kt(t){t.draggable=!1}function Wt(){Ot=!1}function zt(t){return setTimeout(t,0)}function Gt(t){return clearTimeout(t)}Ht.prototype={constructor:Ht,_isOutsideThisEl:function(t){this.el.contains(t)||t===this.el||(bt=null)},_getDirection:function(t,e){return"function"==typeof this.options.direction?this.options.direction.call(this,t,e,$):this.options.direction},_onTapStart:function(e){if(e.cancelable){var n=this,o=this.el,t=this.options,i=t.preventOnFilter,r=e.type,a=e.touches&&e.touches[0]||e.pointerType&&"touch"===e.pointerType&&e,l=(a||e).target,s=e.target.shadowRoot&&(e.path&&e.path[0]||e.composedPath&&e.composedPath()[0])||l,c=t.filter;if(!function(t){Mt.length=0;var e=t.getElementsByTagName("input"),n=e.length;for(;n--;){var o=e[n];o.checked&&Mt.push(o)}}(o),!$&&!(/mousedown|pointerdown/.test(r)&&0!==e.button||t.disabled)&&!s.isContentEditable&&(this.nativeDraggable||!u||!l||"SELECT"!==l.tagName.toUpperCase())&&!((l=P(l,t.draggable,o,!1))&&l.animated||nt===l)){if(rt=j(l),lt=j(l,t.draggable),"function"==typeof c){if(c.call(this,e,l,this))return Z({sortable:n,rootEl:s,name:"filter",targetEl:l,toEl:o,fromEl:o}),q("filter",n,{evt:e}),void(i&&e.preventDefault())}else if(c=c&&c.split(",").some(function(t){if(t=P(s,t.trim(),o,!1))return Z({sortable:n,rootEl:t,name:"filter",targetEl:l,fromEl:o,toEl:o}),q("filter",n,{evt:e}),!0}))return void(i&&e.preventDefault());t.handle&&!P(s,t.handle,o,!1)||this._prepareDragStart(e,a,l)}}},_prepareDragStart:function(t,e,n){var o,i=this,r=i.el,a=i.options,l=r.ownerDocument;n&&!$&&n.parentNode===r&&(o=X(n),tt=r,Q=($=n).parentNode,et=$.nextSibling,nt=n,ct=a.group,dt={target:Ht.dragged=$,clientX:(e||t).clientX,clientY:(e||t).clientY},gt=dt.clientX-o.left,mt=dt.clientY-o.top,this._lastX=(e||t).clientX,this._lastY=(e||t).clientY,$.style["will-change"]="all",o=function(){q("delayEnded",i,{evt:t}),Ht.eventCanceled?i._onDrop():(i._disableDelayedDragEvents(),!c&&i.nativeDraggable&&($.draggable=!0),i._triggerDragStart(t,e),Z({sortable:i,name:"choose",originalEvent:t}),k($,a.chosenClass,!0))},a.ignore.split(",").forEach(function(t){E($,t.trim(),Kt)}),f(l,"dragover",Ft),f(l,"mousemove",Ft),f(l,"touchmove",Ft),a.supportPointer?(f(l,"pointerup",i._onDrop),this.nativeDraggable||f(l,"pointercancel",i._onDrop)):(f(l,"mouseup",i._onDrop),f(l,"touchend",i._onDrop),f(l,"touchcancel",i._onDrop)),c&&this.nativeDraggable&&(this.options.touchStartThreshold=4,$.draggable=!0),q("delayStart",this,{evt:t}),!a.delay||a.delayOnTouchOnly&&!e||this.nativeDraggable&&(w||y)?o():Ht.eventCanceled?this._onDrop():(a.supportPointer?(f(l,"pointerup",i._disableDelayedDrag),f(l,"pointercancel",i._disableDelayedDrag)):(f(l,"mouseup",i._disableDelayedDrag),f(l,"touchend",i._disableDelayedDrag),f(l,"touchcancel",i._disableDelayedDrag)),f(l,"mousemove",i._delayedDragTouchMoveHandler),f(l,"touchmove",i._delayedDragTouchMoveHandler),a.supportPointer&&f(l,"pointermove",i._delayedDragTouchMoveHandler),i._dragStartTimer=setTimeout(o,a.delay)))},_delayedDragTouchMoveHandler:function(t){t=t.touches?t.touches[0]:t;Math.max(Math.abs(t.clientX-this._lastX),Math.abs(t.clientY-this._lastY))>=Math.floor(this.options.touchStartThreshold/(this.nativeDraggable&&window.devicePixelRatio||1))&&this._disableDelayedDrag()},_disableDelayedDrag:function(){$&&Kt($),clearTimeout(this._dragStartTimer),this._disableDelayedDragEvents()},_disableDelayedDragEvents:function(){var t=this.el.ownerDocument;p(t,"mouseup",this._disableDelayedDrag),p(t,"touchend",this._disableDelayedDrag),p(t,"touchcancel",this._disableDelayedDrag),p(t,"pointerup",this._disableDelayedDrag),p(t,"pointercancel",this._disableDelayedDrag),p(t,"mousemove",this._delayedDragTouchMoveHandler),p(t,"touchmove",this._delayedDragTouchMoveHandler),p(t,"pointermove",this._delayedDragTouchMoveHandler)},_triggerDragStart:function(t,e){e=e||"touch"==t.pointerType&&t,!this.nativeDraggable||e?this.options.supportPointer?f(document,"pointermove",this._onTouchMove):f(document,e?"touchmove":"mousemove",this._onTouchMove):(f($,"dragend",this),f(tt,"dragstart",this._onDragStart));try{document.selection?zt(function(){document.selection.empty()}):window.getSelection().removeAllRanges()}catch(t){}},_dragStarted:function(t,e){var n;Et=!1,tt&&$?(q("dragStarted",this,{evt:e}),this.nativeDraggable&&f(document,"dragover",jt),n=this.options,t||k($,n.dragClass,!1),k($,n.ghostClass,!0),Ht.active=this,t&&this._appendGhost(),Z({sortable:this,name:"start",originalEvent:e})):this._nulling()},_emulateDragOver:function(){if(ht){this._lastX=ht.clientX,this._lastY=ht.clientY,Yt();for(var t=document.elementFromPoint(ht.clientX,ht.clientY),e=t;t&&t.shadowRoot&&(t=t.shadowRoot.elementFromPoint(ht.clientX,ht.clientY))!==e;)e=t;if($.parentNode[K]._isOutsideThisEl(t),e)do{if(e[K])if(e[K]._onDragOver({clientX:ht.clientX,clientY:ht.clientY,target:t,rootEl:e})&&!this.options.dragoverBubble)break}while(e=m(t=e));Bt()}},_onTouchMove:function(t){if(dt){var e=this.options,n=e.fallbackTolerance,o=e.fallbackOffset,i=t.touches?t.touches[0]:t,r=J&&D(J,!0),a=J&&r&&r.a,l=J&&r&&r.d,e=Nt&&Dt&&S(Dt),a=(i.clientX-dt.clientX+o.x)/(a||1)+(e?e[0]-xt[0]:0)/(a||1),l=(i.clientY-dt.clientY+o.y)/(l||1)+(e?e[1]-xt[1]:0)/(l||1);if(!Ht.active&&!Et){if(n&&Math.max(Math.abs(i.clientX-this._lastX),Math.abs(i.clientY-this._lastY))<n)return;this._onDragStart(t,!0)}J&&(r?(r.e+=a-(ft||0),r.f+=l-(pt||0)):r={a:1,b:0,c:0,d:1,e:a,f:l},r="matrix(".concat(r.a,",").concat(r.b,",").concat(r.c,",").concat(r.d,",").concat(r.e,",").concat(r.f,")"),R(J,"webkitTransform",r),R(J,"mozTransform",r),R(J,"msTransform",r),R(J,"transform",r),ft=a,pt=l,ht=i),t.cancelable&&t.preventDefault()}},_appendGhost:function(){if(!J){var t=this.options.fallbackOnBody?document.body:tt,e=X($,!0,Nt,!0,t),n=this.options;if(Nt){for(Dt=t;"static"===R(Dt,"position")&&"none"===R(Dt,"transform")&&Dt!==document;)Dt=Dt.parentNode;Dt!==document.body&&Dt!==document.documentElement?(Dt===document&&(Dt=O()),e.top+=Dt.scrollTop,e.left+=Dt.scrollLeft):Dt=O(),xt=S(Dt)}k(J=$.cloneNode(!0),n.ghostClass,!1),k(J,n.fallbackClass,!0),k(J,n.dragClass,!0),R(J,"transition",""),R(J,"transform",""),R(J,"box-sizing","border-box"),R(J,"margin",0),R(J,"top",e.top),R(J,"left",e.left),R(J,"width",e.width),R(J,"height",e.height),R(J,"opacity","0.8"),R(J,"position",Nt?"absolute":"fixed"),R(J,"zIndex","100000"),R(J,"pointerEvents","none"),Ht.ghost=J,t.appendChild(J),R(J,"transform-origin",gt/parseInt(J.style.width)*100+"% "+mt/parseInt(J.style.height)*100+"%")}},_onDragStart:function(t,e){var n=this,o=t.dataTransfer,i=n.options;q("dragStart",this,{evt:t}),Ht.eventCanceled?this._onDrop():(q("setupClone",this),Ht.eventCanceled||((ot=T($)).removeAttribute("id"),ot.draggable=!1,ot.style["will-change"]="",this._hideClone(),k(ot,this.options.chosenClass,!1),Ht.clone=ot),n.cloneId=zt(function(){q("clone",n),Ht.eventCanceled||(n.options.removeCloneOnHide||tt.insertBefore(ot,$),n._hideClone(),Z({sortable:n,name:"clone"}))}),e||k($,i.dragClass,!0),e?(St=!0,n._loopId=setInterval(n._emulateDragOver,50)):(p(document,"mouseup",n._onDrop),p(document,"touchend",n._onDrop),p(document,"touchcancel",n._onDrop),o&&(o.effectAllowed="move",i.setData&&i.setData.call(n,o,$)),f(document,"drop",n),R($,"transform","translateZ(0)")),Et=!0,n._dragStartId=zt(n._dragStarted.bind(n,e,t)),f(document,"selectstart",n),vt=!0,window.getSelection().removeAllRanges(),u&&R(document.body,"user-select","none"))},_onDragOver:function(n){var o,i,r,t,e,a=this.el,l=n.target,s=this.options,c=s.group,u=Ht.active,d=ct===c,h=s.sort,f=ut||u,p=this,g=!1;if(!Ot){if(void 0!==n.preventDefault&&n.cancelable&&n.preventDefault(),l=P(l,s.draggable,a,!0),O("dragOver"),Ht.eventCanceled)return g;if($.contains(n.target)||l.animated&&l.animatingX&&l.animatingY||p._ignoreWhileAnimating===l)return A(!1);if(St=!1,u&&!s.disabled&&(d?h||(i=Q!==tt):ut===this||(this.lastPutMode=ct.checkPull(this,u,$,n))&&c.checkPut(this,u,$,n))){if(r="vertical"===this._getDirection(n,l),o=X($),O("dragOverValid"),Ht.eventCanceled)return g;if(i)return Q=tt,M(),this._hideClone(),O("revert"),Ht.eventCanceled||(et?tt.insertBefore($,et):tt.appendChild($)),A(!0);var m=F(a,s.draggable);if(m&&(S=n,c=r,x=X(F((E=this).el,E.options.draggable)),E=L(E.el,E.options,J),!(c?S.clientX>E.right+10||S.clientY>x.bottom&&S.clientX>x.left:S.clientY>E.bottom+10||S.clientX>x.right&&S.clientY>x.top)||m.animated)){if(m&&(t=n,e=r,C=X(B((_=this).el,0,_.options,!0)),_=L(_.el,_.options,J),e?t.clientX<_.left-10||t.clientY<C.top&&t.clientX<C.right:t.clientY<_.top-10||t.clientY<C.bottom&&t.clientX<C.left)){var v=B(a,0,s,!0);if(v===$)return A(!1);if(D=X(l=v),!1!==Lt(tt,a,$,o,l,D,n,!1))return M(),a.insertBefore($,v),Q=a,N(),A(!0)}else if(l.parentNode===a){var b,y,w,D=X(l),E=$.parentNode!==a,S=(S=$.animated&&$.toRect||o,x=l.animated&&l.toRect||D,_=(e=r)?S.left:S.top,t=e?S.right:S.bottom,C=e?S.width:S.height,v=e?x.left:x.top,S=e?x.right:x.bottom,x=e?x.width:x.height,!(_===v||t===S||_+C/2===v+x/2)),_=r?"top":"left",C=Y(l,"top","top")||Y($,"top","top"),v=C?C.scrollTop:void 0;if(bt!==l&&(y=D[_],Ct=!1,Tt=!S&&s.invertSwap||E),0!==(b=function(t,e,n,o,i,r,a,l){var s=o?t.clientY:t.clientX,c=o?n.height:n.width,t=o?n.top:n.left,o=o?n.bottom:n.right,n=!1;if(!a)if(l&&wt<c*i){if(Ct=!Ct&&(1===yt?t+c*r/2<s:s<o-c*r/2)?!0:Ct)n=!0;else if(1===yt?s<t+wt:o-wt<s)return-yt}else if(t+c*(1-i)/2<s&&s<o-c*(1-i)/2)return function(t){return j($)<j(t)?1:-1}(e);if((n=n||a)&&(s<t+c*r/2||o-c*r/2<s))return t+c/2<s?1:-1;return 0}(n,l,D,r,S?1:s.swapThreshold,null==s.invertedSwapThreshold?s.swapThreshold:s.invertedSwapThreshold,Tt,bt===l)))for(var T=j($);(w=Q.children[T-=b])&&("none"===R(w,"display")||w===J););if(0===b||w===l)return A(!1);yt=b;var x=(bt=l).nextElementSibling,E=!1,S=Lt(tt,a,$,o,l,D,n,E=1===b);if(!1!==S)return 1!==S&&-1!==S||(E=1===S),Ot=!0,setTimeout(Wt,30),M(),E&&!x?a.appendChild($):l.parentNode.insertBefore($,E?x:l),C&&H(C,0,v-C.scrollTop),Q=$.parentNode,void 0===y||Tt||(wt=Math.abs(y-X(l)[_])),N(),A(!0)}}else{if(m===$)return A(!1);if((l=m&&a===n.target?m:l)&&(D=X(l)),!1!==Lt(tt,a,$,o,l,D,n,!!l))return M(),m&&m.nextSibling?a.insertBefore($,m.nextSibling):a.appendChild($),Q=a,N(),A(!0)}if(a.contains($))return A(!1)}return!1}function O(t,e){q(t,p,I({evt:n,isOwner:d,axis:r?"vertical":"horizontal",revert:i,dragRect:o,targetRect:D,canSort:h,fromSortable:f,target:l,completed:A,onMove:function(t,e){return Lt(tt,a,$,o,t,X(t),n,e)},changed:N},e))}function M(){O("dragOverAnimationCapture"),p.captureAnimationState(),p!==f&&f.captureAnimationState()}function A(t){return O("dragOverCompleted",{insertion:t}),t&&(d?u._hideClone():u._showClone(p),p!==f&&(k($,(ut||u).options.ghostClass,!1),k($,s.ghostClass,!0)),ut!==p&&p!==Ht.active?ut=p:p===Ht.active&&ut&&(ut=null),f===p&&(p._ignoreWhileAnimating=l),p.animateAll(function(){O("dragOverAnimationComplete"),p._ignoreWhileAnimating=null}),p!==f&&(f.animateAll(),f._ignoreWhileAnimating=null)),(l===$&&!$.animated||l===a&&!l.animated)&&(bt=null),s.dragoverBubble||n.rootEl||l===document||($.parentNode[K]._isOutsideThisEl(n.target),t||Ft(n)),!s.dragoverBubble&&n.stopPropagation&&n.stopPropagation(),g=!0}function N(){at=j($),st=j($,s.draggable),Z({sortable:p,name:"change",toEl:a,newIndex:at,newDraggableIndex:st,originalEvent:n})}},_ignoreWhileAnimating:null,_offMoveEvents:function(){p(document,"mousemove",this._onTouchMove),p(document,"touchmove",this._onTouchMove),p(document,"pointermove",this._onTouchMove),p(document,"dragover",Ft),p(document,"mousemove",Ft),p(document,"touchmove",Ft)},_offUpEvents:function(){var t=this.el.ownerDocument;p(t,"mouseup",this._onDrop),p(t,"touchend",this._onDrop),p(t,"pointerup",this._onDrop),p(t,"pointercancel",this._onDrop),p(t,"touchcancel",this._onDrop),p(document,"selectstart",this)},_onDrop:function(t){var e=this.el,n=this.options;at=j($),st=j($,n.draggable),q("drop",this,{evt:t}),Q=$&&$.parentNode,at=j($),st=j($,n.draggable),Ht.eventCanceled||(Ct=Tt=Et=!1,clearInterval(this._loopId),clearTimeout(this._dragStartTimer),Gt(this.cloneId),Gt(this._dragStartId),this.nativeDraggable&&(p(document,"drop",this),p(e,"dragstart",this._onDragStart)),this._offMoveEvents(),this._offUpEvents(),u&&R(document.body,"user-select",""),R($,"transform",""),t&&(vt&&(t.cancelable&&t.preventDefault(),n.dropBubble||t.stopPropagation()),J&&J.parentNode&&J.parentNode.removeChild(J),(tt===Q||ut&&"clone"!==ut.lastPutMode)&&ot&&ot.parentNode&&ot.parentNode.removeChild(ot),$&&(this.nativeDraggable&&p($,"dragend",this),Kt($),$.style["will-change"]="",vt&&!Et&&k($,(ut||this).options.ghostClass,!1),k($,this.options.chosenClass,!1),Z({sortable:this,name:"unchoose",toEl:Q,newIndex:null,newDraggableIndex:null,originalEvent:t}),tt!==Q?(0<=at&&(Z({rootEl:Q,name:"add",toEl:Q,fromEl:tt,originalEvent:t}),Z({sortable:this,name:"remove",toEl:Q,originalEvent:t}),Z({rootEl:Q,name:"sort",toEl:Q,fromEl:tt,originalEvent:t}),Z({sortable:this,name:"sort",toEl:Q,originalEvent:t})),ut&&ut.save()):at!==rt&&0<=at&&(Z({sortable:this,name:"update",toEl:Q,originalEvent:t}),Z({sortable:this,name:"sort",toEl:Q,originalEvent:t})),Ht.active&&(null!=at&&-1!==at||(at=rt,st=lt),Z({sortable:this,name:"end",toEl:Q,originalEvent:t}),this.save())))),this._nulling()},_nulling:function(){q("nulling",this),tt=$=Q=J=et=ot=nt=it=dt=ht=vt=at=st=rt=lt=bt=yt=ut=ct=Ht.dragged=Ht.ghost=Ht.clone=Ht.active=null;var e=this.el;Mt.forEach(function(t){e.contains(t)&&(t.checked=!0)}),Mt.length=ft=pt=0},handleEvent:function(t){switch(t.type){case"drop":case"dragend":this._onDrop(t);break;case"dragenter":case"dragover":$&&(this._onDragOver(t),function(t){t.dataTransfer&&(t.dataTransfer.dropEffect="move");t.cancelable&&t.preventDefault()}(t));break;case"selectstart":t.preventDefault()}},toArray:function(){for(var t,e=[],n=this.el.children,o=0,i=n.length,r=this.options;o<i;o++)P(t=n[o],r.draggable,this.el,!1)&&e.push(t.getAttribute(r.dataIdAttr)||function(t){var e=t.tagName+t.className+t.src+t.href+t.textContent,n=e.length,o=0;for(;n--;)o+=e.charCodeAt(n);return o.toString(36)}(t));return e},sort:function(t,e){var n={},o=this.el;this.toArray().forEach(function(t,e){e=o.children[e];P(e,this.options.draggable,o,!1)&&(n[t]=e)},this),e&&this.captureAnimationState(),t.forEach(function(t){n[t]&&(o.removeChild(n[t]),o.appendChild(n[t]))}),e&&this.animateAll()},save:function(){var t=this.options.store;t&&t.set&&t.set(this)},closest:function(t,e){return P(t,e||this.options.draggable,this.el,!1)},option:function(t,e){var n=this.options;if(void 0===e)return n[t];var o=G.modifyOption(this,t,e);n[t]=void 0!==o?o:e,"group"===t&&Xt(n)},destroy:function(){q("destroy",this);var t=this.el;t[K]=null,p(t,"mousedown",this._onTapStart),p(t,"touchstart",this._onTapStart),p(t,"pointerdown",this._onTapStart),this.nativeDraggable&&(p(t,"dragover",this),p(t,"dragenter",this)),Array.prototype.forEach.call(t.querySelectorAll("[draggable]"),function(t){t.removeAttribute("draggable")}),this._onDrop(),this._disableDelayedDragEvents(),_t.splice(_t.indexOf(this.el),1),this.el=t=null},_hideClone:function(){it||(q("hideClone",this),Ht.eventCanceled||(R(ot,"display","none"),this.options.removeCloneOnHide&&ot.parentNode&&ot.parentNode.removeChild(ot),it=!0))},_showClone:function(t){"clone"===t.lastPutMode?it&&(q("showClone",this),Ht.eventCanceled||($.parentNode!=tt||this.options.group.revertClone?et?tt.insertBefore(ot,et):tt.appendChild(ot):tt.insertBefore(ot,$),this.options.group.revertClone&&this.animate($,ot),R(ot,"display",""),it=!1)):this._hideClone()}},At&&f(document,"touchmove",function(t){(Ht.active||Et)&&t.cancelable&&t.preventDefault()}),Ht.utils={on:f,off:p,css:R,find:E,is:function(t,e){return!!P(t,e,t,!1)},extend:function(t,e){if(t&&e)for(var n in e)e.hasOwnProperty(n)&&(t[n]=e[n]);return t},throttle:C,closest:P,toggleClass:k,clone:T,index:j,nextTick:zt,cancelNextTick:Gt,detectDirection:Rt,getChild:B,expando:K},Ht.get=function(t){return t[K]},Ht.mount=function(){for(var t=arguments.length,e=new Array(t),n=0;n<t;n++)e[n]=arguments[n];(e=e[0].constructor===Array?e[0]:e).forEach(function(t){if(!t.prototype||!t.prototype.constructor)throw"Sortable: Mounted plugin must be a constructor function, not ".concat({}.toString.call(t));t.utils&&(Ht.utils=I(I({},Ht.utils),t.utils)),G.mount(t)})},Ht.create=function(t,e){return new Ht(t,e)};var Ut,qt,Vt,Zt,$t,Qt,Jt=[],te=!(Ht.version="1.15.7");function ee(){Jt.forEach(function(t){clearInterval(t.pid)}),Jt=[]}function ne(){clearInterval(Qt)}var oe,ie=C(function(n,t,e,o){if(t.scroll){var i,r=(n.touches?n.touches[0]:n).clientX,a=(n.touches?n.touches[0]:n).clientY,l=t.scrollSensitivity,s=t.scrollSpeed,c=O(),u=!1;qt!==e&&(qt=e,ee(),Ut=t.scroll,i=t.scrollFn,!0===Ut&&(Ut=M(e,!0)));var d=0,h=Ut;do{var f=h,p=X(f),g=p.top,m=p.bottom,v=p.left,b=p.right,y=p.width,w=p.height,D=void 0,E=void 0,S=f.scrollWidth,_=f.scrollHeight,C=R(f),T=f.scrollLeft,p=f.scrollTop,E=f===c?(D=y<S&&("auto"===C.overflowX||"scroll"===C.overflowX||"visible"===C.overflowX),w<_&&("auto"===C.overflowY||"scroll"===C.overflowY||"visible"===C.overflowY)):(D=y<S&&("auto"===C.overflowX||"scroll"===C.overflowX),w<_&&("auto"===C.overflowY||"scroll"===C.overflowY)),T=D&&(Math.abs(b-r)<=l&&T+y<S)-(Math.abs(v-r)<=l&&!!T),p=E&&(Math.abs(m-a)<=l&&p+w<_)-(Math.abs(g-a)<=l&&!!p);if(!Jt[d])for(var x=0;x<=d;x++)Jt[x]||(Jt[x]={});Jt[d].vx==T&&Jt[d].vy==p&&Jt[d].el===f||(Jt[d].el=f,Jt[d].vx=T,Jt[d].vy=p,clearInterval(Jt[d].pid),0==T&&0==p||(u=!0,Jt[d].pid=setInterval(function(){o&&0===this.layer&&Ht.active._onTouchMove($t);var t=Jt[this.layer].vy?Jt[this.layer].vy*s:0,e=Jt[this.layer].vx?Jt[this.layer].vx*s:0;"function"==typeof i&&"continue"!==i.call(Ht.dragged.parentNode[K],e,t,n,$t,Jt[this.layer].el)||H(Jt[this.layer].el,e,t)}.bind({layer:d}),24))),d++}while(t.bubbleScroll&&h!==c&&(h=M(h,!1)));te=u}},30),n=function(t){var e=t.originalEvent,n=t.putSortable,o=t.dragEl,i=t.activeSortable,r=t.dispatchSortableEvent,a=t.hideGhostForTarget,t=t.unhideGhostForTarget;e&&(i=n||i,a(),e=e.changedTouches&&e.changedTouches.length?e.changedTouches[0]:e,e=document.elementFromPoint(e.clientX,e.clientY),t(),i&&!i.el.contains(e)&&(r("spill"),this.onSpill({dragEl:o,putSortable:n})))};function re(){}function ae(){}re.prototype={startIndex:null,dragStart:function(t){t=t.oldDraggableIndex;this.startIndex=t},onSpill:function(t){var e=t.dragEl,n=t.putSortable;this.sortable.captureAnimationState(),n&&n.captureAnimationState();t=B(this.sortable.el,this.startIndex,this.options);t?this.sortable.el.insertBefore(e,t):this.sortable.el.appendChild(e),this.sortable.animateAll(),n&&n.animateAll()},drop:n},a(re,{pluginName:"revertOnSpill"}),ae.prototype={onSpill:function(t){var e=t.dragEl,t=t.putSortable||this.sortable;t.captureAnimationState(),e.parentNode&&e.parentNode.removeChild(e),t.animateAll()},drop:n},a(ae,{pluginName:"removeOnSpill"});var le,se,ce,ue,de,he=[],fe=[],pe=!1,ge=!1,me=!1;function ve(n,o){fe.forEach(function(t,e){e=o.children[t.sortableIndex+(n?Number(e):0)];e?o.insertBefore(t,e):o.appendChild(t)})}function be(){he.forEach(function(t){t!==ce&&t.parentNode&&t.parentNode.removeChild(t)})}return Ht.mount(new function(){function t(){for(var t in this.defaults={scroll:!0,forceAutoScrollFallback:!1,scrollSensitivity:30,scrollSpeed:10,bubbleScroll:!0},this)"_"===t.charAt(0)&&"function"==typeof this[t]&&(this[t]=this[t].bind(this))}return t.prototype={dragStarted:function(t){t=t.originalEvent;this.sortable.nativeDraggable?f(document,"dragover",this._handleAutoScroll):this.options.supportPointer?f(document,"pointermove",this._handleFallbackAutoScroll):t.touches?f(document,"touchmove",this._handleFallbackAutoScroll):f(document,"mousemove",this._handleFallbackAutoScroll)},dragOverCompleted:function(t){t=t.originalEvent;this.options.dragOverBubble||t.rootEl||this._handleAutoScroll(t)},drop:function(){this.sortable.nativeDraggable?p(document,"dragover",this._handleAutoScroll):(p(document,"pointermove",this._handleFallbackAutoScroll),p(document,"touchmove",this._handleFallbackAutoScroll),p(document,"mousemove",this._handleFallbackAutoScroll)),ne(),ee(),clearTimeout(v),v=void 0},nulling:function(){$t=qt=Ut=te=Qt=Vt=Zt=null,Jt.length=0},_handleFallbackAutoScroll:function(t){this._handleAutoScroll(t,!0)},_handleAutoScroll:function(e,n){var o,i=this,r=(e.touches?e.touches[0]:e).clientX,a=(e.touches?e.touches[0]:e).clientY,t=document.elementFromPoint(r,a);$t=e,n||this.options.forceAutoScrollFallback||w||y||u?(ie(e,this.options,t,n),o=M(t,!0),!te||Qt&&r===Vt&&a===Zt||(Qt&&ne(),Qt=setInterval(function(){var t=M(document.elementFromPoint(r,a),!0);t!==o&&(o=t,ee()),ie(e,i.options,t,n)},10),Vt=r,Zt=a)):this.options.bubbleScroll&&M(t,!0)!==O()?ie(e,this.options,M(t,!1),!1):ee()}},a(t,{pluginName:"scroll",initializeByDefault:!0})}),Ht.mount(ae,re),Ht.mount(new function(){function t(){this.defaults={swapClass:"sortable-swap-highlight"}}return t.prototype={dragStart:function(t){t=t.dragEl;oe=t},dragOverValid:function(t){var e=t.completed,n=t.target,o=t.onMove,i=t.activeSortable,r=t.changed,a=t.cancel;i.options.swap&&(t=this.sortable.el,i=this.options,n&&n!==t&&(t=oe,oe=!1!==o(n)?(k(n,i.swapClass,!0),n):null,t&&t!==oe&&k(t,i.swapClass,!1)),r(),e(!0),a())},drop:function(t){var e,n,o=t.activeSortable,i=t.putSortable,r=t.dragEl,a=i||this.sortable,l=this.options;oe&&k(oe,l.swapClass,!1),oe&&(l.swap||i&&i.options.swap)&&r!==oe&&(a.captureAnimationState(),a!==o&&o.captureAnimationState(),n=oe,t=(e=r).parentNode,l=n.parentNode,t&&l&&!t.isEqualNode(n)&&!l.isEqualNode(e)&&(i=j(e),r=j(n),t.isEqualNode(l)&&i<r&&r++,t.insertBefore(n,t.children[i]),l.insertBefore(e,l.children[r])),a.animateAll(),a!==o&&o.animateAll())},nulling:function(){oe=null}},a(t,{pluginName:"swap",eventProperties:function(){return{swapItem:oe}}})}),Ht.mount(new function(){function t(o){for(var t in this)"_"===t.charAt(0)&&"function"==typeof this[t]&&(this[t]=this[t].bind(this));o.options.avoidImplicitDeselect||(o.options.supportPointer?f(document,"pointerup",this._deselectMultiDrag):(f(document,"mouseup",this._deselectMultiDrag),f(document,"touchend",this._deselectMultiDrag))),f(document,"keydown",this._checkKeyDown),f(document,"keyup",this._checkKeyUp),this.defaults={selectedClass:"sortable-selected",multiDragKey:null,avoidImplicitDeselect:!1,setData:function(t,e){var n="";he.length&&se===o?he.forEach(function(t,e){n+=(e?", ":"")+t.textContent}):n=e.textContent,t.setData("Text",n)}}}return t.prototype={multiDragKeyDown:!1,isMultiDrag:!1,delayStartGlobal:function(t){t=t.dragEl;ce=t},delayEnded:function(){this.isMultiDrag=~he.indexOf(ce)},setupClone:function(t){var e=t.sortable,t=t.cancel;if(this.isMultiDrag){for(var n=0;n<he.length;n++)fe.push(T(he[n])),fe[n].sortableIndex=he[n].sortableIndex,fe[n].draggable=!1,fe[n].style["will-change"]="",k(fe[n],this.options.selectedClass,!1),he[n]===ce&&k(fe[n],this.options.chosenClass,!1);e._hideClone(),t()}},clone:function(t){var e=t.sortable,n=t.rootEl,o=t.dispatchSortableEvent,t=t.cancel;this.isMultiDrag&&(this.options.removeCloneOnHide||he.length&&se===e&&(ve(!0,n),o("clone"),t()))},showClone:function(t){var e=t.cloneNowShown,n=t.rootEl,t=t.cancel;this.isMultiDrag&&(ve(!1,n),fe.forEach(function(t){R(t,"display","")}),e(),de=!1,t())},hideClone:function(t){var e=this,n=(t.sortable,t.cloneNowHidden),t=t.cancel;this.isMultiDrag&&(fe.forEach(function(t){R(t,"display","none"),e.options.removeCloneOnHide&&t.parentNode&&t.parentNode.removeChild(t)}),n(),de=!0,t())},dragStartGlobal:function(t){t.sortable;!this.isMultiDrag&&se&&se.multiDrag._deselectMultiDrag(),he.forEach(function(t){t.sortableIndex=j(t)}),he=he.sort(function(t,e){return t.sortableIndex-e.sortableIndex}),me=!0},dragStarted:function(t){var e,n=this,t=t.sortable;this.isMultiDrag&&(this.options.sort&&(t.captureAnimationState(),this.options.animation&&(he.forEach(function(t){t!==ce&&R(t,"position","absolute")}),e=X(ce,!1,!0,!0),he.forEach(function(t){t!==ce&&x(t,e)}),pe=ge=!0)),t.animateAll(function(){pe=ge=!1,n.options.animation&&he.forEach(function(t){A(t)}),n.options.sort&&be()}))},dragOver:function(t){var e=t.target,n=t.completed,t=t.cancel;ge&&~he.indexOf(e)&&(n(!1),t())},revert:function(t){var n,o,e=t.fromSortable,i=t.rootEl,r=t.sortable,a=t.dragRect;1<he.length&&(he.forEach(function(t){r.addAnimationState({target:t,rect:ge?X(t):a}),A(t),t.fromRect=a,e.removeAnimationState(t)}),ge=!1,n=!this.options.removeCloneOnHide,o=i,he.forEach(function(t,e){e=o.children[t.sortableIndex+(n?Number(e):0)];e?o.insertBefore(t,e):o.appendChild(t)}))},dragOverCompleted:function(t){var e,n=t.sortable,o=t.isOwner,i=t.insertion,r=t.activeSortable,a=t.parentEl,l=t.putSortable,t=this.options;i&&(o&&r._hideClone(),pe=!1,t.animation&&1<he.length&&(ge||!o&&!r.options.sort&&!l)&&(e=X(ce,!1,!0,!0),he.forEach(function(t){t!==ce&&(x(t,e),a.appendChild(t))}),ge=!0),o||(ge||be(),1<he.length?(o=de,r._showClone(n),r.options.animation&&!de&&o&&fe.forEach(function(t){r.addAnimationState({target:t,rect:ue}),t.fromRect=ue,t.thisAnimationDuration=null})):r._showClone(n)))},dragOverAnimationCapture:function(t){var e=t.dragRect,n=t.isOwner,t=t.activeSortable;he.forEach(function(t){t.thisAnimationDuration=null}),t.options.animation&&!n&&t.multiDrag.isMultiDrag&&(ue=a({},e),e=D(ce,!0),ue.top-=e.f,ue.left-=e.e)},dragOverAnimationComplete:function(){ge&&(ge=!1,be())},drop:function(t){var o,i,r,a,n,e,l,s=t.originalEvent,c=t.rootEl,u=t.parentEl,d=t.sortable,h=t.dispatchSortableEvent,f=t.oldIndex,t=t.putSortable,p=t||this.sortable;s&&(o=this.options,i=u.children,me||(o.multiDragKey&&!this.multiDragKeyDown&&this._deselectMultiDrag(),k(ce,o.selectedClass,!~he.indexOf(ce)),~he.indexOf(ce)?(he.splice(he.indexOf(ce),1),le=null,U({sortable:d,rootEl:c,name:"deselect",targetEl:ce,originalEvent:s})):(he.push(ce),U({sortable:d,rootEl:c,name:"select",targetEl:ce,originalEvent:s}),s.shiftKey&&le&&d.el.contains(le)?(r=j(le),a=j(ce),~r&&~a&&r!==a&&function(){for(var e,t=r<a?(e=r,a):(e=a,r+1),n=o.filter;e<t;e++)~he.indexOf(i[e])||P(i[e],o.draggable,u,!1)&&(n&&("function"==typeof n?n.call(d,s,i[e],d):n.split(",").some(function(t){return P(i[e],t.trim(),u,!1)}))||(k(i[e],o.selectedClass,!0),he.push(i[e]),U({sortable:d,rootEl:c,name:"select",targetEl:i[e],originalEvent:s})))}()):le=ce,se=p)),me&&this.isMultiDrag&&(ge=!1,(u[K].options.sort||u!==c)&&1<he.length&&(n=X(ce),e=j(ce,":not(."+this.options.selectedClass+")"),!pe&&o.animation&&(ce.thisAnimationDuration=null),p.captureAnimationState(),pe||(o.animation&&(ce.fromRect=n,he.forEach(function(t){var e;t.thisAnimationDuration=null,t!==ce&&(e=ge?X(t):n,t.fromRect=e,p.addAnimationState({target:t,rect:e}))})),be(),he.forEach(function(t){i[e]?u.insertBefore(t,i[e]):u.appendChild(t),e++}),f===j(ce)&&(l=!1,he.forEach(function(t){t.sortableIndex!==j(t)&&(l=!0)}),l&&(h("update"),h("sort")))),he.forEach(function(t){A(t)}),p.animateAll()),se=p),(c===u||t&&"clone"!==t.lastPutMode)&&fe.forEach(function(t){t.parentNode&&t.parentNode.removeChild(t)}))},nullingGlobal:function(){this.isMultiDrag=me=!1,fe.length=0},destroyGlobal:function(){this._deselectMultiDrag(),p(document,"pointerup",this._deselectMultiDrag),p(document,"mouseup",this._deselectMultiDrag),p(document,"touchend",this._deselectMultiDrag),p(document,"keydown",this._checkKeyDown),p(document,"keyup",this._checkKeyUp)},_deselectMultiDrag:function(t){if(!(void 0!==me&&me||se!==this.sortable||t&&P(t.target,this.options.draggable,this.sortable.el,!1)||t&&0!==t.button))for(;he.length;){var e=he[0];k(e,this.options.selectedClass,!1),he.shift(),U({sortable:this.sortable,rootEl:this.sortable.el,name:"deselect",targetEl:e,originalEvent:t})}},_checkKeyDown:function(t){t.key===this.options.multiDragKey&&(this.multiDragKeyDown=!0)},_checkKeyUp:function(t){t.key===this.options.multiDragKey&&(this.multiDragKeyDown=!1)}},a(t,{pluginName:"multiDrag",utils:{select:function(t){var e=t.parentNode[K];e&&e.options.multiDrag&&!~he.indexOf(t)&&(se&&se!==e&&(se.multiDrag._deselectMultiDrag(),se=e),k(t,e.options.selectedClass,!0),he.push(t))},deselect:function(t){var e=t.parentNode[K],n=he.indexOf(t);e&&e.options.multiDrag&&~n&&(k(t,e.options.selectedClass,!1),he.splice(n,1))}},eventProperties:function(){var n=this,o=[],i=[];return he.forEach(function(t){var e;o.push({multiDragElement:t,index:t.sortableIndex}),e=ge&&t!==ce?-1:ge?j(t,":not(."+n.options.selectedClass+")"):j(t),i.push({multiDragElement:t,index:e})}),{items:e(he),clones:[].concat(fe),oldIndicies:o,newIndicies:i}},optionListeners:{multiDragKey:function(t){return"ctrl"===(t=t.toLowerCase())?t="Control":1<t.length&&(t=t.charAt(0).toUpperCase()+t.substr(1)),t}}})}),Ht});
</script>
<script>
````

### E11 — app: o album da Lista leva o id e a caixa de selecao — `app/index.html`

**Ancora, literal:**

````
      songs.forEach(song => rows.appendChild(renderRow(song)));
      sec.appendChild(rows);
````

**Texto novo, literal:**

````
      songs.forEach(song => rows.appendChild(renderRow(song)));
      sec.appendChild(rows);
      // I3: o id do album (alvo do arrastar e do .json solto) e a caixa que marca as visiveis dele.
      sec.dataset.album = album.id;
      const ac = document.createElement("input");
      ac.type = "checkbox"; ac.className = "album-sel";
      ac.setAttribute("aria-label", "Selecionar as faixas de " + album.title);
      ac.addEventListener("click", () => selectAlbum(sec));
      sec.querySelector(".album-head").insertBefore(ac, sec.querySelector("h2"));
````

### E12 — app: o render fecha com as alcas e a selecao — `app/index.html`

**Ancora, literal:**

````
  if (currentView() === "list") { afterListRender(); openFromHash(); }
}
````

**Texto novo, literal:**

````
  if (currentView() === "list") { afterListRender(); openFromHash(); }
  afterOrganizeRender();   // I3: alcas, selecao e barra de lote
}
````

### E13 — app: o pe do cartao troca ↑ ↓ mover excluir pelo «⋯» — `app/index.html`

**Ancora, literal:**

````
  // Modo «editar» (DEC-028): so com o acervo guardado, que e onde o rascunho mora.
  if (App.editing && App.saved) {
    const loc = locateSong(song.id);
    const mk = (txt, title, fn, off) => {
      const b = document.createElement("button");
      b.type = "button"; b.className = "edit-btn"; b.textContent = txt; b.title = title; b.disabled = !!off;
      b.addEventListener("click", fn);
      foot.appendChild(b);
    };
    mk("↑", "Subir no álbum", () => moveSongBy(song.id, -1), !loc || loc.index === 0);
    mk("↓", "Descer no álbum", () => moveSongBy(song.id, 1), !loc || loc.index === loc.album.songs.length - 1);
    mk("mover…", "Levar para outro álbum ou para um álbum novo", () => openMoveDialog(song.id));
    mk("excluir", "Tirar do rascunho; o arquivo só muda quando você baixar o novo", () => deleteSong(song.id));
  }
````

**Texto novo, literal:**

````
  // I3 (DEC-030): sem o interruptor «editar». Organizar vive no «⋯» da faixa,
  // o mesmo menu da linha da Lista; no detalhe, ele fica no alto (o daqui some).
  const more = document.createElement("button");
  more.type = "button"; more.className = "card-more"; more.textContent = "⋯";
  more.setAttribute("aria-label", "Ações de " + song.title);
  more.setAttribute("aria-haspopup", "menu"); more.setAttribute("aria-expanded", "false");
  more.title = "Mover, subir, descer, exportar ou excluir";
  more.addEventListener("click", () => openTrackMenu(song.id, more));
  foot.appendChild(more);
````

### E14 — app: o aviso comum tira o botao do aviso anterior — `app/index.html`

**Ancora, literal:**

````
  t.textContent = msg; t.classList.add("show");
````

**Texto novo, literal:**

````
  t.textContent = msg; t.classList.remove("has-action"); t.classList.add("show");
````

### E15 — app: salvar esquece o «Desfazer» — `app/index.html`

**Ancora, literal:**

````
  if (!App.saved) return;
  App.changes = 0;
````

**Texto novo, literal:**

````
  if (!App.saved) return;
  App.undo = null;   // I3: depois de salvar, a volta nao vale mais
  App.changes = 0;
````

### E16 — app: trocar de acervo esquece a volta e a selecao — `app/index.html`

**Ancora, literal:**

````
  closeDetail({ noFocus: true });   // I2: a faixa aberta era do acervo anterior
````

**Texto novo, literal:**

````
  closeDetail({ noFocus: true });   // I2: a faixa aberta era do acervo anterior
  App.undo = null;   // I3: a volta e a selecao eram do acervo anterior
  if (App.selection) { App.selection.clear(); App.selecting = false; }
````

### E17 — app: sai o estado do interruptor — `app/index.html`

**Ancora, literal:**

````
   =================================================================== */
App.editing = false;          // o interruptor «editar», so da sessao
App.saved = false;            // o acervo aberto tem copia guardada (sem ela, nao ha rascunho)
````

**Texto novo, literal:**

````
   =================================================================== */
App.saved = false;            // o acervo aberto tem copia guardada (sem ela, nao ha rascunho)
````

### E18 — app: o aviso de cada operacao traz o «Desfazer» — `app/index.html`

**Ancora, literal:**

````
  rerender(focusId);
  const ok = await persistDraft(true);
  toast(msg + (ok ? "" : " · não consegui guardar no navegador: baixe o .json para não perder"));
}
````

**Texto novo, literal:**

````
  rerender(focusId);
  const ok = await persistDraft(true);
  // I3: a volta guardada pelo beginEdit ganha o rotulo do aviso.
  if (App.undo && !App.undo.label) App.undo.label = msg;
  const text = msg + (ok ? "" : " · não consegui guardar no navegador: baixe o .json para não perder");
  if (App.undo) toastAction(text, "Desfazer", undoLast); else toast(text);
}
````

### E19 — app: sai o interruptor «editar» — `app/index.html`

**Ancora, literal:**

````
}

function toggleEditing() {
  App.editing = !App.editing;
  setOrigin();
  rerender();
}

/** ↑ / ↓: troca com a vizinha na ordem COMPLETA do album, mesmo com filtro ligado. */
````

**Texto novo, literal:**

````
}


/** ↑ / ↓: troca com a vizinha na ordem COMPLETA do album, mesmo com filtro ligado. */
````

### E20 — app: subir e descer guardam a volta — `app/index.html`

**Ancora, literal:**

````
  [songs[loc.index], songs[j]] = [songs[j], songs[loc.index]];
````

**Texto novo, literal:**

````
  beginEdit();   // I3: a volta do «Desfazer»
  [songs[loc.index], songs[j]] = [songs[j], songs[loc.index]];
````

### E21 — app: «Mover para…» leva uma faixa ou varias — `app/index.html`

**Ancora, literal:**

````
/** «mover…»: para o fim de outro album, ou de um album novo. A marca «usei», os
    modulos ligados e o BPM vao junto, porque ficam presos ao id da faixa. */
function openMoveDialog(id) {
  const loc = locateSong(id);
  if (!loc) return;
  const dlg = document.getElementById("move-dialog");
  const sel = document.getElementById("move-target"), inp = document.getElementById("move-new-title");
  document.getElementById("move-song-title").textContent = loc.album.songs[loc.index].title;
  sel.innerHTML = "";
  App.collection.albums.filter(a => a !== loc.album).forEach(a => sel.appendChild(new Option(a.title, a.id)));
  sel.appendChild(new Option("novo álbum…", "__new"));
  inp.value = "";
  const sync = () => { inp.hidden = sel.value !== "__new"; };
  sel.onchange = sync; sync();
  document.getElementById("move-cancel-btn").onclick = () => dlg.close();
  document.getElementById("move-ok-btn").onclick = async () => {
    let target;
    if (sel.value === "__new") {
      const title = inp.value.trim();
      if (!title) { inp.focus(); return; }
      target = { id: nextFreeId(idSlug(title), albumIdSet()), title, songs: [] };
      App.collection.albums.push(target);
    } else {
      target = App.collection.albums.find(a => a.id === sel.value);
    }
    if (!target) return;
    dlg.close();
    const src = loc.album;
    const [song] = src.songs.splice(loc.index, 1);
    target.songs.push(song);
    const gone = pruneEmpty(src);
    await afterEdit("«" + song.title + "» foi para «" + target.title + "»" + gone, song.id);
  };
  dlg.showModal();
}
````

**Texto novo, literal:**

````
/** «Mover para…»: uma faixa ou varias (o lote), para o fim de outro album ou
    de um album novo, na ordem do acervo. A marca «usei», os modulos ligados e
    o BPM vao junto, porque ficam presos ao id da faixa. `forceNew` abre com
    «novo álbum…» escolhido (soltar em «+ Novo álbum», na lateral). */
function openMoveDialog(idOrIds, opts = {}) {
  const ids = (Array.isArray(idOrIds) ? idOrIds : [idOrIds]).filter(id => locateSong(id));
  if (!ids.length) return;
  const locs = ids.map(id => locateSong(id)), one = ids.length === 1;
  const from = locs.every(l => l.album === locs[0].album) ? locs[0].album : null;
  const dlg = document.getElementById("move-dialog");
  const sel = document.getElementById("move-target"), inp = document.getElementById("move-new-title");
  document.getElementById("move-dialog-title").textContent = one ? "Mover faixa" : "Mover " + ids.length + " faixas";
  document.getElementById("move-dialog-text").textContent = one
    ? "«" + locs[0].album.songs[locs[0].index].title + "» vai para o fim do álbum escolhido."
    : "As " + ids.length + " faixas vão para o fim do álbum escolhido, na ordem em que estão.";
  sel.innerHTML = "";
  App.collection.albums.filter(a => a !== from).forEach(a => sel.appendChild(new Option(a.title, a.id)));
  sel.appendChild(new Option("novo álbum…", "__new"));
  if (opts.forceNew) sel.value = "__new";
  inp.value = "";
  const sync = () => { inp.hidden = sel.value !== "__new"; };
  sel.onchange = sync; sync();
  document.getElementById("move-cancel-btn").onclick = () => dlg.close();
  document.getElementById("move-ok-btn").onclick = async () => {
    let target;
    if (sel.value === "__new") {
      const title = inp.value.trim();
      if (!title) { inp.focus(); return; }
      beginEdit();   // I3: a volta do «Desfazer»
      target = { id: nextFreeId(idSlug(title), albumIdSet()), title, songs: [] };
      App.collection.albums.push(target);
    } else {
      target = App.collection.albums.find(a => a.id === sel.value);
      if (!target) return;
      // No lote, as que ja estao no destino ficam onde estao; sem nenhuma para mover, nada muda.
      if (!locs.some(l => l.album !== target)) { dlg.close(); toast("Nada a mover: já estão em «" + target.title + "»"); return; }
      beginEdit();
    }
    dlg.close();
    const want = new Set(ids), picked = [], touched = new Set();
    App.collection.albums.forEach(a => {
      if (a === target) return;
      const keep = [];
      (a.songs || []).forEach(s => { if (want.has(s.id)) { picked.push(s); touched.add(a); } else keep.push(s); });
      a.songs = keep;
    });
    target.songs.push(...picked);
    let gone = "";
    touched.forEach(a => { if (a !== target) gone += pruneEmpty(a); });
    App.selection.clear();
    await afterEdit((one ? "«" + picked[0].title + "» foi" : picked.length + " faixas foram") + " para «" + target.title + "»" + gone, picked[0].id);
  };
  dlg.showModal();
  if (opts.forceNew) inp.focus();
}
````

### E22 — app: a janela de mover diz uma faixa ou varias — `app/index.html`

**Ancora, literal:**

````
  <h2 id="move-dialog-title">Mover faixa</h2>
  <p>«<span id="move-song-title"></span>» vai para o fim do álbum escolhido.</p>
````

**Texto novo, literal:**

````
  <h2 id="move-dialog-title">Mover faixa</h2>
  <p id="move-dialog-text"></p>
````

### E23 — app: excluir guarda a volta — `app/index.html`

**Ancora, literal:**

````
  loc.album.songs.splice(loc.index, 1);
  const by = App.ui.usedBy && App.ui.usedBy[App.source];
````

**Texto novo, literal:**

````
  beginEdit();   // I3: a volta do «Desfazer»
  loc.album.songs.splice(loc.index, 1);
  const by = App.ui.usedBy && App.ui.usedBy[App.source];
````

### E24 — app: importar faixas guarda a volta — `app/index.html`

**Ancora, literal:**

````
  const coll = App.collection;
  const n = { imported: 0, same: 0, renamed: 0, modsAdded: 0, modsRenamed: 0, missing: 0 };
````

**Texto novo, literal:**

````
  const coll = App.collection;
  const prevUndo = App.undo;
  beginEdit();   // I3: a volta do «Desfazer» (sem nada importado, fica a anterior)
  const n = { imported: 0, same: 0, renamed: 0, modsAdded: 0, modsRenamed: 0, missing: 0 };
````

### E25 — app: nada importado devolve a volta anterior — `app/index.html`

**Ancora, literal:**

````
  if (!n.imported) { toast("Nada importado" + tail); return; }
````

**Texto novo, literal:**

````
  if (!n.imported) { App.undo = prevUndo; toast("Nada importado" + tail); return; }
````

### E26 — app: ler o .json de faixas com um album de destino — `app/index.html`

**Ancora, literal:**

````
function readTracksFile(file) {
````

**Texto novo, literal:**

````
function readTracksFile(file, dest) {
````

### E27 — app: o destino vai para a janela de importar — `app/index.html`

**Ancora, literal:**

````
    openImportDialog(src, file.name);
````

**Texto novo, literal:**

````
    openImportDialog(src, file.name, dest);
````

### E28 — app: a janela de importar aceita o destino — `app/index.html`

**Ancora, literal:**

````
function openImportDialog(src, name) {
````

**Texto novo, literal:**

````
function openImportDialog(src, name, dest) {
````

### E29 — app: com destino, ele ja vem escolhido — `app/index.html`

**Ancora, literal:**

````
  sel.appendChild(new Option("novo álbum…", "__new"));
  inp.value = "";
  const sync = () => { inp.hidden = sel.value !== "__new"; };
  sel.onchange = sync; sync();
  document.getElementById("import-cancel-btn").onclick = () => dlg.close();
````

**Texto novo, literal:**

````
  sel.appendChild(new Option("novo álbum…", "__new"));
  if (dest && App.collection.albums.some(a => a.id === dest)) sel.value = dest;   // I3: soltou sobre um album
  inp.value = "";
  const sync = () => { inp.hidden = sel.value !== "__new"; };
  sel.onchange = sync; sync();
  document.getElementById("import-cancel-btn").onclick = () => dlg.close();
````

### E30 — app: soltar o .json sobre um album importa as faixas nele — `app/index.html`

**Ancora, literal:**

````
  const f = e.dataTransfer.files[0];
  if (f) importFromFile(f);
});
````

**Texto novo, literal:**

````
  const f = e.dataTransfer.files[0];
  // I3: sobre um album (o cabecalho na Lista, ou a lateral), as faixas vao para ele.
  const alb = fileDropAlbum(e.target);
  markFileTarget(null);
  if (f && alb && App.saved) readTracksFile(f, alb.id);
  else if (f) importFromFile(f);
});
````

### E31 — app: a barra perde o «editar»; «Importar faixas…» no «⋯» — `app/index.html`

**Ancora, literal:**

````
  const be = document.getElementById("bar-edit");
  be.textContent = "";
  if (App.saved) {
    const mk = (label, role, title, fn) => {
      const b = document.createElement("button");
      b.type = "button"; b.textContent = label; b.dataset.role = role; b.title = title;
      b.addEventListener("click", fn); be.appendChild(b); return b;
    };
    const e = mk("editar", "edit-btn", "Liga a curadoria: mudar a ordem, mover, excluir e importar faixas.", toggleEditing);
    e.setAttribute("aria-pressed", App.editing ? "true" : "false");
    if (App.editing) mk("importar faixas…", "import-tracks-btn", "Traz faixas de outro .json para este acervo.", pickTracksFile);
  }
  const me = document.getElementById("menu-edit");
  me.hidden = !App.saved;
  me.textContent = App.editing ? "Desligar editar" : "Ligar editar";
  document.getElementById("menu-import-tracks").hidden = !(App.saved && App.editing);
````

**Texto novo, literal:**

````
  // I3 (DEC-030): sem o interruptor «editar»; «Importar faixas…» mora no «⋯» da barra.
  document.getElementById("menu-import-tracks").hidden = !App.saved;
````

### E32 — app: sai o ouvinte do «Ligar editar» — `app/index.html`

**Ancora, literal:**

````
document.getElementById("menu-import").addEventListener("click", () => document.getElementById("file-input").click());
document.getElementById("menu-edit").addEventListener("click", toggleEditing);
document.getElementById("menu-import-tracks").addEventListener("click", pickTracksFile);
````

**Texto novo, literal:**

````
document.getElementById("menu-import").addEventListener("click", () => document.getElementById("file-input").click());
document.getElementById("menu-import-tracks").addEventListener("click", pickTracksFile);
````

### E33 — app: no modo de selecao do celular, tocar no titulo marca — `app/index.html`

**Ancora, literal:**

````
  open.addEventListener("click", () => openDetail(song.id));
````

**Texto novo, literal:**

````
  open.addEventListener("click", () => { if (App.selecting && isMobile()) toggleSel(song.id); else openDetail(song.id); });
````

### E34 — app: a linha ganha alca, caixa e «⋯» — `app/index.html`

**Ancora, literal:**

````
  // Clique no resto da linha (estado, BPM, saude) tambem abre; o teclado usa o titulo.
  li.addEventListener("click", e => { if (!e.target.closest("button")) openDetail(song.id); });
  return li;
````

**Texto novo, literal:**

````
  // Clique no resto da linha (estado, BPM, saude) tambem abre; o teclado usa o titulo.
  // I3: no modo de selecao do celular, marca; a caixa e a alca nao contam como clique na linha.
  li.addEventListener("click", e => {
    if (e.target.closest("button, input, label")) return;
    if (App.selecting && isMobile()) toggleSel(song.id); else openDetail(song.id);
  });
  decorateRow(li, song);   // I3: alca, caixa de selecao e «⋯»
  return li;
````

### E35 — app: a saude em duas partes (a marca fica quando o texto cede) — `app/index.html`

**Ancora, literal:**

````
  el.textContent = HEALTH_MARK[h.level] + " " + h.text;
````

**Texto novo, literal:**

````
  // I3: marca e texto separados, para o texto ceder antes do titulo (a marca fica).
  el.textContent = "";
  const mk = document.createElement("span"); mk.className = "hm"; mk.textContent = HEALTH_MARK[h.level];
  const tx = document.createElement("span"); tx.className = "ht"; tx.textContent = h.text;
  el.appendChild(mk); el.appendChild(document.createTextNode(" ")); el.appendChild(tx);
````

### E36 — app: o album da lateral leva o id (alvo do arrastar) — `app/index.html`

**Ancora, literal:**

````
    b.type = "button"; b.className = "side-item" + (n ? "" : " empty-album");
````

**Texto novo, literal:**

````
    b.type = "button"; b.className = "side-item" + (n ? "" : " empty-album");
    if (id) b.dataset.album = id;   // I3: alvo do arrastar e do .json solto
````

### E37 — app: «+ Novo álbum» na lateral, so durante o arrastar — `app/index.html`

**Ancora, literal:**

````
  albums.forEach((a, i) => item(a.title, counts[i], a.id));
}
````

**Texto novo, literal:**

````
  albums.forEach((a, i) => item(a.title, counts[i], a.id));
  // I3: alvo que so aparece enquanto se arrasta uma faixa (o CSS mostra).
  const nl = document.createElement("li"); nl.className = "side-new-li";
  const nb = document.createElement("button");
  nb.type = "button"; nb.className = "side-item side-new"; nb.id = "side-new"; nb.tabIndex = -1;
  nb.textContent = "+ Novo álbum (solte aqui)";
  nl.appendChild(nb); ul.appendChild(nl);
}
````

### E38 — app: a alca aparece quando a copia guardada fica pronta — `app/index.html`

**Ancora, literal:**

````
  renderSideAcervos();   // I2: abrir, importar ou esquecer muda a lista da lateral
}
````

**Texto novo, literal:**

````
  renderSideAcervos();   // I2: abrir, importar ou esquecer muda a lista da lateral
  organizeSavedChanged();   // I3: a copia guardada ficou pronta (ou saiu): a alca aparece (ou some)
}
````

### E39 — app: ir para Cartoes limpa a selecao — `app/index.html`

**Ancora, literal:**

````
  if (v === "cards") closeDetail({ noFocus: true });
````

**Texto novo, literal:**

````
  if (v === "cards") { closeDetail({ noFocus: true }); clearSelection(true); }   // I3: sem caixas em Cartoes
````

### E40 — app: o bloco de organizar — `app/index.html`

**Ancora, literal:**

````
// A abertura e assincrona (IndexedDB); a importacao espera por ela.
````

**Texto novo, literal:**

````
/* ===================================================================
   Organizar (I3, DEC-030, DEC-032 — spec meta/specs/261106-organizar.md)
   Sem o interruptor «editar»: a alca (SortableJS, embutida acima), o «⋯» de
   cada faixa e a selecao em lote ficam sempre a mao num acervo com copia
   guardada (App.saved), que e onde o rascunho mora (DEC-028). Toda operacao
   de rascunho fotografa o acervo antes (beginEdit) para um «Desfazer» — so a
   ultima volta.
   =================================================================== */
App.selection = new Set();   // ids marcados; so os que estao na Lista
App.selecting = false;       // celular: modo de selecao, ligado pelo «⋯»
App.lastSel = null;          // ancora do Shift+clique
App.undo = null;             // a volta da ultima operacao de rascunho
App.dragging = null;         // { id, target, cancelled } enquanto se arrasta

/** Fotografa o que uma operacao de rascunho pode mudar. O rotulo vem depois,
    do aviso da propria operacao (afterEdit). */
function beginEdit() {
  const by = App.ui.usedBy && App.ui.usedBy[App.source];
  const active = {};
  Object.keys(App.activeModules).forEach(id => { active[id] = [...App.activeModules[id]]; });
  App.undo = { label: "", source: App.source, coll: JSON.stringify(App.collection),
               used: by ? JSON.stringify(by) : null, active, bpm: JSON.stringify(App.bpm),
               changes: App.changes, editedAt: App.editedAt };
}
/** «Desfazer»: volta o acervo, as marcas «usei» das faixas que sairam, os
    modulos ligados e o BPM da sessao, e o numero de alteracoes. */
async function undoLast() {
  const u = App.undo;
  if (!u || u.source !== App.source || !App.collection) return;
  App.undo = null;
  closeTrackMenu(false);
  App.collection = JSON.parse(u.coll);
  App.modulesById = {};
  (App.collection.styleModules || []).forEach(m => { App.modulesById[m.id] = m; });
  App.ui.usedBy = App.ui.usedBy || {};
  if (u.used) App.ui.usedBy[u.source] = JSON.parse(u.used); else delete App.ui.usedBy[u.source];
  saveUiState();
  App.activeModules = {};
  Object.keys(u.active).forEach(id => { App.activeModules[id] = new Set(u.active[id]); });
  App.bpm = JSON.parse(u.bpm);
  App.changes = u.changes; App.editedAt = u.editedAt;
  rerender();
  const ok = await persistDraft(false);
  toast("Desfeito: " + u.label + (ok ? "" : " · não consegui guardar no navegador: baixe o .json para não perder"));
}
/** Aviso com um botao (o «Desfazer»). Fica mais que o aviso comum: 8 s. */
function toastAction(msg, label, fn) {
  const t = document.getElementById("toast");
  t.textContent = msg + " ";
  const b = document.createElement("button");
  b.type = "button"; b.className = "toast-btn"; b.textContent = label;
  b.addEventListener("click", () => { t.classList.remove("show", "has-action"); fn(); });
  t.appendChild(b);
  t.classList.add("show", "has-action");
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => t.classList.remove("show", "has-action"), 8000);
}

/* ---- A linha: alca, caixa e «⋯» ---- */
/** Completa a linha da I2. A alca so existe com copia guardada; clicada sem
    arrastar, ela abre o «⋯» (como no Notion). */
function makeGrip(song) {
  const g = document.createElement("button");
  g.type = "button"; g.className = "row-grip"; g.textContent = "⋮⋮";
  g.setAttribute("aria-label", "Arrastar " + song.title + " (ou Alt+↑ e Alt+↓ no título)");
  g.title = "Arraste para mudar de lugar ou de álbum; clique para as ações";
  g.addEventListener("click", () => openTrackMenu(song.id, g));
  return g;
}
function decorateRow(li, song) {
  const t = song.title;
  if (App.saved) li.insertBefore(makeGrip(song), li.firstChild);
  const lab = document.createElement("label");
  lab.className = "row-sel";
  const cb = document.createElement("input");
  cb.type = "checkbox";
  cb.setAttribute("aria-label", "Selecionar " + t);
  cb.checked = App.selection.has(song.id);
  cb.addEventListener("click", e => selectClick(song.id, cb.checked, e.shiftKey));
  lab.appendChild(cb);
  li.insertBefore(lab, li.querySelector(".row-open"));
  const m = document.createElement("button");
  m.type = "button"; m.className = "row-more"; m.textContent = "⋯";
  m.setAttribute("aria-label", "Ações de " + t);
  m.setAttribute("aria-haspopup", "menu"); m.setAttribute("aria-expanded", "false");
  m.addEventListener("click", () => openTrackMenu(song.id, m));
  li.appendChild(m);
}

/* ---- Selecao ---- */
function selectClick(id, checked, shift) {
  if (shift && App.lastSel) {
    const ids = rowIds(), a = ids.indexOf(App.lastSel), b = ids.indexOf(id);
    if (a >= 0 && b >= 0) {
      ids.slice(Math.min(a, b), Math.max(a, b) + 1).forEach(x => { if (checked) App.selection.add(x); else App.selection.delete(x); });
    }
  } else if (checked) App.selection.add(id);
  else App.selection.delete(id);
  App.lastSel = id;
  syncSelection();
}
const toggleSel = id => selectClick(id, !App.selection.has(id), false);
/** A caixa do album: marca as visiveis dele; com todas marcadas, desmarca. */
function selectAlbum(sec) {
  const ids = [...sec.querySelectorAll("li.row")].map(l => l.dataset.id);
  const all = ids.every(id => App.selection.has(id));
  ids.forEach(id => { if (all) App.selection.delete(id); else App.selection.add(id); });
  syncSelection();
}
function clearSelection(quiet) {
  const was = App.selecting;
  App.selection.clear(); App.selecting = false; App.lastSel = null;
  if (quiet) return;
  if (was) afterOrganizeRender(); else syncSelection();
}
/** Caixas, caixa do album, barra de lote. A selecao so guarda o que esta na
    Lista: um filtro que esconde uma faixa marcada tira ela da selecao. */
function syncSelection() {
  const list = currentView() === "list";
  const ids = new Set(list ? rowIds() : []);
  [...App.selection].forEach(id => { if (!ids.has(id)) App.selection.delete(id); });
  document.querySelectorAll("#main li.row").forEach(li => {
    const on = App.selection.has(li.dataset.id);
    li.classList.toggle("selected", on);
    const cb = li.querySelector(".row-sel input");
    if (cb) cb.checked = on;
  });
  document.querySelectorAll("#main section.album").forEach(sec => {
    const cb = sec.querySelector(".album-sel");
    if (!cb) return;
    const rows = [...sec.querySelectorAll("li.row")].map(l => l.dataset.id);
    const n = rows.filter(id => App.selection.has(id)).length;
    cb.checked = n > 0 && n === rows.length;
    cb.indeterminate = n > 0 && n < rows.length;
  });
  const n = App.selection.size;
  const show = list && (n > 0 || (App.selecting && isMobile()));
  document.getElementById("batch").hidden = !show;
  document.body.classList.toggle("has-batch", show);
  document.body.classList.toggle("selecting", list && App.selecting);
  document.getElementById("batch-count").textContent = nPlural(n, "faixa selecionada", "faixas selecionadas");
  const allUsed = n > 0 && [...App.selection].every(isUsed);
  document.getElementById("batch-used").textContent = allUsed ? "Desmarcar usei" : "Marcar usei";
  const why = App.saved ? "" : "Para organizar, importe o .json: a cópia guardada é o rascunho.";
  ["batch-move", "batch-delete"].forEach(k => { const b = document.getElementById(k); b.disabled = !App.saved || !n; b.title = why; });
  ["batch-export", "batch-used"].forEach(k => { document.getElementById(k).disabled = !n; });
}
function enterSelecting(id) {
  closeTrackMenu(false);
  closeDetail({ noFocus: true });
  App.selecting = true;
  App.selection = new Set([id]);
  App.lastSel = id;
  afterOrganizeRender();
}

/* ---- O «⋯» de cada faixa ---- */
let trackMenuFor = null, trackMenuAnchor = null;
function openTrackMenu(id, anchor) {
  const loc = locateSong(id);
  if (!loc) return;
  if (trackMenuFor === id && trackMenuAnchor === anchor) { closeTrackMenu(true); return; }
  closeTrackMenu(false);
  closePopovers(false);
  trackMenuFor = id; trackMenuAnchor = anchor;
  const song = loc.album.songs[loc.index], can = App.saved;
  document.getElementById("track-pop-title").textContent = song.title;
  document.getElementById("tm-move").disabled = !can;
  document.getElementById("tm-up").disabled = !can || loc.index === 0;
  document.getElementById("tm-down").disabled = !can || loc.index === loc.album.songs.length - 1;
  document.getElementById("tm-delete").disabled = !can;
  document.getElementById("tm-select").disabled = currentView() !== "list";
  document.getElementById("tm-note").hidden = can;
  const pop = document.getElementById("track-pop");
  pop.hidden = false;
  document.getElementById("track-backdrop").hidden = !isMobile();
  anchor.setAttribute("aria-expanded", "true");
  if (!isMobile()) {
    // Abaixo do botao, alinhado pela direita; sem espaco embaixo, acima.
    const r = anchor.getBoundingClientRect(), h = pop.offsetHeight, w = pop.offsetWidth;
    const top = r.bottom + 4 + h > window.innerHeight ? Math.max(8, r.top - 4 - h) : r.bottom + 4;
    pop.style.top = top + "px";
    pop.style.left = Math.max(8, Math.min(window.innerWidth - w - 8, r.right - w)) + "px";
  } else { pop.style.top = ""; pop.style.left = ""; }
  const first = [...pop.querySelectorAll('[role="menuitem"]')].find(b => !b.disabled && b.offsetParent !== null);
  if (first) first.focus();
}
function closeTrackMenu(restore) {
  if (!trackMenuFor) return;
  document.getElementById("track-pop").hidden = true;
  document.getElementById("track-backdrop").hidden = true;
  const a = trackMenuAnchor;
  trackMenuFor = null; trackMenuAnchor = null;
  if (a) { a.setAttribute("aria-expanded", "false"); if (restore && a.isConnected) a.focus(); }
}
/** Liga um item do menu: fecha o menu e roda a acao com a faixa dele. */
function trackItem(elId, fn) {
  document.getElementById(elId).addEventListener("click", () => {
    const id = trackMenuFor;
    closeTrackMenu(false);
    const loc = id && locateSong(id);
    if (loc) fn(loc.album.songs[loc.index], id);
  });
}
trackItem("tm-move", (s, id) => openMoveDialog(id));
trackItem("tm-up", (s, id) => moveAndFocus(id, -1));
trackItem("tm-down", (s, id) => moveAndFocus(id, 1));
trackItem("tm-md", s => { downloadFile(slug(s.title) + ".md", songToMarkdown(s, true), "text/markdown"); toast("Faixa exportada: " + s.title); });
trackItem("tm-json", s => exportSongJson(s));
trackItem("tm-select", (s, id) => enterSelecting(id));
trackItem("tm-delete", (s, id) => deleteSong(id));
document.getElementById("tm-cancel").addEventListener("click", () => closeTrackMenu(true));
document.getElementById("track-backdrop").addEventListener("click", () => closeTrackMenu(true));
document.getElementById("detail-more").addEventListener("click", e => { if (App.detailId) openTrackMenu(App.detailId, e.currentTarget); });
document.addEventListener("pointerdown", e => {
  if (!trackMenuFor) return;
  if (document.getElementById("track-pop").contains(e.target) || (trackMenuAnchor && trackMenuAnchor.contains(e.target))) return;
  closeTrackMenu(false);
});
/** Subir/Descer (o menu e Alt+↑/↓) e devolve o foco ao titulo da faixa. */
async function moveAndFocus(id, d) {
  await moveSongBy(id, d);
  const b = rowButton(id);
  if (b) b.focus({ preventScroll: true });
}

/* ---- Lote ---- */
/** A faixa saiu: as marcas «usei», os modulos ligados e o BPM dela tambem. */
function forgetSongMarks(id) {
  const by = App.ui.usedBy && App.ui.usedBy[App.source];
  if (by && by[id]) {
    delete by[id];
    if (!Object.keys(by).length) delete App.ui.usedBy[App.source];
    saveUiState();
  }
  delete App.activeModules[id]; delete App.bpm[id];
}
async function deleteSongs(ids) {
  ids = ids.filter(id => locateSong(id));
  if (!ids.length) return;
  if (ids.length === 1) { await deleteSong(ids[0]); return; }
  if (!(await confirmAsk("Excluir " + ids.length + " faixas deste acervo? Elas continuam no arquivo até você salvar o novo.", "excluir"))) return;
  beginEdit();
  const touched = new Set(), want = new Set(ids);
  App.collection.albums.forEach(a => {
    const before = (a.songs || []).length;
    a.songs = (a.songs || []).filter(s => !want.has(s.id));
    if (a.songs.length !== before) touched.add(a);
  });
  ids.forEach(forgetSongMarks);
  let gone = "";
  touched.forEach(a => { gone += pruneEmpty(a); });
  App.selection.clear();
  await afterEdit(ids.length + " faixas excluídas do rascunho" + gone);
}
/** As N saem como um acervo: nos albuns de origem (id e titulo), com os
    modulos que citam — a mesma forma do exportar de uma faixa (DEC-028). */
function exportSongsJson(ids) {
  const want = new Set(ids), coll = App.collection;
  const json = { schemaVersion: coll.schemaVersion || "1.0", title: (coll.title || "Acervo") + " — " + ids.length + " faixas" };
  if (coll.targetTool) json.targetTool = coll.targetTool;
  json.albums = [];
  const mods = [], seen = new Set();
  let missing = 0;
  (coll.albums || []).forEach(a => {
    const songs = (a.songs || []).filter(s => want.has(s.id));
    if (!songs.length) return;
    json.albums.push({ id: a.id, title: a.title, songs: songs.map(s => JSON.parse(JSON.stringify(s))) });
    songs.forEach(s => (s.styleModules || []).forEach(id => {
      const m = typeof id === "string" ? App.modulesById[id] : null;
      if (!m) { missing++; return; }
      if (seen.has(id)) return;
      seen.add(id); mods.push(JSON.parse(JSON.stringify(m)));
    }));
  });
  if (mods.length) json.styleModules = mods;
  stripInternalKeys(json);
  const name = slug(coll.title || "acervo") + "-" + ids.length + "-faixas.json";
  downloadFile(name, JSON.stringify(json, null, 2), "application/json");
  toast(ids.length + " faixas exportadas em .json: " + name + " · " + nPlural(mods.length, "módulo", "módulos")
    + (missing ? " · " + missing + " módulo(s) citado(s) não existe(m) no acervo" : ""));
}
const selIds = () => rowIds().filter(id => App.selection.has(id));   // na ordem da tela
document.getElementById("batch-move").addEventListener("click", () => openMoveDialog(selIds()));
document.getElementById("batch-export").addEventListener("click", () => exportSongsJson(selIds()));
document.getElementById("batch-delete").addEventListener("click", () => deleteSongs(selIds()));
document.getElementById("batch-clear").addEventListener("click", () => clearSelection());
document.getElementById("batch-used").addEventListener("click", () => {
  const ids = selIds(), all = ids.every(isUsed);
  ids.forEach(id => { if (isUsed(id) === all) toggleUsed(id); });
  const y = window.scrollY; render(); window.scrollTo(0, y);
  toast(nPlural(ids.length, all ? "faixa desmarcada" : "faixa marcada como usada", all ? "faixas desmarcadas" : "faixas marcadas como usadas"));
});

/* ---- Arrastar ---- */
let sortables = [];
function setupSortables() {
  sortables.forEach(s => { try { s.destroy(); } catch (e) { /* lista ja saiu da tela */ } });
  sortables = [];
  if (typeof Sortable === "undefined" || currentView() !== "list" || !App.saved) return;
  if (App.selecting && isMobile()) return;   // no modo de selecao do celular, a alca da lugar a caixa
  document.querySelectorAll("#main ul.rows").forEach(ul => {
    sortables.push(Sortable.create(ul, {
      group: "faixas", handle: ".row-grip", draggable: "li.row",
      animation: 120, forceFallback: true, fallbackOnBody: true, fallbackTolerance: 3,
      delay: 250, delayOnTouchOnly: true, touchStartThreshold: 4,
      ghostClass: "row-ghost", chosenClass: "row-chosen", dragClass: "row-drag",
      scroll: true, scrollSensitivity: 70, bubbleScroll: true,
      onStart: dragStart, onEnd: dragEnd,
    }));
  });
}
/** O alvo da lateral sob o ponteiro (um album, ou «+ Novo álbum»). */
function sideTargetAt(x, y) {
  const el = document.elementFromPoint(x, y);
  return el ? el.closest("#side .side-item[data-album], #side-new") : null;
}
function dragTrack(e) {
  const p = e.touches ? e.touches[0] : e;
  if (!App.dragging || !p) return;
  const t = sideTargetAt(p.clientX, p.clientY);
  if (t === App.dragging.target) return;
  if (App.dragging.target) App.dragging.target.classList.remove("drop-hover");
  App.dragging.target = t;
  if (t) t.classList.add("drop-hover");
}
const DRAG_EVENTS = ["pointermove", "mousemove", "touchmove"];
function dragStart(evt) {
  closeTrackMenu(false);
  App.dragging = { id: evt.item.dataset.id, target: null, cancelled: false };
  document.body.classList.add("dragging-track");
  DRAG_EVENTS.forEach(k => document.addEventListener(k, dragTrack, { capture: true, passive: true }));
}
async function dragEnd(evt) {
  // O SortableJS (modo fallback) marca «ignorar o proximo clique» ao comecar a
  // arrastar, para o soltar sobre a alca nao virar clique. Quando nenhum clique
  // vem do soltar (soltou na lateral, ou longe da alca), a marca fica e engole o
  // proximo clique da pessoa — o «mover» da janela, por exemplo. Este clique
  // sintetico, logo depois, consome a marca; se ela ja foi consumida, nao faz nada.
  setTimeout(() => document.body.dispatchEvent(new MouseEvent("click", { bubbles: true })), 0);
  DRAG_EVENTS.forEach(k => document.removeEventListener(k, dragTrack, { capture: true }));
  document.body.classList.remove("dragging-track");
  const d = App.dragging;
  App.dragging = null;
  if (d && d.target) d.target.classList.remove("drop-hover");
  if (!d || d.cancelled) { rerender(); return; }
  if (d.target) {
    rerender();
    if (d.target.id === "side-new") openMoveDialog([d.id], { forceNew: true });
    else await moveToAlbumEnd(d.id, d.target.dataset.album);
    return;
  }
  if (evt.from === evt.to && evt.oldIndex === evt.newIndex) return;   // soltar no mesmo lugar nao conta
  await dropAt(d.id, evt.item, evt.to);
}
/** Onde a faixa solta cai, na ORDEM COMPLETA do album de destino: logo antes da
    proxima faixa visivel; sem proxima, logo depois da anterior visivel; sem
    nenhuma, no fim. As escondidas por filtro nao mudam de ordem entre si. */
async function dropAt(id, item, ul) {
  const sec = ul.closest("section.album");
  const target = sec && App.collection.albums.find(a => a.id === sec.dataset.album);
  const loc = locateSong(id);
  if (!target || !loc) { rerender(); return; }
  const next = item.nextElementSibling, prev = item.previousElementSibling;
  const nextId = next && next.dataset.id, prevId = prev && prev.dataset.id;
  const before = (target.songs || []).map(s => s.id).join("\n") + "|" + loc.album.songs.map(s => s.id).join("\n");
  const plan = (target.songs || []).filter(s => s.id !== id);
  let i = nextId ? plan.findIndex(s => s.id === nextId) : -1;
  if (i < 0) { const p = prevId ? plan.findIndex(s => s.id === prevId) : -1; i = p >= 0 ? p + 1 : plan.length; }
  const song = loc.album.songs[loc.index];
  plan.splice(i, 0, song);
  const srcAfter = loc.album === target ? plan : loc.album.songs.filter(s => s.id !== id);
  if (plan.map(s => s.id).join("\n") + "|" + srcAfter.map(s => s.id).join("\n") === before) { rerender(); return; }
  beginEdit();
  loc.album.songs.splice(loc.index, 1);
  target.songs = plan;
  const gone = loc.album !== target ? pruneEmpty(loc.album) : "";
  const nextSong = nextId && plan.find(s => s.id === nextId);
  await afterEdit("«" + song.title + "» foi para " + (nextSong ? "antes de «" + nextSong.title + "»" : "o fim de «" + target.title + "»") + gone, id);
}
async function moveToAlbumEnd(id, albumId) {
  const loc = locateSong(id), target = App.collection.albums.find(a => a.id === albumId);
  if (!loc || !target) return;
  if (loc.album === target && loc.index === target.songs.length - 1) return;   // ja e a ultima: nada muda
  beginEdit();
  const [song] = loc.album.songs.splice(loc.index, 1);
  target.songs.push(song);
  const gone = loc.album !== target ? pruneEmpty(loc.album) : "";
  await afterEdit("«" + song.title + "» foi para o fim de «" + target.title + "»" + gone, id);
}
/** Fecho do render() na I3: alcas, selecao e barra de lote. */
let renderedSaved = null;   // o App.saved da ultima Lista desenhada
function afterOrganizeRender() {
  if (currentView() !== "list") { if (App.selection.size || App.selecting) clearSelection(true); }
  renderedSaved = App.collection ? App.saved : null;
  setupSortables();
  syncSelection();
}
/** Abrir e importar desenham a Lista antes de a copia guardada ficar pronta
    (App.saved vem depois do IndexedDB). Quando ela muda, so poe (ou tira) as
    alcas: redesenhar a Lista inteira de novo custava ~60 ms com 205 faixas. */
function organizeSavedChanged() {
  if (!App.collection || renderedSaved === null || renderedSaved === App.saved) return;
  renderedSaved = App.saved;
  document.querySelectorAll("#main li.row").forEach(li => {
    const g = li.querySelector(".row-grip"), loc = locateSong(li.dataset.id);
    if (App.saved && !g && loc) li.insertBefore(makeGrip(loc.album.songs[loc.index]), li.firstChild);
    else if (!App.saved && g) g.remove();
  });
  setupSortables();
  syncSelection();
}

/* ---- Soltar um .json sobre um album ---- */
/** O album sob o arquivo arrastado: o cabecalho na Lista, ou o item da lateral. */
function fileDropAlbum(el) {
  if (!el || !el.closest) return null;
  const head = el.closest("#main section.album[data-album] .album-head");
  if (head) return { el: head, id: head.closest("section.album").dataset.album };
  const side = el.closest("#side .side-item[data-album]");
  return side ? { el: side, id: side.dataset.album } : null;
}
let fileTarget = null;
function markFileTarget(t) {
  if (fileTarget && (!t || fileTarget !== t.el)) fileTarget.classList.remove("file-target");
  fileTarget = t ? t.el : null;
  if (fileTarget) fileTarget.classList.add("file-target");
}
document.addEventListener("dragover", e => { if (hasFiles(e)) markFileTarget(fileDropAlbum(e.target)); });
document.addEventListener("dragleave", e => { if (hasFiles(e) && !dragDepth) markFileTarget(null); });

/* ---- Teclado (em captura: decide antes da I1 e da I2) ----
   Esc: o menu da faixa, depois a selecao (o painel da barra e o detalhe
   ficam com a I1 e a I2). Alt+↑/↓ no titulo: sobe e desce. Ctrl+Z / ⌘Z fora
   de campo de texto: «Desfazer». */
const isTextField = el => !!el && (el.isContentEditable || el.tagName === "TEXTAREA" || el.tagName === "SELECT"
  || (el.tagName === "INPUT" && !["checkbox", "radio", "button", "submit"].includes(el.type)));
document.addEventListener("keydown", e => {
  const t = e.target;
  if (e.key === "Escape") {
    if (App.dragging) {
      // Cancela: a faixa volta. O SortableJS termina o arraste no soltar.
      App.dragging.cancelled = true;
      ["pointerup", "mouseup"].forEach(k => document.dispatchEvent(new MouseEvent(k, { bubbles: true })));
      e.preventDefault(); e.stopImmediatePropagation(); return;
    }
    if (trackMenuFor) { e.preventDefault(); e.stopImmediatePropagation(); closeTrackMenu(true); return; }
    if ((App.selection.size || App.selecting) && !openPop && !document.querySelector("dialog[open]") && !isTextField(t)) {
      e.preventDefault(); e.stopImmediatePropagation(); clearSelection(); return;
    }
    return;
  }
  if (e.altKey && !e.ctrlKey && !e.metaKey && (e.key === "ArrowUp" || e.key === "ArrowDown")
      && t && t.classList && t.classList.contains("row-open")) {
    e.preventDefault(); e.stopImmediatePropagation();
    if (App.saved) moveAndFocus(t.closest("li").dataset.id, e.key === "ArrowUp" ? -1 : 1);
    return;
  }
  if ((e.ctrlKey || e.metaKey) && !e.altKey && !e.shiftKey && e.key.toLowerCase() === "z") {
    if (isTextField(t) || document.querySelector("dialog[open]") || !App.undo) return;
    e.preventDefault(); e.stopImmediatePropagation(); undoLast();
  }
}, true);

// A abertura e assincrona (IndexedDB); a importacao espera por ela.
````

### E41 — validate: oito checagens — `scripts/validate.py`

**Ancora, literal:**

````
Checa sete coisas:
````

**Texto novo, literal:**

````
Checa oito coisas:
````

### E42 — validate: a oitava, no cabecalho — `scripts/validate.py`

**Ancora, literal:**

````
     qualidade do app (QUALITY_LIMITS): o kit nao envelhece separado (DEC-027).
````

**Texto novo, literal:**

````
     qualidade do app (QUALITY_LIMITS): o kit nao envelhece separado (DEC-027).
  8. A SortableJS embutida no app e a 1.15.7 sem mudanca: o sha256 do trecho
     confere com o do Sortable.min.js do npm (DEC-030, DEC-032).
````

### E43 — validate: hashlib — `scripts/validate.py`

**Ancora, literal:**

````
import json
import re
````

**Texto novo, literal:**

````
import hashlib
import json
import re
````

### E44 — validate: a checagem da biblioteca — `scripts/validate.py`

**Ancora, literal:**

````
def main(argv):
````

**Texto novo, literal:**

````
SORTABLE_SHA256 = "bf4241bc73fef7f11c59a283a69fe8051cdd31c6d8ff5a2b9ba219e7831fcf76"
SORTABLE_START = b"/* ---- SortableJS 1.15.7: da linha seguinte ate o fim deste script, o Sortable.min.js do npm sem mudanca ---- */\n"


def check_sortable():
    """A biblioteca de arrastar embutida e a SortableJS 1.15.7 sem mudanca (DEC-032).

    O trecho vai da linha seguinte ao marcador ate o fim do script; o sha256 e o do
    Sortable.min.js do pacote npm sortablejs@1.15.7 (medido em 2026-11-06). Trocar
    de versao e decisao: muda o hash aqui, o comentario no app e a DEC.
    """
    try:
        with open(os.path.join(ROOT, "app/index.html"), "rb") as f:
            s = f.read().replace(b"\r\n", b"\n")   # um checkout com autocrlf poe CRLF; o hash e do arquivo em LF
    except OSError as e:
        print(f"ERRO na biblioteca: nao consegui ler app/index.html: {e}")
        return 1
    i = s.find(SORTABLE_START)
    j = s.find(b"\n</script>", i) if i >= 0 else -1
    if i < 0 or j < 0:
        print("ERRO na biblioteca: o trecho da SortableJS nao esta no app/index.html")
        return 1
    got = hashlib.sha256(s[i + len(SORTABLE_START):j]).hexdigest()
    if got != SORTABLE_SHA256:
        print(f"ERRO na biblioteca: o sha256 da SortableJS embutida mudou ({got[:12]}..., esperado {SORTABLE_SHA256[:12]}...)")
        return 1
    print("OK  biblioteca: SortableJS 1.15.7 embutida sem mudanca")
    return 0


def main(argv):
````

### E45 — validate: chama a checagem — `scripts/validate.py`

**Ancora, literal:**

````
    errors += check_kit()
````

**Texto novo, literal:**

````
    errors += check_kit()
    # biblioteca de arrastar: a SortableJS 1.15.7 sem mudanca (DEC-032)
    errors += check_sortable()
````

### E46 — CHANGELOG: 0.16.0 — `meta/CHANGELOG.md`

**Ancora, literal:**

````
## [0.15.0] — 2026-11-06
````

**Texto novo, literal:**

````
## [0.16.0] — 2026-11-06

Terceira entrega da frente de interface (I3, DEC-030, DEC-032): organizar o acervo sem ligar nada. O cartão não muda.

### Added
- **Arrastar pela alça ⋮⋮** de cada linha da Lista, dentro do álbum ou para outro, com o SortableJS 1.15.7 embutido no app (MIT, sem mudança; o `validate.py` confere o sha256). Com filtro ou busca ligados, a faixa cai logo antes da próxima visível, e o aviso diz onde («… foi para antes de «X»»). Soltar no mesmo lugar não conta alteração.
- **Soltar sobre a lateral:** num álbum, a faixa vai para o fim dele; em «+ Novo álbum», que só aparece durante o arrastar, o app pede o título e cria o álbum com ela.
- **O «⋯» de cada faixa**, na linha, no detalhe e no pé do cartão, com os mesmos itens: Mover para…, Subir, Descer, Exportar .md, Exportar .json e Excluir…. `Alt+↑` e `Alt+↓` no título sobem e descem.
- **Várias de uma vez:** uma caixa por linha e uma por álbum (marca as visíveis), `Shift`+clique para o intervalo e uma barra de lote com Mover para…, Exportar .json (um acervo com as faixas, nos álbuns de origem e com os módulos citados), Marcar usei e Excluir….
- **«Desfazer»** no aviso de cada operação, e `Ctrl+Z` fora dos campos de texto: volta o acervo, as marcas «usei» das excluídas e o número de alterações. Só a última; salvar e trocar de acervo esquecem a volta.
- **Soltar um `.json` sobre um álbum** (o cabeçalho na lista, ou o nome na lateral) abre «importar faixas» com ele escolhido; fora dele, importa como acervo, como antes.
- **Celular:** o «⋯» do detalhe e o toque na alça abrem uma folha de baixo; «Selecionar várias…» liga as caixas de 44 px e a barra de lote; tocar na linha marca. A alça só pega depois de segurar.

### Changed
- **Sem o interruptor «editar».** Organizar vale sempre que o acervo tem cópia guardada no navegador; sem ela (o exemplo do Pages), não há alça, e o «⋯» traz só os Exportar, com a explicação.
- **«Importar faixas…»** mora no «⋯» da barra, também no computador.
- O pé do cartão perde ↑ ↓, «mover…» e «excluir», e ganha o «⋯».

Spec `meta/specs/261106-organizar.md`: 15 de 15 critérios no Chromium headless, com prova de vida no app da 0.15.0. Abrir um acervo de 205 faixas leva de 148 a 159 ms, até cerca de 30 ms a mais que a 0.15.0 nas mesmas rodadas (o limite era 100), e a Lista de 300 faixas desenha em cerca de 60 ms. Os testes das entregas 1 a 3, da I1 e da I2 seguem em 15 de 15, 25 de 25, 19 de 19, 14 de 14 e 15 de 15, com o «⋯» no lugar do «editar». O app passa de 158 KB para 239 KB, 45 KB deles da biblioteca.

---

## [0.15.0] — 2026-11-06
````

### E47 — README: versao — `README.md`

**Ancora, literal:**

````
> **Estado:** v0.15.0 — ferramenta em uso. Lê, guarda e edita vários acervos, copia por campo, troca módulos de estilo, ajusta o BPM, **mede cada prompt contra os limites do Suno**, exporta Markdown, exporta uma faixa como `.json` e **entrega o prompt para chats gerarem canções no esquema**. Publicada no GitHub Pages. Ver `meta/ROADMAP.md`.
````

**Texto novo, literal:**

````
> **Estado:** v0.16.0 — ferramenta em uso. Lê, guarda e edita vários acervos, copia por campo, troca módulos de estilo, ajusta o BPM, **mede cada prompt contra os limites do Suno**, exporta Markdown, exporta uma faixa como `.json` e **entrega o prompt para chats gerarem canções no esquema**. Publicada no GitHub Pages. Ver `meta/ROADMAP.md`.
````

### E48 — README: organizar — `README.md`

**Ancora, literal:**

````
7. Para reorganizar, ligue *editar* na barra: cada cartão ganha ↑ ↓, *mover…* e *excluir*, e *importar faixas…* traz faixas de outro `.json`. As mudanças ficam num rascunho no navegador; a barra mostra quantas são, com *Salvar .json*, que baixa com o nome do arquivo original — substitua o antigo por ele, e ele passa a ser a fonte.
````

**Texto novo, literal:**

````
7. Para reorganizar, não há nada a ligar: na Lista, arraste a faixa pela alça ⋮⋮ (para outra posição, outro álbum ou um álbum da lateral; durante o arrastar, a lateral oferece *+ Novo álbum*), ou use o «⋯» da faixa (*Mover para…*, *Subir*, *Descer*, *Excluir…*; `Alt+↑` e `Alt+↓` no título). Marque as caixas para mover, exportar, marcar ou excluir várias de uma vez. Cada operação mostra *Desfazer* no aviso (ou `Ctrl+Z`), até a próxima. Para trazer faixas de outro `.json`, use *Importar faixas…* no «⋯» da barra, ou solte o arquivo sobre um álbum. As mudanças ficam num rascunho no navegador; a barra mostra quantas são, com *Salvar .json*, que baixa com o nome do arquivo original — substitua o antigo por ele, e ele passa a ser a fonte. Só se organiza um acervo com cópia guardada no navegador (importado por arquivo); no exemplo que o Pages carrega sozinho, o «⋯» só exporta. cada cartão ganha ↑ ↓, *mover…* e *excluir*, e *importar faixas…* traz faixas de outro `.json`. As mudanças ficam num rascunho no navegador; a barra mostra quantas são, com *Salvar .json*, que baixa com o nome do arquivo original — substitua o antigo por ele, e ele passa a ser a fonte.
````

### E49 — README: rascunho e DEC-032 — `README.md`

**Ancora, literal:**

````
O acervo canônico são **arquivos JSON** no esquema: os exemplos versionados em `data/`, e o acervo pessoal fora do repo (DEC-026). O navegador guarda **cópias dos acervos importados** (IndexedDB) e, no localStorage, as marcações por acervo e a estrutura do cartão — cache, nunca a fonte: o menu do seletor de acervo diz de onde a cópia veio e quando, e *Esquecer este acervo* a apaga sem tocar no arquivo. Com *editar*, a cópia vira rascunho até você salvar o `.json` e substituir o arquivo. Ver `meta/DECISIONS.md` (DEC-004, DEC-022, DEC-028, DEC-029, DEC-030, DEC-031).
````

**Texto novo, literal:**

````
O acervo canônico são **arquivos JSON** no esquema: os exemplos versionados em `data/`, e o acervo pessoal fora do repo (DEC-026). O navegador guarda **cópias dos acervos importados** (IndexedDB) e, no localStorage, as marcações por acervo e a estrutura do cartão — cache, nunca a fonte: o menu do seletor de acervo diz de onde a cópia veio e quando, e *Esquecer este acervo* a apaga sem tocar no arquivo. Ao organizar, a cópia vira rascunho até você salvar o `.json` e substituir o arquivo. Ver `meta/DECISIONS.md` (DEC-004, DEC-022, DEC-028, DEC-029, DEC-030, DEC-031, DEC-032).
````

### E50 — README: o validate confere a biblioteca — `README.md`

**Ancora, literal:**

````
Checa todos os `data/*.json` contra o esquema. Rode antes de commitar mudança em `data/` ou `schema/`.
````

**Texto novo, literal:**

````
Checa todos os `data/*.json` contra o esquema e confere que a SortableJS embutida no app é a 1.15.7 sem mudança (pelo sha256). Rode antes de commitar mudança em `data/`, `schema/` ou `app/`.
````

### E51 — DECISIONS: DEC-032 — `meta/DECISIONS.md`

**Ancora, literal:**

````
**Consequências:** (+) A I2 entrega o ganho dela já na primeira abertura. (−) Quem copiava o título pelo clique na Lista passa a abrir o detalhe; o aviso da primeira abertura diz onde está cada coisa. (−) Se a gaveta fizer falta no celular, ela volta como ideia.
````

**Texto novo, literal:**

````
**Consequências:** (+) A I2 entrega o ganho dela já na primeira abertura. (−) Quem copiava o título pelo clique na Lista passa a abrir o detalhe; o aviso da primeira abertura diz onde está cada coisa. (−) Se a gaveta fizer falta no celular, ela volta como ideia.

## DEC-032 — I3: arrastar com filtro pela próxima visível, Cartões só com o «⋯», seleção no celular pelo «⋯»; a SortableJS 1.15.7 embutida com o hash

**Data:** 2026-11-06
**Status:** aceita
**Contexto:** A spec da I3 (`meta/specs/261106-organizar.md`) trouxe três pontos para o dono, decididos por ele em 2026-11-06, os três como recomendados. A DEC-030 deixou para a entrega que trouxesse a biblioteca o registro do hash.
**Decisão:**
- **Arrastar com filtro ou busca ligados é permitido.** A faixa solta cai logo antes da próxima faixa visível, na ordem completa do álbum (sem próxima, logo depois da anterior; sem nenhuma, no fim); as escondidas mantêm a ordem entre si. O aviso diz onde ela foi, e o «Desfazer» volta.
- **Na visão Cartões, só o «⋯», sem arrastar.** A Lista é onde se organiza.
- **No celular, a seleção começa por «Selecionar várias…» no «⋯».** Segurar a linha fica para a alça.
- **A biblioteca:** o `Sortable.min.js` do pacote npm `sortablejs@1.15.7`, sem mudança, num `<script id="lib-sortable">` com a licença MIT acima; sha256 `bf4241bc73fef7f11c59a283a69fe8051cdd31c6d8ff5a2b9ba219e7831fcf76`, conferido pelo `scripts/validate.py` a cada execução. Trocar de versão é decisão, não acidente.
**Alternativas consideradas:** desligar a alça com filtro ligado (mais previsível, menos à mão); arrastar também a grade de Cartões (impreciso com cartões de 700 px); segurar a linha para selecionar no celular, como nos apps de e-mail (o mesmo gesto da alça, a poucos milímetros); carregar a biblioteca de uma CDN (quebraria o `file://` sem rede).
**Consequências:** (+) Organizar fica sempre à mão, sem o interruptor, com um caminho sem arrastar para tudo (o «⋯», WCAG 2.5.7). (+) O hash no `validate.py` torna visível qualquer mudança na biblioteca. (−) São 45 KB de código de terceiro no app; abrir 205 faixas ficou até cerca de 30 ms mais lento que na 0.15.0. (−) A SortableJS, no modo de arrastar que o app usa, engole o primeiro clique depois de soltar; o app desfaz isso com um clique sintético ao fim de cada arrastar (comentado em `dragEnd`), e uma versão nova pede reconferir. (−) Com filtro ligado, pode haver faixas escondidas entre a solta e a vizinha; o aviso e o «Desfazer» seguram.
````

### E52 — IDEAS: i-048 entregue (1) — `meta/IDEAS.md`

**Ancora, literal:**

````
### i-048 💡 Edição e organização com UX de verdade, arrastando onde for útil
````

**Texto novo, literal:**

````
### i-048 ✅ Edição e organização com UX de verdade, arrastando onde for útil
````

### E53 — IDEAS: i-048 entregue (2) e as ideias novas — `meta/IDEAS.md`

**Ancora, literal:**

````
**Planejada (DEC-030):** é a I3 (0.16.0): arrastar pela alça, com o SortableJS embutido; o «⋯» por faixa como caminho sem arrastar; seleção em lote; «Desfazer»; o fim do interruptor «editar».
````

**Texto novo, literal:**

````
**Entregue (DEC-030, DEC-032):** a I3 (0.16.0): arrastar pela alça, com a SortableJS embutida; o «⋯» por faixa como caminho sem arrastar; seleção em lote; «Desfazer»; o fim do interruptor «editar»; soltar o `.json` sobre um álbum. Ficaram de fora e viraram ideias próprias: organizar os álbuns (i-049) e arrastar uma faixa para outro acervo (i-050).

### i-049 💡 Organizar os álbuns
`[capturada pelo chat, 2026-11-06, na spec da I3]` Renomear um álbum, reordenar os álbuns arrastando na lateral e juntar dois. A I3 organiza as faixas; os álbuns só nascem (pelo «+ Novo álbum» ou pelo «Mover para…») e somem quando esvaziam. Fora da I3 por escopo.

### i-050 💡 Arrastar uma faixa para outro acervo
`[relatado pelo dono, 2026-11-05, na i-048]` Soltar uma faixa sobre outro acervo da lateral para copiá-la ou movê-la para ele. Mexe em dois rascunhos de uma vez (e em dois arquivos a salvar), e pede uma análise própria antes da spec. Hoje o caminho é exportar a faixa em `.json` e importá-la no outro acervo.
````

### E54 — ROADMAP: I3 entregue — `meta/ROADMAP.md`

**Ancora, literal:**

````
- 🔨 Frente de interface (i-043 a i-048, DEC-030), em quatro entregas: ✅ barra única, com o seletor de acervo, os filtros com etiquetas e o «⋯» (0.14.0) · ✅ lista e detalhe, com a lateral de álbuns e acervos (0.15.0) · ⬜ organizar: arrastar, «⋯» por faixa, lote, «Desfazer», sem o interruptor «editar» (0.16.0) · ⬜ salvar direto no arquivo (0.17.0, i-043).
````

**Texto novo, literal:**

````
- 🔨 Frente de interface (i-043 a i-048, DEC-030), em quatro entregas: ✅ barra única, com o seletor de acervo, os filtros com etiquetas e o «⋯» (0.14.0) · ✅ lista e detalhe, com a lateral de álbuns e acervos (0.15.0) · ✅ organizar: arrastar, «⋯» por faixa, lote, «Desfazer», sem o interruptor «editar» (0.16.0) · ⬜ salvar direto no arquivo (0.17.0, i-043).
````

### E55 — STATUS inteiro — `meta/STATUS.md`

**Arquivo inteiro, literal** (substitui o arquivo; chegada `8c330ae7be3ab8620eb0b37cbda7203749fd6643`):

````
# STATUS.md — Cancioneiro

> **O agora.** O que funciona, o que está em progresso, o que está quebrado, backlog curto.
> Rolante: item resolvido sai daqui e vai para o CHANGELOG. Médio/longo prazo vive no ROADMAP.

**Versão atual:** 0.16.0 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveniências de uso concluídos e conferidos · os álbuns antigos convertidos (i-008, fora do repo) · curadoria no app concluída nas três entregas (DEC-028, DEC-029) · frente de interface na I3 de quatro (DEC-030 a DEC-032) · kit de música lido pelo KCM, à espera da resposta (i-039)

---

## Última conversa (2026-11-06, I3: protótipo, spec e implementação, WO 0027)

- **I2 conferida na tela pelo dono** (roteiro OK `[relatado pelo dono]`): lista e detalhe (0.15.0) estão fechados.
- **I3, organizar (0.16.0):** protótipo no canvas «Cancioneiro: nova interface» (fileira da I3), spec `meta/specs/261106-organizar.md` e os três pontos decididos pelo dono como recomendados (DEC-032): arrastar com filtro pela regra da próxima visível, Cartões só com o «⋯», seleção no celular pelo «⋯». 15 de 15 critérios no Chromium headless, testados pelo chat.
- **Este bloco substitui o anterior, da WO 0026** (I2). O que ele dizia está no CHANGELOG [0.15.0], na spec `meta/specs/261106-lista-e-detalhe.md` e em `logs/2026-11-06.md` (Conversas 1 a 3).

## Funciona (pronto)

- **Ferramenta `app/index.html`:** importa/carrega JSON, cartões por álbum, copiar Style/Lyrics/Exclude por botão (o botão entrega o texto que está na tela — FIX-007), marca «usei», filtros por álbum/estado/uso, busca, módulos de estilo que recompõem o Style ao vivo, variantes e notas recolhíveis, «Baixar .json» limpo e «Importar .json» que saneia chaves internas e diz quantas removeu (FIX-004/006). A versão aparece no cabeçalho. A importação avisa quantos módulos citados não existem na coleção (FIX-009).
- **Painel de qualidade (0.5.0, DEC-018):** linha abaixo de Style, Lyrics e Exclude com caracteres contra o limite do campo, tags do Style e negações «no X». Vermelho só para truncamento.
- **Custo de cada módulo no chip (0.6.0, DEC-019):** com o painel de módulos aberto, cada chip mostra `−N`, `+N` ou `0` tags; a linha de qualidade diz quanto o style base usa sozinho quando o recomposto passa de 10.
- **Controle de BPM no cartão (0.7.0, DEC-020):** campo 20-300 com `−5`/`+5` e «voltar a N» governa todo «NN bpm» do Style principal; o chip de andamento é atalho (no máximo um ligado); variantes e «Baixar .json» não mudam; o valor é só da sessão.
- **Esquema JSON canônico** (`schema/`). Biblioteca de referência para autoria em `schema/style-modules.json` (27 módulos, sete camadas); cada acervo traz os seus (DEC-016).
- **Datasets:** `data/exemplo-cinzeiro.json` (1 faixa, com os 5 módulos que cita) e `data/demo.json` (2 álbuns, 3 faixas). Os acervos do dono moram fora do repo (DEC-026): `../album-referencias (1).json` (7 faixas, 50 módulos) `../acervos/rainha-da-preguica.json` (10 álbuns, 151 faixas) e `../acervos/albuns-reagrupados.json` (12 álbuns, 205 faixas), os dois gerados pelos conversores.
- **Conversor da família BR** (`scripts/convert_br.py`, 0.9.1, DEC-026): guias `..._VOL<n>_GUIA.md` → coleção no esquema, um álbum por volume, rótulos fora do copiável, variantes e referência levadas; relata o que passa do limite do Suno sem cortar. Teste: `python3 scripts/test_convert_br.py`.
- **Conversor dos guias de `Albuns/`** (`scripts/convert_guides.py`, 0.10.0): formatos mistos → coleção, com mapa de grupos que reprova faixa perdida. Teste: `python3 scripts/test_convert_guides.py`.
- **Kit de música** (`kit-musica/`, 0.10.0, DEC-027): bloco para Instruções e CEREBRO de um projeto de música, skills `macetes-suno` e `revisar-faixa`. Uso à mão em `kit-musica/README.md`.
- **Validação** (`scripts/validate.py`): sintaxe, esquema (com `jsonschema`), integridade referencial dos módulos (id ausente ou objeto no lugar do id, sem traceback — FIX-009), versão igual nos quatro lugares, um BPM só por faixa (DEC-020) e as marcações do prompt que o app lê (DEC-021) e os limites da skill `revisar-faixa` contra o app (DEC-027); código 1 se falhar; a última linha diz se o esquema foi de fato conferido.
- **Export MD** (faixa / álbum / acervo), com o rótulo fora do bloco e o Style da tela nos três (0.9.0, D5).
- **Exportar faixa como `.json`** (0.11.0, DEC-028): botão no rodapé do cartão; a faixa sai como acervo — o álbum de origem (id e título), a faixa e os módulos que ela cita — e importa como qualquer acervo. Sai o dado do acervo, não os módulos ligados nem o BPM da tela; o toast conta os módulos e os citados que não existem. Conferido na tela pelo dono em 2026-11-04.
- **Vários acervos no navegador** (0.12.0, DEC-028): cada importado fica no IndexedDB pelo nome do arquivo; o seletor de acervo, na barra, abre ou esquece cada um; reabre no último aberto; marcas «usei» por acervo. Sem IndexedDB, guarda só o último, como antes.
- **Curadoria pela tela** (0.13.0, DEC-028, DEC-029): mover, novo álbum, excluir e importar faixas num rascunho gravado no navegador; «● N alterações não salvas» com «Salvar .json» pelo nome de origem. Desde a 0.16.0, sem o interruptor «editar».
- **Organizar** (0.16.0, DEC-030, DEC-032): arrastar pela alça ⋮⋮ na Lista (com filtro, antes da próxima visível) e para os álbuns da lateral ou «+ Novo álbum»; o «⋯» de cada faixa (linha, detalhe e cartão) com Mover, Subir, Descer, Exportar e Excluir, e `Alt+↑`/`Alt+↓`; caixas e barra de lote; «Desfazer» e `Ctrl+Z` da última operação; soltar o `.json` sobre um álbum importa faixas nele. Só com cópia guardada no navegador. A SortableJS 1.15.7 vai embutida, com o hash no `validate.py`.
- **Lista e detalhe** (0.15.0, DEC-030, DEC-031): Lista (padrão) ou Cartões; uma linha por faixa com Style, Lyrics, ✓ e a saúde do prompt; o cartão de hoje ao lado, com ‹ ›, setas e `#faixa=<id>` no endereço; a lateral de álbuns e acervos a partir de 1280 px; no celular, o detalhe em tela própria com os botões de copiar no pé.
- **Barra única** (0.14.0, DEC-030): fixa, de 48 px; seletor de acervo como menu, busca com `/`, Filtros num painel com etiquetas removíveis e «N de M», rascunho e o «⋯» com Importar, Importar faixas, Baixar, Exportar .md, Prompt para chats, Baixar exemplo e Estrutura do cartão. No celular, 51 px, botões de 44 px, a busca numa linha própria e o rascunho no pé.
- **Prompt-modelo** (`schema/PROMPT-PARA-CHATS.md`, DEC-021, DEC-023): contrato de módulo, style com 6 a 8 tags e até 10 com os módulos ligados; pede o JSON como arquivo e, sem arquivo, em bloco de código. Dois retestes em 2026-10-29: 6 de 6 faixas dentro do contrato e do orçamento, nos dois.
- **«Prompt para chats» e «Baixar exemplo»** (0.8.0, DEC-021; no «⋯» desde a 0.14.0): buscam o prompt e o `data/demo.json` do repositório no clique; a janela do prompt recebe o «Meu pedido».
- **Conveniências (0.9.0, DEC-022, DEC-023):** «Estrutura» do cartão (ordem e blocos visíveis, no navegador); copiar o título; arrastar o `.json` para importar; o último acervo importado volta ao abrir, com origem, data e «esquecer»; a importação aceita a resposta do chat colada inteira e avisa.
- **Publicado no GitHub Pages** em `https://joaolucas-nds.github.io/cancioneiro/app/index.html` — o push em `main` publica.

## Em progresso

- **Kit de música no KCM (i-039)** — o KCM leu a carta 01 e responde por carta, sem data. Gatilho: sem resposta até o primeiro projeto de música novo, o projeto usa o kit à mão (`kit-musica/README.md`).

## Quebrado / pendências que travam

- (nada quebrado)

## Pendências do dono

- **Conferir a I3 na tela** — roteiro na conversa de 2026-11-06 (WO 0027), depois do push, no computador e no celular.
- **Instalar o validador de esquema nesta máquina.** Sem `jsonschema` e `referencing`, o `validate.py` só confere sintaxe e diz `ESQUEMA NAO CONFERIDO` na última linha. Uma vez, no CMD: `pip install jsonschema referencing --break-system-packages`. Depois, `python3 scripts/validate.py` deve terminar em `Tudo conforme ao esquema.`

## Backlog curto (próximas ações concretas)

1. **I4 — Salvar no arquivo** (i-043, DEC-030) — protótipo no canvas, depois spec: gravar o rascunho direto no `.json` de origem onde o navegador deixar, sem baixar e substituir à mão.
2. **Organizar os álbuns** (i-049) — renomear, reordenar na lateral, juntar dois; candidata depois da I4.
3. **Rampa de BPM** (i-042) — três faixas BR reprovam no `validate.py` por mudarem de andamento de propósito.
4. **Pesquisar outras plataformas de música por IA** (i-032) — um turno de pesquisa antes de qualquer mudança de esquema.
5. **Avisar palavra de andamento que contradiz o BPM** (i-029) — pede uma tabela palavra → faixa de BPM, com fonte e data.
6. **Importar prompts prontos dos álbuns como módulos** — o último ⬜ da 3b no ROADMAP; o índice-mestre da BR e os «estilos originais» do VOL5 trazem fórmulas de estilo.

## Notas de estado

- **Repo local do dono:** `C:\Users\alexk\Tools\cancioneiro\cancioneiro` (Windows). O chat lê e grava na pasta vinculada; commit e push são do Code (DEC-010). A pasta-pai guarda relatórios, notas e o acervo do dono, fora do Git; o lido vai para `../notas-arquivadas/`.
- **Canal:** pasta vinculada é o padrão; a cópia achatada (FlatDrop) é reserva (DEC-017).
- **Limites do Suno:** o v6 saiu em 2026-09-09 e a nota oficial não documenta limite de campo; os números do painel vêm de fonte secundária, com fonte e data no `QUALITY_LIMITS` (DEC-018). Outra fonte secundária (2026-08) põe o ideal em 4 a 7 descritores; o prompt usa 6 a 8. Reconferir quando houver documentação oficial. O `meta/HISTORY.md` §5 ganhou a interface do v6 vista na conta (2026-10-29); o resto do arquivo ainda descreve o v5.5.
- **Exclude no v6-mini:** o formulário gratuito não tem o campo (capturas de 2026-10-29). Desde a 0.9.1 (DEC-025) o bloco vem oculto por padrão, com o aviso «no X → Exclude» junto (D3); o dado continua no JSON e no export. Quem usa o campo liga em «Estrutura».
- **Navegador (DEC-004, DEC-022, DEC-028):** guarda as cópias dos acervos importados (IndexedDB, banco `cancioneiro`), as marcas «usei» por acervo e a estrutura do cartão (`localStorage`, `cancioneiro:ui`). As cópias são cache: se o arquivo mudou fora, importe de novo; o menu do seletor de acervo diz quando a cópia foi feita. Os avisos de primeira abertura guardam `tour14` (0.14.0) e `tour15` (0.15.0), e a visão escolhida, `view`, no mesmo `cancioneiro:ui`.
- **Rascunho (DEC-028, DEC-029, DEC-032):** com alterações, a cópia guardada está à frente do arquivo até «Salvar .json» e substituir. A marca na barra é o lembrete; esquecer e reimportar pedem confirmação. O «Desfazer» guarda só a última operação, na memória da aba: recarregar a página o esquece.
- **No `file://`, todas as páginas locais dividem o armazenamento** (sonda de 2026-11-04): o app só lê e grava o que tem o nome `cancioneiro`. O `file://` e o Pages são origens diferentes — o que está guardado num não aparece no outro.
- **Conversores são de primeira geração (DEC-028):** depois de mudar um acervo (à mão ou, com a entrega 3, no app), não rode o conversor por cima dele.
- **«Prompt para chats» e «Baixar exemplo»:** dependem de rede e do Pages. No `file://`, só funcionam se o Pages aceitar o `fetch` de uma página local — não conferido (o dono abriu o `file://` em 2026-10-29, sem relatar o resultado do botão); sem isso, a janela mostra o link para a versão publicada (DEC-021).
- **Estado de sessão** (módulos ligados e BPM escolhido) sobrevive a filtro, busca e «marcar usei»; volta ao acervo ao recarregar a página ou importar de novo (FIX-008, DEC-020).
- **Limite conhecido:** `tryAutoLoad` (carregamento automático pelo Pages) não saneia chaves internas — só a importação por arquivo faz isso. Inócuo enquanto nenhum acervo contaminado for para `data/`.
- **Pendência de contexto — ASU:** o dono perguntou se o «modo ASU» do KCM seria melhor que o modo Code para este projeto; ficou pendente até ele trazer a descrição do ASU `[relatado pelo dono, sem material de apoio]`.
- Design: na recomposição do Style a base manda — desligar um módulo não remove o que já está no style base; módulos só somam. O dedup compara sequências de palavras (FIX-003). Os módulos de gênero e de andamento costumam custar 0 tag por isso (DEC-019). O chip de andamento é atalho do controle de BPM, no máximo um ligado (DEC-020).
````

## Fora de escopo

- A I4 (salvar direto no arquivo, i-043), organizar os albuns (i-049) e arrastar uma faixa para outro acervo (i-050).
- Spec, CONTEXT e log: ja gravados pelo chat; nao edite.
- Nada em `data/`, `schema/` ou `kit-musica/`. Em `scripts/`, so o `validate.py`.

## Armadilhas desta WO

- **A edicao da biblioteca traz uma linha de 45.478 bytes** (o `Sortable.min.js` inteiro, minificado). **Nao redigite nem reformate:** copie o bloco por script, byte a byte. Qualquer mudanca nela reprova a checagem 2 (`ERRO na biblioteca`) e a 1 (hash do app). Ela nao tem quatro crases nem `</script` dentro.
- **`autocrlf=true` na maquina do dono:** os hashes valem no disco em LF, antes do `add`. Nao rode `git checkout -- <arquivo>`: ele regrava em CRLF. O `validate.py` confere o sha256 da biblioteca lendo o app em bytes e trocando CRLF por LF antes, entao o checkout em CRLF nao o reprova; o sha1 da checagem 1, sim.
- **As edicoes do CSS e do bloco de codigo da I3 sao longas** (antes de «A abertura e assincrona»): se o aplicador ler ancora linha a linha, compare o bloco inteiro; o hash de chegada do `app/index.html` e a prova.
- **O `validate.py` desta maquina termina em `ESQUEMA NAO CONFERIDO`** (falta `jsonschema`): estado conhecido. A linha da biblioteca nao depende do `jsonschema`.
- **Os testes escrevem no stderr:** use `2>&1 >/dev/null | tail -1`.

## Depois de aplicar — conferencia antes do commit

| # | Checagem | Comando | Esperado |
|---|---|---|---|
| 1 | **Os onze arquivos sao os testados** | `sha1sum app/index.html scripts/validate.py README.md meta/CHANGELOG.md meta/DECISIONS.md meta/IDEAS.md meta/ROADMAP.md meta/STATUS.md meta/specs/261106-organizar.md meta/CONTEXT.md logs/2026-11-06.md` | a coluna **chegada**, os onze. **Prova as 55 edicoes.** |
| 2 | Validacao | `python3 scripts/validate.py; echo "exit=$?"` | `exit=0`, com as linhas `OK  versao 0.16.0 igual em CHANGELOG, app, README e STATUS` e `OK  biblioteca: SortableJS 1.15.7 embutida sem mudanca`; ultima linha `Tudo conforme ao esquema.` ou `ESQUEMA NAO CONFERIDO (...)` (esta maquina) |
| 3 | Os conversores seguem passando | `python3 scripts/test_convert_br.py 2>&1 >/dev/null \| tail -1` e `python3 scripts/test_convert_guides.py 2>&1 >/dev/null \| tail -1` | `OK` e `OK` |
| 4 | O codigo novo, e o interruptor fora | `grep -c 'id="lib-sortable"' app/index.html`, `grep -c '^function openTrackMenu' app/index.html`, `grep -c '^async function undoLast' app/index.html`, `grep -c 'toggleEditing\|bar-edit\|menu-edit' app/index.html` | `1`, `1`, `1`, `0` |
| 5 | O registro | `grep -m1 '^## \[' meta/CHANGELOG.md`, `grep -c '^## DEC-032 ' meta/DECISIONS.md`, `grep -c '^### i-048 ✅' meta/IDEAS.md`, `grep -c '^### i-049 💡\|^### i-050 💡' meta/IDEAS.md` | `## [0.16.0] — 2026-11-06`, `1`, `1`, `2` |
| 6 | A pendencia resolvida saiu | `grep -c '^- \*\*Conferir a I2 na tela' meta/STATUS.md`, `grep -c '^- \*\*Conferir a I3 na tela' meta/STATUS.md` | `0`, `1` |
| 7 | Nada alem do previsto | `GIT_OPTIONAL_LOCKS=0 git status --short --untracked-files=all` | os onze arquivos e esta WO, e nada mais (nenhum `.txt`, nenhum `__pycache__`) |

**Os tres campos de cada passo:** as sete sao rodadas por **quem aplica (o Code)**, na raiz do repo, em Git Bash,
com `LC_ALL=C.UTF-8`. **Chega no ramo?** A checagem 1 cobre os onze arquivos inteiros, inclusive o `app/index.html`
que o chat executou (`setupSortables`, `dropAt`, `dragEnd`, `openTrackMenu`, `syncSelection`, `beginEdit`, `undoLast`,
`openMoveDialog`, `readTracksFile`). **Esta e qual pergunta?** A 2 e a 3 respondem «funciona?»; as outras, «esta la?».
O «funciona?» do arrastar no navegador do dono e dele, depois do push, pelo roteiro do chat.

## Relatorio de aplicacao

Grave em `../261106-HHMM-code-cancioneiro-apply-wo0027.txt`, com o `HHMM` de `date +%y%m%d-%H%M` rodado na
hora. Diga o resultado da checagem 1 em primeiro lugar.

**Proximo comando** (ultima linha do relatorio, cru e sozinho):

```
/wrap
```

## Commit

```
git add app/index.html scripts/validate.py README.md meta/CHANGELOG.md meta/DECISIONS.md meta/IDEAS.md meta/ROADMAP.md meta/STATUS.md meta/specs meta/CONTEXT.md logs/2026-11-06.md meta/workorders
```

```
git commit -m "feat: organizar o acervo, versao 0.16.0" -m "Frente de interface, entrega I3 (DEC-030, DEC-032): sem o interruptor editar; arrastar pela alca na Lista e para a lateral, com a SortableJS 1.15.7 embutida e o hash conferido pelo validate.py; o menu de cada faixa; selecao e barra de lote; Desfazer e Ctrl+Z; soltar o .json sobre um album. Spec com o resultado, CONTEXT, IDEAS (i-048, i-049, i-050), ROADMAP, README, STATUS inteiro."
```

```
git push
```
