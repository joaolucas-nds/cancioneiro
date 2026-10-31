# WO 0020 — Conversor de `Albuns/`, kit de música e versão 0.10.0

## Cabecalho

> **Tipo:** WO de CODIGO (`scripts/`, `kit-musica/`, versao do app) e de registro.
> **Config sugerida:** Sonnet · `/effort medium`. 20 edicoes literais e 8 arquivos inteiros (7 novos e o STATUS), todos aplicados e testados pelo chat numa copia; cada arquivo tem hash de chegada.
> **Pre-requisito:** commit `3405b9b`, branch `main`, sincronizada com `origin/main`, **arvore limpa** (so esta WO aparece como `??`).
> **Base:** decisoes do dono de 2026-10-29 (grupos de `Albuns/` aprovados; kit de musica 1A, 2A, 3A); leitura do KCM v1.133.0 com acesso concedido pelo dono.
> **Depende de:** WO 0019, ja aplicada (`d9b401f`, wrap `3405b9b`).
>
> **Arquivos — partida e chegada, os dois medidos pelo chat** (partida conferida no disco do dono em 2026-10-31; chegada = resultado de aplicar literalmente as edicoes abaixo, em LF):
>
> | arquivo | partida (sha1) | chegada (sha1) |
> |---|---|---|
> | `app/index.html` | `1bba24aa98ee575d98ffdb103e308a168f8b044e` | `492bf70c278df44f5c93bfea922eb107f57ffe4d` |
> | `scripts/validate.py` | `ef1cc0a09fd3a69d6e0b95022010a4a28c398b40` | `0f5a5be23f02018df89b58da09419501311fc716` |
> | `meta/CHANGELOG.md` | `7ee775b065e90cf6439a51f0ec3832e46f1b5f9c` | `ab37dc656fd5f59fe305998764bd0e60d5e8b6b2` |
> | `README.md` | `4ee8f90ffbb04f4611cdc1e4213f017f35fa58b9` | `d76009fef63217e421221ec429b5a27b2f109528` |
> | `meta/CONTEXT.md` | `c66682378c223edadda1f2e27c96e8a5bd525b0a` | `6b574812a0df85e7e98d6a9ec46497500adc4dd0` |
> | `meta/analises/261029-ANALISE-conversao-dos-albuns.md` | `f3cc98227eab129939ced75ad47f8db509be5bc5` | `3c750aa0a6244744731b45c48f02dbce37717ac9` |
> | `meta/analises/261029-ANALISE-kit-de-musica.md` | `354f04adb7b04ca3f615591e79238bde1eb16f1a` | `8f9298a3de8bd4e8036da1ec9e10dcd83e8a6d25` |
> | `meta/IDEAS.md` | `8565acfdc0e9d818547e7f873124783cd2558a24` | `b4ee9da4a911a769146c0c8b0bd64446c7a75857` |
> | `meta/ROADMAP.md` | `2539ded2102f0f282a340d089e034f511936ee4b` | `35478d9b3c0cf02f6ccb9b9f1498756b19c63728` |
> | `meta/DECISIONS.md` | `7a011004f9ac99d31fc672c714ed7dd220716d04` | `f1649e2cf9f3c40ecd33c252f5cf5ee145552421` |
> | `scripts/convert_guides.py` | (nao existe) | `babdcd4968782c2efc2a89ac87e4be1a03a3b1b8` |
> | `scripts/test_convert_guides.py` | (nao existe) | `b481f108ab2a0a947111c55092ae5898f8f58ffa` |
> | `kit-musica/README.md` | (nao existe) | `f97088403a74482dd37a285b28785d97298d1f27` |
> | `kit-musica/BLOCO-SUNO.md` | (nao existe) | `e401e8f6fe07625bdfcf24fdb92cdc80cff8426a` |
> | `kit-musica/skills/macetes-suno/SKILL.md` | (nao existe) | `f67f59528df6585052a1bf0b6fe2865afbb155b5` |
> | `kit-musica/skills/revisar-faixa/SKILL.md` | (nao existe) | `11e1cc7460864fde4bbc19e95ec57e0e5d6f6d2e` |
> | `logs/2026-10-31.md` | (nao existe) | `c7d9213ed96cafdef10c4353e27c14e607dc35af` |
> | `meta/STATUS.md` | `172781e422e826d66a079e023d74f9347bad5d35` | `116bf617489b154e79f249cdee2a7dc0cf971a61` |
>
> **Ancora semantica:** se um trecho-ancora nao bater EXATAMENTE, PARE e reporte.
> **Idempotencia:** antes de cada edicao, procure o texto NOVO INTEIRO; se ja estiver la, PULE e diga no relatorio. Arquivo inteiro: se o hash ja for o de chegada, PULE.
>
> **Ancoras lidas em:** cada ancora foi extraida pelo chat do arquivo de partida (`git show 3405b9b:<arquivo>`, igual ao disco do dono pelos hashes acima) e conferida como ocorrendo **exatamente 1 vez** no estado em que a edicao e aplicada, na ordem abaixo.

---

## 1. Por que

**`Albuns/` (i-008, i-038).** O dono aprovou os 12 grupos. `scripts/convert_guides.py` le os oito guias de
formatos mistos e, com um mapa de grupos (fora do repo), grava uma colecao por cena de uso. Medido pelo chat:
**205 de 205** faixas, 0 rotulos no copiavel, validador completo verde, 205 cartoes no app; o resultado nao
depende da ordem dos arquivos (mesmo hash com a ordem invertida). O acervo e o mapa ja estao em `../acervos/`.
Duas contas da proposta corrigidas na analise: eram 205 faixas, nao 172; «Rise of the Eternal» sao duas cancoes.

**Kit de musica (i-039, DEC-027).** O nicho Musica do KCM e de musica tocada; `kit-musica/` traz o que muda quando
a faixa e gerada pelo Suno: um bloco para as Instrucoes e o CEREBRO do projeto, a skill `macetes-suno` e a skill
`revisar-faixa`, cujo script acha nos acervos do dono o que o painel do app acha (72 letras e 138 styles na Rainha
da Preguica). O `validate.py` passa a prender os limites da skill aos do app.

**0.10.0** no app, CHANGELOG, README e STATUS. **Registro:** DEC-027, as duas analises com desfecho, IDEAS
(i-008, i-022, i-023 e i-038 entregues; i-039 em trabalho, com gatilho; feedback ao KCM), ROADMAP, CONTEXT, log
novo de 2026-10-31, STATUS (sai o item que o `/wrap` anexou no fim do arquivo; o conteudo dele esta no log).

## Edicao 0 — Conferencia de hash e de arvore

```
sha1sum app/index.html scripts/validate.py meta/CHANGELOG.md README.md meta/CONTEXT.md meta/analises/261029-ANALISE-conversao-dos-albuns.md meta/analises/261029-ANALISE-kit-de-musica.md meta/IDEAS.md meta/ROADMAP.md meta/DECISIONS.md meta/STATUS.md
ls scripts
GIT_OPTIONAL_LOCKS=0 git status --short
```

Os onze batem com a coluna **partida**; `scripts` tem `convert_br.py`, `test_convert_br.py` e `validate.py`; o
`git status` mostra so esta WO. Qualquer outra coisa: **PARE e reporte**.

## Edicoes E01 a E28

Na ordem. **Todas as secoes de edicao tem o mesmo titulo, `### Exx — ...`**, inclusive as de arquivo inteiro.
Copie o que esta ENTRE as linhas de quatro crases, sem elas. **O bloco termina na linha de quatro crases, nunca
num titulo:** varios blocos trazem `## `, `### `, `---` ou cercas de tres crases (os guias sinteticos do teste, o
script da skill, o bloco do `BLOCO-SUNO.md`).

### E01 — app: versao (1) — `app/index.html`

**Ancora, literal:**

````
         que app, CHANGELOG, README e STATUS dizem a mesma (i-027). -->
    <span class="version" data-role="app-version">v0.9.1</span>
  </div>
````

**Texto novo, literal:**

````
         que app, CHANGELOG, README e STATUS dizem a mesma (i-027). -->
    <span class="version" data-role="app-version">v0.10.0</span>
  </div>
````

### E02 — validate: limites do kit (1) — `scripts/validate.py`

**Ancora, literal:**

````

Checa seis coisas:
  1. Sintaxe JSON de todos os schemas e datasets.
````

**Texto novo, literal:**

````

Checa sete coisas:
  1. Sintaxe JSON de todos os schemas e datasets.
````

### E03 — validate: limites do kit (2) — `scripts/validate.py`

**Ancora, literal:**

````
     abaixo de «## Meu pedido» (DEC-021).

````

**Texto novo, literal:**

````
     abaixo de «## Meu pedido» (DEC-021).
  7. Os limites da skill kit-musica/skills/revisar-faixa sao os do painel de
     qualidade do app (QUALITY_LIMITS): o kit nao envelhece separado (DEC-027).

````

### E04 — validate: limites do kit (3) — `scripts/validate.py`

**Ancora, literal:**

````

def main(argv):
````

**Texto novo, literal:**

````

KIT_SKILL = "kit-musica/skills/revisar-faixa/SKILL.md"


def check_kit():
    """Os limites da skill revisar-faixa sao os do app (DEC-027).

    A skill copia os numeros do `QUALITY_LIMITS` para o script que o chat roda no
    projeto de musica. Se o app mudar um limite e a skill nao, o projeto passa a
    revisar contra o numero velho sem nada falhar — por isso a checagem.
    """
    def read(path):
        with open(os.path.join(ROOT, path), encoding="utf-8") as f:
            return f.read()

    try:
        app, skill = read("app/index.html"), read(KIT_SKILL)
    except OSError as e:
        print(f"ERRO no kit: nao consegui ler: {e}")
        return 1
    block = re.search(r"const QUALITY_LIMITS = \{(.*?)\n\};", app, re.S)
    lim = {}
    for name, body in re.findall(r"^\s*(\w+):\s*\{([^}]*)\}", block.group(1) if block else "", re.M):
        for key, val in re.findall(r"(\w+):\s*(\d+)", body):
            lim[f"{name}.{key}"] = int(val)
    want = {  # constante da skill -> chave do QUALITY_LIMITS
        "LYRICS_MAX": "lyrics.max", "LYRICS_WARN": "lyrics.warn", "STYLE_MAX": "style.max",
        "STYLE_WARN": "style.warn", "TAGS_VAGUE": "tags.vague", "TAGS_MANY": "tags.many",
    }
    got = {}
    for names, values in re.findall(r"^(\w+(?:,\s*\w+)*)\s*=\s*(\d+(?:,\s*\d+)*)", skill, re.M):
        for n, v in zip(re.split(r",\s*", names), re.split(r",\s*", values)):
            got[n] = int(v)
    bad = [f"{k} = {got.get(k, 'ausente')} na skill, {lim.get(v, 'ausente')} no app ({v})"
           for k, v in want.items() if got.get(k) is None or got.get(k) != lim.get(v)]
    if bad:
        print(f"ERRO no kit {KIT_SKILL}: limites diferentes do QUALITY_LIMITS do app:")
        for b in bad:
            print(f"   {b}")
        return 1
    print(f"OK  kit: limites da skill revisar-faixa iguais ao app ({len(want)})")
    return 0


def main(argv):
````

### E05 — validate: limites do kit (4) — `scripts/validate.py`

**Ancora, literal:**

````
    errors += check_prompt()

````

**Texto novo, literal:**

````
    errors += check_prompt()
    # kit de musica: os limites da skill sao os do app (DEC-027)
    errors += check_kit()

````

### E06 — CHANGELOG: [0.10.0] (1) — `meta/CHANGELOG.md`

**Ancora, literal:**

````
> Histórico de versões entregues. SemVer + Keep a Changelog. Cresce no topo.

````

**Texto novo, literal:**

````
> Histórico de versões entregues. SemVer + Keep a Changelog. Cresce no topo.

---

## [0.10.0] — 2026-10-31

Os álbuns antigos de `Albuns/` convertidos e reagrupados (i-008, i-038), e o kit de música para os projetos do KCM (i-039, DEC-027).

### Added
- **Conversor dos guias de `Albuns/` (`scripts/convert_guides.py`):** lê os oito guias de formatos mistos — rótulo no bloco, «Style — Opção A/B», «Style Prompt»/«Letra», letra em Markdown fora de bloco, «Variações para» — e grava uma coleção no esquema. Com `--groups`, um mapa (fora do repo) reagrupa as faixas em álbuns e reprova faixa perdida ou id inexistente. Teste com guias sintéticos em `scripts/test_convert_guides.py` (8 casos). Medido no acervo do dono: 205 de 205 faixas, 12 álbuns por cena de uso; o arquivo fica fora do repo.
- **Kit de música (`kit-musica/`, DEC-027):** `BLOCO-SUNO.md` (cinco linhas para as Instruções de um projeto de música do KCM e uma seção para o CEREBRO dele), skill `macetes-suno` (o que tem efeito no Suno, com exemplo bom e ruim) e skill `revisar-faixa` (oito conferências por faixa, com script que conta). A revisão acha nos acervos do dono o que o painel do app acha: 72 letras acima de 5.000 caracteres e 138 styles acima de 10 tags na Rainha da Preguiça.
- **Validação:** o `validate.py` confere que os limites da skill `revisar-faixa` são os do `QUALITY_LIMITS` do app.

````

### E07 — README (1) — `README.md`

