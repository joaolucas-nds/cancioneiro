# WO 0046 — i-057 decidida (DEC-040) e o registro do handoff

## Cabecalho

> **Tipo:** so registro: DEC-040, IDEAS e STATUS; versionar a spec (pronta) e o log. O app continua 0.21.0.
> **Config sugerida:** Sonnet · `/effort medium` (aplicacao literal por script; muitas edicoes).
> **Pre-requisito:** commit `e13b9d9`, branch `main`, sincronizada com `origin/main`. O `git status --short` mostra exatamente: ` M logs/2026-11-16.md`, ` M meta/specs/261116-varios-json.md` e `?? meta/workorders/261116-wo0046-i-057-decidida-e-handoff.md`.
> **Base:** a decisao do dono sobre os quatro pontos da spec da i-057 (como recomendados) e o pedido de encerrar a conversa por handoff, em 2026-11-16 `[relatado pelo dono]`; o aviso de lido do KCM (cartas 05 a 07). Detalhe no log de 2026-11-16, Conversa 5.
> **Depende de:** `e13b9d9` (WO 0045).
>
> | arquivo | partida (sha1) | chegada (sha1) |
> |---|---|---|
> | `meta/DECISIONS.md` | `74690204b790a7b697d56dded19e94280680f928` | `ece29d3225f9cd18bedf623939ce59c12bfdc912` |
> | `meta/IDEAS.md` | `df2d743273611549e4b490072bb0a53c3b472974` | `3487cb9c4a256f3f88adec614558f7b97577d0d1` |
> | `meta/STATUS.md` | `41aa15ed3deb052627d4734f793c8ba22feb8d3f` | `ec9b6dccac7a8736281ca0f023ebd7e975558fd4` |
> | `logs/2026-11-16.md` | `16ec604c1fb6edee8fa6c4dd57a93031f7166bca` | o mesmo (gravado pelo chat; so versionar) |
> | `meta/specs/261116-varios-json.md` | `fd5793c365a1ccd29588ae3b3f57dad5a0ee45f0` | o mesmo (gravado pelo chat; so versionar) |
>
> **Ancora semantica:** se um trecho-ancora nao bater EXATAMENTE, PARE e reporte.
> **Idempotencia:** antes de cada edicao, procure o texto NOVO INTEIRO; se ja estiver la, PULE e diga no relatorio.
> **Ancoras:** linhas inteiras (uma linha ou um bloco de linhas inteiras), cada uma 1 vez no arquivo no momento da edicao, na ordem abaixo. Toda edicao «substitui a ancora inteira».
> **Âncoras lidas em** (lidas pelo chat NESTE turno, de `e13b9d9` clonado do GitHub e conferido contra o disco do dono — os arquivos versionados com o mesmo sha1; aplicadas em ordem num clone, com a chegada medida):
> - E01 (`meta/DECISIONS.md`, DEC-040): linha `**Consequências:** (+) O que aparece é sempre um acervo do dono. (+) Esquecer tudo é um …`
> - E02 (`meta/IDEAS.md`, i-039: a cópia do KCM): bloco de 4 linhas, começando por `**Leva 2 em prova de campo (2026-11-15):** os rascunhos de 'escrever-letra-suno' e 'conc…`
> - E03 (`meta/IDEAS.md`, i-057 decidida): bloco de 4 linhas, começando por `'[relatado pelo dono, 2026-11-15]' Arrastar mais de um '.json' de uma vez (faixas e álbu…`
> - E04 (`meta/STATUS.md`, última conversa): bloco de 6 linhas, começando por `## Última conversa (2026-11-16, i-029 fechada, spec da i-057, WO 0045)`
> - E05 (`meta/STATUS.md`, backlog para a conversa nova): bloco de 5 linhas, começando por `1. **Responder ao projeto Rainha quando a medição chegar** — o fim de faixa (i-056, núme…`
> **Canal dos meta neste ciclo = CODE:** STATUS, DECISIONS e IDEAS pelo Code (DEC-010); o log e a spec ja estao gravados pelo chat.

---

## 1. Por que

O dono decidiu os quatro pontos da spec da i-057 como recomendados (DEC-040) e pediu para encerrar a conversa do chat. Esta WO registra a decisao, atualiza o STATUS para a conversa nova (o backlog com a 0.22.0 em primeiro) e anota no IDEAS que o KCM copiou o kit do `94235bd`. Tudo o que esta conversa produziu fica commitado; o handoff mora fora do repo.

## Edicao 0 — Conferencia de hash e de arvore

```
sha1sum meta/DECISIONS.md meta/IDEAS.md meta/STATUS.md logs/2026-11-16.md meta/specs/261116-varios-json.md
GIT_OPTIONAL_LOCKS=0 git status --short
```

