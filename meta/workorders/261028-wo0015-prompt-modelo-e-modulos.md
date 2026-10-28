# WO 0015 — Prompt-modelo: contrato de modulos, orcamento de tags e o prompt pela interface

## Cabecalho

> **Tipo:** WO de CODIGO (`app/index.html`, `scripts/validate.py`, `schema/PROMPT-PARA-CHATS.md`) e de registro.
> **Config sugerida:** Sonnet · `/effort medium`. 22 edicoes literais e dois arquivos inteiros, todos aplicados e testados pelo chat numa copia; cada arquivo tem hash de chegada.
> **Pre-requisito:** commit `cd4b86f`, branch `main`, sincronizada com `origin/main`. **A arvore NAO esta limpa:** `meta/specs/261028-prompt-modelo-e-modulos.md` e nova (a spec, gravada pelo chat em 2026-10-28; esta WO so a versiona). Nada mais deve aparecer no `git status` alem dela e desta WO.
> **Base:** `meta/specs/261028-prompt-modelo-e-modulos.md`, Decisoes **1a, 2a, 3a, 4a** dadas pelo dono em 2026-10-28, e a **5** da nota do dono `261028-1852.txt` (prompt e exemplo pela interface).
> **Depende de:** WO 0014, ja aplicada (`2ea2e80`, wrap `cd4b86f`).
>
> **Arquivos — partida e chegada, os dois medidos pelo chat** (chegada = resultado de aplicar literalmente as edicoes abaixo, em LF):
>
> | arquivo | partida (sha1) | chegada (sha1) |
> |---|---|---|
> | `app/index.html` | `a321d4194db3fd308bbc7a2c0a755742d6d5a4ef` | `0146443aad808e7841cc00eba932737d5545107d` |
> | `scripts/validate.py` | `1836d811b1809065e96c55b5d1a286c6fcd7f719` | `ef1cc0a09fd3a69d6e0b95022010a4a28c398b40` |
> | `schema/PROMPT-PARA-CHATS.md` | `80578534b5391b60c7fd2b23be621f7ee537f7a8` | `577b90fa94faa9b00a3427250c03c7ea0eedf37d` |
> | `meta/DECISIONS.md` | `2dc9f1ddf4d0ab1dabce5e6c8768d8e8e23718b9` | `293a8797a3980e3858935ba90798e42064cc07f0` |
> | `meta/IDEAS.md` | `9e6941648d522bab65ba9f34bd6631a0564dbf24` | `ea72e3729f2e6c25c559aa39caf772996db3bfa9` |
> | `meta/ROADMAP.md` | `9d7e5c3587f5a8f2fb0a6047e9569d91750f25e3` | `4f40aced89a9661c485e27b99fcb4824aeba716b` |
> | `meta/STATUS.md` | `3f3e387b89ad3b4322021abfa9d0cf51653b3379` | `32260b22192382eb823d437034914a8d850f3b8c` |
> | `logs/2026-10-28.md` | `0e282e8c41f76a4cd4096969798dee8c1b9078ee` | `d43b7a7878fd9150da91b3dfd507b3ddab14e192` |
> | `meta/specs/261028-prompt-modelo-e-modulos.md` | `b6d6823bcc3aadbb1079ef8399ded91feefe3162` | `b6d6823bcc3aadbb1079ef8399ded91feefe3162` (nao muda: so entra no Git) |
>
> **Ancora semantica:** se um trecho-ancora nao bater EXATAMENTE, PARE e reporte.
> **Idempotencia:** antes de cada edicao, procure o texto NOVO INTEIRO; se ja estiver la, PULE e diga no relatorio.
>
> **Ancoras lidas em:** cada ancora foi extraida pelo chat do arquivo de partida (`git show cd4b86f:<arquivo>`, igual ao disco do dono pelos hashes acima) e conferida como ocorrendo **exatamente 1 vez** no estado em que a edicao e aplicada, na ordem abaixo.

---

## 1. Por que

O teste base do prompt-modelo (tres chats fora de Projeto, mesmo pedido) mostrou que o prompt acertava o
que ensinava — JSON puro, zero rotulos, BPM coerente em 9 de 9 faixas — e errava o que calava: pedidos
modulos, os tres chats inventaram tres formatos e aninharam o modulo na faixa. E o app aceitava isso em
silencio (painel com 0 chips), enquanto o validador quebrava com traceback. A spec mediu, o dono decidiu:

- **Prompt (DEC-021):** ensina o contrato da DEC-016 (modulos no `styleModules` da colecao com `id`,
  `category`, `label`, `fragment`, `notes`; a faixa cita ids; citado = ligado), o orcamento (style com 6 a 8
  tags, ate 10 com os modulos ligados) e que BPM em modulo so na camada `tempo`.
- **FIX-009:** o validador reprova com mensagem (sem traceback) e a importacao do app diz quantos modulos
  citados nao existem. O toast dura mais quando a mensagem e longa.
- **Prompt e exemplo pela interface (decisao 5, i-031):** botoes «Prompt para chats» (janela com «Meu
  pedido») e «Baixar exemplo», que BUSCAM `schema/PROMPT-PARA-CHATS.md` e `data/demo.json` no clique.
  O app nao guarda copia de nenhum dos dois. O `validate.py` ganha a sexta checagem: as marcacoes do
  prompt que o botao le.
- **Registro:** FIX-009 e DEC-021, i-028 e i-031 em trabalho, i-030 e i-032 capturadas, feedback ao kit,
  Fase 2 no ROADMAP, Conversa 4 no log e o STATUS inteiro.

O app de chegada (`0146443a…`) e o validador de chegada (`ef1cc0a0…`)
foram executados pelo chat: a tabela esta no «Desfecho» da spec. **No acervo do dono, no `data/demo.json` e
no `data/exemplo-cinzeiro.json`, o Style de 11 de 11 cartoes sai byte a byte igual ao da 0.7.0**, e o
validador passa nos dois modos.

**Nao ha versao nova nesta WO.** A 0.8.0 fecha depois do roteiro do dono (tela + reteste do prompt), como a
0.7.0 fechou. **O STATUS vai literal, no apply** — nada «a cargo do `/wrap`».

## Edicao 0 — Conferencia de hash e de arvore

```
sha1sum app/index.html scripts/validate.py schema/PROMPT-PARA-CHATS.md meta/DECISIONS.md meta/IDEAS.md meta/ROADMAP.md meta/STATUS.md logs/2026-10-28.md meta/specs/261028-prompt-modelo-e-modulos.md
GIT_OPTIONAL_LOCKS=0 git status --short
```

Os nove batem com a coluna **partida**, e o `git status` mostra **so** `?? meta/specs/261028-prompt-modelo-e-modulos.md` e esta WO.
Qualquer outra coisa: **PARE e reporte**.

## Edicoes E01 a E22

Na ordem. Copie o que esta ENTRE as linhas de quatro crases, sem elas. **O bloco termina na linha de quatro
crases, nunca num titulo:** varios blocos trazem linhas que comecam com `## ` (o DEC-021, o FIX-009, a
Conversa 4). A edicao troca a ancora pelo texto novo; quase sempre o texto novo comeca ou termina com a ancora.

### E01 — comentario do topo: os botoes novos — `app/index.html`

**Ancora, literal:**

````
   - Em qualquer modo: botoes "Importar .json" e "Baixar .json" sempre disponiveis.

````

**Texto novo, literal:**

````
   - Em qualquer modo: botoes "Importar .json" e "Baixar .json" sempre disponiveis.
   - "Prompt para chats" e "Baixar exemplo" buscam schema/PROMPT-PARA-CHATS.md e
     data/demo.json do repositorio no clique (fonte unica, DEC-021); no file://,
     tentam o endereco publicado.

````

### E02 — CSS da janela do prompt — `app/index.html`

**Ancora, literal:**

````
  a { color: var(--ember); }
</style>
````

**Texto novo, literal:**

