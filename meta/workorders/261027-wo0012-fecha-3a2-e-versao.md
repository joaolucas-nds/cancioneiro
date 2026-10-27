# WO 0012 — Fecha a 3a.2 e a 0.6.0: a versao na tela e conferida pelo validador

## Cabecalho

> **Tipo:** WO de CODIGO (`app/index.html`, `scripts/validate.py`) e de registro.
> **Config sugerida:** Sonnet · `/effort medium`. Treze edicoes literais e um STATUS inteiro, todos aplicados e testados pelo chat numa copia; cada arquivo tem hash de chegada.
> **Pre-requisito:** commit `250f04b`, branch `main`, sincronizada com `origin/main`, **arvore limpa** (so esta WO aparece no `git status`).
> **Base:** roteiro da WO 0011 conferido na tela pelo dono em 2026-10-27, quatro de quatro; i-027 (o app mostra a versao).
> **Depende de:** WO 0011, ja aplicada.
>
> **Arquivos que esta WO edita — partida e chegada, os dois medidos pelo chat** (chegada = resultado de aplicar literalmente as edicoes abaixo, em LF):
>
> | arquivo | partida (sha1) | chegada (sha1) |
> |---|---|---|
> | `app/index.html` | `69112439b4c70aa1a1f0ffc2ba80251193ef2f01` | `6785fca2a47d8fa52a85ac893bd42e171c58e7d7` |
> | `scripts/validate.py` | `bd592136dc2ba81a1cc77f6cb7b9aceabc0db7f8` | `454a39a4d58ed29ed7c86de935f74fdefbf4038c` |
> | `meta/CHANGELOG.md` | `36270f4b32c0fe94f2c19db2c3e29614a630fdd9` | `6ee7151eda1b2a27dbe272d5bba60c80a158317d` |
> | `meta/ROADMAP.md` | `14d937f404204a8c75d07ed6f0a3abfe84955a24` | `a01c4533c8de87b36ab6b8216fd0728693868c45` |
> | `meta/IDEAS.md` | `a8546e9bd7dd125f902fe82601406e80f2cec574` | `9e56969d5abf53744d0d684f620a9792886bddea` |
> | `README.md` | `e914d60bca51ccc35f7fae4be11657c63be4503a` | `014b92f032678bb4d2132d8fcfd94b009d6b4813` |
> | `meta/STATUS.md` | `dab51c8b130ec6c6b0f1d7b54289a0e34cae63ae` | `c3b3b656a2133b69f44eba7985d0b794f31eacc2` |
>
> **Ancora semantica:** se um trecho-ancora nao bater EXATAMENTE, PARE e reporte.
> **Idempotencia:** antes de cada edicao, procure o texto NOVO INTEIRO; se ja estiver la, PULE e diga no relatorio.
>
> **Ancoras lidas em:** cada ancora foi lida pelo chat direto do disco no turno de 2026-10-27 e conferida como ocorrendo **exatamente 1 vez** no arquivo de partida (`str.count`). O texto literal esta em cada edicao.

---

## 1. Por que

O dono conferiu na tela os quatro itens do roteiro da WO 0011. Com isso a 3a.2 fecha, e a versao 0.6.0
pode entrar no CHANGELOG, no ROADMAP, no IDEAS (i-026 ✅) e no README.

Junto, a **i-027**: o cabecalho do app passa a mostrar a versao. Uma versao escrita em quatro lugares
(CHANGELOG, app, README, STATUS) desalinha cedo ou tarde, entao o `scripts/validate.py` ganha uma
quarta checagem: o topo do CHANGELOG manda, e os outros tres tem de dizer o mesmo; se nao, codigo 1.

O chat rodou o `validate.py` de chegada numa copia: **positivo** termina em `exit=0` com
`OK  versao 0.6.0 igual em CHANGELOG, app, README e STATUS`; com o README uma versao atras, `exit=1`
e a linha `README.md: 0.5.0`; com o app sem a versao, `exit=1` e `versao nao encontrada`. O app de
chegada (`6785fca2…`) abriu em Chromium headless sem erro de pagina, mostrando
`v0.6.0` no subtitulo, sem rolagem horizontal a 375 px.

De quebra, a docstring do `validate.py`, que dizia «Checa duas coisas» desde a WO 0006, passa a listar
as quatro.

**O STATUS vai literal, no apply** — nada «a cargo do `/wrap`».

## Edicao 0 — Conferencia de hash e de arvore

