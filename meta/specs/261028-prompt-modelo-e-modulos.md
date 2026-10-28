# SPEC — Prompt-modelo: contrato de modulos e orcamento de tags (i-028)

> **Status:** Decidida
> **Decidida em:** 2026-10-28 pelo dono — **1a, 2a, 3a, 4a** (as quatro recomendadas). A decisao 5 nasceu
> da nota do dono `261028-1852.txt`, no mesmo dia. Aplicacao: `meta/workorders/261028-wo0015-prompt-modelo-e-modulos.md`.
> App e validador testados pelo chat numa copia; o reteste do prompt com chats e do dono (ver «Desfecho»).
> **Data:** 2026-10-28 (data de criacao; nao muda depois)
> **Ideia de origem:** i-028 em `meta/IDEAS.md` («o prompt-modelo pedir folga para os modulos») e o item 2
> do backlog do STATUS («testar o prompt-modelo ponta a ponta»), escolhidos juntos pelo dono em 2026-10-28.
> **Depende de:** DEC-016 (acervo autossuficiente), DEC-019 (custo no chip), DEC-020 (BPM).
> A spec diz **o que** construir e **quando esta pronto**. Como aplicar e a WO, que nasce depois.

---

## Problema

A i-028 dizia: o style base nasce com 10 de 10 tags em ar-01 e ar-04, e nenhum modulo cabe. A proposta
era o prompt pedir um base de 6 a 8 tags. A medicao desta spec mostra que a dor e outra e maior:

1. **O prompt nao ensina o contrato de modulo.** Ele manda deixar `styleModules: []` e nunca menciona o
   `styleModules` da COLECAO, onde a DEC-016 diz que os modulos moram. Pedido a um chat que proponha
   modulos, ele **inventa um formato** — tres amostras, tres formatos diferentes, nenhum no lugar certo.
2. **O app aceita isso em silencio.** A importacao diz «Acervo importado», o painel de modulos abre com
   **0 chips**, e o modulo que o chat marcou como ligado nao entra no Style. Nenhum aviso.
3. **O validador quebra** com `TypeError` (traceback) em vez de reprovar, nos dois modos.
4. **O base ja nasce no limite**, como a i-028 previa: 5 de 9 bases com 10 tags ou mais.

Sem isto, o ciclo «chat gera -> ferramenta le» que a i-002 prometeu funciona para Style e Lyrics e falha
para modulos, que sao o recurso central da ferramenta (troca por menu, i-004).

## Restricoes / o que foi medido

**Teste base (2026-10-28):** o prompt ATUAL (`schema/PROMPT-PARA-CHATS.md`, 5.829 bytes) colado num chat
novo, fora de Projeto e sem instrucoes gerais, com o pedido do roteiro (3 faixas: synth-pop pt-BR com
vocal, ambient instrumental em loop, rap-pop em ingles a 95 BPM, «proponha tambem modulos de estilo»).
Modelo Sonnet 5.5; amostras 1829 e 1831 em esforco Medio, 1833 em esforco Alto `[relatado pelo dono]`.
Arquivos na pasta-pai: `261028-1829.json` (sha1 `aa47c160…`), `261028-1831.json` (`6765a694…`),
`261028-1833.json` (`f86a3e7e…`).

| amostra | tags do base (3 faixas) | modulos por faixa | modulos na colecao | formato que o chat inventou |
|---|---|---|---|---|
| 1829 | 12 · 12 · 10 | 4 · 4 · 4 | 0 | `{id, label, style, default}` — todos `default:false` |
| 1831 | 9 · 11 · 9 | 6 · 6 · 6 | 0 | `{id, label, enabled, text}` — 3 `enabled:true` por faixa, que repetem o base |
| 1833 | 10 · 9 · 8 | 5 · 5 · 5 | 0 | `{id, label, enabled, style, excludeStyles}` — todos `enabled:false` |

Contagem de tags com a regra do app (`countTags`: fragmentos nao vazios entre virgulas).