**Ancora, literal:**

````

> **Estado:** v0.9.1 — ferramenta em uso. Lê o acervo, copia por campo, troca módulos de estilo, ajusta o BPM, **mede cada prompt contra os limites do Suno**, exporta Markdown e **entrega o prompt para chats gerarem canções no esquema**. Publicada no GitHub Pages. Ver `meta/ROADMAP.md`.

````

**Texto novo, literal:**

````

> **Estado:** v0.10.0 — ferramenta em uso. Lê o acervo, copia por campo, troca módulos de estilo, ajusta o BPM, **mede cada prompt contra os limites do Suno**, exporta Markdown e **entrega o prompt para chats gerarem canções no esquema**. Publicada no GitHub Pages. Ver `meta/ROADMAP.md`.

````

### E08 — README (2) — `README.md`

**Ancora, literal:**

````
├── scripts/                   # validador e conversores dos guias antigos
├── data/                      # exemplos no esquema (o acervo pessoal mora fora do repo)
````

**Texto novo, literal:**

````
├── scripts/                   # validador e conversores dos guias antigos
├── kit-musica/                # o que o projeto sabe do Suno, para projetos de música (skills e bloco)
├── data/                      # exemplos no esquema (o acervo pessoal mora fora do repo)
````

### E09 — README (3) — `README.md`

**Ancora, literal:**

````

Liste quantos volumes quiser. O conversor tira os rótulos do que é copiável, não corta nada e diz no fim quantas letras e styles passam do limite do Suno — o painel do app marca as mesmas. Depois, arraste o `.json` gerado para o app. Outras famílias de guia pedem outro conversor (ver `meta/analises/`).

````

**Texto novo, literal:**

````

Liste quantos volumes quiser. O conversor tira os rótulos do que é copiável, não corta nada e diz no fim quantas letras e styles passam do limite do Suno — o painel do app marca as mesmas. Depois, arraste o `.json` gerado para o app.

Os guias de formatos mistos (`Albuns/`) vão pelo `scripts/convert_guides.py`, que aceita um mapa de grupos para reagrupar as faixas em álbuns:

```
python3 scripts/convert_guides.py ../acervos/albuns-reagrupados.json ../Albuns/*.md --groups ../acervos/albuns-grupos.json
```

## Kit de música

`kit-musica/` leva o que este projeto sabe sobre o Suno para os projetos de música do Kit de Contexto Modular: um bloco para as Instruções e o CEREBRO do projeto, e duas skills — `macetes-suno` (o que tem efeito) e `revisar-faixa` (conta letra, tags, rótulos e BPM antes de entregar). Instruções de uso em `kit-musica/README.md`.

````

### E10 — CONTEXT: estrutura (1) — `meta/CONTEXT.md`

**Ancora, literal:**

````
│   ├── convert_br.py          # guias BR antigos -> colecao no esquema (DEC-026)
│   └── test_convert_br.py     # teste do conversor, com guia sintetico
├── data/                      # o acervo real, no esquema
````

**Texto novo, literal:**

````
│   ├── convert_br.py          # guias BR antigos -> colecao no esquema (DEC-026)
│   ├── test_convert_br.py     # teste do conversor, com guia sintetico
│   ├── convert_guides.py      # guias de Albuns/ (formatos mistos) -> colecao, com mapa de grupos
│   └── test_convert_guides.py # teste, com guias sinteticos
├── kit-musica/                # o que o projeto sabe do Suno, para projetos de musica (DEC-027)
│   ├── README.md              # as tres pecas e o mapa para o nicho Musica do KCM
│   ├── BLOCO-SUNO.md          # linhas para as Instrucoes e secao para o CEREBRO do projeto
│   └── skills/                # macetes-suno, revisar-faixa
├── data/                      # o acervo real, no esquema
````

### E11 — analise da conversao: desfecho de Albuns (1) — `meta/analises/261029-ANALISE-conversao-dos-albuns.md`

**Ancora, literal:**

````
**O que fica:** `Albuns/` (oito arquivos, 172 faixas) espera a aprovação dos grupos (i-038); o índice-mestre segue
para o ⬜ «importar prompts prontos como módulos».
````

**Texto novo, literal:**

````
**O que fica:** `Albuns/` (oito arquivos, 172 faixas) espera a aprovação dos grupos (i-038); o índice-mestre segue
para o ⬜ «importar prompts prontos como módulos».

## Desfecho de `Albuns/` — 2026-10-31

Grupos aprovados pelo dono (os 12 da proposta; versões A/B viram variantes). Conversor `scripts/convert_guides.py`
para os formatos mistos, com mapa de grupos fora do repo (`../acervos/albuns-grupos.json`). Medido
`[medido por instrumento]`: **205 de 205** faixas, 12 álbuns, 0 rótulos no copiável, validador completo verde,
205 cartões no app. Gravado em `../acervos/albuns-reagrupados.json`.

**Duas contas erradas da proposta, corrigidas aqui:**
- **172 faixas eram 205.** O VOL5 tem 82, não 49: a listagem de cabeçalhos que contou foi cortada em 60 linhas
  e perdeu 14 de código, 2 de matemática e as 19 instrumentais rítmicas (RITM-M, RITM-C, RITM-B). As 19 foram para
  «Contagem e ritmo», pelo critério das RITM do VOL4 (o álbum ficou com 42 faixas).
- **«Rise of the Eternal» não é duplicata:** são duas canções com o mesmo título (ÉPICO: tenor, outra letra;
  guia_suno: soprano; letras 9% parecidas). O dono decidiu «fica uma só» sobre a premissa errada; as duas ficaram,
  e o mapa descarta uma em uma linha (`drop`) se ele quiser. As «Variações para» desse título ficam na do guia_suno.
````

### E12 — analise do kit: status e desfecho (1) — `meta/analises/261029-ANALISE-kit-de-musica.md`

**Ancora, literal:**

````

> **Status:** Em discussão — espera as decisões 1 a 3 do dono (fim deste arquivo).
> **Data:** 2026-10-29 (data de criação; não muda depois)
````

**Texto novo, literal:**

````

> **Status:** Implementada (0.10.0) — decidida pelo dono em 2026-10-29: 1A, 2A, 3A (ver Desfecho).
> **Data:** 2026-10-29 (data de criação; não muda depois)
````

### E13 — analise do kit: status e desfecho (2) — `meta/analises/261029-ANALISE-kit-de-musica.md`

**Ancora, literal:**

````
(um dos grupos da proposta de `Albuns/`) mede se as faixas novas já saem dentro do orçamento.
````

**Texto novo, literal:**

````
(um dos grupos da proposta de `Albuns/`) mede se as faixas novas já saem dentro do orçamento.

## Desfecho — 2026-10-31

**Decidido: 1A, 2A, 3A** (DEC-027). O dono liberou a leitura do KCM; lido `src/niches/music.js` (v1.133.0) e
o i-N25 do IDEAS dele.

**O que a leitura mudou na forma:** o nicho Música do KCM é de música **tocada** (DAW, arranjo, mix, master;
«não ouço áudio») e já tem o i-N25 «Música: criação completa… prompts p/ IAs como Suno — A AVALIAR». As
Instruções que o KCM gera têm teto (~6.900 caracteres). Por isso a primeira peça não é «Instruções-modelo»
inteiras, que competiriam com as do KCM: é um **bloco** — cinco linhas para as Instruções (679 caracteres) e
uma seção para o CEREBRO —, em `kit-musica/BLOCO-SUNO.md`. As skills seguem a ideia: `macetes-suno` e
`revisar-faixa`, em `kit-musica/skills/`.

**Medido:** o script da `revisar-faixa`, rodado nos acervos do dono, acha **72** letras acima de 5.000 e **138**
styles acima de 10 tags na Rainha da Preguiça — o previsto aqui —, e 0 e 143 nos álbuns reagrupados; nenhum
rótulo falso. O `validate.py` reprova se os limites da skill divergirem do app (duas provas negativas).

**Ao KCM:** carta `261031-cancioneiro-para-kcm-01-kit-de-musica-ia.md` (fora do repo), com o mapa das peças para
os campos do nicho e o pedido de pôr o Cancioneiro no livro de leitura dele.
````

### E14 — IDEAS (1) — `meta/IDEAS.md`

**Ancora, literal:**

````

### i-008 💡 Importar acervo existente convertendo por álbum
Converter os `ALBUM_*.md` e `album_guia_suno.md` para o esquema, um álbum por vez (semi-assistido por chat), populando `data/`. Começar pelo `album_guia_suno.md` (mais limpo). Backlog do STATUS.
````

**Texto novo, literal:**

````

### i-008 ✅ Importar acervo existente convertendo por álbum
Converter os `ALBUM_*.md` e `album_guia_suno.md` para o esquema, um álbum por vez (semi-assistido por chat), populando `data/`. Começar pelo `album_guia_suno.md` (mais limpo). Backlog do STATUS.
````

### E15 — IDEAS (2) — `meta/IDEAS.md`

**Ancora, literal:**

````
**Em trabalho (2026-10-29):** sonda e análise `meta/analises/261029-ANALISE-conversao-dos-albuns.md`, decidida 1A a 4A (DEC-026): conversor determinístico por família, acervo fora do repo. A família BR está convertida (0.9.1, `scripts/convert_br.py`, 151 faixas). `Albuns/` espera os grupos da i-038.

````

**Texto novo, literal:**

````
**Em trabalho (2026-10-29):** sonda e análise `meta/analises/261029-ANALISE-conversao-dos-albuns.md`, decidida 1A a 4A (DEC-026): conversor determinístico por família, acervo fora do repo. A família BR está convertida (0.9.1, `scripts/convert_br.py`, 151 faixas). `Albuns/` espera os grupos da i-038.
**Entregue (0.10.0, 2026-10-31):** os 19 guias convertidos — BR (151 faixas) e `Albuns/` (205 faixas, `scripts/convert_guides.py`), os dois acervos fora do repo.

````

### E16 — IDEAS (3) — `meta/IDEAS.md`

**Ancora, literal:**

````

### i-022 💡 Skill que ensina a gerar o JSON do Cancioneiro
`[relatado pelo dono, 2026-08-22]` Uma skill do projeto que ensine um chat a produzir o JSON canonico seguindo o esquema a risca — estrutura, campos obrigatorios, a regra de dominio (rotulo fora do bloco copiavel). Hoje isso vive no `schema/PROMPT-PARA-CHATS.md`, que e um texto colavel: a skill seria a versao que o proprio Claude Code carrega. **Sobreposicao a resolver antes de construir:** i-002 (o prompt-modelo) ja cobre parte disto; decidir se a skill substitui o prompt-modelo ou se os dois convivem em canais diferentes (chat colavel × skill do repo).

### i-023 💡 Skill com os macetes do Suno
`[relatado pelo dono, 2026-08-22]` Uma skill que consolide o que o projeto sabe sobre gerar musica com IA: como estruturar cada parte, onde cada coisa entra, possibilidades e exemplos. **O material ja existe** — e o `meta/HISTORY.md` §1-13, com nivel de confianca e fontes. A ideia e a FORMA, nao o conteudo: transformar conhecimento lido sob demanda em skill lida antes de trabalhar. Pesar contra o custo: skill e lida sempre, HISTORY so quando preciso.

````

**Texto novo, literal:**

````

### i-022 ✅ Skill que ensina a gerar o JSON do Cancioneiro
`[relatado pelo dono, 2026-08-22]` Uma skill do projeto que ensine um chat a produzir o JSON canonico seguindo o esquema a risca — estrutura, campos obrigatorios, a regra de dominio (rotulo fora do bloco copiavel). Hoje isso vive no `schema/PROMPT-PARA-CHATS.md`, que e um texto colavel: a skill seria a versao que o proprio Claude Code carrega. **Sobreposicao a resolver antes de construir:** i-002 (o prompt-modelo) ja cobre parte disto; decidir se a skill substitui o prompt-modelo ou se os dois convivem em canais diferentes (chat colavel × skill do repo).
**Resolvida em 2026-10-31 (i-039, DEC-027):** sem skill nova — o contrato fica no prompt-modelo, fonte única; o kit de música o leva ao projeto junto das skills.

### i-023 ✅ Skill com os macetes do Suno
`[relatado pelo dono, 2026-08-22]` Uma skill que consolide o que o projeto sabe sobre gerar musica com IA: como estruturar cada parte, onde cada coisa entra, possibilidades e exemplos. **O material ja existe** — e o `meta/HISTORY.md` §1-13, com nivel de confianca e fontes. A ideia e a FORMA, nao o conteudo: transformar conhecimento lido sob demanda em skill lida antes de trabalhar. Pesar contra o custo: skill e lida sempre, HISTORY so quando preciso.
**Entregue em 0.10.0 (2026-10-31):** `kit-musica/skills/macetes-suno/SKILL.md` — lida sob demanda, ao escrever style ou letra.

````

### E17 — IDEAS (4) — `meta/IDEAS.md`

**Ancora, literal:**

````