````
  a { color: var(--ember); }

  /* ---- Janela do prompt para chats (DEC-021) ----
     <dialog> nativo: foco preso, Esc fecha, fica na camada de topo. Por estar no
     topo, o toast (z-index comum) ficaria ATRAS dele — por isso a janela tem a
     propria linha de status em vez de usar o toast. */
  dialog.prompt-dialog {
    border: 1px solid var(--line); border-radius: var(--radius);
    background: var(--paper); color: var(--ink);
    padding: 20px; width: min(640px, calc(100vw - 32px));
  }
  dialog.prompt-dialog::backdrop { background: rgba(35, 32, 27, .45); }
  .prompt-dialog h2 { font-family: var(--serif); font-weight: 600; font-size: 20px; margin: 0 0 6px; }
  .prompt-dialog p { margin: 0 0 12px; font-size: 13px; color: var(--ink-soft); }
  .prompt-dialog label { display: block; font-size: 13px; margin-bottom: 4px; }
  .prompt-dialog textarea {
    width: 100%; box-sizing: border-box; min-height: 120px; resize: vertical;
    font-family: var(--sans); font-size: 14px; padding: 10px;
    border: 1px solid var(--line); border-radius: 8px; background: var(--paper-2); color: var(--ink);
  }
  .prompt-dialog textarea:focus-visible { outline: 2px solid var(--ember); outline-offset: 2px; }
  .prompt-dialog .dialog-actions { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 12px; align-items: center; }
  .prompt-dialog .dialog-actions .spacer { margin-left: auto; }
  .prompt-dialog [data-role="prompt-status"] { min-height: 1.4em; margin: 10px 0 0; }
</style>
````

### E03 — botoes no cabecalho — `app/index.html`

**Ancora, literal:**

````
    <button id="export-md-btn">Exportar .md</button>
    <input type="file" id="file-input" accept=".json,application/json" hidden>
````

**Texto novo, literal:**

````
    <button id="export-md-btn">Exportar .md</button>
    <button id="prompt-btn">Prompt para chats</button>
    <button id="example-btn">Baixar exemplo</button>
    <input type="file" id="file-input" accept=".json,application/json" hidden>
````

### E04 — a janela do prompt — `app/index.html`

**Ancora, literal:**

````
<div class="toast" id="toast"></div>

````

**Texto novo, literal:**

````
<div class="toast" id="toast"></div>

<dialog class="prompt-dialog" id="prompt-dialog" aria-labelledby="prompt-dialog-title">
  <h2 id="prompt-dialog-title">Prompt para chats</h2>
  <p>Escreva o que você quer; o botão copia o prompt-modelo inteiro com o seu pedido no lugar.
  Cole num chat novo e importe aqui o JSON que ele devolver.</p>
  <label for="prompt-request">Meu pedido</label>
  <textarea id="prompt-request" placeholder="ex.: 3 faixas de synth-pop melancólico em pt-BR, uma instrumental…"></textarea>
  <div class="dialog-actions">
    <button type="button" class="btn-primary" id="prompt-copy-btn">Copiar prompt</button>
    <button type="button" id="prompt-close-btn" class="spacer">Fechar</button>
  </div>
  <p class="note" data-role="prompt-status" role="status"></p>
</dialog>

````

### E05 — carga automatica: aviso de modulos — `app/index.html`

**Ancora, literal:**

````
      setCollection(json);
      toast("Acervo carregado de " + path);
      return;
````

**Texto novo, literal:**

````
      setCollection(json);
      toast("Acervo carregado de " + path + moduleRefsNotice(json));
      return;
````

### E06 — importacao: aviso de modulos — `app/index.html`

**Ancora, literal:**

````
      toast("Acervo importado: " + (json.title || file.name)
            + (removidas ? " · " + removidas + " campo(s) interno(s) removido(s) — baixe de novo para gravar limpo" : ""));
    } catch (e) {
````

**Texto novo, literal:**

````
      toast("Acervo importado: " + (json.title || file.name)
            + (removidas ? " · " + removidas + " campo(s) interno(s) removido(s) — baixe de novo para gravar limpo" : "")
            + moduleRefsNotice(json));
    } catch (e) {
````

### E07 — moduleRefsNotice, depois da importacao — `app/index.html`

**Ancora, literal:**

````
  reader.readAsText(file);
}
````

**Texto novo, literal:**

````
  reader.readAsText(file);
}

/** Quantos itens de songs[].styleModules nao resolvem num modulo da colecao:
    objeto no lugar do id (o chat declarou o modulo dentro da faixa) ou id que
    nao existe em styleModules[]. Devolve o trecho do toast, ou "" se nenhum.

    Por que avisar e nao recusar: o resto da faixa (Style, Lyrics) continua util.
    Por que avisar e nao calar: sem isto o painel abria com 0 chips e o modulo
    marcado como ligado sumia do Style sem nenhum sinal (FIX-009) — o mesmo
    principio do FIX-006, que conta as chaves internas que remove. */
function moduleRefsNotice(json) {
  const index = new Set((json.styleModules || []).map(m => m && m.id));
  let bad = 0;
  (json.albums || []).forEach(a => (a.songs || []).forEach(s =>
    (s.styleModules || []).forEach(id => {
      if (typeof id !== "string" || !index.has(id)) bad++;
    })));
  return bad
    ? " · " + bad + " módulo(s) citado(s) nas faixas não existe(m) na coleção — não vão aparecer"
    : "";
}
````

### E08 — toast mais longo e as funcoes do prompt e do exemplo — `app/index.html`

**Ancora, literal:**

````
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => t.classList.remove("show"), 2200);
}
````

**Texto novo, literal:**

````
  clearTimeout(toastTimer);
  // Aviso longo (chaves removidas, modulos que nao resolvem) precisa de tempo
  // de leitura: ~45 ms por caractere, entre 2,2 s e 6 s.
  const ms = Math.min(6000, Math.max(2200, msg.length * 45));
  toastTimer = setTimeout(() => t.classList.remove("show"), ms);
}

/* ===================================================================
   Prompt para chats e exemplo (DEC-021)
   Fonte unica: o app NAO guarda copia do prompt nem do exemplo. Busca os
   arquivos do repositorio no clique — relativo quando servido pelo Pages,
   depois o endereco publicado (caso do file://, se o navegador permitir).
   Cada push que muda o prompt muda o que este botao entrega.
   =================================================================== */
const PUBLISHED_BASE = "https://joaolucas-nds.github.io/cancioneiro/";
const PUBLISHED_APP = PUBLISHED_BASE + "app/index.html";

/** Busca o primeiro caminho que responder; devolve a Response ou null. */
async function fetchFirst(relPath) {
  const candidates = location.protocol === "file:"
    ? [PUBLISHED_BASE + relPath]
    : ["../" + relPath, relPath, PUBLISHED_BASE + relPath];
  for (const url of candidates) {
    try {
      const res = await fetch(url, { cache: "no-store" });
      if (res.ok) return res;
    } catch (e) { /* tenta o proximo */ }
  }
  return null;
}

/** Recorta o prompt entre as linhas de marcacao e poe o pedido no lugar da
    linha entre parenteses abaixo de "## Meu pedido". A mesma regra e conferida
    pelo scripts/validate.py (check_prompt): linha exata. Devolve null se as
    marcacoes nao estiverem la — melhor recusar que copiar o arquivo errado. */
function extractPrompt(md, request) {
  const lines = md.replace(/\r\n/g, "\n").split("\n");
  const start = lines.indexOf("--- INÍCIO ---");
  const end = lines.indexOf("--- FIM ---");
  if (start < 0 || end < start) return null;
  const body = lines.slice(start + 1, end);
  const head = body.indexOf("## Meu pedido");
  if (head < 0) return null;
  let ph = head + 1;
  while (ph < body.length && !body[ph].trim()) ph++;
  if (ph >= body.length || !/^\(.*\)$/.test(body[ph])) return null;
  const req = (request || "").trim();
  if (req) body.splice(ph, 1, req);   // vazio: fica o texto-guia, para completar no chat
  return body.join("\n").trim() + "\n";
}

function promptStatus(msg, html) {
  const el = document.querySelector('[data-role="prompt-status"]');
  if (html) el.innerHTML = msg; else el.textContent = msg;
}