- **O que funcionou, 9 de 9 faixas:** JSON puro (comeca em `{`, termina em `}`, sem cerca nem texto),
  nenhuma chave fora do esquema alem de `styleModules`, obrigatorios presentes, `state` no enum, **zero
  rotulos** dentro de `style`/`lyrics`/variantes (regex `ESTILO|STYLE:|LETRA|LYRICS:|STYLE OF MUSIC`),
  `bpm` igual ao «NN bpm» do style, `excludeStyles` preenchido, `[Instrumental]` nas instrumentais.
  A regra de dominio inviolavel se sustentou sem ajuda.
- **Base:** 5 de 9 com 10 ou mais tags; 1 de 9 dentro de 6 a 8. Comprimento 190 a 294 caracteres —
  longe dos 1.000; o problema e diluicao, nao truncamento.
- **Modulos:** 9 de 9 faixas com modulos **aninhados na faixa como objeto**; o esquema exige ids
  (`song.styleModules.items.type = string`, `additionalProperties: false`). Nenhum trouxe `category`,
  que o app usa para agrupar os chips nas sete camadas (`LAYERS`) — mesmo no lugar certo, sem `category`
  o chip nao apareceria. Dois chats puseram BPM proprio em modulo (1831: 118 e 90; 1833: ~60) e um poe
  `excludeStyles` em modulo, que nem o esquema nem o app conhecem.
- **App (0.7.0, `cd4b86f`), Chromium headless:** arquivo com a FORMA das amostras (objetos na faixa, nada
  na colecao; nao o arquivo em si) -> toast «Acervo importado», 0 erros no console, painel de modulos
  presente com **0 chips**, Style sem o modulo `enabled:true`. Prova de vida: `data/demo.json` no mesmo
  instrumento -> 27 chips por cartao. Caminho no codigo: `setCollection` indexa so `json.styleModules`;
  `recomposedStyle` faz `App.modulesById[objeto]` -> `undefined` -> pula.
- **Validador:** modo sintaxe (maquina do dono) -> traceback em `check_module_refs` (`if mid not in
  index`, `dict` nao e hashable), nenhuma linha de relatorio; modo completo (com `jsonschema`, no
  container) -> reporta o erro de esquema e DEPOIS quebra no mesmo ponto.
- **Fontes sobre quantidade de tags (todas secundarias, nenhuma oficial do v6):** `QUALITY_LIMITS` do app
  (ideal ate 8, dilui acima de ~10; hookgenius, 2026-09) e blakecrosley.com (2026-08-04, sem versao
  declarada: ponto ideal 4 a 7, acima disso as restricoes competem). Mesmo sentido; numeros diferentes.

## Decisoes de design (propostas — o dono decide no fim)

**Decisao 1 — Onde o chat declara os modulos.**
- **1a (recomendada):** o prompt ensina o contrato da DEC-016, sem mudar o esquema: modulos no
  `styleModules` da COLECAO, cada um com `id`, `category` (uma das sete camadas), `label`, `fragment`,
  `notes`; a faixa cita ids; **citado = ligado de saida**. Uma secao curta com um exemplo de modulo.
- 1b: mudar o esquema para aceitar modulo dentro da faixa — e a forma que os tres chats escolheram.
  Contra: desfaz a DEC-016 (modulo repetido em cada faixa, paleta nao compartilhada no album), mexe em
  esquema, app, validador e acervos ja feitos.
- 1c: importador tolerante que «levanta» objetos da faixa para a colecao. Contra: os tres formatos
  divergem nas chaves (`style`/`text`, `default`/`enabled`); normalizar o que cada chat inventa e
  perseguir alvo movel. Ensinar o contrato e a causa; tolerar e o sintoma.

**Decisao 2 — Orcamento de tags.**
- **2a (recomendada):** base com **6 a 8 tags**; a faixa cita (liga de saida) so os modulos que mantem o
  recomposto em **ate 10**; os demais ficam declarados e desligados — paleta para variar com um clique,
  sem custo ate o clique (DEC-019 mostra o custo no chip).
- 2b: so «base com 6 a 8» (a i-028 ao pe da letra). Contra: medido no acervo, o excesso vem dos modulos
  ligados (+2 a +8); o base sozinho resolveria 1 de 7 faixas.
- Contra a 2a, o melhor argumento: base curto pode ficar vago. Mitigacao ja existente: o painel avisa
  abaixo de 4 tags.