### i-038 💡 Reagrupar as faixas de `Albuns/` em álbuns por cena de uso
`[relatado pelo dono, 2026-10-29]` Os oito guias de `Albuns/` misturam gêneros, idiomas e propósitos num arquivo só. O dono quer as faixas em álbuns mais relacionados, para depois ampliar cada um num projeto próprio. Proposta do chat em `../261029-PROPOSTA-grupos-albuns.md` (fora do repo: traz os títulos): 172 faixas em 12 álbuns (épico vocal, trilhas de jogo, romântico multilíngue, Brasil popular, pop asiático, latino, contagem e ritmo, matemática e física, código, foco e estudo, eletrônico instrumental, treino e ação). Um mapa faixa → álbum aplica a escolha por script. Espera a aprovação do dono; depois, conversores dos formatos de `Albuns/` (i-008).

### i-039 💡 Kit de música para os projetos do KCM
`[relatado pelo dono, 2026-10-29]` Criar projetos de música para o Suno já «profissionais» e adaptados ao Cancioneiro: levar ao nicho de música do KCM o que este projeto sabe. Junta i-022, i-023 e o feedback ao kit de 2026-10-28. Análise `meta/analises/261029-ANALISE-kit-de-musica.md`, em discussão: Instruções-modelo de projeto de música, skill de macetes do Suno, skill de revisão de faixa. A medida que motiva: nos guias antigos, 72 de 151 letras passam do limite em que o Suno corta.

````

**Texto novo, literal:**

````

### i-038 ✅ Reagrupar as faixas de `Albuns/` em álbuns por cena de uso
`[relatado pelo dono, 2026-10-29]` Os oito guias de `Albuns/` misturam gêneros, idiomas e propósitos num arquivo só. O dono quer as faixas em álbuns mais relacionados, para depois ampliar cada um num projeto próprio. Proposta do chat em `../261029-PROPOSTA-grupos-albuns.md` (fora do repo: traz os títulos): 172 faixas em 12 álbuns (épico vocal, trilhas de jogo, romântico multilíngue, Brasil popular, pop asiático, latino, contagem e ritmo, matemática e física, código, foco e estudo, eletrônico instrumental, treino e ação). Um mapa faixa → álbum aplica a escolha por script. Espera a aprovação do dono; depois, conversores dos formatos de `Albuns/` (i-008).
**Entregue em 0.10.0 (2026-10-31):** grupos aprovados; 205 faixas (não 172 — a contagem da proposta perdeu 33 do VOL5) em 12 álbuns, `../acervos/albuns-reagrupados.json`, mapa em `../acervos/albuns-grupos.json`.

### i-039 🔄 Kit de música para os projetos do KCM
`[relatado pelo dono, 2026-10-29]` Criar projetos de música para o Suno já «profissionais» e adaptados ao Cancioneiro: levar ao nicho de música do KCM o que este projeto sabe. Junta i-022, i-023 e o feedback ao kit de 2026-10-28. Análise `meta/analises/261029-ANALISE-kit-de-musica.md`, em discussão: Instruções-modelo de projeto de música, skill de macetes do Suno, skill de revisão de faixa. A medida que motiva: nos guias antigos, 72 de 151 letras passam do limite em que o Suno corta.
**Em trabalho (0.10.0, 2026-10-31, DEC-027):** as três peças em `kit-musica/` — `BLOCO-SUNO.md` (bloco para Instruções e CEREBRO, não Instruções inteiras: o KCM tem teto), `macetes-suno`, `revisar-faixa`. Carta 01 ao KCM com o mapa para o nicho Música. **Gatilho:** sem resposta do KCM até o primeiro projeto de música novo do dono, o projeto usa o kit à mão (`kit-musica/README.md`, «Como usar hoje») e o que faltar volta como feedback.

````

### E18 — IDEAS (5) — `meta/IDEAS.md`

**Ancora, literal:**

````
- **[2026-10-29] O fecho de turno nao tem lugar para o comando que o dono cola, e o rodape e o pior lugar.** O esqueleto do CEREBRO tem Proximo, Estado, Arquivar/Manter, Config e Handoff; a linha `/apply-wo` ficou sem endereco, e uma regra escrita so num brief a mandou para o fim da mensagem — o dono rolava ate o fundo a cada WO `[relatado pelo dono]`. Sugestao ao kit: o esqueleto trazer um item «Aplicar» (o comando a colar, num bloco de codigo) **antes** do divisor e do Proximo, e dizer que todo comando que o dono copia vai em bloco de codigo, inclusive a resposta que um chat externo devolve (aqui: o JSON do prompt-modelo, DEC-023). Adotado neste projeto na DEC-024.

````

**Texto novo, literal:**

````
- **[2026-10-29] O fecho de turno nao tem lugar para o comando que o dono cola, e o rodape e o pior lugar.** O esqueleto do CEREBRO tem Proximo, Estado, Arquivar/Manter, Config e Handoff; a linha `/apply-wo` ficou sem endereco, e uma regra escrita so num brief a mandou para o fim da mensagem — o dono rolava ate o fundo a cada WO `[relatado pelo dono]`. Sugestao ao kit: o esqueleto trazer um item «Aplicar» (o comando a colar, num bloco de codigo) **antes** do divisor e do Proximo, e dizer que todo comando que o dono copia vai em bloco de codigo, inclusive a resposta que um chat externo devolve (aqui: o JSON do prompt-modelo, DEC-023). Adotado neste projeto na DEC-024.
- **[2026-10-31] O nicho Música é de música tocada; música gerada por IA pede outro eixo.** O `src/niches/music.js` (v1.133.0) fala de DAW, mix e master; num projeto em que a faixa sai do Suno, o artefato é o pedido (style e letra), com limites que cortam em silêncio. Proposta e material em `kit-musica/` (DEC-027), enviados na carta 01 (`261031-cancioneiro-para-kcm-01-kit-de-musica-ia.md`); casa com o i-N25 do KCM. Seção deste feedback para o livro de leitura do KCM: `meta/IDEAS.md`, «Feedback para o Kit».

````

### E19 — ROADMAP (1) — `meta/ROADMAP.md`

**Ancora, literal:**

````
- ✅ Conveniências de uso: estrutura do cartão configurável, copiar título, arrastar o `.json`, acervo guardado no navegador, prompt que entrega arquivo, export de álbum com o Style da tela (DEC-022, DEC-023; i-030, i-033 a i-037) — 0.9.0, conferidas e retestadas pelo dono; ajustes de tela na 0.9.1 (DEC-025), vistos pelo dono.
- 🔄 Converter os álbuns antigos (i-008, DEC-026): a família BR convertida por `scripts/convert_br.py` na 0.9.1 (151 faixas, acervo fora do repo); `Albuns/` espera os grupos (i-038).
**Marco:** conseguir usar a ferramenta de verdade numa rodada de geração no Suno.
````

**Texto novo, literal:**

````
- ✅ Conveniências de uso: estrutura do cartão configurável, copiar título, arrastar o `.json`, acervo guardado no navegador, prompt que entrega arquivo, export de álbum com o Style da tela (DEC-022, DEC-023; i-030, i-033 a i-037) — 0.9.0, conferidas e retestadas pelo dono; ajustes de tela na 0.9.1 (DEC-025), vistos pelo dono.
- ✅ Converter os álbuns antigos (i-008, DEC-026): a família BR na 0.9.1 (151 faixas) e `Albuns/` na 0.10.0 (205 faixas em 12 álbuns por cena de uso, i-038); os acervos ficam fora do repo.
**Marco:** conseguir usar a ferramenta de verdade numa rodada de geração no Suno.
````

### E20 — DEC-027 no fim (1) — `meta/DECISIONS.md`

**Ancora, literal:**

````
**Consequências:** (+) 151 faixas no esquema com um comando, conferíveis contra o original; o painel passa a mostrar o que o Suno cortaria (72 letras). (+) O repo continua sem material pessoal. (−) Cada formato novo de guia pede o seu conversor, ou uma decisão de converter de outro jeito. (−) O acervo convertido não tem histórico no Git: regerar é rodar o conversor de novo.
````

**Texto novo, literal:**

````
**Consequências:** (+) 151 faixas no esquema com um comando, conferíveis contra o original; o painel passa a mostrar o que o Suno cortaria (72 letras). (+) O repo continua sem material pessoal. (−) Cada formato novo de guia pede o seu conversor, ou uma decisão de converter de outro jeito. (−) O acervo convertido não tem histórico no Git: regerar é rodar o conversor de novo.

## DEC-027 — O kit de música mora neste repo e chega ao KCM por carta; a peça das Instruções é um bloco, não Instruções inteiras

**Data:** 2026-10-31
**Status:** aceita
**Contexto:** O dono quer criar projetos de música para o Suno já «profissionais» e adaptados ao Cancioneiro (i-039). Análise `meta/analises/261029-ANALISE-kit-de-musica.md`, decidida 1A, 2A, 3A. Lido o KCM (v1.133.0): o nicho Música (`src/niches/music.js`) é de música tocada, com teto de Instruções de ~6.900 caracteres, e o i-N25 dele prevê «criação completa… prompts para IAs como Suno», a avaliar.
**Decisão:** (1) Três peças em `kit-musica/`: um bloco para as Instruções e o CEREBRO de um projeto de música (`BLOCO-SUNO.md`), a skill `macetes-suno` e a skill `revisar-faixa`. O contrato JSON continua no prompt-modelo, fonte única (fecha a i-022 sem skill nova). (2) A fonte mora aqui: o `validate.py` reprova se os limites da `revisar-faixa` divergirem do `QUALITY_LIMITS` do app. (3) O KCM recebe por carta, com o mapa das peças para os campos do nicho; o Cancioneiro não escreve no KCM. (4) A peça das Instruções é um bloco de cinco linhas, não Instruções inteiras, porque o projeto nasce do KCM e as Instruções dele já ocupam o teto.
**Alternativas consideradas:** Instruções-modelo inteiras (competiriam com as que o KCM gera, e passariam do teto); uma skill só (paga em contexto a cada conversa o que só se consulta às vezes); fonte no KCM (cada limite do Suno que mudar pediria duas WOs em dois repos); só uma carta, sem peças (o conhecimento viveria em dois lugares e o KCM não tem as medidas para conferir).
**Consequências:** (+) Um projeto de música novo já nasce com o orçamento e a revisão; o dono pode usar hoje, colando o bloco. (+) A revisão é a mesma conta do painel do app (72 e 138 na Rainha da Preguiça). (−) Até o KCM absorver, colar o bloco é à mão, a cada projeto. (−) O texto do bloco e das skills não tem checagem automática além dos limites; regra nova do prompt-modelo pede conferência à mão.
````

### E21 — arquivo novo — `scripts/convert_guides.py`

Arquivo novo: crie com este conteudo (crie as pastas que faltarem).

````
#!/usr/bin/env python3
"""Converte os guias de `Albuns/` (formatos mistos) para uma colecao no esquema (i-008, i-038).

Uso:
    python3 scripts/convert_guides.py SAIDA.json GUIA.md [GUIA.md ...] [--groups MAPA.json] [--title "Nome"]

Diferente do `convert_br.py` (uma familia, um molde), este le os oito guias de
`Albuns/`, que usam seis jeitos de marcar o que vai para o Suno. Uma faixa e um
cabecalho `## ` que tem um style; o resto do guia (indice, dicas, enredo) fica de
fora. Cada bloco de codigo e classificado pelo rotulo da primeira linha ou pela
linha em negrito logo antes dele:

    style       `[ESTILO SUNO]`, `[ESTILO SUNO — ORIGINAL]`, `[Estilo Suno]`, ou bloco
                depois de `**Style — Opção A:**`, `**Style Prompt:**`, `Campo "Style of Music"`
    variante    `[ESTILO SUNO — VAR A: rotulo]` (varias num bloco), `**Style — Opção B:**`,
                um segundo `[Estilo Suno]` (VERSAO B do guia completo) e as secoes
                «Variações para: *Titulo*», que viram variantes da faixa daquele titulo
    lyrics      `[LETRA]`, `[ESTRUTURA]`, ou bloco depois de `Lyrics (opcional):`,
                `Letra:`, `LETRA COMPLETA`; no guia completo a letra e Markdown fora
                de bloco (`**[Verse 1]**`) e sai sem os asteriscos
    titulo      `### "Titulo"`, `**Título:**`, bloco depois de `Campo "Title"`, aspas no
                cabecalho, `# Nome` do jogo, ou o proprio cabecalho

A regra de dominio vale igual: o rotulo nunca entra em `style` nem `lyrics`.
Conversao fiel (DEC-026): nada e cortado; o relatorio conta o que passa do limite.

Sem `--groups`, um album por arquivo. Com `--groups`, o mapa (JSON, fora do repo:
traz os titulos do dono) diz quais faixas vao para qual album:
    {"albums": [{"id": "...", "title": "...", "description": "...", "songs": ["v4-br-01", ...]}],
     "drop": {"gs-epica-1": "duplicata de epico-05"}}
Toda faixa convertida precisa estar em um album ou em `drop`; faixa citada que nao
existe tambem e erro. Saida: codigo 0 se tudo bateu; 1 se nao.
"""
import argparse
import json
import re
import sys
import unicodedata

