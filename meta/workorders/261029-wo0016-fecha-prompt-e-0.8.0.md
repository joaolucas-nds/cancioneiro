# WO 0016 — Fecha o prompt-modelo e a versao 0.8.0

## Cabecalho

> **Tipo:** WO de registro, com uma linha de codigo (a versao no cabecalho do app).
> **Config sugerida:** Sonnet · `/effort low`. 14 edicoes literais, o STATUS inteiro e um arquivo novo (o log do dia), todos aplicados e validados pelo chat numa copia; cada arquivo tem hash de chegada.
> **Pre-requisito:** commit `848e06c`, branch `main`, sincronizada com `origin/main`, **arvore limpa** (so esta WO aparece como `??`).
> **Base:** o reteste do prompt e a conferencia na tela, relatados pelo dono em 2026-10-29 e medidos pelo chat; a nota do dono `261029-1106.txt`.
> **Depende de:** WO 0015, ja aplicada (`8bbe6c1`, wrap `848e06c`).
>
> **Arquivos — partida e chegada, os dois medidos pelo chat** (chegada = resultado de aplicar literalmente as edicoes abaixo, em LF):
>
> | arquivo | partida (sha1) | chegada (sha1) |
> |---|---|---|
> | `app/index.html` | `0146443aad808e7841cc00eba932737d5545107d` | `73e4a54f04ec58cb943587d446501313c9f784e7` |
> | `meta/CHANGELOG.md` | `18220f5002866f6a70a450fcd95fd3aa78d45e8b` | `4767d2881de9b00b1aa1046837d37e43da92a5e2` |
> | `README.md` | `8da6d6119ef0f55f01a1f8d2be66d1f20ef0a42e` | `20c86a70f962ae898fae5b70dd38a079ddf06c77` |
> | `meta/CONTEXT.md` | `fb95d2a1e94e5663c596f302a0cc225745447aa2` | `0fd7bde03dbaf91dc0792f31a64e9d4e53f49cf2` |
> | `meta/HISTORY.md` | `f04af0c5081f4546995620456b14faae00a7ea23` | `72a018d000b8817254ddcf2b5777a07f70a90ecc` |
> | `meta/IDEAS.md` | `ea72e3729f2e6c25c559aa39caf772996db3bfa9` | `3486e8d99fff4ef65aa44f91427f0016b74bdcc0` |
> | `meta/ROADMAP.md` | `4f40aced89a9661c485e27b99fcb4824aeba716b` | `49b78278bec2e094334e66176a1d93a740975998` |
> | `meta/specs/261028-prompt-modelo-e-modulos.md` | `b6d6823bcc3aadbb1079ef8399ded91feefe3162` | `8b4ab2fa341698b002433931500280dd103fb87a` |
> | `meta/STATUS.md` | `c4f333ac660f82b744b7cbfa02098fbdfefc7f2e` | `fd21dbdfc108a069ea79c1ff0ab9de2528aba4f7` |
> | `logs/2026-10-29.md` | (nao existe) | `f0accfb697df6787fc588df20aeadca3d5941dc5` |
>
> **Ancora semantica:** se um trecho-ancora nao bater EXATAMENTE, PARE e reporte.
> **Idempotencia:** antes de cada edicao, procure o texto NOVO INTEIRO; se ja estiver la, PULE e diga no relatorio.
>
> **Ancoras lidas em:** cada ancora foi extraida pelo chat do arquivo de partida (`git show 848e06c:<arquivo>`, igual ao disco do dono pelos hashes acima, medidos em 2026-10-29) e conferida como ocorrendo **exatamente 1 vez** no estado em que a edicao e aplicada, na ordem abaixo.

---

## 1. Por que

A WO 0015 abriu a frente do prompt-modelo; faltavam a tela e o reteste. Os dois vieram em 2026-10-29:

- **Na tela** `[relatado pelo dono]`: itens A1 a A5 ok, visiveis tambem nas capturas (os cinco botoes; o toast
  «18 modulo(s) citado(s)…»).
- **Reteste** (dois chats; o terceiro nao veio), medido pelo chat: 6 de 6 faixas dentro do contrato de modulo e
  do orcamento (base 7-8 tags, recomposto 8-10), 0 rotulos, `validate.py` verde nos dois modos, 10 e 15 chips
  no app. Tabela na spec. A frente fecha com n = 2, dito na spec.

Esta WO fecha a **0.8.0** (app, CHANGELOG, README, STATUS — o `validate.py` confere os quatro), marca i-028,
i-031 e o ROADMAP, poe os botoes no CONTEXT, e registra o que a conversa achou:

- **HISTORY §5 e §6:** a interface do Suno v6 vista nas capturas do dono — v6-mini no plano gratuito, ordem do
  formulario e **nenhum campo de Exclude** nele.
- **IDEAS:** a nota do dono `261029-1106.txt` (i-030 refinada; i-033 copiar o titulo, i-034 arrastar o .json,
  i-035 o acervo sobreviver ao fechar o navegador, i-036 o prompt entregar arquivo) e a i-037: o export de
  album e de acervo sai com o `style` base, o de faixa com o recomposto — desde a 0.4.0, sem estar escrito.
- **STATUS:** a linha que dizia «Export MD (faixa / album / acervo), com o Style recomposto» estava errada
  para dois dos tres; corrigida.

**Codigo:** so a versao (`v0.7.0` → `v0.8.0`). Nenhuma DEC ou FIX nova.

## Edicao 0 — Conferencia de hash e de arvore

```
sha1sum app/index.html meta/CHANGELOG.md README.md meta/CONTEXT.md meta/HISTORY.md meta/IDEAS.md meta/ROADMAP.md meta/specs/261028-prompt-modelo-e-modulos.md meta/STATUS.md
ls logs/2026-10-29.md
GIT_OPTIONAL_LOCKS=0 git status --short
```

Os nove batem com a coluna **partida**; `logs/2026-10-29.md` **nao existe** (o `ls` falha); e o `git status`
mostra **so** esta WO. Qualquer outra coisa: **PARE e reporte**.

