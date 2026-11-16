# ANÁLISE — Avisar quando a palavra de andamento contradiz o BPM (i-029)

> **Status:** Decidida — opção A, pelo dono em 2026-11-16 `[relatado pelo dono]`; aplicada pela WO 0045
> **Data:** 2026-11-16 (data de criação; não muda depois)
> **Ideia de origem:** i-029 (nascida da spec do BPM, 2026-10-28). Frente escolhida pelo dono em 2026-11-16 `[relatado pelo dono]`.

## Problema

Desde a 0.7.0, o controle de BPM do cartão troca o número do Style. A palavra de andamento que já estava lá
(«downtempo», «slow tempo», «uptempo») não muda. O caso que gerou a ideia: uma faixa com «downtempo» levada a 140
pelo controle. Se o Suno recebe sinais opostos, tende a escolher um deles, ou a misturar. A i-029 propõe um aviso
âmbar na linha de qualidade quando palavra e número brigam.

## Restrições / o que foi medido

`[medido pelo chat em 2026-11-16, por script no disco do dono; só contagens]`

- **Nos dois acervos reais, nenhuma briga escrita.** São 806 styles: 491 no `albuns-reagrupados.json` (com as
  variantes) e 315 no `rainha-da-preguica.json`. Desses, 90 têm palavra de andamento e número ao mesmo tempo (56
  e 34). Com limites folgados («lento» a 120 ou mais, «rápido» a 90 ou menos, «médio» fora de 80–130), **0
  conflitos**. Quem escreveu os styles (o dono e os chats) já põe palavra e número de acordo.
- **A palavra crua dá falso positivo em massa.** Os fragmentos mais comuns com «fast» e «slow» falam do canto ou
  do arranjo, não do andamento: «fast rap verses» (10), «fast rap with melodic drops» (6), «fast rap» (4), «fast
  glitchy synthesizers», «powerful slow build to epic chorus», «slow rising tension». Um aviso por palavra
  acenderia nessas faixas sem motivo; o filtro teria de reconhecer o que vem depois da palavra.
- **A briga só nasce do controle.** Como o style escrito não briga, o caso real é o dono mexer no BPM do cartão
  e esquecer a palavra. O app sabe quando isso acontece: o valor do controle difere do inicial.
- **As tabelas não concordam.** Para «downtempo», as fontes dão de 60 a 110 BPM (SampleFocus), de 70 a 89
  (Gearspace), de 80 a 90 (Aulart) e uma mediana medida de 105, com metade entre 98 e 111 (Mixgraph, 1.639
  faixas, 2026-11-12). Para «mid-tempo», de 80 a 120 ou de 90 a 109. Uma tabela única no app seria uma escolha
  nossa, não um fato. É o mesmo motivo que tirou a tabela de gêneros vocais da DEC-019.
- **O que os guias de Suno dizem** (fontes secundárias): número e palavra juntos funcionam melhor que um só
  («95 BPM, slow and deliberate»), e «slow jazz» com «140 BPM» brigam. Ou seja: a briga importa, e a forma de
  evitá-la é escrever os dois de acordo, que é o que os acervos já fazem.

## Opções consideradas

**A — Não construir; uma linha no kit.** A `macetes-suno` §5 ganha: «a palavra de andamento acompanha o número;
ao mudar o BPM, reveja a palavra». A i-029 fecha. Custo: uma linha. Não avisa ninguém na hora.

**B — Aviso só quando o controle mexeu.** Âmbar na linha de qualidade quando o BPM do cartão difere do inicial e
o style tem uma palavra de andamento **sem ambiguidade** (`downtempo`, `slow tempo`, `uptempo`, `up-tempo`,
`mid-tempo`), ignorando «fast»/«slow» soltos. O aviso não julga a faixa de BPM («você mudou o BPM; o style
ainda diz "downtempo"»), então não precisa de tabela. Custo: uma função e uns testes; o falso positivo é quase
nulo, e o aviso também acende numa mudança pequena (de 92 para 95), o que é ruído.

**C — Tabela palavra → faixa de BPM, como a i-029 propõe.** Um objeto único com fonte e data, como o
`QUALITY_LIMITS`. Descartada: as fontes discordam em até 40 BPM, o falso positivo das palavras cruas é grande, e
no dado real o aviso acenderia zero vezes no style escrito.

**D — Trocar a palavra junto com o número.** O controle reescreveria «downtempo» para «uptempo». Descartada: o
app passaria a escrever texto de estilo, que é decisão do dono, e a escolha da palavra cairia na mesma tabela de C.

## Recomendação

**A.** No dado real a briga não existe no que foi escrito. Ela só aparece se o dono mexer no controle, e a
medida não mostra que isso aconteça com frequência. Uma linha no kit cobre o caso com o menor custo, e a i-029
fecha com a medida registrada. Se aparecer no campo uma faixa que saiu errada por isso, B é o próximo passo: fica
descrita aqui, pronta.

## Riscos

- **O caso raro ficar sem aviso.** O dono muda o BPM, esquece a palavra, e o Suno escolhe o andamento errado.
  Sinal: um relato «ficou lento/rápido demais» numa faixa com o controle mexido. Remédio: B.
- **A medida é de dois acervos de um dono só.** Outro jeito de escrever style poderia brigar mais. Por isso B
  fica escrita.

## Ponto de decisão

1. **A** (uma linha na `macetes-suno` §5, i-029 fechada), como recomendado, **B** (aviso só depois de mexer no
   controle, sem tabela), ou **C** (a tabela)?