async function copyPrompt() {
  promptStatus("Buscando o prompt…");
  const res = await fetchFirst("schema/PROMPT-PARA-CHATS.md");
  if (!res) {
    promptStatus('Não consegui buscar o prompt. Abra a <a href="' + PUBLISHED_APP
      + '" target="_blank" rel="noopener">versão publicada</a> e tente lá.', true);
    return;
  }
  const text = extractPrompt(await res.text(), document.getElementById("prompt-request").value);
  if (text === null) {
    promptStatus("O arquivo do prompt veio sem as marcações esperadas — nada foi copiado.");
    return;
  }
  try {
    await navigator.clipboard.writeText(text);
  } catch (e) {
    // Mesmo fallback do copiar dos cartoes (file:// / sem Clipboard API)
    const ta = document.createElement("textarea");
    ta.value = text; document.getElementById("prompt-dialog").appendChild(ta); ta.select();
    try { document.execCommand("copy"); } catch (_) {}
    ta.remove();
  }
  promptStatus("Prompt copiado (" + text.length.toLocaleString("pt-BR")
    + " caracteres). Cole num chat novo, fora de qualquer Projeto.");
}

async function downloadExample() {
  const res = await fetchFirst("data/demo.json");
  if (!res) {
    toast("Não consegui buscar o exemplo — abra a versão publicada do app");
    return;
  }
  downloadFile("cancioneiro-exemplo.json", await res.text(), "application/json");
  toast("Exemplo baixado: cancioneiro-exemplo.json");
}
````

### E09 — eventos dos botoes — `app/index.html`

**Ancora, literal:**