## Edicoes E01 a E14

Na ordem. Copie o que esta ENTRE as linhas de quatro crases, sem elas. **O bloco termina na linha de quatro
crases, nunca num titulo:** varios blocos trazem linhas que comecam com `## ` ou `### `.

### E01 — versao no cabecalho (1) — `app/index.html`

**Ancora, literal:**

````
         que app, CHANGELOG, README e STATUS dizem a mesma (i-027). -->
    <span class="sub">acervo de canções · copiar para o Suno sem procurar · <span data-role="app-version">v0.7.0</span></span>
  </div>
````

**Texto novo, literal:**

````
         que app, CHANGELOG, README e STATUS dizem a mesma (i-027). -->
    <span class="sub">acervo de canções · copiar para o Suno sem procurar · <span data-role="app-version">v0.8.0</span></span>
  </div>
````

### E02 — [0.8.0] no topo (1) — `meta/CHANGELOG.md`

**Ancora, literal:**

````
> Histórico de versões entregues. SemVer + Keep a Changelog. Cresce no topo.

````

**Texto novo, literal:**

````
> Histórico de versões entregues. SemVer + Keep a Changelog. Cresce no topo.

---

## [0.8.0] — 2026-10-29

Prompt-modelo com contrato de modulos e o prompt pela interface do app, conferidos na tela e retestados pelo dono.

### Added
- **Botoes «Prompt para chats» e «Baixar exemplo» (DEC-021, i-031):** a janela do primeiro recebe o «Meu pedido» e copia o prompt-modelo inteiro com o pedido no lugar; o segundo baixa `cancioneiro-exemplo.json`. Os dois buscam `schema/PROMPT-PARA-CHATS.md` e `data/demo.json` no clique — o app nao guarda copia; falhando a busca, a janela mostra o link da versao publicada.
- **`scripts/validate.py` confere o prompt (sexta checagem):** reprova se sumirem as marcacoes que o botao le (`--- INÍCIO ---`, `--- FIM ---` e a linha entre parenteses abaixo de `## Meu pedido`).

### Changed
- **Prompt-modelo (DEC-021, i-028):** ensina o contrato de modulo da DEC-016 (modulos no `styleModules` da colecao com `id`, `category`, `label`, `fragment`, `notes`; a faixa cita ids; citado = ligado), o orcamento (style com 6 a 8 tags; ate 10 com os modulos ligados) e que BPM em modulo so vai na camada `tempo`. Reteste do dono com dois chats: 6 de 6 faixas dentro do orcamento, 0 modulos fora do contrato, 0 rotulos — contra 0 de 3 chats no contrato antes.
- **Toast:** dura conforme o tamanho da mensagem (2,2 a 6 s), para os avisos longos darem tempo de ler.

### Fixed
- **FIX-009:** modulo declarado dentro da faixa sumia em silencio no app (painel com 0 chips) e derrubava o `validate.py` com traceback. Agora o validador reprova com mensagem por item, e a importacao — por arquivo ou pela carga automatica — diz quantos modulos citados nao existem na colecao.

````

### E03 — estado e como gerar com um chat (1) — `README.md`

**Ancora, literal:**

````

> **Estado:** v0.7.0 — ferramenta em uso. Lê o acervo, copia por campo, troca módulos de estilo, ajusta o BPM, **mede cada prompt contra os limites do Suno** e exporta Markdown. Publicada no GitHub Pages. Ver `meta/ROADMAP.md`.

````

**Texto novo, literal:**

````

> **Estado:** v0.8.0 — ferramenta em uso. Lê o acervo, copia por campo, troca módulos de estilo, ajusta o BPM, **mede cada prompt contra os limites do Suno**, exporta Markdown e **entrega o prompt para chats gerarem canções no esquema**. Publicada no GitHub Pages. Ver `meta/ROADMAP.md`.

````

### E04 — estado e como gerar com um chat (2) — `README.md`

**Ancora, literal:**

````

Cole o conteúdo de `schema/PROMPT-PARA-CHATS.md` num chat de IA junto do seu pedido — ele devolve JSON já no esquema, pronto para importar.

````

**Texto novo, literal:**

````

No app, clique em **Prompt para chats**, escreva o seu pedido e copie: o prompt vai inteiro, com o pedido no lugar. Cole num chat novo e importe o JSON que ele devolver. O texto do prompt vive em `schema/PROMPT-PARA-CHATS.md` — o botão busca esse arquivo a cada clique, então o que está no repositório é o que você copia.

**Baixar exemplo** baixa um acervo pronto (`data/demo.json`) para ver a estrutura.

````

### E05 — os botoes no que a ferramenta e (1) — `meta/CONTEXT.md`

**Ancora, literal:**

````

2. **A ferramenta (app/) — o leitor.** Um `index.html` autônomo (v0 já construído) que importa/carrega um JSON no esquema, renderiza cada canção como um cartão organizado por álbum, e oferece copy-por-campo com marcação de "já copiado"/"usei", troca modular de estilo por camada (recompõe o Style ao vivo), filtros e busca, import/download de JSON e export MD seletivo (faixa, álbum ou acervo). **Roda de dois modos** (ver DEC-006): servida por GitHub Pages (`https://`) ela carrega o acervo sozinha; aberta como arquivo local (`file://`) ela espera import manual — auto-detecta o ambiente.

````

**Texto novo, literal:**

````

2. **A ferramenta (app/) — o leitor.** Um `index.html` autônomo (v0 já construído) que importa/carrega um JSON no esquema, renderiza cada canção como um cartão organizado por álbum, e oferece copy-por-campo com marcação de "já copiado"/"usei", troca modular de estilo por camada (recompõe o Style ao vivo), filtros e busca, import/download de JSON, export MD seletivo (faixa, álbum ou acervo) e, pelos botões do cabeçalho, o prompt-modelo para chats (com o pedido do usuário) e um acervo de exemplo — buscados do repositório no clique, sem cópia no app (DEC-021). **Roda de dois modos** (ver DEC-006): servida por GitHub Pages (`https://`) ela carrega o acervo sozinha; aberta como arquivo local (`file://`) ela espera import manual — auto-detecta o ambiente.

