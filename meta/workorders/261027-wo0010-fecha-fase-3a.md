# WO 0010 — Fecha a Fase 3a e a versao 0.5.0

## Cabecalho

> **Tipo:** WO de DOC (registro). Nenhum codigo de produto muda.
> **Config sugerida:** Sonnet · `/effort low`. Todo texto e literal e foi aplicado pelo chat numa copia antes de virar WO; cada arquivo tem hash de chegada.
> **Pre-requisito:** commit `96dfe1d`, branch `main`, sincronizada com `origin/main`, **arvore limpa**.
> **Base:** os cinco itens do roteiro de tela da WO 0009, confirmados pelo dono em 2026-10-27 («item 1 ok, item 2 ok, item 3 ok, item 4 ok, item 5 ok»). Fase 3a conferida.
> **Depende de:** WO 0009, ja aplicada (`2ff6fe3` + `96dfe1d`).
>
> **Arquivos que esta WO edita — partida e chegada, os dois medidos pelo chat** (o de chegada e o resultado de aplicar literalmente as edicoes abaixo; em LF):
>
> | arquivo | partida (sha1) | chegada (sha1) |
> |---|---|---|
> | `meta/STATUS.md` | `c7f816b3b26e5c5e4223dfcb7c1b9e60f5dac11b` | `eeac047bfedcf5bbdb93c1aef6bd8115603ebbd6` |
> | `meta/CHANGELOG.md` | `d621808336845e20fcce942fc72a6af70d00a4fe` | `36270f4b32c0fe94f2c19db2c3e29614a630fdd9` |
> | `meta/ROADMAP.md` | `03ed0dc6c2535ef7bfe1d94ad4158842f9cc0583` | `14d937f404204a8c75d07ed6f0a3abfe84955a24` |
> | `meta/IDEAS.md` | `530ab0b3bebce2d8f9db228151356da23f6fa287` | `3bd707b085b1adb908a59c694af7dfb556655bf1` |
> | `README.md` | `9eed4e68fec8102c5427a053f44e2d13cc7527b0` | `e914d60bca51ccc35f7fae4be11657c63be4503a` |
>
> **Ancora semantica:** se um trecho-ancora nao bater EXATAMENTE, PARE e reporte.
> **Idempotencia:** antes de cada edicao, procure o texto NOVO INTEIRO; se ja estiver la, PULE e diga no relatorio.
>
> **Ancoras lidas em:** cada ancora foi lida pelo chat direto do disco no turno de 2026-10-27 e conferida como ocorrendo **exatamente 1 vez** no arquivo de partida (por `str.count`). O texto literal de cada uma esta na propria edicao.

---

## 1. Por que

A Fase 3a foi conferida na tela, e a documentacao nao sabe disso. Medido no turno: o `STATUS.md` declara
abertas **seis** pendencias que o dono ja fechou (telas das WOs 0006, 0007 e 0009; a pergunta de
2026-10-17; e diz «aguardando conferencia na tela» na linha da versao); o ROADMAP mostra a 3a toda
em ⬜; o IDEAS mostra i-017 a i-019 como 💡; o CHANGELOG para na 0.4.1, embora o app tenha recebido
quatro FIX e uma feature desde entao; e o **README promete «troca modular de estilo/BPM»**, quando o
controle de BPM (i-005) nunca foi implementado — falso na cara publica do projeto.

**Versao 0.5.0:** feature nova (o painel) mais correcoes, desde a 0.4.1 → MINOR, por SemVer. E a
primeira entrada de CHANGELOG desde 2026-07-21, entao ela cobre os FIX-004 a 007 tambem.

**Esta WO nao tem a ambiguidade «a cargo do /wrap».** Nas quatro WOs anteriores eu escrevi «STATUS
a cargo do /wrap» ao lado de uma checagem que exigia o STATUS antes do commit, e o Code resolveu bem
todas as vezes, mas a ambiguidade era minha. Aqui o STATUS e texto literal e entra no apply.