**Decisao 3 — O silencio do app e o crash do validador.**
- **3a (recomendada):** (i) o validador reprova id de modulo que nao e texto com mensagem, sem
  traceback, nos dois modos; (ii) a importacao do app conta os modulos citados que nao resolvem e diz
  isso no toast, como o FIX-006 faz com as chaves internas — importa assim mesmo, nao recusa.
- 3b: so o validador. Contra: quem importa pelo app (o caso normal) continua sem aviso.

**Decisao 4 — Andamento e Exclude em modulo.**
- **4a (recomendada):** o prompt diz que BPM em modulo so na camada `tempo`, no formato «NN bpm» (vira
  atalho do controle, DEC-020), e que modulo nao tem `excludeStyles` (o Exclude e da faixa).
- 4b: deixar o prompt calado. Contra: dois de tres chats ja puseram BPM em modulo de outra camada.

**Decisao 5 — Prompt e exemplo pela interface (decidida pelo dono na nota `261028-1852.txt`).**
O dono nao quer abrir as pastas do repositorio para pegar o prompt ou um exemplo: quer copiar o prompt,
ja com o «Meu pedido», e baixar o exemplo pelo proprio app publicado, como o KCM faz. A objecao desta spec
(uma segunda copia do prompt dentro do app) se resolve sem copia nenhuma:
- **Botao «Prompt para chats»:** abre uma janela com um campo «Meu pedido»; «Copiar prompt» **busca**
  `schema/PROMPT-PARA-CHATS.md` no clique, recorta entre as linhas `--- INÍCIO ---` e `--- FIM ---` e poe o
  pedido no lugar da linha entre parenteses abaixo de `## Meu pedido` (vazio: fica o texto-guia).
- **Botao «Baixar exemplo»:** busca `data/demo.json` e baixa como `cancioneiro-exemplo.json`.
- **Fonte unica:** a busca tenta o caminho relativo (Pages) e depois o endereco publicado; no `file://`, so o
  publicado. Falhando tudo, a janela mostra um link para a versao publicada. Cada push muda o que o botao entrega.
- **O acoplamento vira checagem:** o `validate.py` reprova se as marcacoes que o botao le sumirem do prompt.
- Descartado: embutir o prompt no app (duas fontes que divergem em silencio) e um JSON separado «para ensinar
  a estrutura» (o prompt ja traz o exemplo; o `data/demo.json` e o exemplo real).

## Criterios de aceite (verificaveis)

Reteste nas MESMAS condicoes do teste base (prompt novo, mesmo pedido, Sonnet 5.5, fora de Projeto, tres
amostras: duas em Medio e uma em Alto), medido pelo chat:
- [ ] 3 de 3 amostras: JSON que o `validate.py` aceita no modo completo (container) e no modo sintaxe,
      codigo 0, sem traceback.
- [ ] 0 ids de modulo orfaos; todo modulo da colecao com `category` entre as sete camadas.
- [ ] Base com 6 a 8 tags em pelo menos 8 de 9 faixas.
- [ ] Recomposto padrao (modulos citados ligados, medido com o `recomposedStyle` do app) com ate 10 tags
      em pelo menos 8 de 9 faixas.
- [ ] No app: cada cartao com chips (> 0) e toast de importacao sem aviso.
- [ ] Regra de dominio: 0 rotulos dentro de `style`, `lyrics` e variantes (mesmo regex do teste base).
- [ ] BPM em modulo so na camada `tempo` (se houver).

Instrumento e app (se 3a):
- [ ] Arquivo com a forma das amostras -> `validate.py` codigo 1 com mensagem, sem traceback, nos dois modos.
- [ ] Mesmo arquivo no app -> importa e o toast diz quantos modulos citados nao existem na colecao.
- [ ] **Falso positivo:** `data/demo.json`, `data/exemplo-cinzeiro.json` e `../album-referencias (1).json`
      -> validador codigo 0 e toast sem aviso; Style copiado igual byte a byte ao da 0.7.0.

## Fora de escopo