Todos batem com **partida**; o `git status` mostra exatamente as tres linhas do Pre-requisito. Qualquer outra coisa: **PARE e reporte**.

## Edicoes E01 a E05

Na ordem. Copie o que esta ENTRE as linhas de quatro crases, sem elas. Aplique por script, extraindo os blocos da WO; grave em UTF-8 com LF.

### E01 — DEC-040

**Arquivo:** `meta/DECISIONS.md`

**Ancora:**

````
**Consequências:** (+) O que aparece é sempre um acervo do dono. (+) Esquecer tudo é um gesto, não um por um. (−) Quem abre o Pages pela primeira vez vê a tela vazia; o exemplo fica a dois cliques.
````

**Texto novo (substitui a ancora inteira):**

````
**Consequências:** (+) O que aparece é sempre um acervo do dono. (+) Esquecer tudo é um gesto, não um por um. (−) Quem abre o Pages pela primeira vez vê a tela vazia; o exemplo fica a dois cliques.

## DEC-040 — Importar vários `.json`: uma janela por arquivo, a lateral como zona de «acervo novo»

**Data:** 2026-11-16
**Status:** aceita — implementação pendente (0.22.0)
**Contexto:** O app lê um arquivo por vez (`files[0]`): soltar três importa o primeiro e cala os outros. O dono pediu (i-057, 2026-11-15) escolher por arquivo entre acervo novo e faixas no aberto, e soltar na lateral para guardar direto como acervo. A spec `meta/specs/261116-varios-json.md` trouxe quatro pontos; o dono escolheu os quatro como recomendados em 2026-11-16 `[relatado pelo dono]`.
**Decisão:**
- Um arquivo: nada muda.
- Vários fora da lateral: a janela «Importar N arquivos», uma linha por arquivo (acervo novo, faixas no aberto, pular); **o padrão vem da forma do arquivo** — uma faixa exportada sozinha (1 álbum, 1 faixa) vem em «Faixas», o resto em «Acervo novo»; sem acervo aberto, tudo «Acervo novo». As faixas de todos os arquivos vão para um destino só, com um «Desfazer».
- Depois de guardar vários como acervo novo, **o que estava aberto continua aberto**; sem nenhum aberto, abre o primeiro.
- **A lateral, fora de um álbum, é zona de «acervo novo» direto**, sem janela — **também para um arquivo só**: a zona faz sempre a mesma coisa. Sobre um álbum da lateral, continua «faixas neste álbum».
- O aviso do arraste diz a zona; os botões de importar aceitam vários arquivos.
**Alternativas consideradas:** tudo «Acervo novo» ou tudo «Faixas» como padrão; abrir o último importado; só a janela, sem a lateral como zona; um arquivo na lateral continuar como hoje.
**Consequências:** (+) Vários arquivos num gesto, sem perder nenhum em silêncio. (+) A lateral vira o atalho de guardar. (−) Um arquivo solto na lateral passa a não abrir o acervo (muda o gesto de hoje). (−) O vínculo do «Salvar» de cada arquivo tem de ser pego durante o `drop`.
````

### E02 — i-039: a cópia do KCM

**Arquivo:** `meta/IDEAS.md`

**Ancora:**

````
**Leva 2 em prova de campo (2026-11-15):** os rascunhos de `escrever-letra-suno` e `conceber-album` estão em `meta/specs/261115-kit-v2-leva-2/`, com a spec e os critérios de entrada (P1 a P5). O projeto Rainha os usa no próximo lote de 2 ou 3 faixas e devolve por carta. Mudança desde a análise: a lane comum virou estilo-base fixo com Variety em Off, e a voz sem plano pago vem dele.
**Leva 2 entregue (2026-11-16, WO 0044):** passou nos critérios (carta 05 do projeto Rainha: 3 de 3 sem vermelho, 3 de 3 no orçamento, 2 de 3 aprovadas na escuta); `escrever-letra-suno` e `conceber-album` entram em `kit-musica/skills/`, com o Cover para manter a cantora no gratuito e o modo de canto fora do style-base. A `macetes-suno` §10 troca a hipótese do `[End]` pelo Recortar e a §12 ganha Personalizar e a varinha. Carta 06 ao KCM. O kit v2 está completo.

### i-040 ✅ Curadoria no app: excluir, exportar e importar faixas
````

**Texto novo (substitui a ancora inteira):**