## Edicao 0 — Conferencia de hash e de arvore

```
sha1sum meta/STATUS.md meta/CHANGELOG.md meta/ROADMAP.md meta/IDEAS.md README.md
GIT_OPTIONAL_LOCKS=0 git status --short
```

Os cinco hashes batem com a coluna **partida** da tabela, e o `git status` mostra **so** esta WO (nao
rastreada). Qualquer outra coisa: **PARE e reporte**.

## Edicao 1 — `meta/STATUS.md` · SUBSTITUIR o arquivo inteiro

**O arquivo encolhe de 10.159 para 5.960 bytes, e diz no proprio texto o que saiu e para onde foi:**
os seis blocos «Ultima conversa» de 2026-07-21 a 2026-10-24 saem — o entregue esta no CHANGELOG, as
decisoes no DECISIONS, o detalhe de cada dia em `logs/`. Toda pendencia que ainda e verdade
(`jsonschema`, o painel do Projeto, `tryAutoLoad`, ASU, os albuns antigos) foi mantida.

Substitua o conteudo inteiro de `meta/STATUS.md` por este texto, literal, terminando com uma quebra
de linha:

````
# STATUS.md — Cancioneiro

> **O agora.** O que funciona, o que está em progresso, o que está quebrado, backlog curto.
> Rolante: item resolvido sai daqui e vai para o CHANGELOG. Médio/longo prazo vive no ROADMAP.

**Versão atual:** 0.5.0 · **Fase:** 3a (painel de qualidade) concluída e conferida na tela · Fase 2 com i-008 em aberto · próxima: 3a.2 ou BPM

---

## Última conversa (2026-10-27, fecho da Fase 3a e da 0.5.0)

- **Fase 3a conferida na tela pelo dono:** os cinco itens do roteiro da WO 0009 ok `[relatado pelo dono, 2026-10-27]` — o painel mede o Style recomposto (298 em ar-01, não os 164 do base), acompanha o clique no chip, o botão copia o que se vê (FIX-007), o vermelho aparece em 1.271 com todos os módulos ligados, e a faixa instrumental avisa «no drums» sem avisar «no vocals».
- **0.5.0 fechada no CHANGELOG:** tudo o que entrou no app desde a 0.4.1 — painel de qualidade (DEC-018), FIX-004 a FIX-007, acervo autossuficiente (DEC-016).
- **Este STATUS foi reescrito, não acrescido.** Saíram os seis blocos «Última conversa» de 2026-07-21 a 2026-10-24: o que foi entregue está no CHANGELOG (0.4.1 e 0.5.0), as decisões no DECISIONS (DEC-010 a DEC-018, FIX-003 a FIX-007), e o detalhe de cada dia em `logs/`. As pendências de tela que eles declaravam abertas foram **todas fechadas pelo dono** (WO 0006 item 1; WO 0007 itens 1-3; WO 0009 itens 1-5), e a pergunta de 2026-10-17 está fechada desde a WO 0007. Nada único se perdeu: o que só existia aqui foi para «Notas de estado».

## Funciona (pronto)