```
sha1sum app/index.html scripts/validate.py meta/CHANGELOG.md meta/ROADMAP.md meta/IDEAS.md README.md meta/STATUS.md
GIT_OPTIONAL_LOCKS=0 git status --short
```

Os sete batem com a coluna **partida** e o `git status` mostra **so** esta WO. Qualquer outra coisa:
**PARE e reporte**.

## Edicoes 01 a 13

Na ordem. Quase todas sao «trocar mantendo e acrescentando» — o texto novo **comeca ou termina com a
ancora** —, por isso a idempotencia e pelo texto novo INTEIRO. Copie o que esta ENTRE as linhas de
quatro crases, sem elas.

### E01 — a versao no cabecalho — `app/index.html`

**Ancora, literal:**

````
    <span class="sub">acervo de canções · copiar para o Suno sem procurar</span>
````

**Texto novo, literal:**

````
    <!-- Versao: a mesma do topo do meta/CHANGELOG.md. O scripts/validate.py confere
         que app, CHANGELOG, README e STATUS dizem a mesma (i-027). -->
    <span class="sub">acervo de canções · copiar para o Suno sem procurar · <span data-role="app-version">v0.6.0</span></span>
````

### E02 — docstring: as quatro checagens — `scripts/validate.py`

**Ancora, literal:**

````
Checa duas coisas:
  1. Sintaxe JSON de todos os schemas e datasets.
  2. Conformidade estrutural de cada dataset contra collection.schema.json
     (requer o pacote 'jsonschema'; se ausente, faz so a checagem de sintaxe).
````

**Texto novo, literal:**

````
Checa quatro coisas:
  1. Sintaxe JSON de todos os schemas e datasets.
  2. Conformidade estrutural de cada dataset contra collection.schema.json
     (requer o pacote 'jsonschema'; se ausente, faz so a checagem de sintaxe
     e a ultima linha diz ESQUEMA NAO CONFERIDO).
  3. Integridade referencial: todo id em songs[].styleModules existe no
     styleModules[] da propria colecao (DEC-016). O schema nao alcanca isto.
  4. A versao e a mesma no topo do meta/CHANGELOG.md, no app, no README e no
     STATUS (i-027).
````

### E03 — import re — `scripts/validate.py`

**Ancora, literal:**

````
import json
import sys
````

**Texto novo, literal:**

````
import json
import re
import sys
````

### E04 — check_version, antes de main — `scripts/validate.py`

**Ancora, literal:**

````
def main(argv):
````

**Texto novo, literal:**

````
def check_version():
    """A versao declarada nos quatro lugares tem de ser a mesma (i-027).

    Fonte: o topo do meta/CHANGELOG.md. O README ja ficou tres versoes atras
    sem ninguem notar (auditoria de 2026-07-21); esta checagem impede a volta.
    """
    def first(path, pattern):
        try:
            with open(os.path.join(ROOT, path), encoding="utf-8") as f:
                m = re.search(pattern, f.read(), re.M)
            return m.group(1) if m else None
        except OSError:
            return None

    found = {
        "meta/CHANGELOG.md": first("meta/CHANGELOG.md", r"^## \[(\d+\.\d+\.\d+)\]"),
        "app/index.html": first("app/index.html", r'data-role="app-version">v(\d+\.\d+\.\d+)<'),
        "README.md": first("README.md", r"\*\*Estado:\*\* v(\d+\.\d+\.\d+)"),
        "meta/STATUS.md": first("meta/STATUS.md", r"\*\*Versão atual:\*\* (\d+\.\d+\.\d+)"),
    }
    ref = found["meta/CHANGELOG.md"]
    bad = {k: v for k, v in found.items() if v is None or v != ref}
    if bad:
        print(f"ERRO de versao: o topo do meta/CHANGELOG.md diz {ref or '(nada)'}, mas:")
        for k, v in bad.items():
            print(f"   {k}: {v or 'versao nao encontrada'}")
        return 1
    print(f"OK  versao {ref} igual em CHANGELOG, app, README e STATUS")
    return 0


def main(argv):
````

### E05 — chamar check_version antes do resumo — `scripts/validate.py`

**Ancora, literal:**

````
        errors += check_module_refs(data, rel)

    print()
````

**Texto novo, literal:**

````
        errors += check_module_refs(data, rel)

    # versao: a mesma nos quatro lugares (i-027)
    errors += check_version()

    print()
````