# Prefixo de id por arquivo: o mesmo codigo (ROM-01) existe em dois guias.
PREFIX = {
    "ALBUM_EPICO_GUIA_SUNO": "epico", "ALBUM_VOL4_GUIA_SUNO": "v4", "ALBUM_VOL5_GUIA_SUNO": "v5",
    "ALBUM_VOL6_INSTRUMENTAL_SUNO": "v6", "ALBUM_VOL7_VIOLINO_ELETRONICO_SUNO": "v7",
    "album_guia_completo": "gc", "album_guia_suno": "gs", "guia_musicas_acao_gemini_suno": "ga",
}
# Codigo de faixa no cabecalho: BR-01, MÃE-02, CLK-EN-01, RITM-M-08, R-01, KP-05.
CODE = re.compile(r"(?<![\w-])([A-ZÃÉ]{1,5}(?:-[A-Z]{1,2})?-\d{2})(?![\w-])")
STYLE_LABEL = re.compile(r"^\[(?:ESTILO SUNO|Estilo Suno)\s*(?:—\s*(.*?))?\s*:?\s*(.*?)\]\s*$")
VAR_WORD = re.compile(r"^VAR(?:IAÇÃO)?\b\s*(.*)$", re.I)
LYRICS_LABEL = re.compile(r"^\[(LETRA|ESTRUTURA)\]\s*$")
BPM = re.compile(r"\b(\d{2,3})\s*-?\s*bpm\b", re.I)

# Idioma pelo cabecalho; se nao disser, pela escrita da letra.
LANG_WORDS = [
    # \b no fim: «japonesa» (de «estética japonesa») nao e o idioma da letra
    (r"PT-BR|PORTUGU[ÊE]S\b|🇧🇷", "pt-BR"), (r"INGL[ÊE]S\b|🇺🇸|🇬🇧", "en"), (r"JAPON[ÊE]S\b|🇯🇵", "ja"),
    (r"COREANO\b|🇰🇷", "ko"), (r"CHIN[ÊE]S\b|MANDARIM|🇨🇳", "zh"), (r"ESPANHOL\b|🇪🇸", "es"),
    (r"FRANC[ÊE]S\b|🇫🇷", "fr"), (r"LATIM\b", "la"), (r"TELUGU\b|🇮🇳", "te"),
]
SCRIPTS = [(r"[가-힯]", "ko"), (r"[぀-ヿ]", "ja"), (r"[ఀ-౿]", "te"), (r"[一-鿿]", "zh")]
# Palavras que so uma das linguas usa (o, a, de, que sao das duas e nao contam).
WORDS = {
    "pt-BR": re.compile(r"\b(não|você|eu|mas|muito|até|aqui|sou|é|nós|com|pra|meu|minha)\b", re.I),
    "es": re.compile(r"\b(y|el|los|yo|pero|muy|hasta|aquí|soy|eres|mi|tú|corazón)\b", re.I),
    "en": re.compile(r"\b(the|and|you|my|is|of|I|we|your)\b"),
    "fr": re.compile(r"\b(je|tu|et|les|mon|ma|toujours|avec|nous|c'est)\b", re.I),
}


def slug(text):
    """Minusculas, sem acento, hifens no lugar do resto."""
    ascii_ = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", ascii_.lower()).strip("-")


def clean_md(text):
    """Tira emoji de abertura, asteriscos e espacos sobrando de um cabecalho."""
    text = re.sub(r"^#+\s*", "", text)
    text = re.sub(r"^[^\w\"'(«]+", "", text)  # emoji/simbolos no comeco
    return re.sub(r"\s+", " ", text.replace("*", "")).strip()


def join_style(lines):
    """Style em uma linha: junta as linhas, colapsa espacos, tira a virgula final."""
    text = " ".join(x.strip() for x in lines if x.strip())
    return re.sub(r"\s+", " ", text).strip().rstrip(",").strip()


def trim(lines):
    """Tira linhas em branco das pontas e espacos do fim de cada linha."""
    lines = [x.rstrip() for x in lines]
    while lines and not lines[0].strip():
        lines = lines[1:]
    while lines and not lines[-1].strip():
        lines = lines[:-1]
    return lines


def segments(lines):
    """Divide o guia nos cabecalhos `## ` que estao fora de bloco de codigo.

    Fora de bloco porque letras de codigo trazem `# ` e `## ` como comentario.
    Devolve (cabecalho, itens), onde item e ('text', i, linha) ou ('block', i, linhas).
    """
    out, cur, inside, buf = [], None, False, []
    for i, line in enumerate(lines):
        if line.lstrip().startswith("```"):
            if inside and cur is not None:
                cur[1].append(("block", i, buf))
            buf, inside = [], not inside
            continue
        if inside:
            buf.append(line)
        elif line.startswith("## "):
            cur = (line, [])
            out.append(cur)
        elif cur is not None:
            cur[1].append(("text", i, line))
    return out


def prev_text(items, k):
    """A ultima linha de texto nao vazia antes do item k (o 'rotulo de fora' do bloco)."""
    for kind, _, val in reversed(items[:k]):
        if kind == "text" and val.strip() and val.strip() != "---":
            return val.strip()
        if kind == "block":
            return ""
    return ""


def guess_language(header, lyrics):
    """Idioma: palavra-chave no cabecalho; senao, escrita da letra; instrumental se so tags."""
    words = [x for x in lyrics.split("\n") if x.strip() and not re.fullmatch(r"\s*\[.*\]\s*", x)]
    if not words:
        return "instrumental"
    hits = [(m.start(), code) for pattern, code in LANG_WORDS for m in [re.search(pattern, header, re.I)] if m]
    if hits:
        return min(hits)[1]
    body = "\n".join(words)
    # letra com mais de uma escrita (coreano com trechos em japones): a que mais aparece
    counts = {code: len(re.findall(pattern, body)) for pattern, code in SCRIPTS}
    best = max(counts, key=counts.get)
    if counts[best] > 20:
        return best
    scores = {code: len(rx.findall(body)) for code, rx in WORDS.items()}
    return max(scores, key=scores.get)


def parse_segment(header, items, prefix, ordinal):
    """Um cabecalho `## ` -> dict de faixa, ou None se nao tem style."""
    texts = [val for kind, _, val in items if kind == "text"]
    style, lyrics, variants, title = None, None, [], None
    main_version = ""
    md_lyrics_from = None  # indice do item depois do qual a letra vem em Markdown (guia completo)
    for k, (kind, _, val) in enumerate(items):
        if kind != "block":
            continue
        body = val
        first_i = next((j for j, x in enumerate(body) if x.strip()), None)
        if first_i is None:
            continue
        first = body[first_i].strip()
        before = prev_text(items, k)
        if STYLE_LABEL.match(first):
            # Um bloco pode ter varios rotulos; cada um abre um trecho. O primeiro trecho
            # sem VAR, enquanto nao ha style, e o style principal (o sufixo — ORIGINAL,
            # «ORIGINAL adaptado», «RÉPLICA ...» — e so referencia); o resto vira variante.
            chunks = []
            for x in body:
                mm = STYLE_LABEL.match(x.strip())
                if mm:
                    chunks.append([" ".join(y for y in mm.groups() if y).strip(), []])
                elif chunks:
                    chunks[-1][1].append(x)
            for sfx, chunk in chunks:
                vv = VAR_WORD.match(sfx) if sfx else None
                if style is None and not vv:
                    style = join_style(chunk)
                    md_lyrics_from = k  # guia completo: a letra vem em Markdown depois deste bloco
                    if before.startswith("### "):  # VERSAO A do guia completo
                        main_version = clean_md(before)
                elif sfx:
                    label = ("VAR " + re.sub(r"^([A-Z])\s*:\s*", r"\1 — ", vv.group(1).strip())) if vv else sfx
                    variants.append({"label": re.sub(r"\s+", " ", label).strip(" :—"), "lines": chunk})
                else:  # segundo [Estilo Suno] sem sufixo: VERSAO B do guia completo
                    variants.append({"label": clean_md(before) or "VERSÃO B", "lines": chunk})
            continue
        if LYRICS_LABEL.match(first):
            lyrics = "\n".join(trim(body[first_i + 1:]))
        elif re.search(r"Style\s*—\s*Opção\s*A|Style Prompt|Style of Music", before, re.I) and style is None:
            style = join_style(body)
        elif re.search(r"Style\s*—\s*Opção\s*([B-Z])", before, re.I):
            letter = re.search(r"Opção\s*([B-Z])", before, re.I).group(1).upper()
            variants.append({"label": f"Opção {letter}", "lines": body})
        elif re.search(r"Lyrics|Letra:|LETRA COMPLETA", before, re.I) and lyrics is None:
            lyrics = "\n".join(trim(body))
        elif re.search(r'Campo "Title"', before):
            title = join_style(body)
    if style is None:
        return None

    # Letra em Markdown fora de bloco (guia completo): do bloco da VERSAO A ate o proximo ### ou ---.
    timing = ""
    if lyrics is None and md_lyrics_from is not None:
        buf = []
        for kind, _, val in items[md_lyrics_from + 1:]:
            if kind == "block" or val.startswith("### ") or val.strip() == "---":
                break
            if re.match(r"^\*\(.*\)\*\s*$", val.strip()):  # «*(Usar a mesma letra...)*» e referencia
                continue
            buf.append(val.replace("**", ""))
        buf = trim(buf)
        if buf and buf[0].strip().lower() == "[estrutura]":
            # faixa de treino: roteiro de tempos para quem edita, nao letra para o Suno
            timing = "\n".join(buf[1:]).strip()
            lyrics = "[Instrumental]"
        else:
            lyrics = "\n".join(buf) or None
    if lyrics is None:
        return {"_skip": "sem letra"}

    head = clean_md(header)
    bare = clean_md(re.sub(r"\s*—?\s*\*\(.*?\)\*", "", header))  # sem «*(K-pop, Grupo...)*»
    code_m = CODE.search(header)
    code = code_m.group(1) if code_m else None
    if title is None:
        q = next((re.search(r'"([^"]+)"', x) for x in texts[:4] if x.startswith("### ") and '"' in x), None)
        t = next((x.split(":**", 1)[1].strip() for x in texts if x.startswith("**Título:**")), None)
        game = next((x[2:].strip() for x in texts[:3] if x.startswith("# ")), None)
        bgm = next((clean_md(x).split("—", 1)[-1].strip() for x in texts if x.startswith("### ") and "BGM" in x), None)
        hq = re.search(r'"([^"]+)"', header)
        if q:
            title = q.group(1)
        elif t:
            title = clean_md(t)
        elif game:
            title = clean_md(game) + (f" — {bgm.capitalize()}" if bgm else "")
        elif hq:
            title = hq.group(1)
        else:
            title = bare.split("—", 1)[1].strip() if code and "—" in bare else bare
    title = re.sub(r"\s+", " ", title).strip()

    def field(key):
        prefix_ = f"**{key}:**"
        return next((x.strip()[len(prefix_):].strip() for x in texts if x.strip().startswith(prefix_)), "")

    sid = f"{prefix}-{slug(code)}" if code else f"{prefix}-{ordinal:02d}"
    voice = next((x.split("—", 1)[1].strip() for x in texts[:4] if x.startswith("### ") and '"' in x and "—" in x), "")
    numbers = sorted({int(n) for n in BPM.findall(style)})
    notes = [
        f"Versão principal: {main_version}" if main_version else "",
        f"Voz: {field('Voz') or voice}" if (field("Voz") or voice) else "",
        f"Instrumentos: {field('Instrumentos')}" if field("Instrumentos") else "",
        f"Roteiro de tempos:\n{timing}" if timing else "",
        f"Origem: {head}",
    ]
    return {
        "id": sid,
        "title": title,
        "language": guess_language(header + " " + " ".join(texts[:4]), lyrics),
        "state": "ideia",
        "style": style,
        "lyrics": lyrics,
        "bpm": numbers[0] if len(numbers) == 1 else None,
        "variants": [{"label": v["label"], "style": join_style(v["lines"])} for v in variants if join_style(v["lines"])],
        "context": field("Conceito") or field("Para"),
        "notes": "\n".join(x for x in notes if x),
        "tags": [x for x in [code, prefix] if x],
    }


def extra_variants(header, items):
    """Secao «Variações para: *Titulo*»: (titulo, [variantes]) — cada ### Versão X com o seu bloco."""
    m = re.search(r"Variações para:\s*\*([^*]+)\*", header)
    if not m:
        return None
    out = []
    for k, (kind, _, val) in enumerate(items):
        if kind == "block":
            label = clean_md(prev_text(items, k))
            out.append({"label": label, "style": join_style(val)})
    return m.group(1).strip(), out


def convert_file(path):
    """Um guia -> (faixas, variantes soltas por titulo, avisos)."""
    name = re.sub(r"\.md$", "", path.replace("\\", "/").rsplit("/", 1)[-1])
    prefix = PREFIX.get(name, slug(name)[:6])
    with open(path, encoding="utf-8") as f:
        lines = f.read().replace("\r\n", "\n").split("\n")
    songs, loose, warnings, n = [], [], [], 0
    for header, items in segments(lines):
        ev = extra_variants(header, items)
        if ev:
            loose.append(ev)
            continue
        n += 1
        song = parse_segment(header, items, prefix, n)
        if song is None:
            n -= 1
            continue
        if "_skip" in song:
            warnings.append(f"{name}: {clean_md(header)} — {song['_skip']}, ignorada")
            continue
        songs.append(song)
    return name, songs, loose, warnings


