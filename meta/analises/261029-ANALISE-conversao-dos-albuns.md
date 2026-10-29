# ANALISE — Conversão dos álbuns antigos para o esquema (i-008)

> **Status:** Implementada (0.9.1) — decidida pelo dono em 2026-10-29: 1A, 2A, 3A, 4A (ver Desfecho).
> **Data:** 2026-10-29 (data de criação; não muda depois)
> **Ideia de origem:** i-008 («converter os `ALBUM_*.md` e o `album_guia_suno.md` para o esquema, um álbum por
> vez, semi-assistido por chat»), desbloqueada em 2026-10-29 quando o dono trouxe os álbuns para a pasta-pai.
> **Reabre, em parte:** x-001 (parser universal descartado na fundação) — ver Opção A.

## Problema

O acervo do dono está em 19 guias Markdown, cada família com uma convenção, e quase todos com o **rótulo dentro
do bloco copiável** (`[ESTILO SUNO]`, `[LETRA]`) — a mistura que a regra de domínio proíbe e que o Cancioneiro
existe para eliminar. Enquanto não estiver no esquema, o dono copia rolando arquivos de 2 a 10 mil linhas, sem
painel de qualidade, sem módulos, sem marca de «usei». E o painel mostraria o que hoje não aparece: medido abaixo,
**um terço das letras passa do limite em que o Suno corta em silêncio**.

## Restrições / o que foi medido

**Sonda** (`../261029-sonda-albuns.py`, relatório `../261029-SONDA-albuns-antigos.md`, fora do repo; 19 arquivos,
44.083 linhas, 1.038 blocos de código; 0 alarmes na segunda execução, depois de corrigidos dois defeitos do
próprio instrumento — notas `### Sobre BRn-mm` contadas como faixa, e o código `BRV-N01` não reconhecido):

| família | arquivos | faixas (contadas) | forma |
|---|---|---|---|
| **BR — «Rainha da Preguiça»** | VOL1 a VOL10 + índice | **151** (11 + 20 + 8 × 15) | `## <emoji> BRn-mm — GÊNERO` · `### "Título" — voz` · `**Conceito/Voz/Instrumentos:**` · bloco `[ESTILO SUNO]` · bloco `[LETRA]` · bloco com 2 `[ESTILO SUNO — VAR X: rótulo]`. Em **cada** volume, cabeçalhos = blocos de letra = pares de variante. 106 seções «CONVERSA #n» são narrativa, não faixa. |
| Rótulo dentro, outros | `ALBUM_EPICO`, `ALBUM_VOL4`, `ALBUM_VOL5` | ~15 + 25 + 82 | mesmos rótulos, outros códigos (`BR-01`, `CLK-EN-01`), «VARIAÇÃO A»; VOL4 com 23 cabeçalhos para 25 letras; VOL5 com 19 faixas só de tags (instrumentais) |
| Rótulo fora | `ALBUM_VOL6`, `ALBUM_VOL7`, `album_guia_suno` | 18 + 18 + ~11 | `**Style — Opção A:**` antes do bloco; instrumentais com 2 opções de Style |
| Letra fora de bloco | `album_guia_completo` | ~31 (com VERSÃO A/B) | `[Estilo Suno]` no bloco; a letra é Markdown (`**[Verse 1]**`, 247 linhas assim) |
| Outro propósito | `guia_musicas_acao_gemini_suno` | 5 temas | prompts para o Gemini e para o Suno, sincronização com vídeo |

**Protótipo de conversor só da família BR** (no container do chat; VOL1, VOL3 e VOL10, 41 faixas):
- **41 de 41** convertidas; 0 rótulos dentro de `style`/`lyrics`; 2 variantes por faixa; `context` = Conceito,
  `notes` = Voz, Instrumentos, conversa de origem e gênero; `bpm` preenchido em 40 de 41.
- `validate.py` (modo completo): esquema ok; **1 faixa reprova** — br3-07, «95 BPM to 118 BPM» (crescendo de
  propósito; a DEC-020 reprova dois BPM porque o controle os igualaria).
- No app: 41 cartões em 0,84 s; busca em 0,13 s; cópia no navegador 244 KB (151 faixas ≈ 0,9 MB; cabe).
- **Letras: mediana 4.358 caracteres; 15 de 41 acima de 5.000 (o Suno corta em silêncio); 32 acima de 3.000.**
  **Styles: 36 de 41 com mais de 10 tags.** O painel de qualidade marca as 15 em vermelho.

**Outros fatos:** o Pages publica o app; no plano gratuito do GitHub o Pages exige repositório público — tudo
em `data/` é público `[não conferido: o plano da conta]`. Hoje o acervo pessoal mora fora do repo
(`../album-referencias (1).json`). A x-001 apostou em «conversão semi-assistida por chat»: para a família BR
isso pede a um chat reproduzir ~650 KB de letra, faixa a faixa, sem alterar — onde chat resume, corta e
«corrige».

## Opções consideradas

**Decisão 1 — Método.**
- **A (recomendada): conversor determinístico por família, começando pela BR.** Não é o «parser universal» da
  x-001: é um conversor para UMA convenção medida como regular (151 de 151). Copia letra e estilo byte a byte,
  tira os rótulos, e relata o que não entendeu em vez de adivinhar. Versionado em `scripts/` (não contém letra
  nenhuma), com teste sobre uma faixa sintética. As outras famílias decidem-se depois, cada uma com sua medida:
  as pequenas e irregulares podem sair mais baratas à mão ou por chat.