- **Ferramenta `app/index.html`:** importa/carrega JSON, cartões por álbum, copiar Style/Lyrics/Exclude por botão (o botão entrega o texto que está na tela — FIX-007), marca «usei», filtros por álbum/estado/uso, busca, módulos de estilo que recompõem o Style ao vivo, variantes e notas recolhíveis, «Baixar .json» limpo e «Importar .json» que saneia chaves internas e diz quantas removeu (FIX-004/006).
- **Painel de qualidade (0.5.0, DEC-018):** linha abaixo de Style, Lyrics e Exclude com caracteres contra o limite do campo, tags do Style e negações «no X». Vermelho só para truncamento.
- **Esquema JSON canônico** (`schema/`). Biblioteca de referência para autoria em `schema/style-modules.json` (27 módulos, sete camadas); cada acervo traz os seus (DEC-016).
- **Datasets:** `data/exemplo-cinzeiro.json` (1 faixa, com os 5 módulos que cita) e `data/demo.json` (2 álbuns, 3 faixas). O álbum de referências do dono mora fora do repo, em `../album-referencias (1).json` (7 faixas, 50 módulos).
- **Validação** (`scripts/validate.py`): sintaxe, esquema (com `jsonschema`) e integridade referencial dos módulos; código 1 se falhar; a última linha diz se o esquema foi de fato conferido.
- **Export MD** (faixa / álbum / acervo), com o Style recomposto e o rótulo fora do bloco.
- **Prompt-modelo** (`schema/PROMPT-PARA-CHATS.md`) para chats gerarem JSON no esquema.
- **Publicado no GitHub Pages** em `https://joaolucas-nds.github.io/cancioneiro/app/index.html` — o push em `main` publica.

## Em progresso

- (nada)

## Quebrado / pendências que travam

- (nada quebrado)

## Pendências do dono

- **Instalar o validador de esquema nesta máquina.** Sem `jsonschema` e `referencing`, o `validate.py` só confere sintaxe e diz `ESQUEMA NAO CONFERIDO` na última linha. Uma vez, no Git Bash ou no CMD: `pip install jsonschema referencing --break-system-packages`. Depois, `python3 scripts/validate.py` deve terminar em `Tudo conforme ao esquema.` — o arquivo do álbum já foi validado fora daqui com 0 erros.
- **Colar as Instruções no painel do Projeto.** O painel ainda tem a versão anterior à WO 0008 e diverge do `INSTRUCOES-DO-PROJETO.md` em duas linhas: `**Config:**` (falta `/ultracode`) e `**Commit:**` (falta «Bloco git parcial (só `add`) não serve.»). Abrir o arquivo, copiar tudo, colar no painel.

## Backlog curto (próximas ações concretas)

1. **3a.2 — sugerir o que cortar quando há tags demais** (i-026). 7 de 7 faixas do álbum já acendem âmbar; aviso que sempre acende vira paisagem.
2. **Controle de BPM** (i-005) — pedido explícito na premissa original, ainda não feito.
3. **O app declarar a própria versão** (i-027) — pequeno; torna todo print datável.
4. **Testar o prompt-modelo ponta a ponta:** colar num chat, gerar uma faixa, importar.
5. **Converter 1 álbum real** (i-008) — depende de o dono trazer um `.md` de origem para a pasta-pai.

## Notas de estado

- **Repo local do dono:** `C:\Users\alexk\Tools\cancioneiro\cancioneiro` (Windows). O chat lê e grava na pasta vinculada; commit e push são do Code (DEC-010). A pasta-pai guarda relatórios, notas e o acervo do dono, fora do Git; o lido vai para `../notas-arquivadas/`.
- **Canal:** pasta vinculada é o padrão; a cópia achatada (FlatDrop) é reserva (DEC-017).
- **Limites do Suno:** o v6 saiu em 2026-09-09 e a nota oficial não documenta limite de campo; os números do painel vêm de fonte secundária, com fonte e data no `QUALITY_LIMITS` (DEC-018). Reconferir quando houver documentação oficial. O `meta/HISTORY.md` ainda descreve o v5.5 e precisa de uma atualização sobre o v6.
- **Limite conhecido:** `tryAutoLoad` (carregamento automático pelo Pages) não saneia chaves internas — só a importação por arquivo faz isso. Inócuo enquanto nenhum acervo contaminado for para `data/`.
- **Pendência de contexto — ASU:** o dono perguntou se o «modo ASU» do KCM seria melhor que o modo Code para este projeto; ficou pendente até ele trazer a descrição do ASU `[relatado pelo dono, sem material de apoio]`.
- Os álbuns antigos de julho não estão na pasta. Para converter um (i-008), trazer o `.md` de origem para a pasta-pai.
- Design: na recomposição do Style a base manda — desligar um módulo não remove o que já está no style base; módulos só somam. O dedup compara sequências de palavras (FIX-003).
````