````

### E06 — os botoes no que a ferramenta e (2) — `meta/CONTEXT.md`

**Ancora, literal:**

````

Ferramenta pessoal de hobby. Uso típico: abrir `index.html`, importar o JSON do acervo, escolher um álbum, copiar o style de uma faixa (botão), copiar a letra (botão), gerar no Suno, marcar a faixa como usada. Para levar uma seleção a um chat ou Projeto, exportar em `.md`.
````

**Texto novo, literal:**

````

Ferramenta pessoal de hobby. Uso típico: abrir `index.html`, importar o JSON do acervo, escolher um álbum, copiar o style de uma faixa (botão), copiar a letra (botão), gerar no Suno, marcar a faixa como usada. Para levar uma seleção a um chat ou Projeto, exportar em `.md`. Para gerar canções novas: «Prompt para chats» → colar num chat novo → importar o JSON que ele devolver.
````

### E07 — a interface do v6 e o Exclude (1) — `meta/HISTORY.md`

**Ancora, literal:**

````
- **BPM no v6 (conferido em 2026-10-28):** a nota oficial do v6 (2026-09-09) não fala de tempo, e o help center oficial só documenta BPM no **Studio** («Transport controls»: Tempo padrão 120, «Follow Track» ou «Manual Tempo»). Na criação, o BPM continua indo como **texto no Style**. Não confirmado: um guia secundário de 2026 diz que o slider **Variety** acima de 0 pode reescrever as tags do Style (testado no v5) — se valer para o BPM, Variety 0 é a condição para o número do controle chegar intacto. Fontes na spec `meta/specs/261028-controle-de-bpm.md`.

````

**Texto novo, literal:**

````
- **BPM no v6 (conferido em 2026-10-28):** a nota oficial do v6 (2026-09-09) não fala de tempo, e o help center oficial só documenta BPM no **Studio** («Transport controls»: Tempo padrão 120, «Follow Track» ou «Manual Tempo»). Na criação, o BPM continua indo como **texto no Style**. Não confirmado: um guia secundário de 2026 diz que o slider **Variety** acima de 0 pode reescrever as tags do Style (testado no v5) — se valer para o BPM, Variety 0 é a condição para o número do controle chegar intacto. Fontes na spec `meta/specs/261028-controle-de-bpm.md`.
- **Interface do v6 na conta gratuita (capturas do dono, 2026-10-29) — MEDIDO na conta.** Modelos: **v6-mini** no plano gratuito; **v6** e **v6-wild** só no Pro e no Premier. Formulário **Advanced**, de cima para baixo: **Lyrics** (com «Add a bridge») → **Styles** (com sugestões de tag e o botão de varinha «Personalize style prompt to match your taste») → **More Options** (Vocal Gender, Duration, Max Mode, Weirdness 50%, Style Influence 50%, Variety, Personalize/My Taste) → **título da faixa** → «Save to» (workspace). **Nenhum campo de Exclude** nesse formulário. Plano gratuito: 50 créditos/dia, sem download mensal, sem direitos comerciais; Voices, Inspire, Add vocals/instrumental e Custom Models bloqueados. Aba **Speech** (beta) separada de Songs. Não confirmado: se o botão de varinha ligado reescreve o Style colado — a lista de faixas geradas mostrou um Style diferente do colado.

````

### E08 — a interface do v6 e o Exclude (2) — `meta/HISTORY.md`

**Ancora, literal:**

````
- **Persona (voz):** só ajuda faixas com vocal; não faz nada por instrumental puro. Não combina com Extend nem Cover — planeje a ordem.
- **Campo "exclude styles":** existe em camadas avançadas de criação; funciona melhor que escrever "no X" no texto. Base da ideia i-009.
- **Stems / Suno Studio:** exclusivo do Premier; comunidade relata qualidade ruim de separação (artefatos, taxa de sucesso baixa). Para separar stem de verdade, ferramentas externas (Moises, Lalala, iZotope RX) são melhores. Provavelmente irrelevante para o Cancioneiro.
````

**Texto novo, literal:**

````
- **Persona (voz):** só ajuda faixas com vocal; não faz nada por instrumental puro. Não combina com Extend nem Cover — planeje a ordem.
- **Campo "exclude styles":** existe em camadas avançadas de criação; funciona melhor que escrever "no X" no texto. Base da ideia i-009. **No v6-mini gratuito (2026-10-29) o formulário não mostra o campo** (§5); um guia secundário de 2026-10-19 diz que ele fica em «Advanced Options → Exclude» «onde o controle estiver disponível», sem dizer em quais planos ou modelos.
- **Stems / Suno Studio:** exclusivo do Premier; comunidade relata qualidade ruim de separação (artefatos, taxa de sucesso baixa). Para separar stem de verdade, ferramentas externas (Moises, Lalala, iZotope RX) são melhores. Provavelmente irrelevante para o Cancioneiro.
````

### E09 — i-028 e i-031 entregues; i-030 refinada; i-033 a i-037 (1) — `meta/IDEAS.md`

**Ancora, literal:**

````

### i-028 🔨 O prompt-modelo pedir folga para os modulos
`[nascido da spec da 3a.2, 2026-10-27]` Em ar-01 e ar-04 o style base que o chat escreveu ja usa 10 de 10 tags: nenhum modulo cabe sem estourar. O painel agora diz isso, mas so depois. A regra que o evitaria mora em quem escreve o base — o `schema/PROMPT-PARA-CHATS.md` poderia pedir «style base com 6 a 8 tags, deixando folga para os modulos». Pesar contra: o base mais curto pode ficar vago (abaixo de 4 tags o painel ja avisa).
**Em trabalho (2026-10-28, DEC-021, WO 0015).** O teste base do prompt (tres chats, `meta/specs/261028-prompt-modelo-e-modulos.md`) confirmou o base no limite (10+ tags em 5 de 9 faixas) e mostrou um problema maior: o prompt nao ensinava o contrato de modulo, e os tres chats inventaram tres formatos. O prompt agora pede style com 6 a 8 tags e ate 10 com os modulos ligados. Fecha com o reteste do dono.