- Campos guiados para «estruturar» o pedido (quantidade, idioma, instrumental, BPM): so se o reteste
  mostrar que o texto livre nao basta (i-031).
- A ordem dos campos no cartao, Lyrics acima do Style como no Suno (i-030).
- i-029 (palavra de andamento contra o BPM) e a skill i-022.
- Mudar o esquema (so na decisao 1b).
- Conferir se as faixas soam bem no Suno.

## Riscos

- **Uma amostra por esforco.** O reteste repete as condicoes, mas tres amostras nao medem variancia; o
  criterio «8 de 9» aceita uma falha.
- **Prompt mais longo, adesao menor.** A secao de modulos acrescenta texto; medir o tamanho antes e
  depois e ver se o que funcionou (rotulos, JSON puro) continua 9 de 9.
- **Os numeros de tags sao de fonte secundaria** e divergem (ate 8 x 4 a 7). Ficam no `QUALITY_LIMITS`
  com fonte e data; o prompt cita a faixa, nao a fonte.
- **O chat nao sabe contar a dedup do app.** Um modulo que repete o base custa 0 (DEC-019); o chat vai
  contar tags no texto. O criterio mede o recomposto real, nao a intencao.

## Ponto de decisao

Do dono: **1, 2, 3 e 4** — as recomendadas sao **1a, 2a, 3a, 4a**. Com a resposta: implementar numa copia,
testar no Chromium headless (prompt novo nao se testa la; os criterios de app e validador sim), escrever a
WO com hashes, e o reteste do prompt volta ao dono como roteiro.

---

## Desfecho — 2026-10-28

Implementado numa copia do repositorio em `cd4b86f` (sha1 de partida dos sete arquivos = o disco do dono)
e testado pelo chat: validador em Python, nos dois modos; app em Chromium headless, comparado com a 0.7.0.

| criterio | resultado |
|---|---|
| forma das amostras -> `validate.py`, modo completo e modo sintaxe | codigo 1, mensagem por item («dict no lugar de um id»), **0 traceback** |
| id que nao existe na colecao -> `validate.py`, dois modos | codigo 1, «nao existe em styleModules[]» |
| falso positivo: `data/demo.json`, `data/exemplo-cinzeiro.json`, `album-referencias (1).json` (sha1 `9baca5c1…`) | codigo 0 nos dois modos |
| prompt sem `--- FIM ---` / sem a linha entre parenteses / sem `## Meu pedido` | codigo 1 nos tres |
| forma das amostras -> importacao no app | toast «3 modulo(s) citado(s) nas faixas nao existe(m) na colecao»; Style igual ao da 0.7.0 |
| falso positivo no app (os tres acervos) | toast sem aviso; 27 · 5 · 50 chips; **Style de 11 de 11 cartoes igual byte a byte ao da 0.7.0** |
| cliques em chips de ar-01 e ar-07 | Style igual ao da 0.7.0 |
| toast longo | visivel aos 3 s (o curto ja sumiu); duracao ~45 ms por caractere, entre 2,2 s e 6 s |
| «Prompt para chats» servido por http, com pedido | janela abre e fecha com Esc; copia 6.410 caracteres, comeca em «Voce vai gerar», termina no pedido; sem marcacoes, sem as notas do mantenedor |
| idem, pedido vazio | copia o recorte literal do arquivo (com o texto-guia) |
| prompt servido sem `--- FIM ---` | «veio sem as marcacoes esperadas — nada foi copiado»; area de transferencia intocada |
| `file://` sem rede | «Nao consegui buscar o prompt» + link para a versao publicada |
| «Baixar exemplo» | `cancioneiro-exemplo.json`, igual byte a byte ao `data/demo.json` |
| carga automatica pelo http | toast sem aviso |

**Nao conferido aqui, e por que:**
- **O reteste do prompt com chats** (os criterios de base, recomposto, modulos e rotulos): so o dono roda
  chats fora do Projeto. Volta como roteiro.
- **O `file://` COM rede:** o container nao alcanca o github.io (403 do proxy), entao nao deu para ver se o
  Pages responde ao `fetch` de uma pagina local (CORS). Se nao responder, o botao cai no link — o caso testado.
- Tela real, temas e celular: roteiro do dono.