def main(argv=None):
    """Linha de comando: converte, aplica as variantes soltas e o mapa de grupos, grava."""
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("output", help="arquivo .json de saida (fora do repo)")
    ap.add_argument("guides", nargs="+", help="guias .md de Albuns/")
    ap.add_argument("--groups", help="mapa de grupos .json (fora do repo)")
    ap.add_argument("--title", default="Álbuns reagrupados", help="titulo da colecao")
    args = ap.parse_args(argv)

    by_file, loose_all, errors = [], [], 0
    for path in args.guides:
        name, songs, loose, warnings = convert_file(path)
        by_file.append((name, songs))
        loose_all += [(name, title, variants) for title, variants in loose]
        print(f"{name}: {len(songs)} faixas" + (f", {len(loose)} secao(oes) de variantes" if loose else ""))
        for w in warnings:
            print(f"   aviso {w}")
    index = {s["id"]: s for _, songs in by_file for s in songs}
    dup = len(index) != sum(len(s) for _, s in by_file)
    if dup:
        print("ERRO: id repetido entre faixas")
        errors += 1

    # «Variações para: *Titulo*» -> variantes da(s) faixa(s) com esse titulo
    # Prefere a faixa do mesmo guia: «Rise of the Eternal» existe em dois guias e sao
    # duas cancoes diferentes (letra e voz), nao uma duplicata.
    base = lambda x: re.sub(r"\s*\(.*\)\s*$", "", x).strip().lower()
    for name, title, variants in loose_all:
        same = dict(by_file)[name]
        hits = [s for s in same if base(s["title"]) == base(title)]
        hits = hits or [s for s in index.values() if base(s["title"]) == base(title)]
        if not hits:
            print(f"ERRO: variantes para «{title}» sem faixa com esse titulo")
            errors += 1
        for s in hits:
            s["variants"] += variants

    if args.groups:
        with open(args.groups, encoding="utf-8") as f:
            gmap = json.load(f)
        used = {}
        albums = []
        for g in gmap["albums"]:
            songs = []
            for sid in g["songs"]:
                if sid not in index:
                    print(f"ERRO: o mapa cita '{sid}', que nao existe")
                    errors += 1
                elif sid in used:
                    print(f"ERRO: '{sid}' esta em '{used[sid]}' e em '{g['id']}'")
                    errors += 1
                else:
                    used[sid] = g["id"]
                    songs.append(index[sid])
            albums.append({"id": g["id"], "title": g["title"], "description": g.get("description", ""), "songs": songs})
        drop = gmap.get("drop", {})
        for sid in drop:
            if sid not in index:
                print(f"ERRO: o mapa descarta '{sid}', que nao existe")
                errors += 1
        loose_ids = [sid for sid in index if sid not in used and sid not in drop]
        if loose_ids:
            print(f"ERRO: {len(loose_ids)} faixa(s) fora de qualquer album: {', '.join(loose_ids[:10])}")
            errors += 1
    else:
        albums = [{"id": slug(name), "title": name, "description": "", "songs": songs} for name, songs in by_file]

    collection = {"schemaVersion": "1.0", "title": args.title,
                  "description": "Convertido dos guias de Albuns/ por scripts/convert_guides.py (i-008, i-038).",
                  "targetTool": "suno", "albums": albums}
    with open(args.output, "w", encoding="utf-8", newline="\n") as f:
        json.dump(collection, f, ensure_ascii=False, indent=1)
        f.write("\n")
    songs = [s for a in albums for s in a["songs"]]
    print(f"\n{len(albums)} album(ns), {len(songs)} faixa(s) -> {args.output}")
    print(f"   letras acima de 5000 caracteres: {sum(len(s['lyrics']) > 5000 for s in songs)} de {len(songs)}")
    print(f"   styles com mais de 10 tags: {sum(len([t for t in s['style'].split(',') if t.strip()]) > 10 for s in songs)} de {len(songs)}")
    if errors:
        print(f"FALHOU: {errors} erro(s).")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
````

### E22 — arquivo novo — `scripts/test_convert_guides.py`

Arquivo novo: crie com este conteudo (crie as pastas que faltarem).

````
#!/usr/bin/env python3
"""Testa scripts/convert_guides.py com guias sinteticos (sem letra real no repo).

Uso:
    python3 scripts/test_convert_guides.py

So biblioteca padrao. Um caso por jeito de marcar o que vai para o Suno, mais os
de «nao deve» (CEREBRO, FIX-003): comentario `# ` dentro da letra nao abre faixa,
secao sem style nao vira faixa, e o mapa de grupos reprova faixa perdida.
"""
import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.dont_write_bytecode = True  # nao deixa scripts/__pycache__ na arvore do repo
import convert_guides  # noqa: E402

F = "```"

# Rotulado (VOL4/VOL5): codigo no cabecalho, VAR num bloco, ORIGINAL com sufixo.
LABELED = f"""# 🎵 ÁLBUM HOBBY — VOLUME 4

## ⚙️ COMO USAR

Dicas sem bloco de faixa.

## 🤠 BR-01 — SERTANEJO TESTE
### "Faixa Rotulada" — Dupla de teste

**Conceito:** cena de teste
**Voz:** dupla

{F}
[ESTILO SUNO — ORIGINAL adaptado]
sertanejo test, viola,
72 BPM,
{F}

{F}
[LETRA]

[Verse 1]
linha um
# comentario de codigo dentro da letra
## outro comentario
{F}

**🔄 VARIAÇÕES:**
{F}
[ESTILO SUNO — VAR A: mais animado]
festivo test
[ESTILO SUNO — VAR B: orquestral]
orquestra test
{F}

## 🎮 CODE-EN-01 — INGLÊS
### "Second Track"

{F}
[ESTILO SUNO]
synthwave test
{F}

{F}
[ESTRUTURA]
[Intro]
[Outro]
{F}
"""

# Opcao A/B (VOL6/VOL7): titulo entre aspas no cabecalho, Lyrics (opcional).
OPTIONS = f"""# 🎼 ÁLBUM HOBBY — VOLUME 6

## 🎹 CLS-01 — "Chuva Teste" (Piano Solo)

**Style — Opção A:**
{F}
solo piano test, 68 BPM
{F}

**Style — Opção B:**
{F}
solo piano test, hopeful
{F}

**Lyrics (opcional):**
{F}
[Instrumental]
{F}
"""

# Style Prompt + Letra + Titulo (guia_suno), e a secao de variacoes soltas.
PROMPT = f"""# 🎵 ÁLBUM COMPLETO

## 🇬🇧 ROMÂNTICA 5 — Inglês

**Título:** Under Test Sky *(Sob o Céu de Teste)*

**Style Prompt:**
{F}
indie pop test, female vocalist
{F}

**Letra:**

{F}
[Verse 1]
the sky and you and my heart
{F}

## 🔀 Variações para: *Under Test Sky* (Inglês — Romântica 5)

### Versão A — Soul
{F}
soul test
{F}
"""

# Estilo Suno + letra em Markdown fora de bloco + VERSAO B + roteiro de treino (guia_completo).
MARKDOWN = f"""# 🎵 ÁLBUM HOBBY — GUIA COMPLETO

## 🇰🇷 R-01 — Canção Teste — *Tradução Teste*

### VERSÃO A — Balada, Voz Masculina
{F}
[Estilo Suno]
k-ballad test, 68 BPM
{F}

**[Verse 1]**
linha de teste

*(Usar a mesma letra da Versão A)*

---

### VERSÃO B — Balada, Voz Feminina
{F}
[Estilo Suno]
k-ballad test, soprano
{F}

---

## TR-01 — PRIME TEST *(Instrumental — Sem Vocal)*

{F}
[Estilo Suno]
instrumental only test, 150 BPM
{F}

**[Estrutura]**
- **[0:00–0:30]** — Build up de teste
"""


class ConvertGuides(unittest.TestCase):
    """Casos do conversor dos guias de Albuns/."""

    def setUp(self):
        self.dir = tempfile.mkdtemp()

    def write(self, name, text):
        path = os.path.join(self.dir, name)
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        return path

    def run_main(self, *args):
        out = os.path.join(self.dir, "out.json")
        code = convert_guides.main([out, *args])
        with open(out, encoding="utf-8") as f:
            coll = json.load(f)
        return code, {s["id"]: s for a in coll["albums"] for s in a["songs"]}, coll

    def test_labeled(self):
        code, songs, _ = self.run_main(self.write("ALBUM_VOL4_GUIA_SUNO.md", LABELED))
        self.assertEqual(code, 0)
        self.assertEqual(sorted(songs), ["v4-br-01", "v4-code-en-01"])  # «COMO USAR» nao e faixa
        s = songs["v4-br-01"]
        self.assertEqual((s["title"], s["style"], s["bpm"], s["language"]), ("Faixa Rotulada", "sertanejo test, viola, 72 BPM", 72, "pt-BR"))
        self.assertIn("# comentario de codigo", s["lyrics"])  # comentario na letra nao abriu faixa
        self.assertEqual([v["label"] for v in s["variants"]], ["VAR A — mais animado", "VAR B — orquestral"])
        self.assertEqual(s["context"], "cena de teste")
        self.assertEqual(songs["v4-code-en-01"]["language"], "instrumental")  # [ESTRUTURA] so com tags

    def test_options(self):
        _, songs, _ = self.run_main(self.write("ALBUM_VOL6_INSTRUMENTAL_SUNO.md", OPTIONS))
        s = songs["v6-cls-01"]
        self.assertEqual((s["title"], s["style"], s["lyrics"]), ("Chuva Teste", "solo piano test, 68 BPM", "[Instrumental]"))
        self.assertEqual(s["variants"], [{"label": "Opção B", "style": "solo piano test, hopeful"}])

    def test_prompt_and_loose_variants(self):
        code, songs, _ = self.run_main(self.write("album_guia_suno.md", PROMPT))
        self.assertEqual(code, 0)
        s = songs["gs-01"]
        self.assertEqual((s["title"], s["style"], s["language"]), ("Under Test Sky (Sob o Céu de Teste)", "indie pop test, female vocalist", "en"))
        self.assertEqual(s["variants"], [{"label": "Versão A — Soul", "style": "soul test"}])

    def test_markdown_lyrics_and_version_b(self):
        _, songs, _ = self.run_main(self.write("album_guia_completo.md", MARKDOWN))
        s = songs["gc-r-01"]
        self.assertEqual(s["title"], "Canção Teste — Tradução Teste")  # a traducao fica; o descritor *(...)* sai (ver PRIME TEST)
        self.assertEqual(s["lyrics"], "[Verse 1]\nlinha de teste")  # sem ** e sem a nota *(...)*
        self.assertEqual([v["label"] for v in s["variants"]], ["VERSÃO B — Balada, Voz Feminina"])
        self.assertIn("Versão principal: VERSÃO A — Balada, Voz Masculina", s["notes"])

    def test_training_timing_goes_to_notes(self):
        """Nao deve: o roteiro de tempos («0:00–0:30») nao vai para o Lyrics."""
        _, songs, _ = self.run_main(self.write("album_guia_completo.md", MARKDOWN))
        s = songs["gc-tr-01"]
        self.assertEqual((s["title"], s["lyrics"]), ("PRIME TEST", "[Instrumental]"))
        self.assertIn("[0:00–0:30] — Build up de teste", s["notes"])

    def test_label_never_inside_copyable(self):
        """Regra de dominio: nenhum rotulo em style, lyrics ou variante."""
        paths = [self.write(n, t) for n, t in [("ALBUM_VOL4_GUIA_SUNO.md", LABELED), ("ALBUM_VOL6_INSTRUMENTAL_SUNO.md", OPTIONS),
                                              ("album_guia_suno.md", PROMPT), ("album_guia_completo.md", MARKDOWN)]]
        _, songs, _ = self.run_main(*paths)
        for s in songs.values():
            for text in [s["style"], s["lyrics"]] + [v["style"] for v in s["variants"]]:
                for label in ("ESTILO SUNO", "Estilo Suno", "[LETRA]", "[ESTRUTURA]", "**"):
                    self.assertNotIn(label, text, s["id"])

    def test_groups(self):
        guide = self.write("ALBUM_VOL4_GUIA_SUNO.md", LABELED)
        gmap = self.write("g.json", json.dumps({"albums": [{"id": "a", "title": "A", "songs": ["v4-code-en-01", "v4-br-01"]}]}))
        code, _, coll = self.run_main(guide, "--groups", gmap)
        self.assertEqual(code, 0)
        self.assertEqual([s["id"] for s in coll["albums"][0]["songs"]], ["v4-code-en-01", "v4-br-01"])  # ordem do mapa

    def test_groups_reject_lost_and_unknown(self):
        """Nao deve: faixa fora de todo album, ou id que nao existe, passar calado."""
        guide = self.write("ALBUM_VOL4_GUIA_SUNO.md", LABELED)
        lost = self.write("g1.json", json.dumps({"albums": [{"id": "a", "title": "A", "songs": ["v4-br-01"]}]}))
        self.assertEqual(self.run_main(guide, "--groups", lost)[0], 1)
        ghost = self.write("g2.json", json.dumps({"albums": [{"id": "a", "title": "A", "songs": ["v4-br-01", "v4-code-en-01", "x-99"]}]}))
        self.assertEqual(self.run_main(guide, "--groups", ghost)[0], 1)
        dropped = self.write("g3.json", json.dumps({"albums": [{"id": "a", "title": "A", "songs": ["v4-br-01"]}],
                                                    "drop": {"v4-code-en-01": "teste"}}))
        self.assertEqual(self.run_main(guide, "--groups", dropped)[0], 0)


if __name__ == "__main__":
    unittest.main()
````

### E23 — arquivo novo — `kit-musica/README.md`

Arquivo novo: crie com este conteudo (crie as pastas que faltarem).