````

**Texto novo, literal:**

````

### i-028 ✅ O prompt-modelo pedir folga para os modulos
`[nascido da spec da 3a.2, 2026-10-27]` Em ar-01 e ar-04 o style base que o chat escreveu ja usa 10 de 10 tags: nenhum modulo cabe sem estourar. O painel agora diz isso, mas so depois. A regra que o evitaria mora em quem escreve o base — o `schema/PROMPT-PARA-CHATS.md` poderia pedir «style base com 6 a 8 tags, deixando folga para os modulos». Pesar contra: o base mais curto pode ficar vago (abaixo de 4 tags o painel ja avisa).
**Em trabalho (2026-10-28, DEC-021, WO 0015).** O teste base do prompt (tres chats, `meta/specs/261028-prompt-modelo-e-modulos.md`) confirmou o base no limite (10+ tags em 5 de 9 faixas) e mostrou um problema maior: o prompt nao ensinava o contrato de modulo, e os tres chats inventaram tres formatos. O prompt agora pede style com 6 a 8 tags e ate 10 com os modulos ligados. Fecha com o reteste do dono.
**Entregue em 0.8.0.** Reteste (2026-10-29, dois chats): base com 7 ou 8 tags e recomposto com 8 a 10 em 6 de 6 faixas.

````

### E10 — i-028 e i-031 entregues; i-030 refinada; i-033 a i-037 (2) — `meta/IDEAS.md`

**Ancora, literal:**

````
`[relatado pelo dono, 2026-10-28]` O cartao mostra Style em cima e Lyrics embaixo; no Suno e o contrario, e copiar na ordem da tela agilizaria. O dono prefere que seja **configuravel**. A preferencia e estado de interface e pode morar no navegador (DEC-004). A decidir na spec: se o export MD segue a ordem escolhida, e onde fica o controle (cabecalho ou cartao).

### i-031 🔨 Prompt e exemplo pela interface do app
`[relatado pelo dono, 2026-10-28, notas 1813 e 1852]` O dono nao quer abrir as pastas do repositorio para pegar o prompt-modelo ou um exemplo: quer copiar o prompt ja com o «Meu pedido» e baixar um exemplo pelo app publicado, como o KCM faz. **Em trabalho (DEC-021, WO 0015):** botoes «Prompt para chats» e «Baixar exemplo», que buscam `schema/PROMPT-PARA-CHATS.md` e `data/demo.json` no clique — fonte unica, sem copia no app. Evolucao possivel: campos guiados para «estruturar» o pedido (quantidade, idioma, instrumental, BPM), so se o reteste mostrar que o texto livre nao basta.

````

**Texto novo, literal:**

````
`[relatado pelo dono, 2026-10-28]` O cartao mostra Style em cima e Lyrics embaixo; no Suno e o contrario, e copiar na ordem da tela agilizaria. O dono prefere que seja **configuravel**. A preferencia e estado de interface e pode morar no navegador (DEC-004). A decidir na spec: se o export MD segue a ordem escolhida, e onde fica o controle (cabecalho ou cartao).
`[relatado pelo dono, 2026-10-29, nota 1106]` **Refinado:** a ordem atual (titulo, Style, Lyrics) faz sentido para quem preenche o Suno de baixo para cima — o dono faz assim. O pedido e **controlar a estrutura na interface e salvar no navegador**, com a ordem atual como padrao. Medido nas capturas do dono (2026-10-29): o formulario do v6 e, de cima para baixo, Lyrics → Styles → opcoes → titulo, e **nao tem campo de Exclude** no v6-mini gratuito — o bloco Exclude do cartao fica sem destino para ele hoje. Candidato: mostrar/ocultar cada campo, alem da ordem.

### i-031 ✅ Prompt e exemplo pela interface do app
`[relatado pelo dono, 2026-10-28, notas 1813 e 1852]` O dono nao quer abrir as pastas do repositorio para pegar o prompt-modelo ou um exemplo: quer copiar o prompt ja com o «Meu pedido» e baixar um exemplo pelo app publicado, como o KCM faz. **Em trabalho (DEC-021, WO 0015):** botoes «Prompt para chats» e «Baixar exemplo», que buscam `schema/PROMPT-PARA-CHATS.md` e `data/demo.json` no clique — fonte unica, sem copia no app. Evolucao possivel: campos guiados para «estruturar» o pedido (quantidade, idioma, instrumental, BPM), so se o reteste mostrar que o texto livre nao basta.
**Entregue em 0.8.0**, conferido na tela pelo dono. O reteste com texto livre passou em 6 de 6 faixas: os campos guiados nao sao necessarios por ora.

````

### E11 — i-028 e i-031 entregues; i-030 refinada; i-033 a i-037 (3) — `meta/IDEAS.md`

**Ancora, literal:**

````
`[relatado pelo dono, 2026-10-28]` Existem outros sites e apps de celular com estrutura parecida com a do Suno e diferente dela; o dono quer sugestoes para testar e, se valer, ampliar a estrutura do projeto para comporta-los. O esquema ja e agnostico no nome (`targetTool`), mas `style`/`lyrics`/`excludeStyles` espelham os campos do Suno. Proximo passo: um turno de pesquisa atual (plano gratuito, campos equivalentes, limites, API, app mobile) antes de qualquer mudanca de esquema. Pesar contra: generalizar o esquema antes de usar uma segunda plataforma de verdade e especular.

````

**Texto novo, literal:**

