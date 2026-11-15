# WO 0042 — Leva 2 do kit v2 em prova de campo; ideias i-057 e i-058

## Cabecalho

> **Tipo:** so registro (IDEAS e STATUS) e versionar a spec da leva 2 com os rascunhos. O app nao muda (0.20.0); o kit nao muda.
> **Config sugerida:** Sonnet · `/effort low` (aplicacao literal por script; 5 edicoes).
> **Pre-requisito:** commit `c1648ee`, branch `main`, sincronizada com `origin/main`. O `git status --short` mostra exatamente: ` M logs/2026-11-15.md`, `?? meta/specs/261115-kit-v2-leva-2.md`, `?? meta/specs/261115-kit-v2-leva-2/` e `?? meta/workorders/261115-wo0042-leva-2-em-prova.md`.
> **Base:** frente escolhida pelo dono em 2026-11-15 `[relatado pelo dono]`; a analise `261109-ANALISE-kit-de-musica-v2.md`; o PROJETO, a LETRAS e o FAIXAS do projeto Rainha; a nota `261115-1820` do dono. Detalhe no log de 2026-11-15, Conversa 4.
> **Depende de:** `c1648ee` (WO 0041).
>
> | arquivo | partida (sha1) | chegada (sha1) |
> |---|---|---|
> | `meta/IDEAS.md` | `c7418ee7cbe1288754f18beedd7191a5e1a7a42e` | `bcf3a247632a4ac6c9425aa3473e241ef06415c7` |
> | `meta/STATUS.md` | `3926ee6420cf63d29df4a8e8dabd7b99258c532f` | `73aae846d0bc249784b7ba168c202f54506bb4cb` |
> | `logs/2026-11-15.md` | `eb2c67909a8a5884c0a12b893b3041fed12e7651` | o mesmo (gravado pelo chat; so versionar) |
> | `meta/specs/261115-kit-v2-leva-2.md` | `53a3e02ea7112d6cffe17bd1825a98613c4ac471` | o mesmo (gravado pelo chat; so versionar) |
> | `meta/specs/261115-kit-v2-leva-2/escrever-letra-suno.SKILL.md` | `1410ef369ef74da502536882e744911ed253c4f2` | o mesmo (gravado pelo chat; so versionar) |
> | `meta/specs/261115-kit-v2-leva-2/conceber-album.SKILL.md` | `faa3086f5ee3274612e159b5a19e063d5d1307f3` | o mesmo (gravado pelo chat; so versionar) |
>
> **Ancora semantica:** se um trecho-ancora nao bater EXATAMENTE, PARE e reporte.
> **Idempotencia:** antes de cada edicao, procure o texto NOVO INTEIRO; se ja estiver la, PULE e diga no relatorio.
> **Ancoras:** linhas inteiras (uma linha ou um bloco de linhas inteiras), cada uma 1 vez no arquivo no momento da edicao, na ordem abaixo. Toda edicao «substitui a ancora inteira».
> **Âncoras lidas em** (lidas pelo chat NESTE turno, de `c1648ee` clonado do GitHub e conferido contra o disco do dono — os arquivos versionados com o mesmo sha1; aplicadas em ordem num clone, com a chegada medida):
> - E01 (`meta/IDEAS.md`, i-039: a leva 2 em prova de campo): bloco de 4 linhas, começando por `**Kit v2 (análise 'meta/analises/261109-ANALISE-kit-de-musica-v2.md', decidida pelo dono…`
> - E02 (`meta/IDEAS.md`, i-057 e i-058): bloco de 6 linhas, começando por `### i-056 💡 Conferir o fim da faixa`
> - E03 (`meta/STATUS.md`, última conversa): linha `- **WO 0040 aplicada** ('fb9cd70'); o CI ficou vermelho num teste antigo, por corrida (Q…`
> - E04 (`meta/STATUS.md`, quebrado: nada): linha `- **CI do 'fb9cd70' vermelho em 1 teste antigo** (run '43760238300', 'test_ctrl_z_na_bus…`
> - E05 (`meta/STATUS.md`, backlog: a leva 2 em prova; antes e depois do recesso): bloco de 2 linhas, começando por `3. **Kit de música v2, leva 2** (i-039) — as skills 'escrever-letra-suno' e 'conceber-al…`
> **Canal dos meta neste ciclo = CODE:** STATUS e ROADMAP pelo Code (DEC-010); o log ja esta gravado pelo chat.

---

## 1. Por que