- B: conversão por chat, volume a volume (a premissa da x-001). Descartada para a BR: 15 faixas × ~4.400
  caracteres de letra por volume é exatamente onde chat corta ou parafraseia, e não há como conferir fidelidade
  sem comparar com o original — que é o que o conversor faz de graça.
- C: à mão, no editor. Descartada para 151 faixas; viável para as famílias pequenas.

**Decisão 2 — Onde mora o acervo convertido.**
- **A (recomendada): fora do repositório**, na pasta-pai (ex.: `../acervos/rainha-da-preguica.json`), importado
  no app (e guardado no navegador, DEC-022). Igual ao `album-referencias`. Letra e persona são material do dono;
  publicar é escolha dele, não efeito colateral.
- B: em `data/`, versionado e publicado no Pages. Ganha histórico no Git e acesso de qualquer aparelho; perde a
  privacidade.

**Decisão 3 — Um arquivo ou um por volume.**
- **A (recomendada): um acervo com 11 álbuns (VOL1 a VOL10 + nada do índice).** Uma importação; o filtro de
  álbum separa os volumes. ~0,9 MB.
- B: um arquivo por volume. Mais fácil de regerar um só; obriga a trocar de acervo para mudar de volume.

**Decisão 4 — O que passa do limite do Suno.**
- **A (recomendada): converter fiel e deixar o painel mostrar.** O conversor não decide o que cortar de uma
  letra; 15 de 41 em vermelho é a lista de trabalho, e encurtar é edição (do dono, ou frente futura).
- B: o conversor cortar no limite. Descartada: perde texto em silêncio, o mesmo defeito do Suno.

**Sem decisão do dono (técnico):** `state` = «ideia» em todas (o guia não diz quais foram geradas); as 106
«Conversas» ficam de fora (narrativa); o BPM em faixa («120–130 BPM») e o BPM duplo (br3-07) ficam no texto
como estão, com `bpm` vazio, e o conversor os lista no relatório — a DEC-020 continua valendo para o
`validate.py`; o índice-mestre (fórmulas de estilo) fica para o ⬜ «importar prompts prontos como módulos».

## Recomendação

**1A, 2A, 3A, 4A.** O dado que decide é o tamanho das letras: copiar texto longo sem alterar é trabalho de
máquina, e é o único ponto em que errar não avisa. A família BR é regular o bastante para isso (151 de 151), e
começar por ela entrega metade do acervo com um script pequeno.

## Riscos

- **Faixa fora do molde dentro de um volume regular** (cabeçalho diferente, bloco faltando): o conversor relata
  «sem estilo»/«sem letra» e não inclui a faixa. Sinal: contagem convertida ≠ 151.
- **Rótulo de variante mal lido** («VARIAÇÃO» × «VAR»): o protótipo já aceita os dois; conferir no relatório.
- **Arquivo de 0,9 MB no navegador:** cabe hoje; um segundo acervo grande pode passar dos ~5 MB do `localStorage`
  — a DEC-022 já avisa quando não cabe.
- **Repositório público** se a decisão 2 for B.

## Ponto de decisão

Decisões **1, 2, 3 e 4** (recomendadas **A, A, A, A**). Com elas: o conversor entra em `scripts/` por WO, junto
com a 0.9.1; o dono roda um comando para gerar o acervo dele (o arquivo fica na pasta-pai) e confere na tela.

## Desfecho — 2026-10-29

**Decidido pelo dono: 1A, 2A, 3A, 4A**, e mais: os acervos convertidos são produtos para outros projetos e
álbuns, **não são versionados** neste repo (reforça a 2A). Registrado na DEC-026.

**Implementado (0.9.1):** `scripts/convert_br.py`, com teste em guia sintético (`scripts/test_convert_br.py`, 8
casos). Medido nos dez volumes `[medido por instrumento]`:
- **151 de 151** cabeçalhos viraram faixa; 0 rótulos em `style`/`lyrics`; 2 variantes em cada faixa; nenhuma
  diferença contra o protótipo nos campos copiáveis.
- **Dez álbuns, não onze:** a 3A dizia «11 álbuns (VOL1 a VOL10 + nada do índice)» — são dez volumes; o 11º
  arquivo é o índice, que não vira álbum. Erro de conta desta análise.
- Letras: **72 de 151 acima de 5.000** caracteres, 141 acima de 3.000. Styles: **138 de 151 com mais de 10 tags**.
- BPM: **três** faixas com rampa de andamento de propósito («95 BPM to 118 BPM», br2-09, br3-07, br4-07), não
  uma; ficam com `bpm` vazio e o `validate.py` as reprova (DEC-020) — ver i-042. Nenhum BPM em faixa
  («120–130 BPM») nos dez volumes.
- No app: 151 cartões, sem erro; cópia no navegador ~955 mil caracteres.
- Saída gravada em `../acervos/rainha-da-preguica.json`, fora do repo.

**O que fica:** `Albuns/` (oito arquivos, 172 faixas) espera a aprovação dos grupos (i-038); o índice-mestre segue
para o ⬜ «importar prompts prontos como módulos».