### E06 — [0.6.0] no topo — `meta/CHANGELOG.md`

**Ancora, literal:**

````
## [0.5.0] — 2026-10-27
````

**Texto novo, literal:**

````
## [0.6.0] — 2026-10-27

Fase 3a.2: o custo de cada modulo no chip, conferido na tela. E a versao passa a aparecer no app.

### Added
- **Custo de cada modulo no chip (DEC-019):** com o painel de modulos aberto, cada chip mostra quantas tags ele muda no Style daquele cartao — `−N` ligado, `+N` desligado, `0` quando nao muda o prompt (o chip que antes acendia sem efeito nenhum). Recalculado em todos os chips a cada clique, so com o painel aberto. A linha de qualidade passa a dizer quanto o style base usa sozinho quando o recomposto passa de 10 tags. A lista de corte automatica foi descartada: medida, ela mandaria cortar a voz de rap em faixas de rap-pop.
- **A versao na tela (i-027):** o cabecalho do app mostra `v0.6.0`. Todo print passa a ser datavel.
- **`scripts/validate.py` confere a versao:** o topo do CHANGELOG, o app, o README e o STATUS tem de dizer a mesma; senao, codigo 1.

### Fixed
- O cabecalho do `scripts/validate.py` dizia «checa duas coisas» desde a WO 0006, que acrescentou a terceira; agora lista as quatro.

---

## [0.5.0] — 2026-10-27
````

### E07 — 3a.2 concluida — `meta/ROADMAP.md`

**Ancora, literal:**

````
**3a.2 — próxima fatia:**
- ⬜ Sugerir o que cortar quando há tags demais (i-026) — 7 de 7 faixas do álbum de referências já acendem âmbar.
````

**Texto novo, literal:**

````
**3a.2 — ✅ concluída em 0.6.0 (DEC-019), conferida na tela pelo dono em 2026-10-27:**
- ✅ O custo de cada módulo em tags, no próprio chip, e a folga do style base na linha de qualidade (i-026). A lista de corte automática foi descartada pela medição: mandaria cortar a voz de rap em faixas de rap-pop.
````

### E08 — i-026 vira ✅ — `meta/IDEAS.md`

**Ancora, literal:**

````
### i-026 💡 Sugerir o que cortar quando ha tags demais (Fase 3a.2)
````

**Texto novo, literal:**

````
### i-026 ✅ Sugerir o que cortar quando ha tags demais (Fase 3a.2)
````

### E09 — i-026 nota de entrega — `meta/IDEAS.md`

**Ancora, literal:**

````
**Corrigido em 2026-10-27 (DEC-019).** A frase acima sobre classificar o base estava errada: medido, o style base nunca passa de 10 tags e o excesso vem todo dos modulos. E a lista de corte automatica erra em 2 de 7 faixas (manda cortar a voz de rap em rap-pop). A 3a.2 entrega o **custo de cada modulo no chip** e a folga do base, nao uma sugestao; aguarda a conferencia na tela.
````

**Texto novo, literal:**

````
**Corrigido em 2026-10-27 (DEC-019).** A frase acima sobre classificar o base estava errada: medido, o style base nunca passa de 10 tags e o excesso vem todo dos modulos. E a lista de corte automatica erra em 2 de 7 faixas (manda cortar a voz de rap em rap-pop). A 3a.2 entrega o **custo de cada modulo no chip** e a folga do base, nao uma sugestao; aguarda a conferencia na tela.

**Entregue em 0.6.0, conferido na tela em 2026-10-27** — como custo no chip, nao como lista de corte.
````

### E10 — i-027 vira ✅ — `meta/IDEAS.md`

**Ancora, literal:**

````
### i-027 💡 O app declarar a propria versao na tela
````

**Texto novo, literal:**

````
### i-027 ✅ O app declarar a propria versao na tela
````

### E11 — i-027 nota de entrega — `meta/IDEAS.md`

**Ancora, literal:**

````
`[nascido da exploracao de 2026-10-21, candidato C4]` STATUS, CHANGELOG e README dizem a versao; o `app/index.html` publicado nao a declara em lugar nenhum. Consequencia observada: a captura de tela de 2026-10-17 nao permitia saber qual versao estava no ar. Uma linha discreta no rodape (ou no `title`) torna todo print do dono datavel, e um teste pode afirmar que ela bate com o topo do CHANGELOG. Pequeno; candidato a ir junto da proxima WO de codigo.
````

**Texto novo, literal:**

