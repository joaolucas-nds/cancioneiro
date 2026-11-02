# WO 0022 — Exportar faixa como .json (curadoria, entrega 1), DEC-028 e versao 0.11.0

## Cabecalho

> **Tipo:** mista — CODIGO (`app/index.html`, cabecalho dos dois conversores) e registro (DEC-028, IDEAS, ROADMAP, CHANGELOG, README, STATUS inteiro).
> **Config sugerida:** Sonnet · `/effort medium`. 17 edicoes literais e o STATUS inteiro, aplicados e testados pelo chat num clone de `b9a07da`; cada arquivo tem hash de chegada.
> **Pre-requisito:** commit `b9a07da`, branch `main`, sincronizada com `origin/main`. O `git status` mostra **so** o que o chat gravou: `M logs/2026-11-02.md`, `M meta/CONTEXT.md`, `M meta/analises/261102-ANALISE-curadoria-no-app.md`, `?? meta/specs/261102-exportar-faixa-json.md` e esta WO (`?? meta/workorders/...wo0022...`).
> **Base:** analise `meta/analises/261102-ANALISE-curadoria-no-app.md`, decidida pelo dono em 2026-11-02 (F1 + G1, entregas 1 → 2 → 3, o `.json` curado manda sobre os conversores); spec `meta/specs/261102-exportar-faixa-json.md`.
> **Depende de:** WO 0021, ja aplicada (`b03dcc8`, wrap `c7927b3`).
>
> **Arquivos — partida e chegada, os dois medidos pelo chat** (em LF; chegada = aplicar literalmente as edicoes abaixo):
>
> | arquivo | partida (sha1) | chegada (sha1) |
> |---|---|---|
> | `app/index.html` | `492bf70c278df44f5c93bfea922eb107f57ffe4d` | `0cecb28694af6fb7022ed86a812793c1a49740e6` |
> | `README.md` | `d76009fef63217e421221ec429b5a27b2f109528` | `22964e30a7e3d41910be8f85ed9189a6521d4261` |
> | `scripts/convert_br.py` | `ec91466a05fc16f6a65e1e1b3cbb8fec95b0c158` | `aa686dba61637555a2141464af7b3705db78a44d` |
> | `scripts/convert_guides.py` | `babdcd4968782c2efc2a89ac87e4be1a03a3b1b8` | `f352d1bd9010e46442c54e312fbd37ac04ee97f4` |
> | `meta/CHANGELOG.md` | `ab37dc656fd5f59fe305998764bd0e60d5e8b6b2` | `5b6e87be4591189087c9eb07a5ba27db0c3d03ab` |
> | `meta/DECISIONS.md` | `f1649e2cf9f3c40ecd33c252f5cf5ee145552421` | `5bd8181db118f1b600484080e553e326990e69a8` |
> | `meta/IDEAS.md` | `46b11df4e4079c766e66d1d5b871fa7bff0001fd` | `7f2c164da87b0465e534c3c032c2ce27f551e5aa` |
> | `meta/ROADMAP.md` | `35478d9b3c0cf02f6ccb9b9f1498756b19c63728` | `136a685a25a6e349909e77f3beb0e18863b8d5c4` |
> | `meta/STATUS.md` | `e8e05223efd3bd9a010260cbab2ff0da7308e258` | `8fc2112fdd2d10341f309c023c5542fbea7d359c` |
> | `meta/specs/261102-exportar-faixa-json.md` | `c489f41a3b74fa90569c42dcc8db4f7611ee8203` | `c489f41a3b74fa90569c42dcc8db4f7611ee8203` (gravado pelo chat; so versiona) |
> | `meta/analises/261102-ANALISE-curadoria-no-app.md` | `145dda814e9fee6c0eba8ffb12f40f83f9849de6` | `145dda814e9fee6c0eba8ffb12f40f83f9849de6` (gravado pelo chat; so versiona) |
> | `meta/CONTEXT.md` | `c77c8c39379cf86685cf9449f94879cb4403a9f1` | `c77c8c39379cf86685cf9449f94879cb4403a9f1` (gravado pelo chat; so versiona) |
> | `logs/2026-11-02.md` | `5d91ac664856c10a537fe397e010a8f40eb0452c` | `5d91ac664856c10a537fe397e010a8f40eb0452c` (gravado pelo chat; so versiona) |
>
> **Ancora semantica:** se um trecho-ancora nao bater EXATAMENTE, PARE e reporte.
> **Idempotencia:** antes de cada edicao, procure o texto NOVO INTEIRO; se ja estiver la, PULE e diga no relatorio. Arquivo inteiro (E18): se o hash ja for o de chegada, PULE.
> **Ancoras lidas em:** cada ancora foi recortada pelo chat do arquivo de partida (`git show b9a07da:<arquivo>`, igual ao disco do dono pelos hashes da coluna partida, medidos no disco em 2026-11-02) e conferida como ocorrendo **exatamente 1 vez** no estado em que a edicao e aplicada, na ordem abaixo. Ancora sempre de linha inteira.
> **Canal dos meta neste ciclo = CODE:** esta WO e o registro. A spec, a analise, o CONTEXT e o log ja estao gravados pelo chat (DEC-010); a WO so os versiona.

---

## 1. Por que

O dono decidiu a analise da curadoria (i-040, i-041). Esta WO entrega a **primeira das tres entregas** e registra a decisao:

