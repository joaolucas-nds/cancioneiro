# HISTORY.md — Cancioneiro

> Conhecimento consolidado que não cabe no CONTEXT enxuto. Lido sob demanda.
> Aqui: o conhecimento técnico do Suno que fundamenta o esquema e a ferramenta.
> **Datado e com nível de confiança** — a interface do Suno muda; reconfirme na conta antes de tratar como lei.

---

## Origem deste conhecimento

Duas fontes se somam:
1. **Guia de produção do Cinzeiro-OST** (`GUIA-PRODUCAO__meta-music`, jun/2026) — pesquisa dedicada de um projeto irmão, focada em OST instrumental com loop. Fonte mais confiável porque foi destilada com ceticismo (separou "confirmado" de "relato de comunidade").
2. **Pesquisa de fundação do Cancioneiro** (jul/2026) — atualização sobre o estado atual (Suno v5.5) e sobre o ecossistema de ferramentas concorrentes.

Suno **não publica manual técnico completo e estável**. A maior parte do que circula é wiki de comunidade (suno.wiki, a mais confiável), Help Center oficial (help.suno.com), blog oficial (suno.com/blog) e blogs de criadores (qualidade variável, muitos vendendo curso). Trate como **confirmado** o convergente em várias fontes ou no material oficial; como **relato de comunidade** (cite com cautela) o de fonte única.

---

## 1 · Os dois campos (a base de tudo) — CONFIRMADO

Suno separa dois campos que fazem trabalhos diferentes. Confundir é a causa nº1 de resultado ruim.

- **Style of Music:** o mundo sonoro — gênero, instrumentos, clima, tempo. Texto livre, vírgulas, **sem colchetes**.
- **Lyrics:** estrutura e vocal — colchetes vão aqui. Mesmo instrumental usa este campo (para dizer "não cante" e onde a energia sobe/cai).

Regra: Style define o universo; Lyrics define a arquitetura de tempo dentro dele. **O esquema do Cancioneiro espelha isso** em `style` e `lyrics` como campos separados — e é por isso que rótulo de referência ("ESTILO SUNO", "LETRA") jamais entra no conteúdo copiável.

## 2 · `[Instrumental]` contra vocal-fantasma — RELATO DE COMUNIDADE (consistente)

Instrumental "puro" tende a ganhar voz cantarolando após ~15–20s, mesmo com "no vocals" no Style. A técnica:
- Campo Lyrics: **só** `[Instrumental]`, nada mais.
- Campo Style: descreve o som + `no vocals` como reforço redundante.
- Lógica: dois sinais em camadas diferentes (estrutural + descritivo). Números de "9 em 10" citados por blogs são estimativa, não garantia — mas a lógica é sólida.

## 3 · Tags de estrutura em instrumental — CONFIRMADO (com ressalva de vocabulário)

- **Real:** Suno reconhece `[Intro]`, `[Build]`, `[Breakdown]`, `[Outro]` como marcadores estruturais mesmo sem vocal. Tags com descrição curta (`[Build: percussão entra]`) funcionam melhor que a tag pelada.
- **Não funciona bem:** vocabulário de um gênero aplicado a outro. `[Drop]`/`[Bass Drop]` faz sentido em EDM; não em ambient/orquestral. Use vocabulário **neutro de gênero**.
- **Quando usar:** só em faixas com arco linear (aberturas, stings, finais, fases de boss). Faixas-loop de exploração são circulares — `[Instrumental]` sozinho é o certo.
- **Evitar:** `[Verse]`, `[Chorus]`, `[Hook]`, `[Drop]` fora do gênero apropriado.

## 4 · Limite e ordem de tags — CONFIRMADO