## Edicoes 2 a 5 — CHANGELOG, ROADMAP, IDEAS, README

Treze substituicoes de texto. Na mesma ordem em que aparecem; varias do IDEAS e do README sao «trocar
mantendo e acrescentando» — o texto novo **comeca com a ancora**. Por isso a idempotencia e pelo texto
novo INTEIRO, nunca pela ancora.

### E1 · nova entrada [0.5.0] no topo — `meta/CHANGELOG.md`

**Ancora, literal:**

````
## [0.4.1] — 2026-07-21
````

**Texto novo, literal:**

````
## [0.5.0] — 2026-10-27

Painel de qualidade do prompt (Fase 3a) e quatro correcoes que o tornaram confiavel. Tudo o que entrou no app desde a 0.4.1.

### Added
- **Painel de qualidade (DEC-018):** abaixo de Style, Lyrics e Exclude, uma linha que mede o que vai para o Suno — caracteres contra o limite do campo (Style e Exclude 1.000; Lyrics 5.000, com aviso a partir de ~3.000), tags do Style (ambar acima de ~10, nunca vermelho) e negacoes «no X» (por fronteira de palavra; so avisa; `no vocals` nao dispara em faixa instrumental). Mede o Style **recomposto** e se atualiza a cada clique num chip de modulo. Vermelho reservado ao truncamento, o unico caso que perde texto. Limites num objeto unico, com fonte e data.
- **`scripts/validate.py`:** checagem de integridade referencial (todo id em `songs[].styleModules` existe no `styleModules[]` da propria colecao — DEC-016), e a ultima linha passa a declarar se o esquema foi de fato conferido.
- `meta/specs/` (primeira spec: o painel) e `meta/analises/` (primeira analise: o round-trip do acervo).

### Fixed
- **FIX-004:** o «Baixar .json» gravava um `Set` serializado como `{}` em cada faixa, e o «Importar .json» quebrava nele — o app estragava o proprio arquivo. O estado dos modulos ligados saiu de dentro da colecao.
- **FIX-005:** a importacao relatava qualquer falha como «nao e um JSON valido», e o `validate.py` dizia «Tudo conforme ao esquema» sem ter conferido esquema nenhum. Mensagem que nomeia um resultado so pode vir da operacao que o produz.
- **FIX-006:** arquivos ja contaminados continuavam propagando a chave interna. A importacao saneia as chaves com prefixo `_` e **diz quantas removeu**.
- **FIX-007:** o botao «copiar» do Style entregava o texto de antes do clique no chip de modulo. O que se via nao era o que se colava no Suno; a troca de estilo por modulo so chegava ao Suno pelo export MD.

### Changed
- **DEC-016 — acervo autossuficiente:** cada colecao traz os modulos que suas faixas citam; `schema/style-modules.json` e biblioteca de referencia para autoria. `data/exemplo-cinzeiro.json` recebeu os 5 modulos que citava sem ter.
- Kit de contexto atualizado de v1.74.0 para v1.131.0 (DEC-010 a DEC-015, DEC-017) — processo e documentacao, nenhuma mudanca de produto.

---

## [0.4.1] — 2026-07-21
````

### E2 · Fase 3: 3a concluida, 3a.2 aberta — `meta/ROADMAP.md`

**Ancora, literal:**

````
## ⬜ Fase 3 — Qualidade de prompt e modularidade
O diferencial real sobre os builders genéricos: a ferramenta não só organiza, ela **impede prompt ruim**. Fundamentado em constraints verificados (HISTORY §9-11). Núcleo modular já entregue no v0.