- **Exportar faixa como `.json`:** botao «exportar .json» no rodape de cada cartao. A faixa sai como acervo — album de origem (id e titulo), a faixa, os modulos que ela cita —, com o dado do acervo e nao o estado da sessao. Detalhe e criterios na spec.
- **DEC-028:** F1 (o arquivo e a fonte; a curadoria edita um rascunho marcado), G1 (acervos no IndexedDB, marcas por acervo), o `.json` curado manda sobre os conversores, e a ordem das entregas. A DEC-022 ganha a nota de revisao.
- **Registro:** IDEAS (i-039: o KCM leu a carta 01; i-040 em desenvolvimento; i-041 decidida; i-043 nova, gravar direto no arquivo), ROADMAP, CHANGELOG 0.11.0, README, o aviso de «primeira geracao» nos dois conversores, e o STATUS inteiro (sai a pendencia «levar a carta 01»; saem os dois itens que o `/wrap` anexou no fim; entram o roteiro de tela e a sonda como pendencias do dono).

O app de chegada foi executado pelo chat no Chromium headless (`file://`): **15 de 15** criterios da spec, com prova de vida no app de partida (reprova). `validate.py` exit=0, `test_convert_br.py` e `test_convert_guides.py` OK.

**Versao 0.11.0 nesta WO** (os quatro lugares que o `validate.py` confere). A conferencia de tela e do dono, depois do push.

## Edicao 0 — Conferencia de hash e de arvore

```
sha1sum app/index.html README.md scripts/convert_br.py scripts/convert_guides.py meta/CHANGELOG.md meta/DECISIONS.md meta/IDEAS.md meta/ROADMAP.md meta/STATUS.md meta/specs/261102-exportar-faixa-json.md meta/analises/261102-ANALISE-curadoria-no-app.md meta/CONTEXT.md logs/2026-11-02.md
GIT_OPTIONAL_LOCKS=0 git status --short
```

Os treze batem com a coluna **partida**; o `git status` mostra exatamente as cinco linhas do Pre-requisito. Qualquer outra coisa: **PARE e reporte**.

## Edicoes E01 a E18

Na ordem. **Todas as secoes de edicao tem o mesmo titulo, `### Exx — ...`**, inclusive a de arquivo inteiro.
Copie o que esta ENTRE as linhas de quatro crases, sem elas. **O bloco termina na linha de quatro crases, nunca
num titulo:** a DEC-028, o CHANGELOG e o STATUS trazem `## ` e `### ` dentro do bloco.

### E01 — app: versao — `app/index.html`

**Ancora, literal:**

````
    <span class="version" data-role="app-version">v0.10.0</span>
````

**Texto novo, literal:**

````
    <span class="version" data-role="app-version">v0.11.0</span>
````

### E02 — app: exportar faixa como .json, as funcoes — `app/index.html`

**Ancora, literal:**

````
/* ===================================================================
   Export para Markdown (legivel, para colar num chat/Projeto)
````

**Texto novo, literal:**

````
/* ===================================================================
   Export de uma faixa como .json (i-040, entrega 1 — spec
   meta/specs/261102-exportar-faixa-json.md, DEC-028)
   A faixa sai como uma colecao completa: o album de origem (so id e
   titulo), a faixa e os modulos que ela cita. Assim o arquivo importa
   como qualquer acervo, e a faixa nao chega com modulo faltando (FIX-009).
   Sai o DADO do acervo, nunca o estado da sessao (modulos ligados, BPM do
   controle): a mesma regra do «Baixar .json». O Style da tela e do .md.
   =================================================================== */

/** Monta a colecao de uma faixa so. Copia profunda: o objeto exportado nunca
    compartilha referencia com o acervo aberto. Devolve {json, missing}:
    `missing` conta as citacoes de modulo que nao resolvem no acervo aberto
    (id inexistente ou objeto no lugar do id). Elas seguem citadas na faixa,
    por fidelidade, e o toast avisa — sem saneamento mudo (FIX-006). */
function songToCollection(song) {
  const coll = App.collection || {};
  const album = (coll.albums || []).find(a => (a.songs || []).includes(song));
  const copy = JSON.parse(JSON.stringify(song));
  const modules = [];
  const seen = new Set();
  let missing = 0;
  (song.styleModules || []).forEach(id => {
    const mod = typeof id === "string" ? App.modulesById[id] : null;
    if (!mod) { missing++; return; }
    if (seen.has(id)) return;   // citado duas vezes: o modulo vai uma vez so
    seen.add(id);
    modules.push(JSON.parse(JSON.stringify(mod)));
  });
  const json = { schemaVersion: coll.schemaVersion || "1.0", title: song.title };
  if (coll.targetTool) json.targetTool = coll.targetTool;
  json.albums = [{
    id: album ? album.id : "faixa",
    title: album ? album.title : song.title,
    songs: [copy],
  }];
  if (modules.length) json.styleModules = modules;
  // Chave interna (prefixo _) nunca sai do app (FIX-004). Aqui nao deveria
  // haver nenhuma, mas saida nova passa pela mesma peneira.
  stripInternalKeys(json);
  return { json, missing };
}

/** Baixa a faixa como `<id>.json` (o id e ASCII pelo esquema) e diz no toast
    quantos modulos foram junto e quantos citados nao existem no acervo. */