````
# Kit de música — o que o Cancioneiro sabe sobre o Suno, para projetos de música

> **Fonte única aqui** (DEC-027): os números e as regras vêm do app, do `meta/HISTORY.md` e das decisões
> deste repo; o `scripts/validate.py` reprova se os limites da skill `revisar-faixa` divergirem do painel
> de qualidade do app. O KCM (Kit de Contexto Modular) copia daqui — não o contrário.

## Para que serve

Os projetos de música que o dono monta com o KCM nascem do nicho **Música**, feito para música tocada:
DAW, arranjo, mix e master. Quando a faixa é **gerada pelo Suno**, o artefato muda — o que se escreve é o
pedido (style e letra) — e entram regras que o nicho não traz: limites que cortam em silêncio, orçamento de
tags, rótulo fora do copiável, o JSON que o Cancioneiro lê. Medido nos guias antigos do dono, escritos sem
essas regras: 72 de 151 letras acima do limite, 138 de 151 styles com tags demais.

## As três peças

| Peça | O que é | Quando é lida |
|---|---|---|
| `BLOCO-SUNO.md` | Parte 1: cinco linhas para as Instruções do projeto (679 caracteres). Parte 2: seção para o CEREBRO do projeto | sempre (Parte 1); sob demanda (Parte 2) |
| `skills/macetes-suno/SKILL.md` | o que tem efeito no Suno e o que é mito, com exemplo bom e ruim | ao escrever ou reescrever style e letra |
| `skills/revisar-faixa/SKILL.md` | oito conferências por faixa, com script que conta (não estima) | antes de entregar faixa ou álbum |

O contrato do JSON não é peça nova: é o prompt-modelo (`schema/PROMPT-PARA-CHATS.md`, ou o botão «Prompt»
do app), que o projeto recebe junto.

## Como usar hoje, sem esperar o KCM

1. Crie o projeto de música pelo KCM, nicho Música.
2. Cole a Parte 1 do `BLOCO-SUNO.md` no fim das Instruções do projeto (meça: o KCM tem teto) e a Parte 2 no
   `meta/CEREBRO.md` dele.
3. Suba ao projeto as duas skills e o prompt-modelo.
4. Peça faixas; o chat entrega o `.json`; arraste para o Cancioneiro.

## Como o KCM pode absorver (mapa para o molde do nicho)

O nicho Música do KCM é um módulo (`src/niches/music.js`) com `behaviors`, `conventions`, `contextFiles`,
`skillsPack`, `promptsExtra` e `outputs`. Proposta de encaixe, sem mexer no que o nicho já faz para música
tocada:

| Peça do kit | Campo do nicho no KCM |
|---|---|
| eixo «música tocada × gerada por IA» | um seletor no `topbar` (hoje há «DAW / ferramenta»), que liga o resto |
| Parte 1 do bloco | `behaviors` (curto nas Instruções, inteiro no CEREBRO) e `conventions` |
| Parte 2 do bloco | seção do CEREBRO gerado |
| `macetes-suno`, `revisar-faixa` | `skillsPack.skills` (o formato dele: `name`, `gatilho`, `description`, `body`) |
| pedido de faixa no JSON | `promptsExtra` («Gerar faixa para o Suno») e `outputs` (o `.json`) |
| catálogo | `FAIXAS.md` segue com estado e o que falta; o JSON é o copiável |

O behavior `sound_honest` do nicho («não ouço áudio») continua valendo e ganha a forma do Suno: o dono gera,
ouve e relata.

## Manter em sincronia

- Limite do Suno mudou → muda o `QUALITY_LIMITS` do app, a skill `revisar-faixa` e o HISTORY na mesma WO; o
  `validate.py` acusa a skill que ficou para trás.
- Regra nova do prompt-modelo → conferir o `BLOCO-SUNO.md` e a `macetes-suno`.
- O que mudar aqui chega ao KCM por carta (correspondência entre projetos, CEREBRO).
````

### E24 — arquivo novo — `kit-musica/BLOCO-SUNO.md`

Arquivo novo: crie com este conteudo (crie as pastas que faltarem).

````
# Bloco Suno — para um projeto de música do KCM que gera faixas no Suno

> Parte do kit de música do Cancioneiro (`kit-musica/`). O projeto nasce do nicho **Música** do KCM
> (PROJETO, FAIXAS, LETRAS, ARRANJO); este bloco acrescenta o que muda quando a faixa é **gerada por IA**
> e não tocada: o pedido ao Suno vira o artefato, e o Cancioneiro organiza e copia.
>
> **Como usar:** cole a **Parte 1** no fim das Instruções do projeto (cabe no teto do KCM: medir antes e
> depois) e a **Parte 2** no `meta/CEREBRO.md` do projeto. Suba ao projeto as duas skills de
> `kit-musica/skills/` e o prompt-modelo (`schema/PROMPT-PARA-CHATS.md`, ou o botão «Prompt» do app).

---

## Parte 1 — para as Instruções do projeto

```
## Suno (faixa gerada por IA)
- Toda faixa sai no JSON do Cancioneiro (prompt-modelo no projeto): arquivo .json; sem arquivo, um bloco de código.
- Copiável × referência: `style`/`lyrics` só com o que se cola no Suno; título, idioma, nota e rótulo vão nos campos de referência. Nunca «[ESTILO SUNO]» ou «LETRA» dentro do texto.
- Style: 6 a 8 tags, gênero primeiro; até 10 com módulos. Letra até ~3.000 caracteres (acima de 5.000 o Suno corta em silêncio). Um BPM por faixa.
- Antes de entregar faixa ou álbum, rode a skill `revisar-faixa`; ao escrever style ou letra, consulte `macetes-suno`.
- Não ouço o áudio: o dono gera, ouve e diz o que saiu; eu não digo que «ficou bom».
```

---

## Parte 2 — para o `meta/CEREBRO.md` do projeto

```
## Produção com IA de música (Suno)

**O artefato é o pedido.** Num projeto em que a faixa é gerada pelo Suno, o que se escreve não é a gravação,
é o pedido: o `style` (mundo sonoro) e a `lyrics` (arquitetura no tempo). O trabalho do assistente é escrever
esse pedido bem e explicar o porquê de cada escolha; o do dono é gerar, ouvir e decidir.

**Onde cada coisa mora.** O JSON do Cancioneiro (formato no prompt-modelo) é o catálogo copiável: uma coleção,
álbuns, faixas, módulos de estilo. O `FAIXAS.md` do projeto continua com o estado de cada faixa e o que falta;
o `LETRAS.md` guarda a letra em construção e a prosódia; a versão que vai ao Suno é a do JSON. Quando os dois
divergirem, o JSON é o que foi entregue; o `.md` registra por quê mudou.

**Orçamento, porque o Suno corta em silêncio.** Style com 6 a 8 tags (até 10 com módulos ligados), gênero nas
primeiras palavras; letra até ~3.000 caracteres, nunca acima de 5.000; um BPM por faixa, no style e no campo
`bpm`; instrumental em loop com `[Instrumental]` sozinho no Lyrics; tirar algo é `excludeStyles`, não «no X».
Os números são os do painel de qualidade do Cancioneiro, que os mantém com fonte e data.

**Revisão antes de entregar.** A skill `revisar-faixa` conta letra, tags, rótulos e BPM — com código quando a
conversa tiver execução, nunca de cabeça. Vermelho (o Suno corta) se resolve antes de entregar, com proposta
concreta de corte; cortar letra é decisão do dono.

**Ciclo de uma faixa.** Conceito (PROJETO) → letra com prosódia (LETRAS) → pedido ao Suno (JSON, revisado) →
o dono gera e relata o que ouviu → ajuste do pedido (variante ou módulo, sem reescrever a faixa) → estado em
FAIXAS. Relato do dono é a única medida de som; registre-o com a data e a versão do Suno.

**A interface do Suno muda.** Limites e campos vêm de fonte secundária (o Suno não publica os do v6).
Se o dono disser que um campo não existe na conta dele (o Exclude não aparece no v6-mini gratuito), acredite
e adapte.
```

---

## De onde vem cada regra

| Regra | Fonte no Cancioneiro |
|---|---|
| Dois campos, rótulo fora do copiável | `meta/HISTORY.md` §1; DEC-005 |
| Cinco camadas, começo pesa mais | HISTORY §4, §10; prompt-modelo |
| 6 a 8 tags, até 10 com módulos | HISTORY §10; DEC-018; DEC-021 |
| Letra ~3.000 / 5.000 | HISTORY §9; `QUALITY_LIMITS` no app |
| Um BPM por faixa | DEC-020 |
| `[Instrumental]` sozinho; arco só em faixa linear | HISTORY §2, §3 |
| Exclude, não «no X»; v6-mini sem Exclude | HISTORY §5, §11 |
| JSON canônico, módulos na coleção | DEC-016; DEC-021; DEC-023 |
````

### E25 — arquivo novo — `kit-musica/skills/macetes-suno/SKILL.md`

Arquivo novo: crie com este conteudo (crie as pastas que faltarem).

````
---
name: macetes-suno
description: O que tem efeito no Suno e o que é mito — os dois campos, o style em camadas, o orçamento de tags, os limites que cortam em silêncio, BPM, instrumental e exclusão. USE ao escrever ou reescrever o style ou a letra de uma faixa para o Suno, ao montar variantes, e quando o dono perguntar «por que saiu assim?» ou «como faço o Suno fazer X?». Para conferir uma faixa pronta, use a skill revisar-faixa.
---

# Macetes do Suno — o que tem efeito

> Parte do kit de música do Cancioneiro (`kit-musica/`). Fonte: `meta/HISTORY.md` do Cancioneiro, que
> traz cada item com data, fonte e nível de confiança. **Conferido em 2026-10, Suno v6.** A interface
> do Suno muda: se o dono disser que um botão ou campo não existe na conta dele, acredite nele.

## 1. Dois campos, dois trabalhos

- **Style of Music** = o mundo sonoro: gênero, instrumentos, voz, clima, produção, andamento. Texto
  separado por vírgulas, **sem colchetes**.
- **Lyrics** = a arquitetura no tempo: seções e voz. **Colchetes moram aqui** (`[Verse]`, `[Chorus]`).

Ruim: `[ESTILO SUNO] k-pop, synth` no Style. O rótulo é texto que o Suno lê como pedido.
Bom: `k-pop girl crush, punchy synth bass, …` — só o que se cola.

**Regra que não se dobra:** rótulo de referência (título, «ESTILO SUNO», «LETRA», «VAR A», idioma, nota)
nunca entra no texto que vai para o Suno. No JSON do Cancioneiro isso já é estrutural: `style` e `lyrics`
de um lado; `title`, `context` e `notes` do outro.

## 2. O style em cinco camadas audíveis

1. **Gênero** — uma família e um sabor (`dark ambient cinematic`). No máximo dois gêneros.
2. **Movimento** — como pulsa (`driving rhythm`, `half-time pulse`, `sparse`).
3. **Instrumentos** — de 2 a 4, com frase específica (`delicate piano arpeggios` > `piano`).
4. **Voz** — quem conduz (`close-mic alto`, `male duo tenor and baritone`, `no vocals`).
5. **Produção e clima** — o espaço da mixagem e uma ou duas palavras de clima.

Descreva o que dá para **ouvir**. «Épico», «lindo», «profissional» não mudam nada.
**O começo pesa mais:** as primeiras ~20 a 30 palavras mandam. Gênero primeiro; detalhe depois.

## 3. Orçamento de tags

Cada trecho entre vírgulas é uma tag. **De 6 a 8 tags**; abaixo de 4 fica vago; **acima de ~10 as
últimas perdem efeito** e os sinais se anulam em resultado genérico.

Ruim: `warm, analog, synth, pads, dreamy, soft, lush, airy, nostalgic, retro, 80s, chill` (12 adjetivos
soltos).
Bom: `warm analog synth pads, dreamy 80s nostalgia, airy close vocal` (3 tags que dizem mais).

Precisa cortar? Em geral: gênero > clima > instrumento principal > voz > BPM. **Exceção:** em gênero
centrado na voz (rap, rap-pop) a voz é o gênero — não corte a voz primeiro.

## 4. Limites — o Suno corta em silêncio

| Campo | Limite | Na prática |
|---|---|---|
| Style | ~1.000 caracteres | sobra muito: o problema é o número de tags, não o tamanho |
| Lyrics | 5.000 caracteres | **a partir de ~3.000 o Suno corre**: pula seções, encurta |
| Título | 100 caracteres | — |

Passou do limite, o excedente **não chega** — sem erro, sem aviso. A letra longa é o defeito mais comum:
refrão repetido por extenso quatro vezes come mil caracteres. Escreva o refrão completo uma ou duas vezes
e marque as repetições com a tag (`[Chorus]`).

## 5. BPM é aproximação

- `NN bpm` no style ajuda a mirar o andamento; o Suno **não obedece com precisão**.
- **Um número por faixa.** Dois números («95 BPM to 118 BPM») viram ruído para o Suno e confusão para o
  controle de BPM do Cancioneiro. Para acelerar, descreva (`gradual build, accelerating`), não some números.
- O campo `bpm` do JSON repete o número do style.

## 6. Instrumental

- **Faixa em loop** (exploração, estudo): Lyrics só com `[Instrumental]`, nada mais; no style, `no
  vocals` como reforço. Sem isso, o Suno tende a cantarolar depois de ~15 a 20 segundos.