````
**Leva 2 em prova de campo (2026-11-15):** os rascunhos de `escrever-letra-suno` e `conceber-album` estão em `meta/specs/261115-kit-v2-leva-2/`, com a spec e os critérios de entrada (P1 a P5). O projeto Rainha os usa no próximo lote de 2 ou 3 faixas e devolve por carta. Mudança desde a análise: a lane comum virou estilo-base fixo com Variety em Off, e a voz sem plano pago vem dele.
**Leva 2 entregue (2026-11-16, WO 0044):** passou nos critérios (carta 05 do projeto Rainha: 3 de 3 sem vermelho, 3 de 3 no orçamento, 2 de 3 aprovadas na escuta); `escrever-letra-suno` e `conceber-album` entram em `kit-musica/skills/`, com o Cover para manter a cantora no gratuito e o modo de canto fora do style-base. A `macetes-suno` §10 troca a hipótese do `[End]` pelo Recortar e a §12 ganha Personalizar e a varinha. Carta 06 ao KCM. O kit v2 está completo.
**O KCM copiou** do `94235bd` as quatro skills e a Parte 2 do `BLOCO-SUNO.md`, com carimbo (D-183, WO 0174, v1.145.0; aviso de lido de 2026-11-16, `[relatado pelo KCM]`). A linha da §5 da carta 07 entra numa cópia curta depois do `e13b9d9`.

### i-040 ✅ Curadoria no app: excluir, exportar e importar faixas
````

### E03 — i-057 decidida

**Arquivo:** `meta/IDEAS.md`

**Ancora:**

````
`[relatado pelo dono, 2026-11-15]` Arrastar mais de um `.json` de uma vez (faixas e álbuns misturados) abre uma janela que pergunta, por arquivo: importar como **acervo novo** ou como **faixas no acervo e álbum abertos**. Variante do dono: o lugar onde se solta decide — soltar na **lateral esquerda** importa direto, rápido, como acervo separado (vai para «Acervos neste navegador»); soltar na lista importa como faixas. Hoje: um arquivo por vez; soltar sobre um álbum já importa faixas nele (0.16.0). Pede spec (a janela de vários arquivos e as duas zonas).
**Spec em rascunho (2026-11-16):** `meta/specs/261116-varios-json.md`, com quatro pontos para o dono (o padrão de cada linha, qual acervo fica aberto, a lateral como zona e um arquivo na lateral).

### i-058 ✅ Começar vazio: sem acervo de exemplo
````

**Texto novo (substitui a ancora inteira):**

````
`[relatado pelo dono, 2026-11-15]` Arrastar mais de um `.json` de uma vez (faixas e álbuns misturados) abre uma janela que pergunta, por arquivo: importar como **acervo novo** ou como **faixas no acervo e álbum abertos**. Variante do dono: o lugar onde se solta decide — soltar na **lateral esquerda** importa direto, rápido, como acervo separado (vai para «Acervos neste navegador»); soltar na lista importa como faixas. Hoje: um arquivo por vez; soltar sobre um álbum já importa faixas nele (0.16.0). Pede spec (a janela de vários arquivos e as duas zonas).
**Spec em rascunho (2026-11-16):** `meta/specs/261116-varios-json.md`, com quatro pontos para o dono (o padrão de cada linha, qual acervo fica aberto, a lateral como zona e um arquivo na lateral).
**Decidida (2026-11-16, DEC-040):** os quatro pontos da spec como recomendados `[relatado pelo dono]`. Implementação na próxima conversa (0.22.0).

### i-058 ✅ Começar vazio: sem acervo de exemplo
````

### E04 — última conversa

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
## Última conversa (2026-11-16, i-029 fechada, spec da i-057, WO 0045)

- **i-029 fechada sem código** (opção A, decidida pelo dono em 2026-11-16 `[relatado pelo dono]`; análise `meta/analises/261116-ANALISE-palavra-de-andamento.md`): 0 conflitos nos 806 styles; uma linha na `macetes-suno` §5. Carta 07 ao KCM.
- **Spec da i-057 em rascunho** (`meta/specs/261116-varios-json.md`): vários `.json` numa janela, por arquivo «acervo novo» ou «faixas no aberto»; a lateral como zona de «acervo novo» direto; quatro pontos para o dono.
- **A leva 2 entrou no kit** antes disso (`94235bd`, WO 0044, CI verde); o kit v2 está completo.
- **Este bloco substitui o anterior** (0.21.0 conferida, leva 2 no kit). O que ele dizia está em `logs/2026-11-16.md`.
````

**Texto novo (substitui a ancora inteira):**

````
## Última conversa (2026-11-14 a 2026-11-16, 0.20.0 a 0.21.0, kit v2 completo, i-057 decidida; encerrada por handoff)