````
`[nascido da exploracao de 2026-10-21, candidato C4]` STATUS, CHANGELOG e README dizem a versao; o `app/index.html` publicado nao a declara em lugar nenhum. Consequencia observada: a captura de tela de 2026-10-17 nao permitia saber qual versao estava no ar. Uma linha discreta no rodape (ou no `title`) torna todo print do dono datavel, e um teste pode afirmar que ela bate com o topo do CHANGELOG. Pequeno; candidato a ir junto da proxima WO de codigo.

**Entregue em 0.6.0.** O cabecalho mostra `v0.6.0`, e o `scripts/validate.py` reprova (codigo 1) se o topo do CHANGELOG, o app, o README e o STATUS divergirem.
````

### E12 — estado v0.6.0 — `README.md`

**Ancora, literal:**

````
> **Estado:** v0.5.0 — ferramenta em uso. Lê o acervo, copia por campo, troca módulos de estilo, **mede cada prompt contra os limites do Suno** e exporta Markdown. Publicada no GitHub Pages. Ver `meta/ROADMAP.md`.
````

**Texto novo, literal:**

````
> **Estado:** v0.6.0 — ferramenta em uso. Lê o acervo, copia por campo, troca módulos de estilo, **mede cada prompt contra os limites do Suno** e exporta Markdown. Publicada no GitHub Pages. Ver `meta/ROADMAP.md`.
````

### E13 — o custo no chip no passo a passo — `README.md`

**Ancora, literal:**

````
5. Leia a linha embaixo de cada campo antes de copiar: **vermelho** = o Suno vai cortar o texto (passou do limite, ele trunca sem avisar); **âmbar** = vai funcionar, mas pior (tags demais, ou negação «no X» que rende mais no campo Exclude).
````

**Texto novo, literal:**

````
5. Leia a linha embaixo de cada campo antes de copiar: **vermelho** = o Suno vai cortar o texto (passou do limite, ele trunca sem avisar); **âmbar** = vai funcionar, mas pior (tags demais, ou negação «no X» que rende mais no campo Exclude). Com os módulos abertos, cada chip mostra quantas tags ele põe ou tira (`+2`, `−2`, ou `0` quando não muda nada) — use isso para decidir o que desligar.
````

## Edicao 14 — STATUS inteiro — `meta/STATUS.md`

Substitua o arquivo **inteiro** pelo bloco abaixo (o fim de linha do arquivo e LF, e ele termina com uma
quebra de linha depois da ultima linha). Nao ha ancora: a partida e garantida pela Edicao 0.

````
# STATUS.md — Cancioneiro

> **O agora.** O que funciona, o que está em progresso, o que está quebrado, backlog curto.
> Rolante: item resolvido sai daqui e vai para o CHANGELOG. Médio/longo prazo vive no ROADMAP.

**Versão atual:** 0.6.0 · **Fase:** 3a e 3a.2 concluídas e conferidas na tela · Fase 2 com i-008 em aberto · próxima: BPM (i-005)

---

## Última conversa (2026-10-27, fecho da 3a.2 e da 0.6.0)

- **3a.2 conferida na tela pelo dono:** os quatro itens do roteiro da WO 0011 ok `[relatado pelo dono, 2026-10-27; a captura de tela das 17:21 mostra a folga do base em ar-01, ar-02 e ar-03 com os números medidos]` — a folga do base em ar-01, os custos exatos dos chips, o chip clicado trocando de sinal, e o vizinho de ar-04 indo de +1 a +2.
- **0.6.0 fechada no CHANGELOG:** o custo no chip (DEC-019) e a versão na tela (i-027), com o `validate.py` passando a conferir que o topo do CHANGELOG, o app, o README e o STATUS dizem a mesma versão.
- **Este bloco substitui o anterior, de 2026-10-27, que fechava a 0.5.0** e acumulava sete linhas de aplicação de WO. O que ele dizia está no CHANGELOG (0.5.0 e 0.6.0), no DECISIONS (DEC-018 e DEC-019) e em `logs/2026-10-27.md`.

## Funciona (pronto)