**3a — Painel de qualidade (recomendado primeiro):**
- ⬜ Contador de caracteres do Style (~1.000) e Lyrics (5.000 / doce em 3.000) — o Suno trunca em silêncio (i-017).
- ⬜ Contador de tags com aviso acima de ~10 (i-018).
- ⬜ Detectar "no X" no style e sugerir migrar para `excludeStyles` (i-019).
- ⬜ Aviso leve de ordem: gênero nas primeiras palavras (i-020).


````

**Texto novo, literal:**

````
## 🔨 Fase 3 — Qualidade de prompt e modularidade
O diferencial real sobre os builders genéricos: a ferramenta não só organiza, ela **impede prompt ruim**. Fundamentado em constraints verificados (HISTORY §9-11). Núcleo modular já entregue no v0.

**3a — Painel de qualidade — ✅ concluída em 0.5.0 (DEC-018), conferida na tela pelo dono em 2026-10-27:**
- ✅ Contador de caracteres do Style e do Exclude (1.000) e do Lyrics (5.000, aviso a partir de ~3.000), medindo o Style **recomposto** e atualizando a cada chip (i-017).
- ✅ Contador de tags: âmbar acima de ~10, nunca vermelho (i-018).
- ✅ «no X» no style detectado por fronteira de palavra; **só avisa** — migrar num clique ficou fora (DEC-018); `no vocals` não dispara em faixa instrumental (i-019).
- ⏸ Aviso de ordem: gênero nas primeiras palavras (i-020) — **adiado**: dispara em 0 de 10 faixas reais; gatilho no IDEAS.

**3a.2 — próxima fatia:**
- ⬜ Sugerir o que cortar quando há tags demais (i-026) — 7 de 7 faixas do álbum de referências já acendem âmbar.


````

### E3 · i-017 vira ✅ com a nota de entrega — `meta/IDEAS.md`

**Ancora, literal:**

````
### i-017 💡 Contador de caracteres do Style e do Lyrics
````

**Texto novo, literal:**

````
### i-017 ✅ Contador de caracteres do Style e do Lyrics
````

### E3 · i-017 nota — `meta/IDEAS.md`

**Ancora, literal:**

````
O Suno **trunca em silêncio** ao passar de ~1.000 caracteres no Style (5.000 no Lyrics, com ~3.000 como ponto doce). Sem aviso, sem erro — o excedente só não chega ao modelo. É um problema invisível que só uma ferramenta resolve. Mostrar contador ao vivo, com aviso ao aproximar do limite. Ver HISTORY §9. **Alta prioridade** — é exatamente o "consumir espaço desnecessário" da premissa original.
````

**Texto novo, literal:**

````
O Suno **trunca em silêncio** ao passar de ~1.000 caracteres no Style (5.000 no Lyrics, com ~3.000 como ponto doce). Sem aviso, sem erro — o excedente só não chega ao modelo. É um problema invisível que só uma ferramenta resolve. Mostrar contador ao vivo, com aviso ao aproximar do limite. Ver HISTORY §9. **Alta prioridade** — é exatamente o "consumir espaço desnecessário" da premissa original.

**Entregue em 0.5.0 (DEC-018), conferido na tela em 2026-10-27.** Mede tambem o Exclude (1.000) e mede o Style **recomposto** — a medicao mostrou que o risco mora nos modulos: nenhum style base passa de 174 caracteres, e todas as faixas do album passam de 1.000 com a biblioteca inteira ligada.
````

### E3 · i-018 vira ✅ com a nota de entrega — `meta/IDEAS.md`

**Ancora, literal:**

````
### i-018 💡 Contador de tags com aviso de excesso
````

**Texto novo, literal:**

````
### i-018 ✅ Contador de tags com aviso de excesso
````

### E3 · i-018 nota — `meta/IDEAS.md`

**Ancora, literal:**

````
Acima de ~10 tags o Suno começa a ignorar as finais e a média dos sinais vira resultado genérico; o ponto doce fica entre 5 e 8. A ferramenta pode contar as vírgulas do Style e avisar quando passar, sugerindo o que cortar pela ordem de prioridade (gênero > clima > instrumento > vocal > BPM). Ver HISTORY §10.
````