- **Entregue e conferido nesta conversa do chat:** 0.20.0 (fórmulas de referência, DEC-037) e 0.21.0 (começar vazio, esquecer todos, importação por grupo, DEC-039), as duas conferidas na tela pelo dono `[relatado pelo dono]`; o v6 no kit (Variety em Off, Voices, Letrista); a leva 2 do kit v2 (provada no projeto Rainha); a i-029 fechada sem código. CI verde no `e13b9d9` (run `43877057878`, `[medido pelo Code]`).
- **i-057 decidida** (DEC-040, os quatro pontos como recomendados `[relatado pelo dono, 2026-11-16 10:45]`); a implementação (0.22.0) fica para a conversa nova.
- **O KCM copiou o kit do `94235bd`** (D-183, v1.145.0); a carta 07 entra numa cópia curta depois do `e13b9d9` `[relatado pelo KCM]`.
- **Conversa do chat encerrada** em 2026-11-16 a pedido do dono (pesada); a próxima arranca pelo `../261116-HANDOFF-BRIEF.md`.
- **Este bloco substitui o anterior** (i-029 fechada, spec da i-057, WO 0045). O que ele dizia está em `logs/2026-11-16.md`.
````

### E05 — backlog para a conversa nova

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
1. **Responder ao projeto Rainha quando a medição chegar** — o fim de faixa (i-056, número F-1) e o teste de Voice v6 com Variety em Off; o que for regra vai ao kit e, por carta, ao KCM.
2. **Paleta de módulos do acervo** (i-052) — pede análise; depois dos primeiros projetos.
3. **Kit de música v2 completo** (i-039): a leva 2 entrou no kit pela WO 0044; o KCM copia pela carta 06. Próximo gatilho: o que o projeto Rainha relatar nas próximas faixas.
4. **Antes do recesso:** importar vários `.json` e a lateral como zona de «acervo novo» (i-057, 0.22.0) — spec em rascunho em `meta/specs/261116-varios-json.md`, à espera dos quatro pontos do dono. A i-029 fechou sem código (uma linha na `macetes-suno` §5).
5. **Depois de um recesso:** outras plataformas de música por IA (i-032) e arrastar faixa para outro acervo (i-050).
````

**Texto novo (substitui a ancora inteira):**

````
1. **Importar vários `.json` (i-057, 0.22.0, DEC-040)** — spec `meta/specs/261116-varios-json.md` pronta, os quatro pontos decididos: implementar num clone (chat), testes V1 a V8, WO para o Code. Último item antes do recesso.
2. **Paleta de módulos do acervo** (i-052) — pede análise; depois dos primeiros projetos. Com o estilo-base fixo e o Variety em Off virando a regra, a análise pode concluir que não compensa.
3. **Kit de música v2 completo** (i-039) — próximo gatilho: o que o projeto Rainha relatar das próximas faixas (cartas na pasta deles); o que virar regra vai ao kit e, por carta, ao KCM. Ideias à espera do campo: i-055 (configuração junto da faixa) e i-060 (medir a referência).
4. **Depois de um recesso:** outras plataformas de música por IA (i-032) e arrastar faixa para outro acervo (i-050).
````

## Depois de aplicar — conferencia antes do commit

| # | Checagem | Comando | Esperado |
|---|---|---|---|
| 1 | Os arquivos sao os previstos | `sha1sum meta/DECISIONS.md meta/IDEAS.md meta/STATUS.md logs/2026-11-16.md meta/specs/261116-varios-json.md` | a coluna **chegada** |
| 2 | A decisao | `grep -c '^## DEC-040' meta/DECISIONS.md` | `1` |
| 3 | O backlog para a conversa nova | `grep -c '^1. \*\*Importar vários' meta/STATUS.md` | `1` |
| 4 | Validacao | `python scripts/validate.py; echo "exit=$?"` | `exit=0` |
| 5 | Nada alem do previsto | `GIT_OPTIONAL_LOCKS=0 git status --short --untracked-files=all` | os 5 arquivos da tabela e esta WO |
| 6 | Depois do push: o CI | `gh run list --limit 1`, em laco com `gh run view <id> --json status,conclusion` ate `completed` | `success` |

As checagens 2 a 4 rodaram no clone do chat; no Git Bash, **nao testado**. So doc: o CI roda os testes de sempre.
**Esta e qual pergunta?** A 1 responde «esta la?»; a 5, «nada ficou de fora do commit?».

## Relatorio de aplicacao

Grave em `../AAMMDD-HHMM-code-cancioneiro-apply-wo0046.txt`, com o carimbo de `date +%y%m%d-%H%M` rodado na hora. Checagem 1 em primeiro lugar e o estado final do CI. **Sem `/wrap` depois desta WO**, e sem secao sua no log, salvo se algo fugir do literal.

## Commit

```
git add meta/DECISIONS.md meta/IDEAS.md meta/STATUS.md logs/2026-11-16.md meta/specs/261116-varios-json.md meta/workorders/261116-wo0046-i-057-decidida-e-handoff.md
```

```
git commit -m "docs: i-057 decidida (DEC-040) e registro do handoff de 2026-11-16" -m "Os quatro pontos da spec de importar varios json como recomendados. STATUS para a conversa nova; IDEAS com a copia do KCM; log de 2026-11-16."
```

```
git push
```