- **Ferramenta `app/index.html`:** importa/carrega JSON, cartões por álbum, copiar Style/Lyrics/Exclude por botão (o botão entrega o texto que está na tela — FIX-007), marca «usei», filtros por álbum/estado/uso, busca, módulos de estilo que recompõem o Style ao vivo, variantes e notas recolhíveis, «Baixar .json» limpo e «Importar .json» que saneia chaves internas e diz quantas removeu (FIX-004/006). A versão aparece no cabeçalho.
- **Painel de qualidade (0.5.0, DEC-018):** linha abaixo de Style, Lyrics e Exclude com caracteres contra o limite do campo, tags do Style e negações «no X». Vermelho só para truncamento.
- **Custo de cada módulo no chip (0.6.0, DEC-019):** com o painel de módulos aberto, cada chip mostra `−N`, `+N` ou `0` tags; a linha de qualidade diz quanto o style base usa sozinho quando o recomposto passa de 10.
- **Esquema JSON canônico** (`schema/`). Biblioteca de referência para autoria em `schema/style-modules.json` (27 módulos, sete camadas); cada acervo traz os seus (DEC-016).
- **Datasets:** `data/exemplo-cinzeiro.json` (1 faixa, com os 5 módulos que cita) e `data/demo.json` (2 álbuns, 3 faixas). O álbum de referências do dono mora fora do repo, em `../album-referencias (1).json` (7 faixas, 50 módulos).
- **Validação** (`scripts/validate.py`): sintaxe, esquema (com `jsonschema`), integridade referencial dos módulos e versão igual nos quatro lugares; código 1 se falhar; a última linha diz se o esquema foi de fato conferido.
- **Export MD** (faixa / álbum / acervo), com o Style recomposto e o rótulo fora do bloco.
- **Prompt-modelo** (`schema/PROMPT-PARA-CHATS.md`) para chats gerarem JSON no esquema.
- **Publicado no GitHub Pages** em `https://joaolucas-nds.github.io/cancioneiro/app/index.html` — o push em `main` publica.

## Em progresso

- (nada)

## Quebrado / pendências que travam

- (nada quebrado)

## Pendências do dono

- **Instalar o validador de esquema nesta máquina.** Sem `jsonschema` e `referencing`, o `validate.py` só confere sintaxe e diz `ESQUEMA NAO CONFERIDO` na última linha. Uma vez, no CMD: `pip install jsonschema referencing --break-system-packages`. Depois, `python3 scripts/validate.py` deve terminar em `Tudo conforme ao esquema.` — o arquivo do álbum já foi validado fora daqui com 0 erros.

## Backlog curto (próximas ações concretas)

1. **Controle de BPM** (i-005) — pedido explícito na premissa original, ainda não feito. Começa por spec: o BPM aparece no `style`, no campo `bpm` e nos módulos de andamento, e as três fontes podem divergir.
2. **Folga no prompt-modelo** (i-028) — pedir ao chat um style base com 6 a 8 tags. Em ar-01 e ar-04 o base nasce com 10 de 10.
3. **Testar o prompt-modelo ponta a ponta:** colar num chat, gerar uma faixa, importar.
4. **Converter 1 álbum real** (i-008) — depende de o dono trazer um `.md` de origem para a pasta-pai.

## Notas de estado

- **Repo local do dono:** `C:\Users\alexk\Tools\cancioneiro\cancioneiro` (Windows). O chat lê e grava na pasta vinculada; commit e push são do Code (DEC-010). A pasta-pai guarda relatórios, notas e o acervo do dono, fora do Git; o lido vai para `../notas-arquivadas/`.
- **Canal:** pasta vinculada é o padrão; a cópia achatada (FlatDrop) é reserva (DEC-017).
- **Limites do Suno:** o v6 saiu em 2026-09-09 e a nota oficial não documenta limite de campo; os números do painel vêm de fonte secundária, com fonte e data no `QUALITY_LIMITS` (DEC-018). Reconferir quando houver documentação oficial. O `meta/HISTORY.md` ainda descreve o v5.5 e precisa de uma atualização sobre o v6.
- **Limite conhecido:** `tryAutoLoad` (carregamento automático pelo Pages) não saneia chaves internas — só a importação por arquivo faz isso. Inócuo enquanto nenhum acervo contaminado for para `data/`.
- **Pendência de contexto — ASU:** o dono perguntou se o «modo ASU» do KCM seria melhor que o modo Code para este projeto; ficou pendente até ele trazer a descrição do ASU `[relatado pelo dono, sem material de apoio]`.
- Os álbuns antigos de julho não estão na pasta. Para converter um (i-008), trazer o `.md` de origem para a pasta-pai.
- Design: na recomposição do Style a base manda — desligar um módulo não remove o que já está no style base; módulos só somam. O dedup compara sequências de palavras (FIX-003). Os módulos de gênero e de andamento costumam custar 0 tag por isso (DEC-019).
````