A leva 2 do kit v2 (as skills `escrever-letra-suno` e `conceber-album`) so entra no kit depois de prova de campo (analise de 2026-11-09). O chat escreveu a spec e os rascunhos, agora com o que o projeto Rainha mediu (estilo-base fixo com Variety em Off; as regras de letra da escuta do dono); o projeto Rainha testa no proximo lote. Esta WO registra isso e as duas ideias novas do dono (i-057, i-058), e versiona a spec com os rascunhos.

## Edicao 0 — Conferencia de hash e de arvore

```
sha1sum meta/IDEAS.md meta/STATUS.md logs/2026-11-15.md meta/specs/261115-kit-v2-leva-2.md meta/specs/261115-kit-v2-leva-2/escrever-letra-suno.SKILL.md meta/specs/261115-kit-v2-leva-2/conceber-album.SKILL.md
GIT_OPTIONAL_LOCKS=0 git status --short
```

Todos batem com **partida**; o `git status` mostra exatamente as quatro linhas do Pre-requisito. Qualquer outra coisa: **PARE e reporte**.

## Edicoes E01 a E05

Na ordem. Copie o que esta ENTRE as linhas de quatro crases, sem elas. Aplique por script, extraindo os blocos da WO; grave em UTF-8 com LF.

### E01 — i-039: a leva 2 em prova de campo

**Arquivo:** `meta/IDEAS.md`

**Ancora:**

````
**Kit v2 (análise `meta/analises/261109-ANALISE-kit-de-musica-v2.md`, decidida pelo dono em 2026-11-09):** leva 1 entregue em 2026-11-09 — o README na 0.17.0, a `macetes-suno` com «Depois de ouvir» (§10) e as ferramentas do Suno de 2026 (§11), o ciclo do bloco com elas. Leva 2 (skills `escrever-letra-suno` e `conceber-album`) espera um projeto de música para a prova de campo; a carta 02 ao KCM vai depois dela.
**Carta 03 do KCM (2026-11-14, `../notas-arquivadas/261114-kcm-para-cancioneiro-03-o-suno-no-nicho-musica.md`):** o KCM propõe um eixo «Produção» no nicho Música (análise `261114-ANALISE-musica-gerada-por-ia.md` deles) e copiar o bloco e as skills com carimbo. Respondida pela carta 04 (DEC-038): as duas linhas novas (tags de seção por gênero; direito de uso e nome de artista) nascem no `BLOCO-SUNO.md` (WO 0039); o prompt de faixa não pede fórmulas; nenhum limite mudou desde 31/10. A «carta 02» das linhas acima era o nome provisório da próxima carta; a 02 de fato foi a das chaves no `file://` (2026-11-05), e a próxima, de qualquer lado, é a 05.

### i-040 ✅ Curadoria no app: excluir, exportar e importar faixas
````

**Texto novo (substitui a ancora inteira):**

````
**Kit v2 (análise `meta/analises/261109-ANALISE-kit-de-musica-v2.md`, decidida pelo dono em 2026-11-09):** leva 1 entregue em 2026-11-09 — o README na 0.17.0, a `macetes-suno` com «Depois de ouvir» (§10) e as ferramentas do Suno de 2026 (§11), o ciclo do bloco com elas. Leva 2 (skills `escrever-letra-suno` e `conceber-album`) espera um projeto de música para a prova de campo; a carta 02 ao KCM vai depois dela.
**Carta 03 do KCM (2026-11-14, `../notas-arquivadas/261114-kcm-para-cancioneiro-03-o-suno-no-nicho-musica.md`):** o KCM propõe um eixo «Produção» no nicho Música (análise `261114-ANALISE-musica-gerada-por-ia.md` deles) e copiar o bloco e as skills com carimbo. Respondida pela carta 04 (DEC-038): as duas linhas novas (tags de seção por gênero; direito de uso e nome de artista) nascem no `BLOCO-SUNO.md` (WO 0039); o prompt de faixa não pede fórmulas; nenhum limite mudou desde 31/10. A «carta 02» das linhas acima era o nome provisório da próxima carta; a 02 de fato foi a das chaves no `file://` (2026-11-05), e a próxima, de qualquer lado, é a 05.
**Leva 2 em prova de campo (2026-11-15):** os rascunhos de `escrever-letra-suno` e `conceber-album` estão em `meta/specs/261115-kit-v2-leva-2/`, com a spec e os critérios de entrada (P1 a P5). O projeto Rainha os usa no próximo lote de 2 ou 3 faixas e devolve por carta. Mudança desde a análise: a lane comum virou estilo-base fixo com Variety em Off, e a voz sem plano pago vem dele.

### i-040 ✅ Curadoria no app: excluir, exportar e importar faixas
````

### E02 — i-057 e i-058