function exportSongJson(song) {
  const { json, missing } = songToCollection(song);
  const name = (song.id || slug(song.title)) + ".json";
  downloadFile(name, JSON.stringify(json, null, 2), "application/json");
  const n = (json.styleModules || []).length;
  toast("Faixa exportada em .json: " + name + " · " + n + " módulo" + (n === 1 ? "" : "s")
    + (missing ? " · " + missing + " módulo(s) citado(s) não existe(m) no acervo — a faixa os cita assim mesmo" : ""));
}

/* ===================================================================
   Export para Markdown (legivel, para colar num chat/Projeto)
````

### E03 — app: o botao no rodape do cartao — `app/index.html`

**Ancora, literal:**

````
  foot.appendChild(mdBtn);
````

**Texto novo, literal:**

````
  foot.appendChild(mdBtn);
  const jsonBtn = document.createElement("button");
  jsonBtn.textContent = "exportar .json";
  jsonBtn.title = "Exporta esta faixa como acervo .json, com os módulos que ela cita. Sai o dado do acervo: sem os módulos ligados nem o BPM da tela.";
  jsonBtn.addEventListener("click", () => exportSongJson(song));
  foot.appendChild(jsonBtn);
````

### E04 — README: versao — `README.md`

**Ancora, literal:**

````
> **Estado:** v0.10.0 — ferramenta em uso. Lê o acervo, copia por campo, troca módulos de estilo, ajusta o BPM, **mede cada prompt contra os limites do Suno**, exporta Markdown e **entrega o prompt para chats gerarem canções no esquema**. Publicada no GitHub Pages. Ver `meta/ROADMAP.md`.
````

**Texto novo, literal:**

````
> **Estado:** v0.11.0 — ferramenta em uso. Lê o acervo, copia por campo, troca módulos de estilo, ajusta o BPM, **mede cada prompt contra os limites do Suno**, exporta Markdown, exporta uma faixa como `.json` e **entrega o prompt para chats gerarem canções no esquema**. Publicada no GitHub Pages. Ver `meta/ROADMAP.md`.
````

### E05 — README: exportar faixa — `README.md`

**Ancora, literal:**

````
6. Exporte em `.md` (faixa, álbum ou acervo inteiro) se precisar do formato legível.
````

**Texto novo, literal:**

````
6. Exporte em `.md` (faixa, álbum ou acervo inteiro) se precisar do formato legível. Uma faixa também sai em `.json` (*exportar .json* no cartão): é um acervo de uma faixa só, com os módulos que ela usa, para mandar a um chat ou juntar a outro acervo.
````

### E06 — README: conversor e primeira geracao — `README.md`

**Ancora, literal:**

````
Liste quantos volumes quiser. O conversor tira os rótulos do que é copiável, não corta nada e diz no fim quantas letras e styles passam do limite do Suno — o painel do app marca as mesmas. Depois, arraste o `.json` gerado para o app.
````

**Texto novo, literal:**

````
Liste quantos volumes quiser. O conversor tira os rótulos do que é copiável, não corta nada e diz no fim quantas letras e styles passam do limite do Suno — o painel do app marca as mesmas. Depois, arraste o `.json` gerado para o app. O conversor é para a primeira geração: se você mudar o `.json` depois — à mão ou, quando a curadoria chegar, no app —, rodar de novo por cima apaga a mudança (DEC-028).
````

### E07 — convert_br: primeira geracao — `scripts/convert_br.py`

**Ancora, literal:**

````
grave a saida fora do repo, por exemplo na pasta-pai.
````

**Texto novo, literal:**

````
grave a saida fora do repo, por exemplo na pasta-pai.

Conversor de PRIMEIRA geracao (DEC-028): depois que o acervo for mudado fora
daqui (a mao ou pela curadoria do app), o `.json` curado manda — rodar de novo
por cima apaga a curadoria. Para comparar, grave a saida com outro nome.
````

### E08 — convert_guides: primeira geracao — `scripts/convert_guides.py`

**Ancora, literal:**

````
Conversao fiel (DEC-026): nada e cortado; o relatorio conta o que passa do limite.
````

**Texto novo, literal:**

````
Conversao fiel (DEC-026): nada e cortado; o relatorio conta o que passa do limite.

Conversor de PRIMEIRA geracao (DEC-028): depois que o acervo for mudado fora
daqui (a mao ou pela curadoria do app), o `.json` curado manda — rodar de novo
por cima apaga a curadoria. Para comparar, grave a saida com outro nome.
````

### E09 — CHANGELOG: 0.11.0 — `meta/CHANGELOG.md`

**Ancora, literal:**

````
## [0.10.0] — 2026-10-31
````

**Texto novo, literal:**

````
## [0.11.0] — 2026-11-02

Primeira das três entregas da curadoria no app (i-040, DEC-028): exportar uma faixa como `.json`.

### Added
- **Exportar faixa como `.json`:** botão «exportar .json» no rodapé de cada cartão, depois de «exportar .md». A faixa sai como um acervo completo — o álbum de origem (id e título), a faixa e os módulos que ela cita, cada um uma vez — e importa como qualquer acervo, sem aviso de módulo faltando. O arquivo leva o id da faixa no nome (`brv-04.json`). Sai o dado do acervo, nunca os módulos ligados nem o BPM da tela (a regra do «Baixar .json»); citação de módulo que não existe no acervo segue citada, e o toast conta. Spec `meta/specs/261102-exportar-faixa-json.md`: 15 de 15 critérios no Chromium headless, com prova de vida no app da 0.10.0.

### Changed
- **Decisão da curadoria (DEC-028):** o app vai editar um rascunho marcado do acervo, guardado no IndexedDB; o arquivo baixado é a fonte, e o `.json` curado passa a mandar sobre os conversores. Os dois conversores e o README dizem isso.

---

## [0.10.0] — 2026-10-31
````

### E10 — DECISIONS: DEC-022 revista — `meta/DECISIONS.md`

**Ancora, literal:**

````
## DEC-022 — O último acervo importado fica guardado no navegador, como cache (amplia a DEC-004)

**Data:** 2026-10-29
**Status:** aceita
````

**Texto novo, literal:**

````
## DEC-022 — O último acervo importado fica guardado no navegador, como cache (amplia a DEC-004)

**Data:** 2026-10-29
**Status:** aceita — revista pela DEC-028 (2026-11-02): com a curadoria, a cópia pode ficar à frente do arquivo.
````

### E11 — DECISIONS: DEC-028 — `meta/DECISIONS.md`

**Ancora, literal:**

````
**Consequências:** (+) Um projeto de música novo já nasce com o orçamento e a revisão; o dono pode usar hoje, colando o bloco. (+) A revisão é a mesma conta do painel do app (72 e 138 na Rainha da Preguiça). (−) Até o KCM absorver, colar o bloco é à mão, a cada projeto. (−) O texto do bloco e das skills não tem checagem automática além dos limites; regra nova do prompt-modelo pede conferência à mão.
````

**Texto novo, literal:**

````
**Consequências:** (+) Um projeto de música novo já nasce com o orçamento e a revisão; o dono pode usar hoje, colando o bloco. (+) A revisão é a mesma conta do painel do app (72 e 138 na Rainha da Preguiça). (−) Até o KCM absorver, colar o bloco é à mão, a cada projeto. (−) O texto do bloco e das skills não tem checagem automática além dos limites; regra nova do prompt-modelo pede conferência à mão.

## DEC-028 — O app edita um rascunho do acervo, guardado no IndexedDB; o arquivo baixado é a fonte, e o `.json` curado manda sobre os conversores (amplia a DEC-004, revê a DEC-022)

**Data:** 2026-11-02
**Status:** aceita
**Contexto:** O dono quer curar o acervo pela tela (i-040) e ter mais de um acervo no navegador (i-041). Análise `meta/analises/261102-ANALISE-curadoria-no-app.md`, decidida pelo dono em 2026-11-02. Medido: os três acervos em uso somam 1.410.184 caracteres; a cota do `localStorage` fica entre ~2,5 e ~5,2 milhões, conforme a fonte, e no Pages é dividida com os outros repositórios do dono; as marcas «usei» são guardadas só pelo id e já colidem entre acervos (`brv-04`, `cinzeiro-01`); regerar um acervo pelo conversor apaga o que for curado nele.
**Decisão:** (1) **F1** — o arquivo `.json` continua sendo a fonte de verdade. A curadoria pela tela muda um rascunho no navegador, marcado «alterado · N mudanças · Baixar .json» até ser baixado; esquecer, reimportar ou fechar a aba com mudança não baixada pede confirmação. (2) **G1** — os acervos passam a ser guardados no IndexedDB, um por nome de arquivo; o `localStorage` fica para as marcas e a estrutura do cartão; as marcas «usei» passam a ser por acervo. (3) Depois da primeira curadoria pela tela, o `.json` curado manda: os conversores (`convert_br.py`, `convert_guides.py`) são para a primeira geração e não se rodam mais por cima daquele acervo. (4) Três entregas, nesta ordem: exportar faixa como `.json` (0.11.0) → vários acervos → curadoria. (5) A faixa exportada é uma coleção com o álbum de origem (id e título), a faixa e os módulos que ela cita, com o dado do acervo e não o da sessão.
**Alternativas consideradas:** baixar o arquivo a cada operação (dez exclusões, dez arquivos em Downloads); o navegador como fonte (o motivo da DEC-004, agora com 1,4 milhão de caracteres em jogo); gravar direto no arquivo pela File System Access (só Chrome e Edge, permissão pedida a cada sessão — virou a i-043, depois da entrega 3); seguir no `localStorage` (um quarto acervo grande não cabe no cenário pessimista); um `id` no esquema da coleção (muda o contrato dos chats por um ganho que o nome do arquivo já dá).
**Consequências:** (+) Curar pela tela, sem chat nem WO; o reagrupamento da i-038 passa a caber no app. (+) Trocar de acervo sem importar de novo. (−) A DEC-022 perde «a cópia é igual ao arquivo»: depois da entrega 3 a cópia pode estar à frente do arquivo, e a marca de rascunho é o que avisa. (−) Rascunho não baixado se perde se o navegador limpar os dados. (−) Regerar pelos guias depois de curar apaga a curadoria — por isso o item 3.
````

### E12 — IDEAS: i-039, o KCM leu a carta — `meta/IDEAS.md`

**Ancora, literal:**

````
**Em trabalho (0.10.0, 2026-10-31, DEC-027):** as três peças em `kit-musica/` — `BLOCO-SUNO.md` (bloco para Instruções e CEREBRO, não Instruções inteiras: o KCM tem teto), `macetes-suno`, `revisar-faixa`. Carta 01 ao KCM com o mapa para o nicho Música. **Gatilho:** sem resposta do KCM até o primeiro projeto de música novo do dono, o projeto usa o kit à mão (`kit-musica/README.md`, «Como usar hoje») e o que faltar volta como feedback.
````

**Texto novo, literal:**

````
**Em trabalho (0.10.0, 2026-10-31, DEC-027):** as três peças em `kit-musica/` — `BLOCO-SUNO.md` (bloco para Instruções e CEREBRO, não Instruções inteiras: o KCM tem teto), `macetes-suno`, `revisar-faixa`. Carta 01 ao KCM com o mapa para o nicho Música. **Gatilho:** sem resposta do KCM até o primeiro projeto de música novo do dono, o projeto usa o kit à mão (`kit-musica/README.md`, «Como usar hoje») e o que faltar volta como feedback.
**O KCM leu a carta 01 (2026-10-31, aviso `../notas-arquivadas/261031-kcm-leu-01.md`):** foi para a i-N25 deles, cujo próximo passo é analisar o eixo «Produção: tocada / gerada por IA» com o teto das Instruções medido; o feedback ao kit foi para a i-N76; o Cancioneiro entrou no livro de leitura. A resposta vem pela carta 02, sem data. O gatilho acima continua valendo.
````

### E13 — IDEAS: i-040 em desenvolvimento (1) — `meta/IDEAS.md`

**Ancora, literal:**

````
### i-040 💡 Curadoria no app: excluir, exportar e importar faixas
````

**Texto novo, literal:**

````
### i-040 🔨 Curadoria no app: excluir, exportar e importar faixas
````

### E14 — IDEAS: i-040 em desenvolvimento (2) — `meta/IDEAS.md`

**Ancora, literal:**

````
`[relatado pelo dono, 2026-10-29, nota 261029-1825.txt]` Exportar uma faixa como `.json` (além do `.md`); excluir uma faixa; importar faixas para o acervo aberto — todas ou as escolhidas de outro `.json` de álbum, ou uma faixa exportada solta; mudar a ordem e levar faixas de um álbum a outro. Leva o app de leitor a editor leve: pede análise antes de spec, porque mexe na fonte de verdade (DEC-004, DEC-022 — hoje a cópia no navegador é cache do arquivo; editar nela cria um acervo que só existe ali até «Baixar .json»). Ids repetidos e módulos citados na importação também. Faria o reagrupamento da i-038 pela tela.
````

**Texto novo, literal:**

````
`[relatado pelo dono, 2026-10-29, nota 261029-1825.txt]` Exportar uma faixa como `.json` (além do `.md`); excluir uma faixa; importar faixas para o acervo aberto — todas ou as escolhidas de outro `.json` de álbum, ou uma faixa exportada solta; mudar a ordem e levar faixas de um álbum a outro. Leva o app de leitor a editor leve: pede análise antes de spec, porque mexe na fonte de verdade (DEC-004, DEC-022 — hoje a cópia no navegador é cache do arquivo; editar nela cria um acervo que só existe ali até «Baixar .json»). Ids repetidos e módulos citados na importação também. Faria o reagrupamento da i-038 pela tela.
**Decidida (2026-11-02, DEC-028):** análise `meta/analises/261102-ANALISE-curadoria-no-app.md`, F1 + G1 em três entregas. **Entrega 1 feita (0.11.0):** exportar faixa como `.json` (spec `meta/specs/261102-exportar-faixa-json.md`). A entrega 2 é a i-041; a 3 é o resto desta ideia (excluir, reordenar, mover, novo álbum, importar faixas), num rascunho marcado.
````

### E15 — IDEAS: i-041 decidida — `meta/IDEAS.md`

**Ancora, literal:**

````
`[relatado pelo dono, 2026-10-29, nota 261029-1825.txt]` Hoje a DEC-022 guarda só o último importado. Com os acervos convertidos (Rainha da Preguiça, os álbuns de `Albuns/`), trocar de acervo obriga a importar de novo. Medida: a Rainha da Preguiça ocupa ~955 mil caracteres na cópia; o `localStorage` costuma dar ~5 MB por site — dois ou três acervos grandes cabem, mais que isso pede IndexedDB. Anda junto com a i-040.
````

**Texto novo, literal:**

````
`[relatado pelo dono, 2026-10-29, nota 261029-1825.txt]` Hoje a DEC-022 guarda só o último importado. Com os acervos convertidos (Rainha da Preguiça, os álbuns de `Albuns/`), trocar de acervo obriga a importar de novo. Medida: a Rainha da Preguiça ocupa ~955 mil caracteres na cópia; o `localStorage` costuma dar ~5 MB por site — dois ou três acervos grandes cabem, mais que isso pede IndexedDB. Anda junto com a i-040.
**Decidida (2026-11-02, DEC-028):** IndexedDB, um acervo por nome de arquivo, marcas «usei» por acervo (hoje colidem: `brv-04`, `cinzeiro-01`). É a entrega 2 da curadoria; a sonda `../261102-sonda-armazenamento.html` mede o navegador do dono antes da spec.
````

### E16 — IDEAS: i-043 nova — `meta/IDEAS.md`

**Ancora, literal:**

````
Achado na conversão BR: três faixas mudam de andamento de propósito. A DEC-020 reprova dois BPM no `validate.py`, e o controle de BPM do cartão igualaria os dois números. Decidir: o controle não aparecer (ou avisar) quando o style tem uma rampa, e o `validate.py` aceitar o par ligado por «to»/«building to», sem perder o erro de autoria que a DEC-020 pega.
````

**Texto novo, literal:**

````
Achado na conversão BR: três faixas mudam de andamento de propósito. A DEC-020 reprova dois BPM no `validate.py`, e o controle de BPM do cartão igualaria os dois números. Decidir: o controle não aparecer (ou avisar) quando o style tem uma rampa, e o `validate.py` aceitar o par ligado por «to»/«building to», sem perder o erro de autoria que a DEC-020 pega.

### i-043 💡 Gravar direto no arquivo do acervo (File System Access)
Achado na análise da curadoria (2026-11-02, opção F4): no Chrome e no Edge o app pode abrir o `.json` com permissão de gravar e «Salvar» no mesmo arquivo, sem passar por Downloads. Não existe no Firefox nem no Safari, e a permissão é pedida de novo a cada sessão. **Gatilho:** depois da entrega 3 da curadoria (DEC-028), se a sonda mostrar a API no navegador do dono — entra como «Salvar no arquivo» onde existir, com «Baixar» onde não.
````

### E17 — ROADMAP: curadoria no app — `meta/ROADMAP.md`

**Ancora, literal:**

````
- ✅ Converter os álbuns antigos (i-008, DEC-026): a família BR na 0.9.1 (151 faixas) e `Albuns/` na 0.10.0 (205 faixas em 12 álbuns por cena de uso, i-038); os acervos ficam fora do repo.
````

**Texto novo, literal:**

````
- ✅ Converter os álbuns antigos (i-008, DEC-026): a família BR na 0.9.1 (151 faixas) e `Albuns/` na 0.10.0 (205 faixas em 12 álbuns por cena de uso, i-038); os acervos ficam fora do repo.
- 🔨 Curadoria no app e vários acervos (i-040, i-041, DEC-028), em três entregas: ✅ exportar faixa como `.json` (0.11.0) · ⬜ vários acervos no navegador (IndexedDB, marcas «usei» por acervo) · ⬜ curadoria pela tela (excluir, reordenar, mover, novo álbum, importar faixas) num rascunho marcado.
````

### E18 — STATUS inteiro — `meta/STATUS.md`

**Arquivo inteiro, literal** (substitui o arquivo; chegada `8fc2112fdd2d10341f309c023c5542fbea7d359c`):

````
# STATUS.md — Cancioneiro

> **O agora.** O que funciona, o que está em progresso, o que está quebrado, backlog curto.
> Rolante: item resolvido sai daqui e vai para o CHANGELOG. Médio/longo prazo vive no ROADMAP.

**Versão atual:** 0.11.0 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveniências de uso concluídos e conferidos · os álbuns antigos convertidos (i-008, fora do repo) · curadoria no app em curso, entrega 1 de 3 (DEC-028) · kit de música lido pelo KCM, à espera da carta 02 (i-039)

---

## Última conversa (2026-11-02, curadoria no app: decisão e entrega 1, WO 0022)

- **Análise da curadoria e de vários acervos decidida** (i-040, i-041, DEC-028): F1 + G1, em três entregas — exportar faixa como `.json` → vários acervos no navegador (IndexedDB, marcas «usei» por acervo) → curadoria pela tela num rascunho marcado. O arquivo baixado é a fonte; depois da primeira curadoria, o `.json` curado manda sobre os conversores.
- **Entrega 1 (0.11.0):** «exportar .json» no rodapé de cada cartão — a faixa como acervo (álbum de origem, a faixa, os módulos que cita), com o dado do acervo e não o da sessão. Spec `meta/specs/261102-exportar-faixa-json.md`; 15 de 15 critérios no Chromium headless, testados pelo chat.
- **O KCM leu a carta 01** (2026-10-31): vai para a i-N25 deles; a resposta vem pela carta 02, sem data. A pendência «levar a carta» saiu.
- **Este bloco substitui o anterior, de 2026-10-31** (`Albuns/` reagrupado e kit de música). O que ele dizia está no CHANGELOG [0.10.0], na DEC-027 e em `logs/2026-10-31.md`. Saíram também os dois itens que o `/wrap` das WOs 0020 e 0021 anexou no fim do arquivo: estão no mesmo log (Conversas 2 e 4), e a pendência do validador segue em «Pendências do dono».

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
- **Exportar faixa como `.json`** (0.11.0, DEC-028): botão no rodapé do cartão; a faixa sai como acervo — o álbum de origem (id e título), a faixa e os módulos que ela cita — e importa como qualquer acervo. Sai o dado do acervo, não os módulos ligados nem o BPM da tela; o toast conta os módulos e os citados que não existem.
- **Prompt-modelo** (`schema/PROMPT-PARA-CHATS.md`, DEC-021, DEC-023): contrato de módulo, style com 6 a 8 tags e até 10 com os módulos ligados; pede o JSON como arquivo e, sem arquivo, em bloco de código. Dois retestes em 2026-10-29: 6 de 6 faixas dentro do contrato e do orçamento, nos dois.
- **Botões «Prompt» e «Exemplo»** (0.8.0, DEC-021): buscam o prompt e o `data/demo.json` do repositório no clique; a janela do prompt recebe o «Meu pedido».
- **Conveniências (0.9.0, DEC-022, DEC-023):** «Estrutura» do cartão (ordem e blocos visíveis, no navegador); copiar o título; arrastar o `.json` para importar; o último acervo importado volta ao abrir, com origem, data e «esquecer»; a importação aceita a resposta do chat colada inteira e avisa.
- **Publicado no GitHub Pages** em `https://joaolucas-nds.github.io/cancioneiro/app/index.html` — o push em `main` publica.

## Em progresso

- **Curadoria no app e vários acervos** (i-040, i-041, DEC-028) — entrega 1 feita (0.11.0). Próximas: a 2 (vários acervos no IndexedDB, marcas «usei» por acervo), com spec depois do relatório da sonda, e a 3 (curadoria pela tela).
- **Kit de música no KCM (i-039)** — o KCM leu a carta 01 e responde pela carta 02, sem data. Gatilho: sem resposta até o primeiro projeto de música novo, o projeto usa o kit à mão (`kit-musica/README.md`).

## Quebrado / pendências que travam

- (nada quebrado)

## Pendências do dono

- **Conferir a entrega 1 na tela** — roteiro na conversa de 2026-11-02, depois do push da WO 0022.
- **Rodar a sonda de armazenamento** — `../261102-sonda-armazenamento.html`: duplo clique, «Medir», «Baixar relatório», e o `.txt` na pasta-pai. É o dado da spec da entrega 2.
- **Instalar o validador de esquema nesta máquina.** Sem `jsonschema` e `referencing`, o `validate.py` só confere sintaxe e diz `ESQUEMA NAO CONFERIDO` na última linha. Uma vez, no CMD: `pip install jsonschema referencing --break-system-packages`. Depois, `python3 scripts/validate.py` deve terminar em `Tudo conforme ao esquema.`

## Backlog curto (próximas ações concretas)

1. **Entrega 2 da curadoria: vários acervos no navegador** (i-041, DEC-028) — spec depois do relatório da sonda; corrige a colisão das marcas «usei».
2. **Entrega 3 da curadoria: excluir, reordenar, mover, novo álbum, importar faixas** (i-040) — num rascunho marcado, com as regras de id e módulo repetidos da análise.
3. **Rampa de BPM** (i-042) — três faixas BR reprovam no `validate.py` por mudarem de andamento de propósito.
4. **Pesquisar outras plataformas de música por IA** (i-032) — um turno de pesquisa antes de qualquer mudança de esquema.
5. **Avisar palavra de andamento que contradiz o BPM** (i-029) — pede uma tabela palavra → faixa de BPM, com fonte e data.
6. **Importar prompts prontos dos álbuns como módulos** — o último ⬜ da 3b no ROADMAP; o índice-mestre da BR e os «estilos originais» do VOL5 trazem fórmulas de estilo.

## Notas de estado

- **Repo local do dono:** `C:\Users\alexk\Tools\cancioneiro\cancioneiro` (Windows). O chat lê e grava na pasta vinculada; commit e push são do Code (DEC-010). A pasta-pai guarda relatórios, notas e o acervo do dono, fora do Git; o lido vai para `../notas-arquivadas/`.
- **Canal:** pasta vinculada é o padrão; a cópia achatada (FlatDrop) é reserva (DEC-017).
- **Limites do Suno:** o v6 saiu em 2026-09-09 e a nota oficial não documenta limite de campo; os números do painel vêm de fonte secundária, com fonte e data no `QUALITY_LIMITS` (DEC-018). Outra fonte secundária (2026-08) põe o ideal em 4 a 7 descritores; o prompt usa 6 a 8. Reconferir quando houver documentação oficial. O `meta/HISTORY.md` §5 ganhou a interface do v6 vista na conta (2026-10-29); o resto do arquivo ainda descreve o v5.5.
- **Exclude no v6-mini:** o formulário gratuito não tem o campo (capturas de 2026-10-29). Desde a 0.9.1 (DEC-025) o bloco vem oculto por padrão, com o aviso «no X → Exclude» junto (D3); o dado continua no JSON e no export. Quem usa o campo liga em «Estrutura».
- **Navegador (DEC-004, DEC-022):** guarda as marcas «usei», a estrutura do cartão e a cópia do último acervo importado. A cópia é cache: se o arquivo mudou fora, importe de novo; a linha de origem diz quando a cópia foi feita.
- **Marcas «usei» colidem entre acervos com o mesmo id** (`brv-04` na Rainha e no demo; `cinzeiro-01` no demo e no exemplo): são guardadas só pelo id. Corrige-se na entrega 2 (DEC-028).
- **Conversores são de primeira geração (DEC-028):** depois de mudar um acervo (à mão ou, com a entrega 3, no app), não rode o conversor por cima dele.
- **Botões «Prompt» e «Exemplo»:** dependem de rede e do Pages. No `file://`, só funcionam se o Pages aceitar o `fetch` de uma página local — não conferido (o dono abriu o `file://` em 2026-10-29, sem relatar o resultado do botão); sem isso, a janela mostra o link para a versão publicada (DEC-021).
- **Estado de sessão** (módulos ligados e BPM escolhido) sobrevive a filtro, busca e «marcar usei»; volta ao acervo ao recarregar a página ou importar de novo (FIX-008, DEC-020).
- **Limite conhecido:** `tryAutoLoad` (carregamento automático pelo Pages) não saneia chaves internas — só a importação por arquivo faz isso. Inócuo enquanto nenhum acervo contaminado for para `data/`.
- **Pendência de contexto — ASU:** o dono perguntou se o «modo ASU» do KCM seria melhor que o modo Code para este projeto; ficou pendente até ele trazer a descrição do ASU `[relatado pelo dono, sem material de apoio]`.
- Design: na recomposição do Style a base manda — desligar um módulo não remove o que já está no style base; módulos só somam. O dedup compara sequências de palavras (FIX-003). Os módulos de gênero e de andamento costumam custar 0 tag por isso (DEC-019). O chip de andamento é atalho do controle de BPM, no máximo um ligado (DEC-020).
````

## Fora de escopo

- Entregas 2 e 3 da curadoria (IndexedDB, varios acervos, excluir, mover, importar faixas).
- `CONTEXT`, analise, spec e log: ja gravados pelo chat; nao edite.
- Nada em `data/`, `schema/` ou `kit-musica/`.

## Armadilhas desta WO

- **`autocrlf=true` na maquina do dono:** os hashes valem no disco em LF, antes do `add`. Nao rode `git checkout -- <arquivo>` para «desfazer»: ele regrava em CRLF e o hash deixa de bater.
- **O `validate.py` desta maquina termina em `ESQUEMA NAO CONFERIDO`** (falta `jsonschema`): e o estado conhecido, nao falha desta WO. No ambiente do chat, com o pacote, terminou em `Tudo conforme ao esquema.`
- **Os testes escrevem no stderr:** use `2>&1 >/dev/null | tail -1`.

## Depois de aplicar — conferencia antes do commit

| # | Checagem | Comando | Esperado |
|---|---|---|---|
| 1 | **Os treze arquivos sao os testados** | `sha1sum app/index.html README.md scripts/convert_br.py scripts/convert_guides.py meta/CHANGELOG.md meta/DECISIONS.md meta/IDEAS.md meta/ROADMAP.md meta/STATUS.md meta/specs/261102-exportar-faixa-json.md meta/analises/261102-ANALISE-curadoria-no-app.md meta/CONTEXT.md logs/2026-11-02.md` | a coluna **chegada**, os treze. **Prova as 18 edicoes.** |
| 2 | Validacao | `python3 scripts/validate.py; echo "exit=$?"` | `exit=0`, com a linha `OK  versao 0.11.0 igual em CHANGELOG, app, README e STATUS`; ultima linha `Tudo conforme ao esquema.` ou `ESQUEMA NAO CONFERIDO (...)` (esta maquina) |
| 3 | Os conversores seguem passando | `python3 scripts/test_convert_br.py 2>&1 >/dev/null \| tail -1` e `python3 scripts/test_convert_guides.py 2>&1 >/dev/null \| tail -1` | `OK` e `OK` |
| 4 | O codigo novo e o registro | `grep -c '^function exportSongJson' app/index.html`, `grep -c '^## DEC-028 ' meta/DECISIONS.md`, `grep -c '^### i-043 ' meta/IDEAS.md`, `grep -m1 '^## \[' meta/CHANGELOG.md` | `1`, `1`, `1`, `## [0.11.0] — 2026-11-02` |
| 5 | Os itens soltos do fim do STATUS sairam | `grep -c '^- \*\*WO 0021 aplicada' meta/STATUS.md` e `grep -c '^- \*\*Instalar o validador de esquema continua pendente' meta/STATUS.md` | `0` e `0` |
| 6 | Nada alem do previsto | `GIT_OPTIONAL_LOCKS=0 git status --short --untracked-files=all` | os treze arquivos e esta WO, e nada mais (nenhum `.txt`, nenhum `__pycache__`) |

**Os tres campos de cada passo:** as seis sao rodadas por **quem aplica (o Code)**, na raiz do repo, em Git Bash,
com `LC_ALL=C.UTF-8`. **Chega no ramo?** A checagem 1 cobre os treze arquivos inteiros, inclusive o
`app/index.html` que o chat executou (`songToCollection`, `exportSongJson`, o botao em `renderCard`). **Esta e
qual pergunta?** A 2 e a 3 respondem «funciona?»; as outras, «esta la?». O «funciona?» do botao na tela e do dono,
depois do push, pelo roteiro do chat.

## Relatorio de aplicacao

Grave em `../261102-HHMM-code-cancioneiro-apply-wo0022.txt`, com o `HHMM` de `date +%y%m%d-%H%M` rodado na
hora. Diga o resultado da checagem 1 em primeiro lugar.

**Proximo comando** (ultima linha do relatorio, cru e sozinho):

```
/wrap
```

## Commit

```
git add app/index.html README.md scripts/convert_br.py scripts/convert_guides.py meta/CHANGELOG.md meta/DECISIONS.md meta/IDEAS.md meta/ROADMAP.md meta/STATUS.md meta/CONTEXT.md meta/analises meta/specs logs/2026-11-02.md meta/workorders
```

```
git commit -m "feat: exporta faixa como json e versao 0.11.0" -m "Entrega 1 da curadoria no app (i-040): botao exportar .json no cartao; a faixa sai como acervo, com o album de origem e os modulos que cita, sem o estado da sessao. DEC-028 registra F1 + G1 e o json curado mandando sobre os conversores. IDEAS, ROADMAP, README, conversores, spec, analise com desfecho e STATUS inteiro."
```

```
git push
```