````
`[relatado pelo dono, 2026-10-28]` Existem outros sites e apps de celular com estrutura parecida com a do Suno e diferente dela; o dono quer sugestoes para testar e, se valer, ampliar a estrutura do projeto para comporta-los. O esquema ja e agnostico no nome (`targetTool`), mas `style`/`lyrics`/`excludeStyles` espelham os campos do Suno. Proximo passo: um turno de pesquisa atual (plano gratuito, campos equivalentes, limites, API, app mobile) antes de qualquer mudanca de esquema. Pesar contra: generalizar o esquema antes de usar uma segunda plataforma de verdade e especular.

### i-033 💡 Copiar o titulo da faixa com um clique
`[relatado pelo dono, 2026-10-29, nota 1106]` Faltou copiar facil o nome da musica. O formulario do v6 tem campo de titulo (o ultimo, antes de «Save to»). Um botao «copiar» ao lado do titulo do cartao, com a mesma marcacao de copiado dos outros campos.

### i-034 💡 Arrastar o .json para a tela e carregar
`[relatado pelo dono, 2026-10-29, nota 1106]` Soltar o arquivo em qualquer lugar da pagina = importar, pelo mesmo caminho do botao (saneamento e avisos iguais: FIX-006, FIX-009). Combina com o prompt que entrega arquivo (i-036): baixar do chat e arrastar para o app.

### i-035 💡 O acervo continuar carregado depois de fechar o navegador
`[relatado pelo dono, 2026-10-29, nota 1106]` Hoje so as marcas «usei» sobrevivem; o acervo some ao fechar. Guardar uma copia do ultimo acervo importado no navegador e recarrega-la ao abrir. **Toca a DEC-004** (o navegador e cache, nunca fonte): uma copia do ultimo arquivo importado e cache legitimo, porque o app nao edita o acervo (FIX-004) — a copia e igual ao arquivo. Risco a tratar: o arquivo mudar fora (um chat gerou versao nova) e o app seguir mostrando a copia velha sem aviso; mitigacao: dizer na tela de onde veio o acervo e quando foi importado, e um botao para esquecer a copia. A carga automatica do Pages (`demo.json`) passa a valer so quando nao houver copia. Pede DEC propria.

### i-036 💡 O prompt pedir o JSON como arquivo para baixar
`[relatado pelo dono, 2026-10-29, nota 1106]` Em vez de texto para copiar, o chat entregar um `.json` para download. Ganha: sem colar no Bloco de notas, sem erro de codificacao, nome de arquivo pronto — e casa com a i-034. Custa: depende de o chat conseguir criar arquivo (varia por produto e por recurso ligado), e o texto atual do prompt foi o que passou no reteste de 2026-10-29 — mudar exige retestar. Forma candidata: pedir arquivo **se o chat puder criar arquivos**, e manter «so o JSON, sem texto» como alternativa.

### i-037 💡 Export de album e de acervo com o Style da tela
Achado em 2026-10-29 nos `.md` que o dono exportou: o export de **faixa** sai com o Style recomposto (modulos ligados, controle de BPM), o de **album** e o de **acervo** saem com o `style` base (`albumToMarkdown` chama `songToMarkdown(s, false)`), desde a 0.4.0. Em ar-01, 18 tags na faixa e 10 no album. Pode ser o certo — o album como documento do acervo, a faixa como «o que vou colar agora» —, mas a diferenca nao aparece na tela nem estava escrita. Decidir: os tres seguem a tela, ou o album/acervo continua base e o botao diz isso.

````

### E12 — Fase 2: a linha da frente (1) — `meta/ROADMAP.md`

**Ancora, literal:**

````
- ✅ Prompt-modelo para chats gerarem no esquema (i-002).
- 🔨 Prompt-modelo com contrato de modulos e orcamento de tags; prompt e exemplo pelos botoes do app (DEC-021, i-028, i-031) — falta o reteste do dono.
- ✅ Script de validação de acervo `scripts/validate.py`.
````

**Texto novo, literal:**

````
- ✅ Prompt-modelo para chats gerarem no esquema (i-002).
- ✅ Prompt-modelo com contrato de modulos e orcamento de tags; prompt e exemplo pelos botoes do app (DEC-021, i-028, i-031) — 0.8.0, retestado pelo dono.
- ✅ Script de validação de acervo `scripts/validate.py`.
````

### E13 — status e reteste (1) — `meta/specs/261028-prompt-modelo-e-modulos.md`

**Ancora, literal:**

````

> **Status:** Decidida
> **Decidida em:** 2026-10-28 pelo dono — **1a, 2a, 3a, 4a** (as quatro recomendadas). A decisao 5 nasceu
````

**Texto novo, literal:**

````

> **Status:** Implementada (0.8.0, 2026-10-29)
> **Decidida em:** 2026-10-28 pelo dono — **1a, 2a, 3a, 4a** (as quatro recomendadas). A decisao 5 nasceu
````

### E14 — status e reteste (2) — `meta/specs/261028-prompt-modelo-e-modulos.md`

**Ancora, literal:**

````
- Tela real, temas e celular: roteiro do dono.
````

**Texto novo, literal:**

````
- Tela real, temas e celular: roteiro do dono.

### Reteste do prompt — 2026-10-29

Pelo dono, nas condicoes do teste base (Sonnet 5.5, fora de Projeto, mesmo pedido), com o prompt copiado
pelo botao do app publicado `[relatado pelo dono]`. **Duas amostras, nao tres:** uma em esforco Alto
(`261029-1254 Alto.json`, sha1 `fc3a2cfe…`) e uma em Medio (`261029-1255 medio.json`, sha1 `830853bd…`).
Medido pelo chat com o `validate.py` (dois modos) e o `recomposedStyle` do app 0.8.0 em Chromium headless.

| criterio | teste base (prompt antigo) | reteste |
|---|---|---|
| `validate.py`, dois modos | traceback nas 3 | codigo 0 nas 2 |
| modulos no contrato (colecao, ids na faixa, `category` valida, so as cinco chaves) | 0 de 3 | 2 de 2 (10 e 15 modulos) |
| base com 6 a 8 tags | 1 de 9 faixas | 6 de 6 (7 ou 8) |
| recomposto padrao com ate 10 tags | — | 6 de 6 (8 a 10) |
| chips no app / toast sem aviso | 0 chips | 10 e 15 chips; toast limpo |
| rotulos dentro do copiavel | 0 | 0 |
| BPM em modulo fora de `tempo` | 2 de 3 chats | 0 (os 3 modulos `tempo` no formato «NN bpm») |