````
document.getElementById("export-md-btn").addEventListener("click", exportCollectionMd);
["filter-album", "filter-state", "filter-used"].forEach(id =>
````

**Texto novo, literal:**

````
document.getElementById("export-md-btn").addEventListener("click", exportCollectionMd);
document.getElementById("prompt-btn").addEventListener("click", () => {
  promptStatus("");
  document.getElementById("prompt-dialog").showModal();
});
document.getElementById("prompt-copy-btn").addEventListener("click", copyPrompt);
document.getElementById("prompt-close-btn").addEventListener("click", () =>
  document.getElementById("prompt-dialog").close());
document.getElementById("example-btn").addEventListener("click", downloadExample);
["filter-album", "filter-state", "filter-used"].forEach(id =>
````

### E10 — docstring: seis checagens — `scripts/validate.py`

**Ancora, literal:**

````

Checa quatro coisas:
  1. Sintaxe JSON de todos os schemas e datasets.
````

**Texto novo, literal:**

````

Checa seis coisas:
  1. Sintaxe JSON de todos os schemas e datasets.
````

### E11 — docstring: a sexta checagem — `scripts/validate.py`

**Ancora, literal:**

````
     campo bpm, quando existe, e o numero do style (DEC-020).

````

**Texto novo, literal:**

````
     campo bpm, quando existe, e o numero do style (DEC-020).
  6. O schema/PROMPT-PARA-CHATS.md tem as marcacoes que o botao «Prompt para
     chats» do app le: as linhas de INICIO e FIM e a linha entre parenteses
     abaixo de «## Meu pedido» (DEC-021).

````

### E12 — check_module_refs: duas listas — `scripts/validate.py`

**Ancora, literal:**

````
    index = {m.get("id") for m in data.get("styleModules", []) if isinstance(m, dict)}
    orphans = []
    for album in data.get("albums", []):
````

**Texto novo, literal:**

````
    index = {m.get("id") for m in data.get("styleModules", []) if isinstance(m, dict)}
    orphans, not_ids = [], []
    for album in data.get("albums", []):
````

### E13 — check_module_refs: objeto no lugar do id (FIX-009) — `scripts/validate.py`

**Ancora, literal:**

````
            for mid in song.get("styleModules", []) or []:
                if mid not in index:
                    orphans.append((album.get("id", "?"), song.get("id", "?"), mid))
    if orphans:
````

**Texto novo, literal:**

````
            for mid in song.get("styleModules", []) or []:
                where = (album.get("id", "?"), song.get("id", "?"))
                # Objeto no lugar do id: o chat declarou o modulo DENTRO da faixa.
                # Testado antes do `in`, porque dict nao e hashable e o `in` num set
                # quebrava o validador com traceback em vez de reprovar (FIX-009).
                if not isinstance(mid, str):
                    not_ids.append(where + (mid,))
                elif mid not in index:
                    orphans.append(where + (mid,))
    if not_ids:
        print(f"ERRO de referencia em {rel} ({len(not_ids)} item(ns) de styleModules nao sao id):")
        for a, s, mid in not_ids[:8]:
            print(f"   [{a} > {s}] styleModules: {type(mid).__name__} no lugar de um id — "
                  "declare o modulo em styleModules[] da colecao e cite so o id na faixa")
    if orphans:
````

### E14 — check_module_refs: retorno das duas listas — `scripts/validate.py`

**Ancora, literal:**

````
            print(f"   [{a} > {s}] styleModules: '{mid}' nao existe em styleModules[]")
        return 1
    return 0

````

**Texto novo, literal:**

````
            print(f"   [{a} > {s}] styleModules: '{mid}' nao existe em styleModules[]")
    return 1 if (orphans or not_ids) else 0

````

### E15 — check_prompt, antes de main — `scripts/validate.py`

**Ancora, literal:**

````
    print(f"OK  versao {ref} igual em CHANGELOG, app, README e STATUS")
    return 0
````

**Texto novo, literal:**

````
    print(f"OK  versao {ref} igual em CHANGELOG, app, README e STATUS")
    return 0


PROMPT_START = "--- INÍCIO ---"
PROMPT_END = "--- FIM ---"


def check_prompt():
    """O prompt-modelo tem o que o botao «Prompt para chats» le (DEC-021).

    O app nao guarda copia do prompt: busca este arquivo no Pages e recorta entre
    as duas linhas de marcacao, trocando a linha entre parenteses abaixo de
    «## Meu pedido» pelo pedido digitado. Marcacao que some quebra o botao em
    producao sem nada falhar aqui — por isso a checagem. Mesma regra do app
    (`extractPrompt` em app/index.html): linha exata, sem espacos em volta.
    """
    path = "schema/PROMPT-PARA-CHATS.md"
    try:
        with open(os.path.join(ROOT, path), encoding="utf-8") as f:
            lines = [l.rstrip("\r\n") for l in f]
    except OSError as e:
        print(f"ERRO no prompt: nao consegui ler {path}: {e}")
        return 1
    bad = []
    starts = [i for i, l in enumerate(lines) if l == PROMPT_START]
    ends = [i for i, l in enumerate(lines) if l == PROMPT_END]
    if len(starts) != 1 or len(ends) != 1 or ends[0] < starts[0]:
        bad.append(f"precisa de uma linha '{PROMPT_START}' e depois uma '{PROMPT_END}' "
                   f"(achei {len(starts)} e {len(ends)})")
    else:
        body = lines[starts[0] + 1:ends[0]]
        heads = [i for i, l in enumerate(body) if l == "## Meu pedido"]
        nxt = [l for l in body[heads[0] + 1:] if l.strip()][:1] if len(heads) == 1 else []
        if not (nxt and nxt[0].startswith("(") and nxt[0].endswith(")")):
            bad.append("entre as marcacoes, '## Meu pedido' (uma vez) seguido de uma linha entre parenteses")
    if bad:
        print(f"ERRO no prompt {path}:")
        for b in bad:
            print(f"   {b}")
        return 1
    print(f"OK  prompt com as marcacoes que o app le ({path})")
    return 0
````

### E16 — check_prompt chamada no fim — `scripts/validate.py`

**Ancora, literal:**

````
    errors += check_version()

````

**Texto novo, literal:**

````
    errors += check_version()
    # prompt-modelo: as marcacoes que o botao do app le (DEC-021)
    errors += check_prompt()

````

### E17 — FIX-009 e DEC-021 no fim — `meta/DECISIONS.md`

**Ancora, literal:**

````
**Consequencias:** (+) O prompt nunca leva dois andamentos — o defeito silencioso da camada Andamento some. (+) No valor original, tudo o que se copia e exporta e byte a byte o da 0.6.0. (+) Os 8 andamentos do album viram pontos de salto. (−) O controle nao sabe se a palavra combina com o numero: a 140, ar-04 ainda diz «downtempo» (i-029). (−) O fragmento de um modulo de andamento que traz palavras alem do numero («slow tempo 70 bpm») perde as palavras pela dedup quando o base ja tem um BPM — o que o chip entrega e o numero.
````

**Texto novo, literal:**

````
**Consequencias:** (+) O prompt nunca leva dois andamentos — o defeito silencioso da camada Andamento some. (+) No valor original, tudo o que se copia e exporta e byte a byte o da 0.6.0. (+) Os 8 andamentos do album viram pontos de salto. (−) O controle nao sabe se a palavra combina com o numero: a 140, ar-04 ainda diz «downtempo» (i-029). (−) O fragmento de um modulo de andamento que traz palavras alem do numero («slow tempo 70 bpm») perde as palavras pela dedup quando o base ja tem um BPM — o que o chip entrega e o numero.

---

## FIX-009 — Modulo declarado dentro da faixa sumia em silencio no app e derrubava o validador

**Data:** 2026-10-28
**Sintoma:** Os tres JSONs do teste base do prompt-modelo, importados no app, davam «Acervo importado», o painel de modulos aberto com 0 chips e o Style sem o modulo que o chat marcou como ligado — nenhum aviso, nenhum erro no console. O `validate.py` terminava em `TypeError: unhashable type: 'dict'` (traceback) nos dois modos; no modo sintaxe, o da maquina do dono, sem nenhuma linha de relatorio.
**Causa raiz:** As duas pontas supunham que `songs[].styleModules` traz texto. O app indexa so o `styleModules` da colecao e procura cada item como id: um objeto vira `undefined` e e pulado. O validador testava `mid not in index` num `set`, e `dict` nao e hashable — a checagem de referencia so tinha visto id errado, nunca tipo errado.
**Solucao:** `check_module_refs` testa o tipo antes do `in` e reprova com uma mensagem por item («dict no lugar de um id — declare o modulo em styleModules[] da colecao e cite so o id na faixa»), nos dois modos. A importacao do app — por arquivo e pela carga automatica — conta os itens que nao resolvem (objeto ou id ausente) e diz no toast; importa assim mesmo, porque Style e Lyrics continuam uteis. O toast passou a durar ~45 ms por caractere (de 2,2 a 6 s), para o aviso dar tempo de ler.
**Licao:** E o FIX-006 de novo, na outra ponta: entrada que o app nao entende tem de virar sinal, nunca silencio. E «o validador reprova» so vale depois de testado com a entrada errada de verdade — a que um chat produz, nao a que o autor da checagem imaginou.

---

## DEC-021 — O prompt-modelo ensina o contrato de modulo e o orcamento; o app entrega o prompt e o exemplo buscando a fonte no clique

**Data:** 2026-10-28
**Contexto:** O teste base do prompt-modelo (`meta/specs/261028-prompt-modelo-e-modulos.md`; tres chats Sonnet 5.5 fora de Projeto, o mesmo pedido) acertou o que o prompt ensinava — JSON puro, zero rotulos dentro do copiavel, BPM coerente, em 9 de 9 faixas — e errou o que ele calava: pedidos modulos, os tres chats inventaram tres formatos e aninharam o modulo na faixa, sem `category` e sem nada no `styleModules` da colecao (DEC-016). O style base saiu com 10 tags ou mais em 5 de 9 faixas, como a i-028 previa. Na mesma conversa o dono pediu o prompt e um exemplo pela interface do app publicado, sem abrir as pastas do repositorio (i-031).

**Decisao:** (1) O prompt ensina o contrato que ja existe: modulos no `styleModules` da colecao com `id`, `category` (as sete camadas do app), `label`, `fragment` e `notes`; a faixa cita ids; citado = ligado de saida. (2) Orcamento: style com 6 a 8 tags; somadas as dos modulos citados, ate 10; os demais modulos ficam declarados e desligados, como paleta. (3) BPM em modulo so na camada `tempo`, no formato «NN bpm» (atalho do controle, DEC-020); modulo nao tem `excludeStyles`. (4) Botoes «Prompt para chats» (janela com «Meu pedido») e «Baixar exemplo» buscam `schema/PROMPT-PARA-CHATS.md` e `data/demo.json` no clique — relativo no Pages, depois o endereco publicado; falhando, a janela mostra um link para a versao publicada. O app nao guarda copia de nenhum dos dois. (5) O `validate.py` ganha a sexta checagem: as marcacoes que o botao le (`--- INÍCIO ---`, `--- FIM ---` e a linha entre parenteses abaixo de `## Meu pedido`).

**Alternativas consideradas:** aceitar modulo dentro da faixa no esquema — desfaz a DEC-016 e repete o modulo em cada faixa; um importador que normaliza os formatos inventados — tres formatos em tres amostras, alvo movel; so «base com 6 a 8» — o excesso medido vem dos modulos ligados (+2 a +8); embutir o prompt no app — duas fontes que divergem em silencio; um JSON separado «para ensinar a estrutura» — o prompt ja traz o exemplo, e o `data/demo.json` e o exemplo real.

**Consequencias:** (+) Quem gera o acervo recebe o contrato que o app le; quem usa o app pega o prompt atual sem abrir pasta, e cada push o atualiza. (+) O acoplamento entre o botao e o arquivo do prompt tem checagem. (−) O botao depende de rede e do Pages; no `file://`, de o Pages aceitar o `fetch` de uma pagina local, nao conferido (sem isso, cai no link). (−) O prompt cresceu de 5.829 para 8.954 bytes (6.500 caracteres copiados); o reteste mede se a adesao caiu. (−) Os numeros de tags vem de fonte secundaria e divergem entre si (ate 8, contra 4 a 7).
````

### E18 — i-028 em trabalho — `meta/IDEAS.md`

**Ancora, literal:**

````

### i-028 💡 O prompt-modelo pedir folga para os modulos
`[nascido da spec da 3a.2, 2026-10-27]` Em ar-01 e ar-04 o style base que o chat escreveu ja usa 10 de 10 tags: nenhum modulo cabe sem estourar. O painel agora diz isso, mas so depois. A regra que o evitaria mora em quem escreve o base — o `schema/PROMPT-PARA-CHATS.md` poderia pedir «style base com 6 a 8 tags, deixando folga para os modulos». Pesar contra: o base mais curto pode ficar vago (abaixo de 4 tags o painel ja avisa).

````

**Texto novo, literal:**

````

### i-028 🔨 O prompt-modelo pedir folga para os modulos
`[nascido da spec da 3a.2, 2026-10-27]` Em ar-01 e ar-04 o style base que o chat escreveu ja usa 10 de 10 tags: nenhum modulo cabe sem estourar. O painel agora diz isso, mas so depois. A regra que o evitaria mora em quem escreve o base — o `schema/PROMPT-PARA-CHATS.md` poderia pedir «style base com 6 a 8 tags, deixando folga para os modulos». Pesar contra: o base mais curto pode ficar vago (abaixo de 4 tags o painel ja avisa).
**Em trabalho (2026-10-28, DEC-021, WO 0015).** O teste base do prompt (tres chats, `meta/specs/261028-prompt-modelo-e-modulos.md`) confirmou o base no limite (10+ tags em 5 de 9 faixas) e mostrou um problema maior: o prompt nao ensinava o contrato de modulo, e os tres chats inventaram tres formatos. O prompt agora pede style com 6 a 8 tags e ate 10 com os modulos ligados. Fecha com o reteste do dono.

````

### E19 — i-030, i-031 e i-032 depois da i-029 — `meta/IDEAS.md`

**Ancora, literal:**

````
`[nascido da spec do BPM, 2026-10-28]` Com o controle, ar-04 vai a 140 e continua dizendo «downtempo» e «slow build». A linha de qualidade poderia avisar, em ambar, quando uma palavra de andamento do Style («downtempo», «slow», «uptempo», «fast») briga com o numero. Pesar contra: exige uma tabela palavra → faixa de BPM, conhecimento de dominio que muda com o Suno — o mesmo motivo que tirou a tabela de generos vocais da DEC-019. Se entrar, a tabela mora num objeto unico com fonte e data, como o `QUALITY_LIMITS`.

````

**Texto novo, literal:**

````
`[nascido da spec do BPM, 2026-10-28]` Com o controle, ar-04 vai a 140 e continua dizendo «downtempo» e «slow build». A linha de qualidade poderia avisar, em ambar, quando uma palavra de andamento do Style («downtempo», «slow», «uptempo», «fast») briga com o numero. Pesar contra: exige uma tabela palavra → faixa de BPM, conhecimento de dominio que muda com o Suno — o mesmo motivo que tirou a tabela de generos vocais da DEC-019. Se entrar, a tabela mora num objeto unico com fonte e data, como o `QUALITY_LIMITS`.

### i-030 💡 Ordem dos campos no cartao: Lyrics acima do Style, como no Suno
`[relatado pelo dono, 2026-10-28]` O cartao mostra Style em cima e Lyrics embaixo; no Suno e o contrario, e copiar na ordem da tela agilizaria. O dono prefere que seja **configuravel**. A preferencia e estado de interface e pode morar no navegador (DEC-004). A decidir na spec: se o export MD segue a ordem escolhida, e onde fica o controle (cabecalho ou cartao).

### i-031 🔨 Prompt e exemplo pela interface do app
`[relatado pelo dono, 2026-10-28, notas 1813 e 1852]` O dono nao quer abrir as pastas do repositorio para pegar o prompt-modelo ou um exemplo: quer copiar o prompt ja com o «Meu pedido» e baixar um exemplo pelo app publicado, como o KCM faz. **Em trabalho (DEC-021, WO 0015):** botoes «Prompt para chats» e «Baixar exemplo», que buscam `schema/PROMPT-PARA-CHATS.md` e `data/demo.json` no clique — fonte unica, sem copia no app. Evolucao possivel: campos guiados para «estruturar» o pedido (quantidade, idioma, instrumental, BPM), so se o reteste mostrar que o texto livre nao basta.

### i-032 💡 Outras plataformas de musica por IA
`[relatado pelo dono, 2026-10-28]` Existem outros sites e apps de celular com estrutura parecida com a do Suno e diferente dela; o dono quer sugestoes para testar e, se valer, ampliar a estrutura do projeto para comporta-los. O esquema ja e agnostico no nome (`targetTool`), mas `style`/`lyrics`/`excludeStyles` espelham os campos do Suno. Proximo passo: um turno de pesquisa atual (plano gratuito, campos equivalentes, limites, API, app mobile) antes de qualquer mudanca de esquema. Pesar contra: generalizar o esquema antes de usar uma segunda plataforma de verdade e especular.

````

### E20 — feedback ao kit: o nicho de musica — `meta/IDEAS.md`

**Ancora, literal:**

````
- **[2026-10-28] Bloco literal da WO com linha de titulo dentro quebra o aplicador por script.** Duas WOs seguidas (0012 e 0013) pararam no meio: o Code aplica lendo os blocos por expressao regular, e um texto novo que contem `## Desfecho` (ou o STATUS inteiro, cheio de `## `) foi lido como o inicio da secao seguinte. As duas se recuperaram so porque a idempotencia pelo texto novo inteiro deixou reexecutar sem duplicar — a regra da idempotencia pagou ali o seu custo. Sugestao ao kit: o modelo de WO dizer que o bloco literal termina na linha de quatro crases e nunca num titulo, e o `apply-wo` delimitar por crases, nao por cabecalho.

````

**Texto novo, literal:**

````
- **[2026-10-28] Bloco literal da WO com linha de titulo dentro quebra o aplicador por script.** Duas WOs seguidas (0012 e 0013) pararam no meio: o Code aplica lendo os blocos por expressao regular, e um texto novo que contem `## Desfecho` (ou o STATUS inteiro, cheio de `## `) foi lido como o inicio da secao seguinte. As duas se recuperaram so porque a idempotencia pelo texto novo inteiro deixou reexecutar sem duplicar — a regra da idempotencia pagou ali o seu custo. Sugestao ao kit: o modelo de WO dizer que o bloco literal termina na linha de quatro crases e nunca num titulo, e o `apply-wo` delimitar por crases, nao por cabecalho.
- **[2026-10-28] O nicho de musica do KCM ainda nao carrega o que este projeto aprendeu sobre o Suno** `[relatado pelo dono]`. Os projetos de musica que o KCM monta nascem sem o conhecimento destilado aqui: `meta/HISTORY.md` §1-13 (o que tem efeito no Suno, com fonte e confianca), a regra de dominio (rotulo fora do copiavel) e o contrato prompt -> JSON. E o teste base de 2026-10-28 mostra o custo de calar: pedido o que o prompt nao ensinava (modulos), tres chats inventaram tres formatos. Sugestao ao kit: o nicho de musica trazer um resumo desse material como ponto de partida — candidato natural e a i-023 (skill com os macetes do Suno), que ja tem o conteudo pronto.

````

### E21 — Fase 2: a linha da frente — `meta/ROADMAP.md`

**Ancora, literal:**

````
- ✅ Prompt-modelo para chats gerarem no esquema (i-002).
- ✅ Script de validação de acervo `scripts/validate.py`.
````

**Texto novo, literal:**

````
- ✅ Prompt-modelo para chats gerarem no esquema (i-002).
- 🔨 Prompt-modelo com contrato de modulos e orcamento de tags; prompt e exemplo pelos botoes do app (DEC-021, i-028, i-031) — falta o reteste do dono.
- ✅ Script de validação de acervo `scripts/validate.py`.
````

### E22 — Conversa 4 no fim — `logs/2026-10-28.md`

**Ancora, literal:**

````
Arvore limpa, `main` == `origin/main`. Relatorio em `../261028-1713-code-cancioneiro-apply-wo0014.txt` confere com `git log` (commit e push). Proxima frente a escolher pelo dono.
````

**Texto novo, literal:**

````
Arvore limpa, `main` == `origin/main`. Relatorio em `../261028-1713-code-cancioneiro-apply-wo0014.txt` confere com `git log` (commit e push). Proxima frente a escolher pelo dono.

## Conversa 4 — chat: teste base do prompt-modelo, spec e WO 0015

### Objetivo do dia
Escolher a proxima frente depois da 0.7.0 e trabalha-la. O dono escolheu a i-028 (folga no prompt-modelo) junto com o teste ponta a ponta do prompt.

### Feito
- Ritual de abertura pelo `261028-HANDOFF-BRIEF.md`; WO 0014 conferida (6 de 7 hashes iguais; o log mudou depois pelo `/wrap`) e arquivada com os dois relatorios.
- Medicao antes de desenhar: o base do acervo tem 8 a 10 tags, mas o excesso vem dos modulos ligados (+2 a +8) — «base com 6 a 8» sozinho resolveria 1 de 7 faixas.
- Teste base do prompt ATUAL pelo dono: tres chats Sonnet 5.5 fora de Projeto (Medio, Medio, Alto) `[relatado pelo dono]`. 9 de 9 faixas com JSON puro, zero rotulos e BPM coerente; 3 de 3 com modulo em formato inventado e aninhado na faixa; 5 de 9 bases com 10+ tags `[medido por instrumento]`.
- Achados de raspao: o app importava isso em silencio (painel com 0 chips) e o `validate.py` quebrava com traceback (FIX-009).
- Spec `meta/specs/261028-prompt-modelo-e-modulos.md`; dono decidiu 1a, 2a, 3a, 4a. A nota `261028-1852.txt` trouxe a decisao 5 (prompt e exemplo pela interface, fonte unica buscada no clique).
- Implementado e testado numa copia (validador nos dois modos; app em Chromium headless contra a 0.7.0): resultados no «Desfecho» da spec. WO 0015 escrita.

### Decisões
DEC-021 (contrato de modulo e orcamento no prompt; prompt e exemplo pela interface).

### Bugs
FIX-009 (modulo dentro da faixa: silencio no app, traceback no validador).

### Aprendizados / armadilhas
- O prompt ensinou bem o que dizia e falhou exatamente no que calava: chat pedido de algo sem contrato inventa um contrato, e cada um inventa um diferente.
- Checagem que nunca viu a entrada errada real nao reprova — quebra. Teste o validador com o que os chats de fato produzem.
- O toast fica atras de um `<dialog>` modal (camada de topo): a janela precisa da propria linha de status.

### Onde parei
WO 0015 entregue. App e validador testados; o reteste do prompt com chats e a conferencia na tela sao do dono, depois do push.

### Próximos passos
Aplicar a WO 0015; roteiro do dono (tela + reteste); fechar a frente na 0.8.0 com CHANGELOG, README e CONTEXT. Depois: i-030 (ordem dos campos) ou i-032 (pesquisa de plataformas).
````

## Edicao E23 — prompt-modelo inteiro — `schema/PROMPT-PARA-CHATS.md`

Sem ancora: substitua o arquivo inteiro pelo bloco abaixo. Ele tem cercas de TRES crases dentro (o exemplo
JSON); o bloco termina na linha de QUATRO.

````
# Prompt-modelo — gerar canções no esquema do Cancioneiro

> **Para que serve:** cole o bloco abaixo num chat de IA (Claude, etc.) junto do seu pedido de música.
> O chat passa a devolver a canção/álbum em **JSON no esquema canônico**, pronto para importar
> na ferramenta Cancioneiro — sem inventar convenção própria.
>
> **Como usar:** no app, botão **Prompt para chats** — escreva o pedido e copie o prompt já completo.
> Ou, à mão: copie tudo dentro da linha `--- INÍCIO ---` até `--- FIM ---`, cole no chat,
> e complete o "Meu pedido" no final. O chat responde só com o JSON.

---

--- INÍCIO ---

Você vai gerar canções para IA de música (Suno) em um formato JSON específico. Siga estas regras à risca.

## Regra inviolável: separe conteúdo copiável de referência humana
- **Copiável** (vai literalmente para os campos do Suno): `style`, `lyrics`, `excludeStyles`.
- **Referência humana** (nunca vai para o Suno, é só para organização): `title`, `language`, `context`, `notes`, `tags`, `key`.
- NUNCA coloque rótulos como "ESTILO:", "[LETRA]", "[ESTILO SUNO]" dentro de `style` ou `lyrics`. Esses campos contêm APENAS o texto que eu colaria direto no Suno.

## Os dois campos do Suno
- **`style`** = o campo "Style of Music": mundo sonoro (gênero, instrumentos, clima, produção, andamento). Texto separado por vírgulas, **sem colchetes**.
- **`lyrics`** = o campo "Lyrics": estrutura e vocal. Colchetes vão aqui.
  - Faixa instrumental em loop/circular: use apenas `[Instrumental]`.
  - Faixa instrumental linear (com arco: abertura, final): use tags de arco `[Intro]`, `[Build]`, `[Climax]`, `[Outro]`, vocabulário neutro de gênero.
  - Faixa com vocal: escreva a letra com tags de seção (`[Verse]`, `[Chorus]`, `[Pre-Chorus]`, etc.).

## Como construir o `style` — cinco camadas audíveis
Descreva decisões que dá para OUVIR, não elogios ("épico", "lindo", "profissional" não ajudam). Pense em camadas:
1. **Gênero/lane** — a família + um sabor secundário (ex.: "dark ambient cinematic", "k-pop girl crush"). 1–2 gêneros no máximo.
2. **Movimento** — como pulsa (ex.: "driving rhythm", "half-time pulse", "sparse").
3. **Instrumentos** — 2–4, com frase específica ("delicate piano arpeggios" > "piano"). Não empilhe.
4. **Voz** — quem conduz ("close-mic alto", "female soprano", ou "no vocals" se instrumental).
5. **Produção/clima** — espaço da mixagem + 1–2 palavras de clima ("dry upfront mix, intimate", "cinematic, ominous").
Coloque o mais característico NO INÍCIO (as primeiras ~20–30 palavras pesam mais). Se quiser sugerir andamento, inclua "NN bpm" — mas saiba que o Suno trata BPM como aproximação, não comando.

**Orçamento de tags.** Cada trecho entre vírgulas é uma tag. Escreva o `style` com **6 a 8 tags**: menos que 4 fica vago; acima de ~10 as últimas perdem efeito. Prefira juntar ideias numa tag específica ("warm analog synth pads") a espalhar adjetivos soltos ("warm, analog, synth, pads"). Se o `style` tiver "NN bpm", use o mesmo número no campo `bpm`.

## Elementos indesejados
Não escreva "no X" dentro do `style` para remover algo. Coloque em `excludeStyles` (array), que mapeia para o campo Exclude do Suno.

## Módulos de estilo (só se eu pedir variações por módulo)
Um módulo é um trecho de `style` que eu ligo e desligo na ferramenta para gerar variações sem reescrever a faixa. Se eu não pedir módulos, deixe `styleModules` vazio (`[]`) na coleção e nas faixas.
- **Onde moram:** os módulos são declarados UMA vez, no `styleModules` da **coleção** (topo do JSON), como objetos. Nunca escreva o objeto do módulo dentro da faixa.
- **Formato de cada módulo:** `id` (único, minúsculas-com-hífens), `category`, `label` (nome curto para o botão), `fragment` (o trecho copiável: 1 a 3 tags separadas por vírgula, sem colchetes, sem "no X"), `notes` (opcional, referência humana). Não existem outros campos: nada de `enabled`, `default`, `text`, `style` ou `excludeStyles` dentro do módulo.
- **`category`** é exatamente um destes valores: `genre`, `motion`, `instrument`, `vocal`, `mood`, `production`, `tempo`.
- **Na faixa, `styleModules` é uma lista de ids** (texto). Os ids citados são os módulos que já vêm **ligados**; os demais da coleção ficam disponíveis, desligados, para eu experimentar.
- **Orçamento com módulos:** o `style` da faixa continua com 6 a 8 tags, e as tags dos módulos citados somadas às do `style` não passam de 10. Módulo que repete um trecho que já está no `style` não soma nada. Ofereça os módulos extras declarados na coleção, sem citar na faixa.
- **Andamento:** BPM só em módulo de `category` `tempo`, com o fragmento no formato "NN bpm". Em outras categorias, não escreva número de BPM.

## Esquema JSON de saída
Devolva um objeto de **coleção** com esta estrutura (campos obrigatórios marcados com *):

```json
{
  "schemaVersion": "1.0",              // * sempre "1.0"
  "title": "Nome do álbum ou acervo",  // *
  "description": "opcional",
  "targetTool": "suno",
  "styleModules": [                    // opcional — os módulos, declarados uma vez (ver seção acima)
    { "id": "mod-tape-warmth", "category": "production", "label": "Textura de fita",
      "fragment": "tape saturation, vintage warmth", "notes": "opcional, referência humana" }
  ],
  "albums": [                          // *
    {
      "id": "album-slug",              // * minúsculas, hífens
      "title": "Nome do Álbum",        // *
      "description": "opcional",
      "songs": [                       // *
        {
          "id": "faixa-slug",          // * único, minúsculas-com-hífens
          "title": "Título da Faixa",  // * referência humana
          "language": "pt-BR",         // * ou "instrumental", "ja", "en", etc.
          "state": "ideia",            // * um de: ideia | gerada | editada | loop-pronto | aprovada
          "style": "...",              // * COPIÁVEL — Style of Music, sem colchetes, 6 a 8 tags
          "lyrics": "...",             // * COPIÁVEL — Lyrics, com colchetes/tags
          "bpm": 120,                  // opcional, número ou null
          "key": "D minor",            // opcional, referência humana
          "excludeStyles": [],         // opcional, array de strings copiáveis p/ Exclude
          "variants": [                // opcional — mesma letra, style alternativo
            { "label": "Nome da variante", "style": "...", "excludeStyles": [] }
          ],
          "styleModules": ["mod-tape-warmth"], // opcional — SÓ ids da coleção; os citados vêm ligados
          "context": "cena/uso",       // opcional, referência humana
          "notes": "notas de produção",// opcional, referência humana
          "tags": []                   // opcional, etiquetas livres
        }
      ]
    }
  ]
}
```

## Saída
- Responda **APENAS com o JSON válido**, sem texto antes ou depois, sem cercas de ``` markdown.
- JSON válido: aspas duplas, sem vírgula sobrando, sem comentários.
- Se eu pedir uma única faixa, ainda assim embrulhe em coleção→álbum→[faixa].

## Meu pedido
(descreva aqui as canções que você quer: tema, quantidade, idioma, clima, se instrumental ou com vocal, referências sonoras…)

--- FIM ---

---

## Notas para o mantenedor (não faz parte do prompt)

- Este prompt reflete o `song.schema.json` e `collection.schema.json` v1.0. Se o esquema mudar, **atualize este arquivo junto** (uma fonte por dado — o esquema é a fonte; este prompt é um espelho didático).
- **O app lê ESTE arquivo** (botão «Prompt para chats»): busca-o no Pages a cada clique e copia o que está entre as linhas `--- INÍCIO ---` e `--- FIM ---`, trocando a linha entre parênteses abaixo de `## Meu pedido` pelo pedido digitado. Não há segunda cópia do prompt. Mantenha as duas linhas de marcação e essa linha entre parênteses: o `scripts/validate.py` reprova se uma delas sumir.
- **Módulos (DEC-016, DEC-021):** a coleção carrega os próprios módulos; a faixa cita ids. O teste de 2026-10-28 (`meta/specs/261028-prompt-modelo-e-modulos.md`) mostrou que, sem a seção de módulos, três chats inventaram três formatos e aninharam o módulo na faixa — o app abria o painel com 0 chips. As sete `category` são as camadas do app (`LAYERS` em `app/index.html`); a de `tempo` vira atalho do controle de BPM (DEC-020).
- **Orçamento de tags (6 a 8 no style; até 10 com os módulos ligados):** mesma faixa do painel de qualidade (`QUALITY_LIMITS` em `app/index.html`, com fonte e data). Se o painel mudar, mude aqui.
- O prompt ensina as cinco camadas e a regra copiável/referência — é o principal contra a bagunça dos álbuns antigos.
- Teste ponta a ponta: copie o prompt pelo app, peça algo num chat novo fora de Projeto, salve a resposta e importe na ferramenta; depois `python3 scripts/validate.py <arquivo>`.
````

## Edicao E24 — STATUS inteiro — `meta/STATUS.md`

Sem ancora: substitua o arquivo inteiro. **O que saiu e para onde foi:** o bloco «Ultima conversa» da 0.7.0
(esta no CHANGELOG [0.7.0], DEC-020, FIX-008 e no log); a linha «Prompt-modelo» de «Funciona» (o prompt
mudou e esta em «Em progresso» ate o reteste); o item 2 do backlog, «testar o prompt-modelo ponta a ponta»
(feito: o teste base; o reteste esta em «Pendencias do dono»). Entraram: i-030 e i-032 no backlog, os botoes
no «Em progresso» e a nota de rede/`file://`.

````
# STATUS.md — Cancioneiro

> **O agora.** O que funciona, o que está em progresso, o que está quebrado, backlog curto.
> Rolante: item resolvido sai daqui e vai para o CHANGELOG. Médio/longo prazo vive no ROADMAP.

**Versão atual:** 0.7.0 · **Fase:** 3a, 3a.2 e o BPM da 3b concluídos · prompt-modelo com contrato de módulos e botões de prompt/exemplo aplicados (WO 0015), à espera do reteste e da conferência na tela · Fase 2 com i-008 em aberto

---

## Última conversa (2026-10-28, prompt-modelo e módulos)

- **Teste base do prompt-modelo** `[relatado pelo dono]`: três chats Sonnet 5.5 fora de Projeto. O que o prompt ensinava saiu certo em 9 de 9 faixas (JSON puro, zero rótulos, BPM coerente); o que ele calava, não — os três inventaram um formato de módulo e o aninharam na faixa, e 5 de 9 bases saíram com 10 tags ou mais `[medido por instrumento]`. Os três JSONs ficam na pasta-pai como linha de base do reteste.
- **Spec `meta/specs/261028-prompt-modelo-e-modulos.md` decidida** (1a, 2a, 3a, 4a, e a 5 da nota do dono) e aplicada pela WO 0015: DEC-021 e FIX-009.
- **Este bloco substitui o anterior, de 2026-10-28, que fechava a 0.7.0.** O que ele dizia está no CHANGELOG [0.7.0], no DECISIONS (DEC-020, FIX-008) e em `logs/2026-10-28.md`.

## Funciona (pronto)

- **Ferramenta `app/index.html`:** importa/carrega JSON, cartões por álbum, copiar Style/Lyrics/Exclude por botão (o botão entrega o texto que está na tela — FIX-007), marca «usei», filtros por álbum/estado/uso, busca, módulos de estilo que recompõem o Style ao vivo, variantes e notas recolhíveis, «Baixar .json» limpo e «Importar .json» que saneia chaves internas e diz quantas removeu (FIX-004/006). A versão aparece no cabeçalho.
- **Painel de qualidade (0.5.0, DEC-018):** linha abaixo de Style, Lyrics e Exclude com caracteres contra o limite do campo, tags do Style e negações «no X». Vermelho só para truncamento.
- **Custo de cada módulo no chip (0.6.0, DEC-019):** com o painel de módulos aberto, cada chip mostra `−N`, `+N` ou `0` tags; a linha de qualidade diz quanto o style base usa sozinho quando o recomposto passa de 10.
- **Controle de BPM no cartão (0.7.0, DEC-020):** campo 20-300 com `−5`/`+5` e «voltar a N» governa todo «NN bpm» do Style principal; o chip de andamento é atalho (no máximo um ligado); variantes e «Baixar .json» não mudam; o valor é só da sessão.
- **Esquema JSON canônico** (`schema/`). Biblioteca de referência para autoria em `schema/style-modules.json` (27 módulos, sete camadas); cada acervo traz os seus (DEC-016).
- **Datasets:** `data/exemplo-cinzeiro.json` (1 faixa, com os 5 módulos que cita) e `data/demo.json` (2 álbuns, 3 faixas). O álbum de referências do dono mora fora do repo, em `../album-referencias (1).json` (7 faixas, 50 módulos).
- **Validação** (`scripts/validate.py`): sintaxe, esquema (com `jsonschema`), integridade referencial dos módulos (id ausente ou objeto no lugar do id, sem traceback — FIX-009), versão igual nos quatro lugares, um BPM só por faixa (DEC-020) e as marcações do prompt que o app lê (DEC-021); código 1 se falhar; a última linha diz se o esquema foi de fato conferido.
- **Export MD** (faixa / álbum / acervo), com o Style recomposto e o rótulo fora do bloco.
- **Publicado no GitHub Pages** em `https://joaolucas-nds.github.io/cancioneiro/app/index.html` — o push em `main` publica.

## Em progresso

- **Prompt-modelo e módulos (DEC-021, FIX-009; i-028, i-031)** — aplicado pela WO 0015, testado pelo chat numa cópia (Desfecho da spec). Falta: (1) a conferência na tela, no app publicado; (2) o reteste do prompt com três chats nas condições do teste base. Com os dois, fecha a 0.8.0 (CHANGELOG, README e CONTEXT).
  - Prompt (`schema/PROMPT-PARA-CHATS.md`): contrato de módulo da DEC-016 (módulos na coleção, faixa cita ids, citado = ligado), style com 6 a 8 tags e até 10 com os módulos ligados, BPM só em módulo de andamento.
  - App: botões «Prompt para chats» (janela com «Meu pedido») e «Baixar exemplo», que buscam o prompt e o `data/demo.json` no clique — fonte única; e o aviso na importação quando um módulo citado não existe na coleção.

## Quebrado / pendências que travam

- (nada quebrado)

## Pendências do dono

- **Conferir na tela e retestar o prompt** — roteiro entregue pelo chat na conversa de 2026-10-28, depois do push da WO 0015.
- **Instalar o validador de esquema nesta máquina.** Sem `jsonschema` e `referencing`, o `validate.py` só confere sintaxe e diz `ESQUEMA NAO CONFERIDO` na última linha. Uma vez, no CMD: `pip install jsonschema referencing --break-system-packages`. Depois, `python3 scripts/validate.py` deve terminar em `Tudo conforme ao esquema.`
- **Trazer os álbuns antigos** para a pasta-pai, quando quiser — o dono disse que vai trazer; desbloqueiam a i-008.

## Backlog curto (próximas ações concretas)

1. **Fechar a frente do prompt-modelo** na 0.8.0, depois do roteiro do dono.
2. **Ordem dos campos no cartão** (i-030) — Lyrics acima do Style, como no Suno, configurável.
3. **Pesquisar outras plataformas de música por IA** (i-032) — um turno de pesquisa antes de qualquer mudança de esquema.
4. **Converter 1 álbum real** (i-008) — quando os `.md` de origem chegarem à pasta-pai.
5. **Avisar palavra de andamento que contradiz o BPM** (i-029) — pede uma tabela palavra → faixa de BPM, com fonte e data.
6. **Importar prompts prontos dos álbuns como módulos** — o último ⬜ da 3b no ROADMAP; ainda sem spec.

## Notas de estado

- **Repo local do dono:** `C:\Users\alexk\Tools\cancioneiro\cancioneiro` (Windows). O chat lê e grava na pasta vinculada; commit e push são do Code (DEC-010). A pasta-pai guarda relatórios, notas e o acervo do dono, fora do Git; o lido vai para `../notas-arquivadas/`.
- **Canal:** pasta vinculada é o padrão; a cópia achatada (FlatDrop) é reserva (DEC-017).
- **Limites do Suno:** o v6 saiu em 2026-09-09 e a nota oficial não documenta limite de campo; os números do painel vêm de fonte secundária, com fonte e data no `QUALITY_LIMITS` (DEC-018). Outra fonte secundária (2026-08) põe o ideal em 4 a 7 descritores; o prompt usa 6 a 8. Reconferir quando houver documentação oficial. O `meta/HISTORY.md` ainda descreve o v5.5 e precisa de uma atualização sobre o v6.
- **Botões de prompt e exemplo:** dependem de rede e do Pages. No `file://`, só funcionam se o Pages aceitar o `fetch` de uma página local — não conferido; sem isso, a janela mostra o link para a versão publicada (DEC-021).
- **Estado de sessão** (módulos ligados e BPM escolhido) sobrevive a filtro, busca e «marcar usei»; volta ao acervo ao recarregar a página ou importar de novo (FIX-008, DEC-020).
- **Limite conhecido:** `tryAutoLoad` (carregamento automático pelo Pages) não saneia chaves internas — só a importação por arquivo faz isso. Inócuo enquanto nenhum acervo contaminado for para `data/`.
- **Pendência de contexto — ASU:** o dono perguntou se o «modo ASU» do KCM seria melhor que o modo Code para este projeto; ficou pendente até ele trazer a descrição do ASU `[relatado pelo dono, sem material de apoio]`.
- Design: na recomposição do Style a base manda — desligar um módulo não remove o que já está no style base; módulos só somam. O dedup compara sequências de palavras (FIX-003). Os módulos de gênero e de andamento costumam custar 0 tag por isso (DEC-019). O chip de andamento é atalho do controle de BPM, no máximo um ligado (DEC-020).
````

## Fora de escopo

- **CHANGELOG, README, CONTEXT e a 0.8.0** — so depois do roteiro do dono, na proxima WO.
- **i-030** (ordem dos campos) e **i-032** (outras plataformas) — capturadas, nao implementadas.
- `data/` e o resto de `schema/` — nada muda. O esquema continua o mesmo: o prompt so ensina o que ele ja dizia.

## Armadilhas desta WO

- **Blocos com `## ` dentro** (E17, E22, E23, E24): delimite pelas crases. Foi o que parou as WOs 0012 e 0013.
- **E23 tem cercas de tres crases dentro** (o exemplo JSON do prompt). O bloco so termina na de quatro.
- **`--- INÍCIO ---` tem acento** e e lido literal pelo app e pelo validador. Grave em UTF-8; `grep` com
  acento precisa de `LC_ALL=C.UTF-8`.
- **Edicoes curtas no `validate.py`** (E10 a E16): a funcao `check_module_refs` muda em tres pedacos seguidos. Aplique na ordem; a idempotencia pelo texto novo inteiro protege a reexecucao.
- **O app busca arquivos no clique.** Nao ha nada para testar no Code: o comportamento so aparece servido
  pelo Pages, depois do push. A tela e do dono.
- **Fim de linha:** os arquivos sao LF. Se um hash de chegada divergir, rode `file <arquivo>` antes de
  concluir que uma edicao errou.

## Depois de aplicar — conferencia antes do commit

| # | Checagem | Comando | Esperado |
|---|---|---|---|
| 1 | **Os nove arquivos sao os testados** | `sha1sum app/index.html scripts/validate.py schema/PROMPT-PARA-CHATS.md meta/DECISIONS.md meta/IDEAS.md meta/ROADMAP.md meta/STATUS.md logs/2026-10-28.md meta/specs/261028-prompt-modelo-e-modulos.md` | a coluna **chegada** do cabecalho, os nove. **Prova as 24 edicoes.** |
| 2 | As funcoes novas do app | `grep -cE 'function (moduleRefsNotice\|fetchFirst\|extractPrompt\|promptStatus\|copyPrompt\|downloadExample)\b' app/index.html` | `6` |
| 3 | O aviso nos dois caminhos de carga | `grep -c 'moduleRefsNotice(json)' app/index.html` | `3` (a definicao e as duas chamadas) |
| 4 | O validador | `grep -c '^def check_prompt' scripts/validate.py`, `grep -c 'errors += check_prompt()' scripts/validate.py`, `grep -c 'not isinstance(mid, str)' scripts/validate.py` | `1`, `1`, `1` |
| 5 | Os registros | `grep -c '^## FIX-009' meta/DECISIONS.md`, `grep -c '^## DEC-021' meta/DECISIONS.md`, `grep -cE '^### i-03[012] ' meta/IDEAS.md`, `grep -c '^## Conversa 4' logs/2026-10-28.md` | `1`, `1`, `3`, `1` |
| 6 | Validacao passa | `python3 scripts/validate.py; echo "exit=$?"` | `exit=0`, com a linha `OK  prompt com as marcacoes que o app le` |
| 7 | O album do dono tambem passa | `python3 scripts/validate.py "../album-referencias (1).json"; echo "exit=$?"` | `exit=0` |
| 8 | Nada de dados | `GIT_OPTIONAL_LOCKS=0 git status --short data` | saida **vazia** |
| 9 | Nenhum relatorio `.txt` no repo | `GIT_OPTIONAL_LOCKS=0 git status --short \| grep -c '\.txt'` | `0` |

**Os tres campos de cada passo:** as nove sao rodadas por **quem aplica (o Code)**, na raiz do repo
(`C:\Users\alexk\Tools\cancioneiro\cancioneiro`), em Git Bash, com `LC_ALL=C.UTF-8`. **Chega no ramo?**
A checagem 1 cobre os nove arquivos inteiros, e o app e o validador de chegada foram executados pelo chat.
**Esta e qual pergunta?** As nove respondem «esta la?». O que so a tela e um chat novo respondem vai no
roteiro que o chat entrega **no corpo da resposta**, nao aqui.

## Relatorio de aplicacao

Grave em `../261028-HHMM-code-cancioneiro-apply-wo0015.txt`, com o `HHMM` de `date +%y%m%d-%H%M` rodado na
hora. Diga o resultado da checagem 1 em primeiro lugar. A conferencia na tela e o reteste **nao sao seus**.

**Proximo comando** (ultima linha do relatorio, cru e sozinho):

```
/wrap
```

## Commit

```
git add app/index.html scripts/validate.py schema/PROMPT-PARA-CHATS.md meta/DECISIONS.md meta/IDEAS.md meta/ROADMAP.md meta/STATUS.md logs/2026-10-28.md meta/specs/261028-prompt-modelo-e-modulos.md meta/workorders
```

```
git commit -m "feat: prompt-modelo com contrato de modulos e botoes de prompt e exemplo no app" -m "DEC-021: o prompt ensina os modulos na colecao com id, category, label e fragment, a faixa cita ids, style com 6 a 8 tags e ate 10 com os modulos ligados, BPM so em modulo de andamento. Botoes Prompt para chats e Baixar exemplo buscam o prompt e o data/demo.json no clique, sem copia no app; o validate.py confere as marcacoes do prompt. FIX-009: modulo declarado dentro da faixa sumia em silencio no app e derrubava o validador com traceback; agora o validador reprova com mensagem e a importacao avisa quantos modulos citados nao existem. Registra i-030, i-031 e i-032."
```

```
git push
```