**Arquivo:** `meta/IDEAS.md`

**Ancora:**

````
### i-056 💡 Conferir o fim da faixa
`[pedida pela carta 01 do projeto Rainha da Preguiça, 2026-11-15]` O Suno segue tocando 10 a 30 s depois da letra e repete eco final. Pedido: aviso âmbar no painel e na `revisar-faixa` para faixa cantada sem tag de fim (`[End]`, `[Fade Out]`) e última linha igual à anterior. Sem medição de `[End]` × `[Fade Out]` × nada ainda: espera o número F-1 do projeto Rainha antes de virar regra. Por ora, só a hipótese na §10 da `macetes-suno`.

## Feedback para o Kit

- **[2026-07-19] Nicho pediria uma variante "ferramenta+conteúdo".** Este projeto é dev, mas o "produto" é metade código (app) e metade dado curado (acervo JSON). O template de Desenvolvimento cobre bem a parte código; a parte "acervo de dados como entregável" ficou por conta do CONTEXT. Não faltou nada crítico, mas um nicho híbrido "ferramenta que consome conteúdo estruturado" seria útil.
````

**Texto novo (substitui a ancora inteira):**

````
### i-056 💡 Conferir o fim da faixa
`[pedida pela carta 01 do projeto Rainha da Preguiça, 2026-11-15]` O Suno segue tocando 10 a 30 s depois da letra e repete eco final. Pedido: aviso âmbar no painel e na `revisar-faixa` para faixa cantada sem tag de fim (`[End]`, `[Fade Out]`) e última linha igual à anterior. Sem medição de `[End]` × `[Fade Out]` × nada ainda: espera o número F-1 do projeto Rainha antes de virar regra. Por ora, só a hipótese na §10 da `macetes-suno`.

### i-057 💡 Importar vários .json de uma vez, e onde soltar decide o que vira
`[relatado pelo dono, 2026-11-15]` Arrastar mais de um `.json` de uma vez (faixas e álbuns misturados) abre uma janela que pergunta, por arquivo: importar como **acervo novo** ou como **faixas no acervo e álbum abertos**. Variante do dono: o lugar onde se solta decide — soltar na **lateral esquerda** importa direto, rápido, como acervo separado (vai para «Acervos neste navegador»); soltar na lista importa como faixas. Hoje: um arquivo por vez; soltar sobre um álbum já importa faixas nele (0.16.0). Pede spec (a janela de vários arquivos e as duas zonas).

### i-058 💡 Começar vazio: sem acervo de exemplo
`[relatado pelo dono, 2026-11-15]` Sem acervo importado, o app deve abrir **vazio**, e não com o exemplo. Medido em 2026-11-15: `data/exemplo-cinzeiro.json` não é lido pelo app nem pelos testes (só citado em docs) e pode sair; `data/demo.json` é o que o Pages carrega sozinho, o que «Baixar exemplo» entrega e a base dos testes — ele fica no repo, só deixa de abrir sozinho. Mudança pequena no app, mas mexe no `tryAutoLoad` e nos testes que contam com ele.

## Feedback para o Kit

- **[2026-07-19] Nicho pediria uma variante "ferramenta+conteúdo".** Este projeto é dev, mas o "produto" é metade código (app) e metade dado curado (acervo JSON). O template de Desenvolvimento cobre bem a parte código; a parte "acervo de dados como entregável" ficou por conta do CONTEXT. Não faltou nada crítico, mas um nicho híbrido "ferramenta que consome conteúdo estruturado" seria útil.
````

### E03 — última conversa

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
- **WO 0040 aplicada** (`fb9cd70`); o CI ficou vermelho num teste antigo, por corrida (Quebrado, abaixo); a WO 0041 corrige e fecha a Fase 2 no ROADMAP (o marco veio com o projeto Rainha).
````

**Texto novo (substitui a ancora inteira):**

````
- **WO 0040 aplicada** (`fb9cd70`); o CI ficou vermelho num teste antigo, por corrida (Quebrado, abaixo); a WO 0041 corrigiu (`c1648ee`, CI verde, run `43764492829`) e fechou a Fase 2.
- **Leva 2 do kit v2 em prova de campo:** spec e rascunhos em `meta/specs/261115-kit-v2-leva-2/`; carta 02 do Cancioneiro ao projeto Rainha com os rascunhos. Ideias novas do dono: i-057 (vários `.json`, zonas de soltar) e i-058 (começar vazio).
````