## Fora de escopo

- **BPM (i-005)** — proxima frente; comeca por spec, nao por WO.
- **i-028** (folga no prompt-modelo) — continua so capturada.
- `tryAutoLoad` sanear, HISTORY sobre o v6 — continuam nas Notas de estado.
- `data/`, `schema/` — nada muda.

## Armadilhas desta WO

- **O CHANGELOG manda.** A `check_version` le a primeira linha `## [x.y.z]` do CHANGELOG e cobra o
  mesmo numero dos outros tres. Ao fechar uma versao no futuro, os quatro mudam juntos — e o validador
  que avisa se um ficou para tras.
- **E01 aninha um `span` dentro do `.sub`.** O seletor do validador e `data-role="app-version"`; nao
  troque o atributo.
- **E04 chama `check_version()` uma vez, fora do laco dos arquivos de `data/`.** Um erro de versao
  conta como 1 no total de erros.
- **Fim de linha:** os sete arquivos sao LF. Se um hash de chegada divergir, rode `file <arquivo>`
  antes de concluir que uma edicao errou.

## Depois de aplicar — conferencia antes do commit

| # | Checagem | Comando | Esperado |
|---|---|---|---|
| 1 | **Os sete arquivos sao os testados** | `sha1sum app/index.html scripts/validate.py meta/CHANGELOG.md meta/ROADMAP.md meta/IDEAS.md README.md meta/STATUS.md` | a coluna **chegada** do cabecalho, os sete. **Prova as catorze edicoes.** |
| 2 | A versao na tela | `grep -c 'data-role="app-version">v0.6.0<' app/index.html` | `1` |
| 3 | A checagem nova existe e e chamada | `grep -c '^def check_version' scripts/validate.py`, `grep -c 'errors += check_version()' scripts/validate.py` | `1`, `1` |
| 4 | Os registros | `grep -c '^## \[0.6.0\]' meta/CHANGELOG.md`, `grep -cE '^### i-02[67] ✅' meta/IDEAS.md`, `grep -c '3a.2 — ✅' meta/ROADMAP.md` | `1`, `2`, `1` |
| 5 | Validacao passa e confere a versao | `python3 scripts/validate.py; echo "exit=$?"` | uma linha `OK  versao 0.6.0 igual em CHANGELOG, app, README e STATUS` e `exit=0` |
| 6 | Nada de dados | `GIT_OPTIONAL_LOCKS=0 git status --short data schema` | saida **vazia** |
| 7 | Nenhum relatorio `.txt` no repo | `GIT_OPTIONAL_LOCKS=0 git status --short \| grep -c '\.txt'` | `0` |

**Os tres campos de cada passo:** as sete sao rodadas por **quem aplica (o Code)**, na raiz do repo
(`C:\Users\alexk\Tools\cancioneiro\cancioneiro`), em Git Bash, com `LC_ALL=C.UTF-8` para os `grep`
com acento. **Chega no ramo?** A checagem 1 cobre os sete arquivos inteiros. **Esta e qual pergunta?**
As sete respondem «esta la?». O que so a tela do dono responde vai no roteiro que o chat entrega **no
corpo da resposta**, nao aqui.

## Relatorio de aplicacao

Grave em `../261027-HHMM-code-cancioneiro-apply-wo0012.txt`, com o `HHMM` de `date +%y%m%d-%H%M` rodado
na hora. Diga o resultado da checagem 1 em primeiro lugar. A conferencia na tela **nao e sua**.

**Proximo comando** (ultima linha do relatorio, cru e sozinho):

```
/wrap
```

## Commit

```
git add app/index.html scripts/validate.py meta/CHANGELOG.md meta/ROADMAP.md meta/IDEAS.md README.md meta/STATUS.md meta/workorders
```

```
git commit -m "feat: versao 0.6.0 na tela e conferida pelo validador" -m "Fecha a Fase 3a.2 (DEC-019), conferida na tela pelo dono. O cabecalho do app mostra a versao (i-027) e o validate.py ganha a quarta checagem: o topo do CHANGELOG manda e app, README e STATUS tem de dizer o mesmo, senao codigo 1. Corrige a docstring do validate.py, que ainda dizia duas checagens. Registra 0.6.0 no CHANGELOG, ROADMAP, IDEAS e README e reescreve o STATUS."
```

```
git push
```