- **Faixa com arco** (abertura, final, trailer): tags de arco no Lyrics — `[Intro]`, `[Build]`,
  `[Climax]`, `[Outro]`, com descrição curta (`[Build: percussão entra]`). Vocabulário **neutro de
  gênero**: `[Drop]` é de EDM, não de orquestra.
- Roteiro de tempos («0:00–0:30 build») é nota para quem edita, não texto do Lyrics.

## 7. Tirar algo: Exclude, não «no X»

`no drums` dentro do style funciona mal; o campo **Exclude** funciona melhor. No JSON, vai em
`excludeStyles`. **O v6-mini (plano gratuito) não mostra o campo Exclude** — ali, uma ou duas negações no
style são o recurso que sobra; mais que isso dilui.

## 8. Mitos que circulam

- «O style caiu para 200 caracteres» — é o limite do v4, copiado para guias novos.
- «O BPM agora é respeitado com precisão» — não está em material oficial.
- «Tag X no fim da lista funciona melhor» — o começo pesa mais, não o fim.
- Números exatos de blog («9 em 10 gerações») são estimativa de quem vende curso.

## 9. O que o assistente não sabe

O assistente **não ouve** o resultado. Ele escreve o pedido e explica o porquê; o dono gera, ouve e diz o
que saiu. «Ficou bom» só quem ouviu pode dizer. Quando o resultado sair estranho, pergunte primeiro: passou
de algum limite? quantas tags? tinha rótulo no texto?
````

### E26 — arquivo novo — `kit-musica/skills/revisar-faixa/SKILL.md`

Arquivo novo: crie com este conteudo (crie as pastas que faltarem).

````
---
name: revisar-faixa
description: Revisão de faixa para o Suno antes de entregar — conta caracteres da letra e tags do style, procura rótulo dentro do que se copia, «no X» no style e dois BPM. USE SEMPRE antes de entregar uma faixa ou um álbum no JSON do Cancioneiro, e quando o dono colar um JSON e pedir «revisa», «confere», «está pronto para o Suno?». Não corta nada sozinha: aponta, e o corte é decisão do dono.
---

# Revisar faixa — o painel de qualidade antes do app

> Parte do kit de música do Cancioneiro (`kit-musica/`). Os números abaixo são os do painel de qualidade
> do app (`QUALITY_LIMITS` em `app/index.html`); o `scripts/validate.py` reprova se divergirem.

O Suno **corta em silêncio**: o que passa do limite do campo não chega ao modelo, sem aviso. E o que fica
dentro do limite pode render menos — tags demais se anulam, letra longa faz o Suno correr. Esta skill
mostra isso **antes** de a faixa sair, para o dono decidir o que cortar. Medido nos guias antigos do
dono, escritos sem esta revisão: 72 de 151 letras acima de 5.000 caracteres, 138 de 151 styles acima de
10 tags.

## Quando

- Antes de entregar qualquer faixa ou álbum.
- Quando o dono colar um JSON (ou um `.md` antigo) e perguntar se está pronto.
- Depois de mudar o style ou a letra de uma faixa já revisada.

## O que conferir (por faixa)

| # | Conferência | Vermelho (o Suno corta ou quebra) | Âmbar (funciona pior) |
|---|---|---|---|
| 1 | Caracteres da **letra** (`lyrics`) | acima de 5.000 | acima de 3.000 — o Suno começa a correr |
| 2 | Caracteres do **style** | acima de 1.000 | acima de 850 |
| 3 | **Tags** do style (trechos entre vírgulas) | — | acima de 10 (as últimas perdem efeito) ou abaixo de 4 (vago) |
| 4 | **Rótulo** dentro do copiável: `ESTILO SUNO`, `[LETRA]`, `Style:`, `Letra:` em `style`/`lyrics` | sempre | — |
| 5 | **Colchete** no style | sempre (colchete é do Lyrics) | — |
| 6 | **«no X»** no style | — | vai para `excludeStyles` (se o plano tiver o campo) |
| 7 | **BPM**: dois números no style, ou campo `bpm` diferente do style | — | um BPM por faixa; rampa («95 to 118 BPM») o app não controla |
| 8 | **Instrumental** com `[Instrumental]` e mais coisa no Lyrics, ou letra cantada com «no vocals» no style | — | sinais que brigam |

Variantes (`variants[].style`) passam pelas conferências 2 a 7.

## Como contar (não estime de cabeça)

Contar caracteres e tags «no olho» erra. Rode a conta. Se a conversa tiver execução de código, use o script
abaixo no JSON da coleção. Ele só lê e imprime:

```python
import json, re, sys

LYRICS_MAX, LYRICS_WARN = 5000, 3000   # = QUALITY_LIMITS.lyrics no app
STYLE_MAX, STYLE_WARN = 1000, 850      # = QUALITY_LIMITS.style
TAGS_VAGUE, TAGS_MANY = 4, 10          # = QUALITY_LIMITS.tags (vague, many)
LABEL = re.compile(r"ESTILO SUNO|\[LETRA\]|^\s*(Style|Letra|Lyrics)\s*:", re.I | re.M)
NEG = re.compile(r"(?<![a-z])no\s+[a-z][a-z-]*", re.I)
BPM = re.compile(r"\b(\d{2,3})\s*-?\s*bpm\b", re.I)

def check_style(style, where, out):
    tags = len([t for t in style.split(",") if t.strip()])
    if len(style) > STYLE_MAX: out.append(f"VERMELHO {where}: style com {len(style)} caracteres (limite {STYLE_MAX})")
    elif len(style) > STYLE_WARN: out.append(f"ambar {where}: style com {len(style)} caracteres")
    if tags > TAGS_MANY: out.append(f"ambar {where}: {tags} tags no style (acima de {TAGS_MANY})")
    elif tags < TAGS_VAGUE: out.append(f"ambar {where}: {tags} tags no style (vago)")
    if "[" in style: out.append(f"VERMELHO {where}: colchete no style")
    if NEG.search(style): out.append(f"ambar {where}: negacao no style: {NEG.search(style).group(0)!r}")
    if len(set(BPM.findall(style))) > 1: out.append(f"ambar {where}: {len(set(BPM.findall(style)))} BPM no style")

def review(coll):
    out = []
    for album in coll.get("albums", []):
        for s in album.get("songs", []):
            where = f"{album.get('id')} > {s.get('id')}"
            style, lyrics = s.get("style", ""), s.get("lyrics", "")
            if len(lyrics) > LYRICS_MAX: out.append(f"VERMELHO {where}: letra com {len(lyrics)} caracteres (limite {LYRICS_MAX})")
            elif len(lyrics) > LYRICS_WARN: out.append(f"ambar {where}: letra com {len(lyrics)} caracteres")
            for field, text in (("style", style), ("lyrics", lyrics)):
                if LABEL.search(text): out.append(f"VERMELHO {where}: rotulo dentro de {field}")
            check_style(style, where, out)
            nums = set(BPM.findall(style))
            if s.get("bpm") is not None and nums and str(s["bpm"]) not in nums:
                out.append(f"ambar {where}: campo bpm {s['bpm']}, style diz {', '.join(sorted(nums))}")
            sung = [l for l in lyrics.split("\n") if l.strip() and not re.fullmatch(r"\s*\[.*\]\s*", l)]
            if lyrics.strip().startswith("[Instrumental]") and sung: out.append(f"ambar {where}: [Instrumental] com letra")
            if sung and re.search(r"\bno vocals?\b", style, re.I): out.append(f"ambar {where}: letra cantada com 'no vocals' no style")
            for i, v in enumerate(s.get("variants", []) or []):
                check_style(v.get("style", ""), f"{where} variante {i + 1}", out)
    return out

coll = json.load(open(sys.argv[1], encoding="utf-8"))
problems = review(coll)
print("\n".join(problems) or "Nada a apontar nas oito conferencias.")
print(f"-- {sum(p.startswith('VERMELHO') for p in problems)} vermelho(s), {sum(p.startswith('ambar') for p in problems)} ambar(es)")
```

Sem execução de código: conte a letra por seção e some, e diga que a conta é estimada.

## Como apresentar

1. **Primeiro os vermelhos**, faixa por faixa, com o número medido e o limite. Vermelho é o que o Suno
   vai cortar ou receber quebrado.
2. Depois os âmbares, agrupados por tipo.
3. Para cada vermelho, **uma proposta concreta** — o trecho exato a tirar, ou as tags a juntar —, nunca
   «encurte a letra». Para letra longa: repetição de refrão é o primeiro candidato; ponte e outro falados,
   o segundo.
4. **Não corte sozinho.** Mostre e espere o dono escolher. Cortar letra é decisão de autor.

## O que esta skill não faz

- Não julga se a faixa **soa** bem: o assistente não ouve áudio. O dono gera no Suno e diz o que ouviu.
- Não garante obediência: passar nas oito conferências quer dizer que o Suno **recebe** tudo; o resultado
  continua variando a cada geração.
- Os limites são de fonte secundária (o Suno não publica os do v6); estão no app com fonte e data.
````

### E27 — arquivo novo — `logs/2026-10-31.md`

Arquivo novo: crie com este conteudo (crie as pastas que faltarem).

````
# Log — 2026-10-31 · Cancioneiro

## Conversa 1 — chat: `Albuns/` reagrupado e kit de música (WO 0020)

### Objetivo do dia
Executar as decisões do dono de 2026-10-29: grupos de `Albuns/` aprovados (os 12; versões viram variantes; a duplicata fica uma só) e kit de música 1A, 2A, 3A.

### Feito
- Relatórios da WO 0019 (`d9b401f`) e do `/wrap` (`3405b9b`) conferidos contra o `git log`.
- `scripts/convert_guides.py` e `scripts/test_convert_guides.py` (8 casos, guias sintéticos): os oito guias de `Albuns/`, seis jeitos de marcar o copiável. Com o mapa de grupos: 205 de 205 faixas em 12 álbuns, 0 rótulos no copiável, validador completo verde, 205 cartões no app `[medido por instrumento]`. Acervo e mapa em `../acervos/` (fora do repo).
- KCM lido com acesso concedido pelo dono (só leitura): `src/niches/music.js` e o i-N25 do IDEAS dele.
- `kit-musica/`: `BLOCO-SUNO.md`, skills `macetes-suno` e `revisar-faixa`, README com o mapa para o nicho Música. O script da `revisar-faixa` acha 72 letras acima de 5.000 e 138 styles acima de 10 tags na Rainha da Preguiça.
- `validate.py` confere os limites da skill contra o app; duas provas negativas reprovam.
- Carta 01 ao KCM, fora do repo.
- WO 0020: 0.10.0, DEC-027, análises com desfecho, IDEAS (i-008, i-022, i-023, i-038 entregues; i-039 em trabalho), log, STATUS.

### Decisões
DEC-027 (kit de música: fonte aqui, bloco em vez de Instruções inteiras, carta ao KCM).

### Bugs
Nenhum no app. Dois erros meus na proposta de grupos, achados ao converter: 172 faixas eram 205 (a listagem do VOL5 foi cortada em 60 linhas); «Rise of the Eternal» não era duplicata (duas canções com o mesmo título). As duas ficaram; o dono decide se descarta uma.

### Aprendizados / armadilhas
- Listagem cortada (`head -60`) virou contagem: a proposta e a aprovação do dono ficaram em cima de 172. Conta que vai para decisão sai de contagem completa, nunca de listagem truncada.
- Mesmo título não é mesma canção: comparar letra e voz antes de chamar de duplicata.
- O detector de idioma casou «japonesa» com «JAPONÊS»; palavra-chave pede limite de palavra.
- Na aplicação da WO 0019, o teste do conversor imprime o resultado do unittest no stderr e o do conversor no stdout: `2>&1 | tail` pega a ordem do pipe, não a do programa (relatório do Code).

### Onde parei
WO 0020 entregue; carta 01 na pasta-pai para o dono levar ao KCM.

### Próximos passos
O dono confere os 12 álbuns no app e leva a carta ao KCM; o primeiro projeto de música novo usa o kit.
````

### E28 — STATUS inteiro — `meta/STATUS.md`

Sem ancora: substitua o arquivo inteiro.

````
# STATUS.md — Cancioneiro

> **O agora.** O que funciona, o que está em progresso, o que está quebrado, backlog curto.
> Rolante: item resolvido sai daqui e vai para o CHANGELOG. Médio/longo prazo vive no ROADMAP.

**Versão atual:** 0.10.0 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveniências de uso concluídos e conferidos · os álbuns antigos convertidos (i-008, fora do repo) · kit de música entregue, à espera do KCM (i-039)

---

## Última conversa (2026-10-31, `Albuns/` reagrupado e kit de música, WO 0020)