- **As primeiras ~20–30 palavras do Style pesam mais.** Coloque gênero/instrumentação central no começo, detalhe secundário depois.
- **Teto prático:** 1–2 gêneros, 2–4 instrumentos, 1–2 palavras de clima. Tag em excesso é o erro nº1 — o modelo "briga" com instruções conflitantes.
- Fórmula de 7 elementos citada em guias 2026: `[Gênero/Subgênero], [Tempo/Energia/BPM], [Instrumentos-chave], [Estilo vocal], [Produção/Clima], [Modificadores]`. Útil como checklist, não como camisa de força.

## 5 · Estado atual do modelo (jul/2026) — CONFIRMADO parcialmente

- **v5 / v5.5** são os modelos atuais. v5.5 gera **até ~8 min por geração** (antes ~2 min) — muda o cálculo de Extend do guia do Cinzeiro (que assumia ~2 min como base). Para faixas longas, talvez não precise mais estender tanto.
- **Três aditivos oficiais do v5.5** (checados contra anúncio oficial por uma fonte cética): **Voices** (clonar/usar voz própria), **Custom Models** (Pro/Premier, treinar até 3 variantes) e **My Taste** (grátis, aprende preferências).
- **Creative Sliders:** terceiro sistema de controle além de style + meta-tags. Disponibilidade/nome variam.
- **CUIDADO — mito de blog:** muito do que blogs afirmam sobre v5.5 (ex.: "BPM agora é respeitado com precisão", "'instrumental' precisa vir no fim da lista") **não está no material oficial**. Uma fonte confiável checou e desmentiu. Trate esses "truques de versão" como relato de comunidade, não como fato. **BPM continua sendo aproximação**, não comando exato — relevante para o controle de BPM planejado na ferramenta (i-005): a ferramenta ajuda a *escrever* o BPM, não garante obediência.

## 6 · Recursos avançados — relevância para o Cancioneiro

- **Extend + Get Whole Song:** continua uma geração para alongar. "Get Whole Song" junta tudo (sem custo de crédito). Comece a extensão num trecho estável, perto do fim.
- **Persona (voz):** só ajuda faixas com vocal; não faz nada por instrumental puro. Não combina com Extend nem Cover — planeje a ordem.
- **Campo "exclude styles":** existe em camadas avançadas de criação; funciona melhor que escrever "no X" no texto. Base da ideia i-009.
- **Stems / Suno Studio:** exclusivo do Premier; comunidade relata qualidade ruim de separação (artefatos, taxa de sucesso baixa). Para separar stem de verdade, ferramentas externas (Moises, Lalala, iZotope RX) são melhores. Provavelmente irrelevante para o Cancioneiro.

## 7 · Ecossistema de ferramentas (por que o Cancioneiro é diferente) — jul/2026

Já existem ferramentas no nicho: usesuno.com (biblioteca de style prompts + extensão Chrome que aplica prompts na página do Suno, local-first), sunobuilder.com e suno-json-builder (geradores de prompt com export JSON/TXT), sunomanager.com (download em lote da biblioteca do Suno). Isso **valida** a direção (biblioteca de prompts com copy é útil) e **delimita o diferencial**: o Cancioneiro não é um gerador de prompt do zero — é um **organizador do acervo próprio por álbum/bloco, com copy marcável e troca modular de estilo/BPM**. O gerador genérico já está resolvido por terceiros; a organização do acervo curado não.

## 8 · Loop em Audacity (herança do Cinzeiro — só se relevante)

Se o Cancioneiro algum dia lidar com faixas de jogo com loop, o guia do Cinzeiro tem um checklist completo de loop (Zero Crossing para faixas com pulso; crossfade para drones; reverb-tail como fallback; teste de 20–30 repetições; export .ogg q6–7). Fora do escopo atual — está aqui como ponteiro, não como conteúdo ativo.

## Fontes (resumo)

Suno.wiki; help.suno.com; suno.com/blog; guias 2026 de criadores (com ceticismo proporcional à venda de curso); r/SunoAI via resumos secundários; guia de produção do Cinzeiro-OST (jun/2026). Datas de verificação: fev–jul/2026. **A interface muda — reconfirme nomes de botão na sua conta.**