**Leitura:** os criterios pediam 3 amostras e «8 de 9» faixas; vieram 2 amostras, e 6 de 6 faixas passam
em tudo. A terceira so derrubaria um criterio de «8 de 9» se falhasse em 2 das suas 3 faixas. Fechado com
n = 2, dito assim. Cada faixa cita **um** modulo e deixa os demais como paleta desligada — a leitura mais
conservadora do orcamento.

**Observado, sem ser criterio:** o BPM saiu do style em 4 de 6 faixas (so as de rap-pop, onde o pedido dava
95, o trazem). Com 6 a 8 tags, o chat corta o numero primeiro. O controle de BPM (DEC-020) cobre isso: vazio,
o numero digitado entra no fim.

**Na tela** `[relatado pelo dono]`: itens A1 a A5 ok — confirmados tambem nas capturas (cabecalho com os
cinco botoes e v0.7.0; toast «18 modulo(s) citado(s)…» ao importar `261028-1831.json`). A6 (`file://`):
o app abriu, sem resultado relatado do botao.

````

## Edicao E15 — STATUS inteiro — `meta/STATUS.md`

Sem ancora: substitua o arquivo inteiro. **O que saiu e para onde foi:** o bloco «Ultima conversa» de
2026-10-28 (esta no CHANGELOG [0.8.0], DEC-021, FIX-009 e no log de 2026-10-28); «Em progresso» do
prompt-modelo (entregue: CHANGELOG [0.8.0]); a pendencia «conferir na tela e retestar» (feita) e o item 1 do
backlog, «fechar a frente» (esta WO). Entraram: o prompt-modelo e os botoes em «Funciona», a correcao da linha
do Export MD, a nota do Exclude no v6-mini e o backlog com as ideias da nota do dono.

````
# STATUS.md — Cancioneiro

> **O agora.** O que funciona, o que está em progresso, o que está quebrado, backlog curto.
> Rolante: item resolvido sai daqui e vai para o CHANGELOG. Médio/longo prazo vive no ROADMAP.

**Versão atual:** 0.8.0 · **Fase:** 3a, 3a.2, o BPM da 3b e o prompt-modelo com módulos concluídos e conferidos · Fase 2 com i-008 em aberto · próxima frente: a escolher (ver backlog)

---

## Última conversa (2026-10-29, reteste do prompt e fecho da 0.8.0)

- **Reteste do prompt-modelo** `[relatado pelo dono]`: dois chats Sonnet 5.5 fora de Projeto (Alto e Médio; o terceiro não veio). 6 de 6 faixas dentro do contrato de módulo e do orçamento (base 7-8 tags, recomposto 8-10), 0 rótulos, validador verde nos dois modos `[medido por instrumento]`. Tabela na spec `meta/specs/261028-prompt-modelo-e-modulos.md`.
- **Conferência na tela** `[relatado pelo dono]`: itens A1 a A5 ok, também visíveis nas capturas. 0.8.0 fechada (WO 0016).
- **Interface do Suno v6 medida nas capturas do dono:** v6-mini no plano gratuito; formulário Lyrics → Styles → opções → título; **sem campo de Exclude**. Registrado no `meta/HISTORY.md` §5.
- **Nota do dono `261029-1106.txt`** capturada como ideias: i-030 refinada, i-033 a i-036; e a i-037, achada nos `.md` exportados.
- **Este bloco substitui o anterior, de 2026-10-28, que abria o prompt-modelo.** O que ele dizia está no CHANGELOG [0.8.0], no DECISIONS (DEC-021, FIX-009) e em `logs/2026-10-28.md`.

## Funciona (pronto)

- **Ferramenta `app/index.html`:** importa/carrega JSON, cartões por álbum, copiar Style/Lyrics/Exclude por botão (o botão entrega o texto que está na tela — FIX-007), marca «usei», filtros por álbum/estado/uso, busca, módulos de estilo que recompõem o Style ao vivo, variantes e notas recolhíveis, «Baixar .json» limpo e «Importar .json» que saneia chaves internas e diz quantas removeu (FIX-004/006). A versão aparece no cabeçalho. A importação avisa quantos módulos citados não existem na coleção (FIX-009).
- **Painel de qualidade (0.5.0, DEC-018):** linha abaixo de Style, Lyrics e Exclude com caracteres contra o limite do campo, tags do Style e negações «no X». Vermelho só para truncamento.
- **Custo de cada módulo no chip (0.6.0, DEC-019):** com o painel de módulos aberto, cada chip mostra `−N`, `+N` ou `0` tags; a linha de qualidade diz quanto o style base usa sozinho quando o recomposto passa de 10.
- **Controle de BPM no cartão (0.7.0, DEC-020):** campo 20-300 com `−5`/`+5` e «voltar a N» governa todo «NN bpm» do Style principal; o chip de andamento é atalho (no máximo um ligado); variantes e «Baixar .json» não mudam; o valor é só da sessão.
- **Esquema JSON canônico** (`schema/`). Biblioteca de referência para autoria em `schema/style-modules.json` (27 módulos, sete camadas); cada acervo traz os seus (DEC-016).
- **Datasets:** `data/exemplo-cinzeiro.json` (1 faixa, com os 5 módulos que cita) e `data/demo.json` (2 álbuns, 3 faixas). O álbum de referências do dono mora fora do repo, em `../album-referencias (1).json` (7 faixas, 50 módulos).
- **Validação** (`scripts/validate.py`): sintaxe, esquema (com `jsonschema`), integridade referencial dos módulos (id ausente ou objeto no lugar do id, sem traceback — FIX-009), versão igual nos quatro lugares, um BPM só por faixa (DEC-020) e as marcações do prompt que o app lê (DEC-021); código 1 se falhar; a última linha diz se o esquema foi de fato conferido.
- **Export MD** (faixa / álbum / acervo), com o rótulo fora do bloco. A faixa sai com o Style recomposto (módulos e BPM da tela); álbum e acervo saem com o `style` base — ver i-037.
- **Prompt-modelo** (`schema/PROMPT-PARA-CHATS.md`, DEC-021): contrato de módulo, style com 6 a 8 tags e até 10 com os módulos ligados. Retestado em 2026-10-29: 6 de 6 faixas dentro do contrato e do orçamento.
- **Botões «Prompt para chats» e «Baixar exemplo»** (0.8.0, DEC-021): buscam o prompt e o `data/demo.json` do repositório no clique; a janela do prompt recebe o «Meu pedido».
- **Publicado no GitHub Pages** em `https://joaolucas-nds.github.io/cancioneiro/app/index.html` — o push em `main` publica.