### E04 — quebrado: nada

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
- **CI do `fb9cd70` vermelho em 1 teste antigo** (run `43760238300`, `test_ctrl_z_na_busca_nao_mexe_no_acervo`, `[medido pelo Code]`), num commit só de doc: corrida no teste, não no app. A descida devolve o foco à linha no fim, e no CI lento o `Ctrl+Z` chegava antes, fora da busca, e desfazia. O chat reproduziu atrasando a descida em 400 ms: o teste velho reprova com o mesmo 0, o novo passa. A WO 0041 faz o teste esperar a descida.
````

**Texto novo (substitui a ancora inteira):**

````
- **Nada quebrado.** O CI do `fb9cd70` (1 teste por corrida) voltou ao verde no `c1648ee` (run `43764492829`, `[medido pelo Code]`).
````

### E05 — backlog: a leva 2 em prova; antes e depois do recesso

**Arquivo:** `meta/STATUS.md`

**Ancora:**

````
3. **Kit de música v2, leva 2** (i-039) — as skills `escrever-letra-suno` e `conceber-album`, com prova de campo no projeto da Rainha; depois, uma carta ao KCM.
4. **Depois de um recesso:** outras plataformas de música por IA (i-032), palavra de andamento contra o BPM (i-029) e arrastar faixa para outro acervo (i-050).
````

**Texto novo (substitui a ancora inteira):**

````
3. **Kit de música v2, leva 2** (i-039) — **em prova de campo** desde 2026-11-15: rascunhos e critérios em `meta/specs/261115-kit-v2-leva-2.md`; o projeto Rainha usa no próximo lote e devolve por carta. Passando, WO para o kit e carta ao KCM.
4. **Antes do recesso, quando der** (pedido do dono em 2026-11-15): marcar e desmarcar por origem na importação (i-053), o texto da janela de importar quando só há fórmulas, começar vazio (i-058) e a palavra de andamento contra o BPM (i-029, que pede uma tabela com fonte antes do código). Importar vários `.json` e as zonas de soltar (i-057) pedem spec.
5. **Depois de um recesso:** outras plataformas de música por IA (i-032) e arrastar faixa para outro acervo (i-050).
````

## Depois de aplicar — conferencia antes do commit

| # | Checagem | Comando | Esperado |
|---|---|---|---|
| 1 | Os arquivos sao os previstos | `sha1sum meta/IDEAS.md meta/STATUS.md logs/2026-11-15.md meta/specs/261115-kit-v2-leva-2.md meta/specs/261115-kit-v2-leva-2/escrever-letra-suno.SKILL.md meta/specs/261115-kit-v2-leva-2/conceber-album.SKILL.md` | a coluna **chegada** |
| 2 | As ideias novas | `grep -c '^### i-05[78] ' meta/IDEAS.md` | `2` |
| 3 | Os rascunhos fora do kit | `ls kit-musica/skills` | so `macetes-suno` e `revisar-faixa` |
| 4 | Validacao | `python scripts/validate.py; echo "exit=$?"` | `exit=0` |
| 5 | Nada alem do previsto | `GIT_OPTIONAL_LOCKS=0 git status --short --untracked-files=all` | os 6 arquivos da tabela e esta WO |
| 6 | Depois do push: o CI | `gh run list --limit 1`, em laco com `gh run view <id> --json status,conclusion` ate `completed` | `success`; se vermelho, o passo e as ultimas 30 linhas de `gh run view <id> --log-failed` |

As checagens 2 a 4 rodaram no clone do chat; no Git Bash, **nao testado**. So doc: o CI roda os testes de sempre, sem mudanca esperada.
**Esta e qual pergunta?** A 1 responde «esta la?»; a 3, «os rascunhos ficaram fora do kit?».

## Relatorio de aplicacao

Grave em `../AAMMDD-HHMM-code-cancioneiro-apply-wo0042.txt`, com o carimbo de `date +%y%m%d-%H%M` rodado na hora. Checagem 1 em primeiro lugar e o estado final do CI. **Sem `/wrap` depois desta WO**, e sem secao sua no log, salvo se algo fugir do literal.

## Commit

```
git add meta/IDEAS.md meta/STATUS.md logs/2026-11-15.md meta/specs/261115-kit-v2-leva-2.md meta/specs/261115-kit-v2-leva-2/escrever-letra-suno.SKILL.md meta/specs/261115-kit-v2-leva-2/conceber-album.SKILL.md meta/workorders/261115-wo0042-leva-2-em-prova.md
```

```
git commit -m "docs: leva 2 do kit v2 em prova de campo; ideias i-057 e i-058" -m "Spec e rascunhos de escrever-letra-suno e conceber-album, fora do kit ate a prova no projeto Rainha. IDEAS e STATUS com as ideias do dono e a ordem antes do recesso."
```

```
git push
```