**Texto novo, literal:**

````
Acima de ~10 tags o Suno começa a ignorar as finais e a média dos sinais vira resultado genérico; o ponto doce fica entre 5 e 8. A ferramenta pode contar as vírgulas do Style e avisar quando passar, sugerindo o que cortar pela ordem de prioridade (gênero > clima > instrumento > vocal > BPM). Ver HISTORY §10.

**Entregue em 0.5.0 (DEC-018), sem a sugestao de corte** — que virou i-026. Ambar acima de ~10, nunca vermelho: diluir nao perde texto, e a fonte do v6 diz que acima de 10 «o ganho achata, nao quebra».
````

### E3 · i-019 vira ✅ com a nota de entrega — `meta/IDEAS.md`

**Ancora, literal:**

````
### i-019 💡 Detectar "no X" no style e sugerir migrar para excludeStyles
````

**Texto novo, literal:**

````
### i-019 ✅ Detectar "no X" no style e sugerir migrar para excludeStyles
````

### E3 · i-019 nota — `meta/IDEAS.md`

**Ancora, literal:**

````
O campo de exclusão dedicado é mais confiável e barato que negação dentro do texto. Quando houver "no alguma-coisa" no `style`, a ferramenta destaca e oferece mover para `excludeStyles` num clique. Ver HISTORY §11.
````

**Texto novo, literal:**

````
O campo de exclusão dedicado é mais confiável e barato que negação dentro do texto. Quando houver "no alguma-coisa" no `style`, a ferramenta destaca e oferece mover para `excludeStyles` num clique. Ver HISTORY §11.

**Entregue em 0.5.0 (DEC-018), so avisando** — mover num clique seria a primeira escrita da ferramenta no acervo e ficou fora por decisao do dono. Deteccao por fronteira de palavra (substring casava pia-no e sopra-no); `no vocals` nao dispara em faixa instrumental (Lyrics sem nenhuma linha de letra).
````

### E4 · i-026 e i-027 depois do i-025 — `meta/IDEAS.md`

**Ancora, literal:**

````
`[nascido do FIX-004, 2026-10-22]` O ciclo baixar→reimportar quebrou por meses sem ninguem notar, e so apareceu porque alguem abriu o app num navegador de verdade. Uma checagem que carregue um acervo, serialize como o `downloadCollection` serializa e reimporte, afirmando igualdade, capturaria a classe inteira — nao so o `_activeModules`. Hoje o `validate.py` valida arquivos parados; isto e o primeiro teste de COMPORTAMENTO do projeto, e exige decidir se entra um harness de navegador (headless) ou se a serializacao e extraida para uma funcao testavel sem DOM. Candidata a analise antes de spec.
````

**Texto novo, literal:**

````
`[nascido do FIX-004, 2026-10-22]` O ciclo baixar→reimportar quebrou por meses sem ninguem notar, e so apareceu porque alguem abriu o app num navegador de verdade. Uma checagem que carregue um acervo, serialize como o `downloadCollection` serializa e reimporte, afirmando igualdade, capturaria a classe inteira — nao so o `_activeModules`. Hoje o `validate.py` valida arquivos parados; isto e o primeiro teste de COMPORTAMENTO do projeto, e exige decidir se entra um harness de navegador (headless) ou se a serializacao e extraida para uma funcao testavel sem DOM. Candidata a analise antes de spec.

### i-026 💡 Sugerir o que cortar quando ha tags demais (Fase 3a.2)
`[nascido da spec do painel, 2026-10-24]` O painel ja avisa quando o Style passa de ~10 tags, mas nao diz QUAIS cortar. O HISTORY §10 traz a ordem de prioridade (genero > clima > instrumento principal > vocal > BPM). Medido: 7 de 7 faixas do album de referencias passam de 10 tags so com os modulos da propria faixa (11 a 18) — o aviso ambar vai acender quase sempre, e aviso que sempre acende vira paisagem. A sugestao e o que transforma o aviso em acao. Exige classificar cada fragmento por camada, o que o recomposto nao carrega hoje: o fragmento do modulo sabe a camada, o do style base nao.