## Em progresso

- (nada)

## Quebrado / pendências que travam

- (nada quebrado)

## Pendências do dono

- **Instalar o validador de esquema nesta máquina.** Sem `jsonschema` e `referencing`, o `validate.py` só confere sintaxe e diz `ESQUEMA NAO CONFERIDO` na última linha. Uma vez, no CMD: `pip install jsonschema referencing --break-system-packages`. Depois, `python3 scripts/validate.py` deve terminar em `Tudo conforme ao esquema.`
- **Trazer os álbuns antigos** para a pasta-pai, quando quiser; desbloqueiam a i-008.

## Backlog curto (próximas ações concretas)

1. **Conveniências de uso** — da nota do dono de 2026-10-29: estrutura do cartão configurável e salva no navegador (i-030), copiar o título (i-033), arrastar o `.json` (i-034), acervo que sobrevive ao fechar o navegador (i-035, pede DEC), prompt que entrega arquivo (i-036, pede reteste). Uma spec com as decisões do dono.
2. **Export de álbum e acervo com o Style da tela?** (i-037) — decidir junto da 1.
3. **Pesquisar outras plataformas de música por IA** (i-032) — um turno de pesquisa antes de qualquer mudança de esquema.
4. **Converter 1 álbum real** (i-008) — quando os `.md` de origem chegarem à pasta-pai.
5. **Avisar palavra de andamento que contradiz o BPM** (i-029) — pede uma tabela palavra → faixa de BPM, com fonte e data.
6. **Importar prompts prontos dos álbuns como módulos** — o último ⬜ da 3b no ROADMAP; ainda sem spec.

## Notas de estado

- **Repo local do dono:** `C:\Users\alexk\Tools\cancioneiro\cancioneiro` (Windows). O chat lê e grava na pasta vinculada; commit e push são do Code (DEC-010). A pasta-pai guarda relatórios, notas e o acervo do dono, fora do Git; o lido vai para `../notas-arquivadas/`.
- **Canal:** pasta vinculada é o padrão; a cópia achatada (FlatDrop) é reserva (DEC-017).
- **Limites do Suno:** o v6 saiu em 2026-09-09 e a nota oficial não documenta limite de campo; os números do painel vêm de fonte secundária, com fonte e data no `QUALITY_LIMITS` (DEC-018). Outra fonte secundária (2026-08) põe o ideal em 4 a 7 descritores; o prompt usa 6 a 8. Reconferir quando houver documentação oficial. O `meta/HISTORY.md` §5 ganhou a interface do v6 vista na conta (2026-10-29); o resto do arquivo ainda descreve o v5.5.
- **Exclude no v6-mini:** o formulário gratuito não tem o campo (capturas de 2026-10-29). O app segue mostrando o bloco Exclude e o painel segue sugerindo levar «no X» para lá; o dado continua útil para quem tem o campo. Decidir na spec das conveniências (i-030: ocultar campos).
- **Botões de prompt e exemplo:** dependem de rede e do Pages. No `file://`, só funcionam se o Pages aceitar o `fetch` de uma página local — não conferido (o dono abriu o `file://` em 2026-10-29, sem relatar o resultado do botão); sem isso, a janela mostra o link para a versão publicada (DEC-021).
- **Estado de sessão** (módulos ligados e BPM escolhido) sobrevive a filtro, busca e «marcar usei»; volta ao acervo ao recarregar a página ou importar de novo (FIX-008, DEC-020).
- **Limite conhecido:** `tryAutoLoad` (carregamento automático pelo Pages) não saneia chaves internas — só a importação por arquivo faz isso. Inócuo enquanto nenhum acervo contaminado for para `data/`.
- **Pendência de contexto — ASU:** o dono perguntou se o «modo ASU» do KCM seria melhor que o modo Code para este projeto; ficou pendente até ele trazer a descrição do ASU `[relatado pelo dono, sem material de apoio]`.
- Design: na recomposição do Style a base manda — desligar um módulo não remove o que já está no style base; módulos só somam. O dedup compara sequências de palavras (FIX-003). Os módulos de gênero e de andamento costumam custar 0 tag por isso (DEC-019). O chip de andamento é atalho do controle de BPM, no máximo um ligado (DEC-020).
````

## Edicao E16 — log do dia, arquivo novo — `logs/2026-10-29.md`

Sem ancora: crie o arquivo com o bloco abaixo. E a secao do chat (Conversa 1); a do Code entra no `/wrap`,
como **Conversa 2**, abaixo dela.

````
# Log — 2026-10-29

## Conversa 1 — chat: reteste do prompt-modelo e fecho da 0.8.0 (WO 0016)

### Objetivo do dia
Medir o reteste do prompt-modelo e a conferência na tela da WO 0015, e fechar a 0.8.0.