- **`Albuns/` convertido e reagrupado** (i-038): `scripts/convert_guides.py` com o mapa de grupos, 205 de 205 faixas em 12 álbuns, em `../acervos/albuns-reagrupados.json` (mapa em `../acervos/albuns-grupos.json`). Duas contas da proposta corrigidas: eram 205 faixas, não 172; «Rise of the Eternal» são duas canções, e as duas ficaram.
- **Kit de música** (i-039, DEC-027): `kit-musica/` com o bloco para Instruções e CEREBRO, `macetes-suno` e `revisar-faixa`; o `validate.py` prende os limites da skill aos do app. Carta 01 ao KCM na pasta-pai.
- **Este bloco substitui o anterior, de 2026-10-29, sobre a família BR.** O que ele dizia está no CHANGELOG [0.9.1], na DEC-026 e em `logs/2026-10-29.md` (Conversas 7 e 8). O item da aplicação da WO 0019, que o `/wrap` anexou no fim do arquivo, saiu: está no log (Conversa 8).

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
- **Prompt-modelo** (`schema/PROMPT-PARA-CHATS.md`, DEC-021, DEC-023): contrato de módulo, style com 6 a 8 tags e até 10 com os módulos ligados; pede o JSON como arquivo e, sem arquivo, em bloco de código. Dois retestes em 2026-10-29: 6 de 6 faixas dentro do contrato e do orçamento, nos dois.
- **Botões «Prompt» e «Exemplo»** (0.8.0, DEC-021): buscam o prompt e o `data/demo.json` do repositório no clique; a janela do prompt recebe o «Meu pedido».
- **Conveniências (0.9.0, DEC-022, DEC-023):** «Estrutura» do cartão (ordem e blocos visíveis, no navegador); copiar o título; arrastar o `.json` para importar; o último acervo importado volta ao abrir, com origem, data e «esquecer»; a importação aceita a resposta do chat colada inteira e avisa.
- **Publicado no GitHub Pages** em `https://joaolucas-nds.github.io/cancioneiro/app/index.html` — o push em `main` publica.

## Em progresso

- **Kit de música no KCM (i-039)** — as peças estão em `kit-musica/`; a carta 01 leva o mapa ao nicho Música do KCM. Gatilho: sem resposta até o primeiro projeto de música novo, o projeto usa o kit à mão.

## Quebrado / pendências que travam

- (nada quebrado)

## Pendências do dono

- **Conferir os 12 álbuns no app** — arrastar `../acervos/albuns-reagrupados.json`; dizer se algum grupo, título ou idioma está errado (o idioma das faixas é deduzido do cabeçalho e da escrita da letra).
- **«Rise of the Eternal»:** as duas canções ficaram (ÉPICO, tenor; guia_suno, soprano). Se quiser só uma, é uma linha no mapa de grupos.
- **Levar a carta 01 ao KCM** — `../261031-cancioneiro-para-kcm-01-kit-de-musica-ia.md`, para a pasta-pai do KCM.
- **Instalar o validador de esquema nesta máquina.** Sem `jsonschema` e `referencing`, o `validate.py` só confere sintaxe e diz `ESQUEMA NAO CONFERIDO` na última linha. Uma vez, no CMD: `pip install jsonschema referencing --break-system-packages`. Depois, `python3 scripts/validate.py` deve terminar em `Tudo conforme ao esquema.`

## Backlog curto (próximas ações concretas)

1. **Curadoria no app e mais de um acervo** (i-040, i-041) — análise antes de spec: o app passaria de leitor a editor leve. Com dois acervos grandes no navegador (Rainha da Preguiça e os 12 álbuns), a i-041 ganhou uso real.
2. **Rampa de BPM** (i-042) — três faixas BR reprovam no `validate.py` por mudarem de andamento de propósito.
3. **Pesquisar outras plataformas de música por IA** (i-032) — um turno de pesquisa antes de qualquer mudança de esquema.
4. **Avisar palavra de andamento que contradiz o BPM** (i-029) — pede uma tabela palavra → faixa de BPM, com fonte e data.
5. **Importar prompts prontos dos álbuns como módulos** — o último ⬜ da 3b no ROADMAP; o índice-mestre da BR e os «estilos originais» do VOL5 trazem fórmulas de estilo.

## Notas de estado

- **Repo local do dono:** `C:\Users\alexk\Tools\cancioneiro\cancioneiro` (Windows). O chat lê e grava na pasta vinculada; commit e push são do Code (DEC-010). A pasta-pai guarda relatórios, notas e o acervo do dono, fora do Git; o lido vai para `../notas-arquivadas/`.
- **Canal:** pasta vinculada é o padrão; a cópia achatada (FlatDrop) é reserva (DEC-017).
- **Limites do Suno:** o v6 saiu em 2026-09-09 e a nota oficial não documenta limite de campo; os números do painel vêm de fonte secundária, com fonte e data no `QUALITY_LIMITS` (DEC-018). Outra fonte secundária (2026-08) põe o ideal em 4 a 7 descritores; o prompt usa 6 a 8. Reconferir quando houver documentação oficial. O `meta/HISTORY.md` §5 ganhou a interface do v6 vista na conta (2026-10-29); o resto do arquivo ainda descreve o v5.5.
- **Exclude no v6-mini:** o formulário gratuito não tem o campo (capturas de 2026-10-29). Desde a 0.9.1 (DEC-025) o bloco vem oculto por padrão, com o aviso «no X → Exclude» junto (D3); o dado continua no JSON e no export. Quem usa o campo liga em «Estrutura».
- **Navegador (DEC-004, DEC-022):** guarda as marcas «usei», a estrutura do cartão e a cópia do último acervo importado. A cópia é cache: se o arquivo mudou fora, importe de novo; a linha de origem diz quando a cópia foi feita.
- **Botões «Prompt» e «Exemplo»:** dependem de rede e do Pages. No `file://`, só funcionam se o Pages aceitar o `fetch` de uma página local — não conferido (o dono abriu o `file://` em 2026-10-29, sem relatar o resultado do botão); sem isso, a janela mostra o link para a versão publicada (DEC-021).
- **Estado de sessão** (módulos ligados e BPM escolhido) sobrevive a filtro, busca e «marcar usei»; volta ao acervo ao recarregar a página ou importar de novo (FIX-008, DEC-020).
- **Limite conhecido:** `tryAutoLoad` (carregamento automático pelo Pages) não saneia chaves internas — só a importação por arquivo faz isso. Inócuo enquanto nenhum acervo contaminado for para `data/`.
- **Pendência de contexto — ASU:** o dono perguntou se o «modo ASU» do KCM seria melhor que o modo Code para este projeto; ficou pendente até ele trazer a descrição do ASU `[relatado pelo dono, sem material de apoio]`.
- Design: na recomposição do Style a base manda — desligar um módulo não remove o que já está no style base; módulos só somam. O dedup compara sequências de palavras (FIX-003). Os módulos de gênero e de andamento costumam custar 0 tag por isso (DEC-019). O chip de andamento é atalho do controle de BPM, no máximo um ligado (DEC-020).
````

## Fora de escopo

- **Os acervos** (`../acervos/*.json`) e a **carta ao KCM** (`../261031-cancioneiro-para-kcm-01-kit-de-musica-ia.md`) —
  fora do repo por decisao (DEC-026, e correspondencia e transitoria). Nao copie para dentro.
- **O KCM** — o Cancioneiro nao escreve la (DEC-027).
- **App alem da versao** — nada muda no comportamento.

## Armadilhas desta WO

- **Aplique uma vez, edicao por edicao.** Se o seu aplicador por script parar a meio, corrija e retome: a
  idempotencia pelo texto novo inteiro pula o que ja entrou. Na WO 0019 ele parou no `## [Unreleased]` de dentro de
  um bloco — delimite pelas **quatro** crases, nunca pelo proximo titulo.
- **Pastas novas:** `kit-musica/skills/macetes-suno/` e `kit-musica/skills/revisar-faixa/` nao existem; crie.
- **`autocrlf=true` nesta maquina:** crie os arquivos novos em LF (o hash de chegada e de LF). Se um hash divergir,
  rode `file <arquivo>` antes de concluir que uma edicao errou.
- **Saida dos testes:** o unittest escreve no **stderr**; para ler so o veredito, use o comando da checagem 2 como
  esta (sem `2>&1` antes do pipe).
- **`__pycache__`:** os testes desligam o bytecode; se aparecer `scripts/__pycache__/`, apague e nao versione.
- **Nenhuma checagem abaixo usa emoji nem conta caracteres.**

## Depois de aplicar — conferencia antes do commit

| # | Checagem | Comando | Esperado |
|---|---|---|---|
| 1 | **Os dezoito arquivos sao os testados** | `sha1sum app/index.html scripts/validate.py meta/CHANGELOG.md README.md meta/CONTEXT.md meta/analises/261029-ANALISE-conversao-dos-albuns.md meta/analises/261029-ANALISE-kit-de-musica.md meta/IDEAS.md meta/ROADMAP.md meta/DECISIONS.md scripts/convert_guides.py scripts/test_convert_guides.py kit-musica/README.md kit-musica/BLOCO-SUNO.md kit-musica/skills/macetes-suno/SKILL.md kit-musica/skills/revisar-faixa/SKILL.md logs/2026-10-31.md meta/STATUS.md` | a coluna **chegada** do cabecalho, os dezoito. **Prova as 28 edicoes.** |
| 2 | Os dois testes passam | `python3 scripts/test_convert_guides.py 2>&1 >/dev/null \| tail -1` e `python3 scripts/test_convert_br.py 2>&1 >/dev/null \| tail -1` | `OK` e `OK` |
| 3 | O conversor no acervo real reproduz o do chat | `python3 scripts/convert_guides.py ../acervos/teste-wo0020.json ../Albuns/*.md --groups ../acervos/albuns-grupos.json; echo "exit=$?"` e depois `sha1sum ../acervos/teste-wo0020.json ../acervos/albuns-reagrupados.json` | `12 album(ns), 205 faixa(s)`, `exit=0`, e os **dois hashes iguais** (`6017c389a01904bcc6f59280fd45bf306f40d1d7`). Depois: `rm ../acervos/teste-wo0020.json` |
| 4 | A versao | `grep -c 'data-role="app-version">v0.10.0<' app/index.html`, `grep -m1 '^## \[' meta/CHANGELOG.md` | `1`, `## [0.10.0] — 2026-10-31` |
| 5 | Os registros | `grep -c '^## DEC-027 ' meta/DECISIONS.md`, `grep -c '^## Conversa 1' logs/2026-10-31.md`, `grep -c 'Status:\*\* Implementada (0.10.0)' meta/analises/261029-ANALISE-kit-de-musica.md`, `grep -cE '^### i-0(08\|22\|23\|38) ✅' meta/IDEAS.md` | `1`, `1`, `1`, `4` |
| 6 | Validacao passa, com o kit preso ao app | `python3 scripts/validate.py; echo "exit=$?"` | `exit=0`, com `OK  versao 0.10.0 igual em CHANGELOG, app, README e STATUS` e `OK  kit: limites da skill revisar-faixa iguais ao app (6)` |
| 7 | A checagem do kit reprova quando deve | `sed -i 's/LYRICS_MAX, LYRICS_WARN = 5000, 3000/LYRICS_MAX, LYRICS_WARN = 5000, 2900/' kit-musica/skills/revisar-faixa/SKILL.md; python3 scripts/validate.py \| grep -c 'ERRO no kit'; sed -i 's/LYRICS_MAX, LYRICS_WARN = 5000, 2900/LYRICS_MAX, LYRICS_WARN = 5000, 3000/' kit-musica/skills/revisar-faixa/SKILL.md; sha1sum kit-musica/skills/revisar-faixa/SKILL.md` | `1`, e o hash volta ao de **chegada** (`11e1cc74...`) |
| 8 | Nenhuma letra entra no repo | `GIT_OPTIONAL_LOCKS=0 git status --short --untracked-files=all \| grep -cE '\.json\|pycache\|\.txt'` | `0` |
| 9 | Nada de dados | `GIT_OPTIONAL_LOCKS=0 git status --short data` | saida **vazia** |

**Os tres campos de cada passo:** as nove sao rodadas por **quem aplica (o Code)**, na raiz do repo
(`C:\Users\alexk\Tools\cancioneiro\cancioneiro`), em Git Bash, com `LC_ALL=C.UTF-8`. **Chega no ramo?**
A checagem 1 cobre os dezoito arquivos inteiros; a 3 roda o conversor de chegada nos guias reais; a 7 prova que a
checagem nova reprova. **Esta e qual pergunta?** A 2, a 3 e a 7 respondem «funciona?»; as outras, «esta la?».
Os 12 albuns na tela sao do dono.

## Relatorio de aplicacao

Grave em `../261031-HHMM-code-cancioneiro-apply-wo0020.txt`, com o `HHMM` de `date +%y%m%d-%H%M` rodado na
hora. Diga o resultado da checagem 1 em primeiro lugar, e o da 3 em segundo.

**Proximo comando** (ultima linha do relatorio, cru e sozinho):

```
/wrap
```

## Commit

```
git add app/index.html scripts/validate.py scripts/convert_guides.py scripts/test_convert_guides.py kit-musica meta/CHANGELOG.md README.md meta/CONTEXT.md meta/analises meta/IDEAS.md meta/ROADMAP.md meta/DECISIONS.md logs/2026-10-31.md meta/STATUS.md meta/workorders
```

```
git commit -m "feat: conversor dos guias de Albuns, kit de musica e versao 0.10.0" -m "scripts/convert_guides.py converte os oito guias de formatos mistos e reagrupa as faixas por um mapa de grupos fora do repo (205 de 205 faixas, 12 albuns). kit-musica/ leva o que o projeto sabe do Suno aos projetos de musica do KCM: bloco para Instrucoes e CEREBRO, skills macetes-suno e revisar-faixa; validate.py prende os limites da skill aos do app (DEC-027). Analises com desfecho; i-008, i-022, i-023 e i-038 entregues."
```

```
git push
```