### i-027 💡 O app declarar a propria versao na tela
`[nascido da exploracao de 2026-10-21, candidato C4]` STATUS, CHANGELOG e README dizem a versao; o `app/index.html` publicado nao a declara em lugar nenhum. Consequencia observada: a captura de tela de 2026-10-17 nao permitia saber qual versao estava no ar. Uma linha discreta no rodape (ou no `title`) torna todo print do dono datavel, e um teste pode afirmar que ela bate com o topo do CHANGELOG. Pequeno; candidato a ir junto da proxima WO de codigo.
````

### E5 · a ferramenta nao tem controle de BPM — `README.md`

**Ancora, literal:**

````
- **Uma ferramenta** (`app/index.html`) que lê o acervo, mostra cada canção como um cartão dentro do seu álbum, com botão de copiar por campo, marcação de "já usei", troca modular de estilo/BPM, e export para `.md`.
````

**Texto novo, literal:**

````
- **Uma ferramenta** (`app/index.html`) que lê o acervo, mostra cada canção como um cartão dentro do seu álbum, com botão de copiar por campo, marcação de "já usei", troca modular de estilo, **aviso quando o prompt vai ser truncado ou diluído**, e export para `.md`.
````

### E5 · estado v0.5.0 — `README.md`

**Ancora, literal:**

````
> **Estado:** v0.4.1 — ferramenta em uso. Lê o acervo, copia por campo, troca módulos de estilo e exporta Markdown. Publicada no GitHub Pages. Ver `meta/ROADMAP.md`.
````

**Texto novo, literal:**

````
> **Estado:** v0.5.0 — ferramenta em uso. Lê o acervo, copia por campo, troca módulos de estilo, **mede cada prompt contra os limites do Suno** e exporta Markdown. Publicada no GitHub Pages. Ver `meta/ROADMAP.md`.
````

### E5 · o painel no passo a passo — `README.md`

**Ancora, literal:**

````
4. Ligue/desligue **módulos de estilo** por camada para gerar variações — o Style recompõe ao vivo.
````

**Texto novo, literal:**

````
4. Ligue/desligue **módulos de estilo** por camada para gerar variações — o Style recompõe ao vivo.
5. Leia a linha embaixo de cada campo antes de copiar: **vermelho** = o Suno vai cortar o texto (passou do limite, ele trunca sem avisar); **âmbar** = vai funcionar, mas pior (tags demais, ou negação «no X» que rende mais no campo Exclude).
````

### E5 · renumera o export — `README.md`

**Ancora, literal:**

````
5. Exporte em `.md` (faixa, álbum ou acervo inteiro) se precisar do formato legível.
````

**Texto novo, literal:**

````
6. Exporte em `.md` (faixa, álbum ou acervo inteiro) se precisar do formato legível.
````

## Fora de escopo

- `meta/DECISIONS.md` — nenhuma decisao nova; os registros desta fase ja entraram (DEC-018, FIX-007).
- `meta/HISTORY.md` sobre o Suno v6 — fica anotado no STATUS («Notas de estado»), vai por WO propria.
- `INSTRUCOES-DO-PROJETO.md` — nao muda. A divergencia e do **painel** do Projeto, e e pendencia do dono.
- `app/`, `data/`, `schema/`, `scripts/` — nada de produto muda.
- **Tag de versao no git.** O projeto nao usa tags ate hoje; criar a primeira e decisao do dono.

## Armadilhas desta WO

- **O STATUS e substituido, nao editado.** O `git diff` vai mostrar quase tudo removido; e esperado. A
  checagem 1 (os hashes) e a prova, nao a leitura do diff.