### Feito
- Relatórios da WO 0015 (`8bbe6c1`) e do `/wrap` (`848e06c`) conferidos contra o `git log`: commit, push e árvore limpa.
- Reteste medido `[medido por instrumento]`: dois chats (o terceiro não veio), 6 de 6 faixas dentro do contrato de módulo e do orçamento; validador verde nos dois modos; 10 e 15 chips no app, toast limpo. Tabela na spec.
- 33 capturas do dono lidas: A1 e A5 confirmados; a interface do Suno v6-mini (formulário, planos, ausência do campo Exclude) registrada no HISTORY §5.
- `.md` exportados pelo dono lidos: export de faixa recomposto, de álbum com o base — virou i-037; a linha do STATUS que dizia «recomposto» para os três foi corrigida.
- Nota `261029-1106.txt` capturada: i-030 refinada, i-033 a i-036.
- WO 0016: 0.8.0 no app, CHANGELOG, README e STATUS; CONTEXT, HISTORY, IDEAS, ROADMAP e spec.

### Decisões
Nenhuma DEC nova. A 0.8.0 fecha com n = 2 no reteste, dito na spec.

### Bugs
Nenhum. A diferença entre o export de faixa e o de álbum é comportamento da 0.4.0 que não estava escrito — virou i-037, não FIX.

### Aprendizados / armadilhas
- Captura de tela do dono é medição da conta dele: respondeu «onde está o Exclude?» melhor que a fonte secundária, que só diz «onde estiver disponível».
- Afirmação de STATUS que cobre três casos («faixa / álbum / acervo, recomposto») precisa ser conferida nos três: valia para um.

### Onde parei
WO 0016 entregue. Próxima frente a escolher pelo dono; a recomendada é a das conveniências (backlog 1).

### Próximos passos
Aplicar a WO 0016. Depois, as decisões das conveniências (i-030, i-033 a i-037).
````

## Fora de escopo

- **As ideias i-030, i-033 a i-037** — so capturadas. A proxima frente as decide numa spec.
- `data/`, `schema/`, `scripts/` — nada muda.

## Armadilhas desta WO

- **Blocos com `## ` e `### ` dentro** (o CHANGELOG, as ideias novas, o reteste da spec, o STATUS e o log):
  delimite pelas crases. Foi o que parou as WOs 0012 e 0013.
- **A versao tem de mudar nos quatro lugares no mesmo commit** (app, CHANGELOG, README, STATUS). Aplicar so
  parte faz a checagem 6 falhar — e e para falhar.
- **`--- INÍCIO ---` e `→` tem acento/simbolo:** `grep` precisa de `LC_ALL=C.UTF-8`.
- **Fim de linha:** os arquivos sao LF. Se um hash de chegada divergir, rode `file <arquivo>` antes de concluir
  que uma edicao errou.

## Depois de aplicar — conferencia antes do commit

| # | Checagem | Comando | Esperado |
|---|---|---|---|
| 1 | **Os dez arquivos sao os testados** | `sha1sum app/index.html meta/CHANGELOG.md README.md meta/CONTEXT.md meta/HISTORY.md meta/IDEAS.md meta/ROADMAP.md meta/specs/261028-prompt-modelo-e-modulos.md meta/STATUS.md logs/2026-10-29.md` | a coluna **chegada** do cabecalho, os dez. **Prova as 16 edicoes.** |
| 2 | A versao no app | `grep -c 'data-role="app-version">v0.8.0<' app/index.html` | `1` |
| 3 | O topo do CHANGELOG | `grep -m1 '^## \[' meta/CHANGELOG.md` | `## [0.8.0] — 2026-10-29` |
| 4 | As ideias | `grep -cE '^### i-03[3-7] ' meta/IDEAS.md`, `grep -cE '^### i-0(28\|31) ✅' meta/IDEAS.md` | `5`, `2` |
| 5 | A spec | `grep -c 'Status:\*\* Implementada' meta/specs/261028-prompt-modelo-e-modulos.md` | `1` |
| 6 | Validacao passa, com a versao nova | `python3 scripts/validate.py; echo "exit=$?"` | `exit=0`, com a linha `OK  versao 0.8.0 igual em CHANGELOG, app, README e STATUS` |
| 7 | Nada de dados nem de codigo alem da versao | `GIT_OPTIONAL_LOCKS=0 git status --short data schema scripts` | saida **vazia** |
| 8 | Nenhum relatorio `.txt` no repo | `GIT_OPTIONAL_LOCKS=0 git status --short \| grep -c '\.txt'` | `0` |

**Os tres campos de cada passo:** as oito sao rodadas por **quem aplica (o Code)**, na raiz do repo
(`C:\Users\alexk\Tools\cancioneiro\cancioneiro`), em Git Bash, com `LC_ALL=C.UTF-8`. **Chega no ramo?**
A checagem 1 cobre os dez arquivos inteiros; a 6 passa pelo `check_version` do validador, que le a versao
nos quatro lugares. **Esta e qual pergunta?** As oito respondem «esta la?». Nao ha roteiro de tela: a unica
mudanca visivel e o `v0.8.0` no cabecalho.

## Relatorio de aplicacao

Grave em `../261029-HHMM-code-cancioneiro-apply-wo0016.txt`, com o `HHMM` de `date +%y%m%d-%H%M` rodado na
hora. Diga o resultado da checagem 1 em primeiro lugar.

**Proximo comando** (ultima linha do relatorio, cru e sozinho):

```
/wrap
```

## Commit

```
git add app/index.html meta/CHANGELOG.md README.md meta/CONTEXT.md meta/HISTORY.md meta/IDEAS.md meta/ROADMAP.md meta/specs/261028-prompt-modelo-e-modulos.md meta/STATUS.md logs/2026-10-29.md meta/workorders
```

```
git commit -m "docs: fecha o prompt-modelo e a versao 0.8.0" -m "Reteste do dono com dois chats: 6 de 6 faixas no contrato de modulo e no orcamento, validador verde; conferencia na tela ok. Versao 0.8.0 no app, CHANGELOG, README e STATUS. HISTORY registra a interface do Suno v6-mini (sem campo Exclude). IDEAS: i-028 e i-031 entregues, i-030 refinada, i-033 a i-037 capturadas. STATUS corrige a linha do export MD."
```

```
git push
```