- **Bloco de codigo com quatro crases:** o texto do STATUS e dos blocos contem crases simples e
  triplas no meio. Copie o que esta ENTRE as linhas de quatro crases, sem elas.
- **As notas do IDEAS entram logo apos a linha de corpo de cada ideia**, antes da linha em branco que
  separa da ideia seguinte. A checagem 6 confere a ordem.
- **Fim de linha:** os cinco arquivos sao LF. Se um hash de chegada divergir, rode `file <arquivo>`
  antes de concluir que uma edicao errou.

## Depois de aplicar — conferencia antes do commit

| # | Checagem | Comando | Esperado |
|---|---|---|---|
| 1 | **Os cinco arquivos sao os testados** | `sha1sum meta/STATUS.md meta/CHANGELOG.md meta/ROADMAP.md meta/IDEAS.md README.md` | a coluna **chegada** da tabela do cabecalho, os cinco. **Esta checagem sozinha prova as catorze edicoes.** |
| 2 | Um bloco so de «Ultima conversa» | `grep -c "^## Última conversa" meta/STATUS.md` | `1` (eram 6) |
| 3 | Versao nos tres lugares | `grep -c "0.5.0" meta/STATUS.md`, `grep -c "^## \[0.5.0\]" meta/CHANGELOG.md`, `grep -c "v0.5.0" README.md` | `≥1`, `1`, `1` |
| 4 | O README parou de prometer BPM | `grep -c "estilo/BPM" README.md` | `0` |
| 5 | ROADMAP: 3a concluida, i-020 adiado, 3a.2 aberta | `grep -c "^- ✅" meta/ROADMAP.md` (conte antes e depois) e `grep -c "i-026" meta/ROADMAP.md` | `14` antes, **`17`** depois; e `1` |
| 6 | IDEAS: tres ✅ e duas ideias novas, na ordem | `grep -n "^### i-0\(1[789]\|2[5-7]\)" meta/IDEAS.md` | i-017 ✅, i-018 ✅, i-019 ✅ ... i-025, i-026, i-027, nesta ordem |
| 7 | Nada de produto mudou | `GIT_OPTIONAL_LOCKS=0 git status --short app data schema scripts` | saida **vazia** |
| 8 | Nenhum relatorio `.txt` no repo | `GIT_OPTIONAL_LOCKS=0 git status --short \| grep -c '\.txt'` | `0` |

**Os tres campos de cada passo:** as oito sao rodadas por **quem aplica (o Code)**, na raiz do repo
(`C:\Users\alexk\Tools\cancioneiro\cancioneiro`), em Git Bash. **Chega no ramo?** A checagem 1 cobre os
cinco arquivos inteiros. **Esta e qual pergunta?** «Esta la?». Nao ha roteiro de tela: nada aqui e
renderizado pelo app.

## Relatorio de aplicacao

Grave em `../261027-HHMM-code-cancioneiro-apply-wo0010.txt`, com o `HHMM` de `date +%y%m%d-%H%M` rodado
na hora. Diga o resultado da checagem 1 em primeiro lugar.

**Proximo comando** (ultima linha do relatorio, cru e sozinho):

```
/wrap
```

## Commit

```
git add meta/STATUS.md meta/CHANGELOG.md meta/ROADMAP.md meta/IDEAS.md README.md meta/workorders
```

```
git commit -m "docs: fecha a Fase 3a e a versao 0.5.0" -m "Fase 3a conferida na tela pelo dono. CHANGELOG ganha a 0.5.0, cobrindo tudo que entrou no app desde a 0.4.1: painel de qualidade (DEC-018) e FIX-004 a FIX-007. STATUS reescrito: seis blocos de historico e seis pendencias ja fechadas saem, o que segue verdadeiro fica. ROADMAP e IDEAS marcam i-017 a i-019 como entregues e abrem i-026 (3a.2) e i-027. README deixa de prometer controle de BPM, que nunca existiu."
```

```
git push
```
