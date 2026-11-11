# SPEC — Rampa de BPM (0.19.0)

> **Status:** Pronta — aplicação pela WO 0036 (0.19.0, DEC-036).
> **Data:** 2026-11-11 (data de criação; não muda depois)
> **Ideia de origem:** i-042 (rampa de BPM no style, «95 BPM to 118 BPM»). Revê um ponto da DEC-020.
> **Protótipo:** tela «0.19 · rampa de BPM» no canvas «Cancioneiro: nova interface»
> (`https://claude.ai/artifact/Sk1Xf5Rpr26WfGLbZJ2GAD`): alterne «Hoje (0.18.0)» e «Proposta (0.19.0)» e clique em
> «Copiar Style».
> **Depende de:** 0.18.0 (`a67ee01`). Os testes entram em `tests/` (DEC-034).

---

## Problema

Três faixas BR (`br2-09`, `br3-07` e `br4-07`, no acervo do dono, fora do repo) mudam de andamento de propósito:
«95 BPM building to 115 BPM», «95 BPM to 118 BPM», «96 BPM to 116 BPM». A i-042 nasceu porque o `validate.py` as
reprova (DEC-020: dois BPM no style). **Medido nesta spec, o problema é maior:** o app reescreve todo número de
BPM para o valor do controle **mesmo sem ninguém mexer nele** — o valor inicial é o primeiro número, e o segundo
vira o primeiro. O que se copia hoje dessas faixas é:

```
dream pop, soft female vocal, 95 BPM building to 95 bpm, warm synths
```

Medido no app da 0.17.0, Chromium sem tela, com uma faixa sintética de style `dream pop, soft female vocal, 95 BPM
building to 115 BPM, warm synths` (`recomposedStyle` e o botão «Style» da linha dão o mesmo texto). A DEC-020 prometia
«no valor original, tudo o que se copia é byte a byte o da 0.6.0»; numa rampa, não é. É um defeito silencioso que
vira um FIX, e é a parte da i-042 que não depende de decisão.

**O que se sabe do Suno** (pesquisa de 2026-11-11, fontes secundárias): o Suno não segue mudança de andamento
dentro de uma geração; para dar a sensação de crescer, os guias recomendam manter um BPM e descrever a subida de
energia (instrumentação mais densa, subdivisões, «build»). É o que a `macetes-suno` §5 já diz. Ou seja: a rampa
provavelmente rende pouco no Suno — mas é escolha do autor, e o app não pode trocá-la em silêncio.

## O que construir

### 1. Reconhecer a rampa (o FIX)

- **Rampa** = dois números de BPM no **mesmo trecho** do style (entre duas vírgulas), ligados por `to`,
  `building to`, `rising to`, `up to`, `climbing to` ou `→` (ponto 1). Ex.: `95 BPM building to 115 BPM`,
  `96 BPM to 116 BPM`, `90 → 120 bpm`.
- **Numa faixa com rampa, o Style sai byte a byte como está escrito**: o controle de BPM não reescreve nada.
- Dois números **soltos** (em trechos diferentes, ou sem a palavra de ligação) continuam sendo o caso da DEC-020: o
  controle governa todos, e o `validate.py` reprova.

### 2. O cartão numa faixa com rampa

- **O controle de BPM vira um rótulo** (ponto 2): «rampa 95 → 115 bpm», com a dica «o controle não mexe numa
  rampa». Sem −5/+5 e sem «voltar a N».
- **Os chips de andamento ficam desligados** nessa faixa, com o porquê no título: ligar um poria um terceiro BPM.
- **A linha de qualidade avisa em âmbar** (ponto 3): «rampa de BPM: o Suno não segue mudança de andamento numa
  geração; para crescer, descreva («gradual build») e deixe um BPM». Âmbar, nunca vermelho: não corta nada.
- O export `.md` leva o Style como está; a linha de metadados diz «rampa 95 → 115 bpm».

### 3. O `validate.py`

- **Rampa declarada vira AVISO, não ERRO** (ponto 4): «[album > faixa] rampa de BPM: 95 → 115». O código de saída
  continua 0 por causa dela.
- O campo `bpm`, quando existe numa faixa com rampa, tem de ser o **número de partida**; senão, ERRO.
- Dois números soltos, ou `bpm` que não bate com um BPM único: ERRO, como hoje (DEC-020).
- A expressão que reconhece a rampa é a mesma do app (como a `BPM_RE`), com um comentário apontando um para o outro.

### 4. O kit e o prompt

- **`revisar-faixa`, conferência 7:** «rampa («95 to 118 BPM»): o app preserva e avisa; o Suno não a segue — prefira
  um BPM e descreva a subida». Âmbar, como já era.
- **`macetes-suno` §5:** acrescenta que o Cancioneiro reconhece e preserva a rampa, mas que a recomendação continua.
- **Prompt-modelo:** não muda (já pede um BPM por faixa).

### O que não muda

- Faixa com um BPM: o controle, os chips e o `validate.py` como hoje (DEC-020).
- Variantes: fora do controle, como hoje.
- O esquema: nada novo (sem `bpmEnd`; ponto 1 discute).

## Critérios de pronto (o chat mede no Chromium headless; viram `tests/test_bpm.py`)

| # | Critério |
|---|---|
| C1 | Faixa com `95 BPM building to 115 BPM`: o Style copiado (linha, cartão e detalhe) é byte a byte o do acervo. **Prova de vida:** na 0.18.0 sai `95 bpm` no lugar de `115 BPM`. |
| C2 | As seis formas de ligação (`to`, `building to`, `rising to`, `up to`, `climbing to`, `→`) são rampa; `95 bpm, 115 bpm` (trechos diferentes) e `95 bpm 115 bpm` (sem ligação) **não** são. |
| C3 | Numa faixa com rampa: o rótulo «rampa 95 → 115 bpm» no lugar do controle; os chips de andamento desligados; a linha de qualidade com o aviso âmbar. |
| C4 | **Falso positivo:** faixa com um BPM: o controle, −5/+5 e os chips funcionam como na 0.18.0 (os testes de BPM existentes passam). |
| C5 | O export `.md` da faixa com rampa leva o Style intacto e «rampa 95 → 115 bpm» na linha de metadados. |
| C6 | `validate.py`: rampa = AVISO e exit 0; `bpm` igual ao número de partida passa; `bpm` igual ao de chegada é ERRO; dois soltos é ERRO. Testado num acervo sintético com os quatro casos. |
| C7 | `v0.19.0`; nenhum erro de página; os 44 testes de `tests/` continuam passando; os novos reprovam na 0.18.0. |

## Resultado (chat, 2026-11-11, clone de `c1fbc17`)

| # | Medido |
|---|---|
| C1 | Style copiado byte a byte na linha, no cartão e no detalhe. Na 0.18.0 sai `95 BPM building to 95 bpm`. |
| C2 | As seis formas reconhecidas; `95 bpm, 115 bpm` e `95 bpm 115 bpm` não. |
| C3 | Rótulo «rampa 95 → 115 bpm», chip de andamento desligado com o porquê, aviso âmbar, coluna da Lista «95→115 bpm». |
| C4 | Faixa com um BPM: +5 dá «pop, 105 bpm, warm synths»; os testes de BPM antigos passam. |
| C5 | Export `.md` com o Style intacto e «BPM: rampa 95 → 115». |
| C6 | Quatro casos sintéticos: rampa AVISO exit 0; `bpm` = partida passa; `bpm` = chegada ERRO; dois soltos ERRO. |
| C7 | `v0.19.0`; 50 testes passam, duas rodadas (45 s); os 6 novos: 5 reprovam na 0.18.0 e o C4 (falso positivo) passa nas duas, como deve. |

- **As três faixas BR** (medidas no acervo do dono, fora do repo): as três são reconhecidas como rampa (95→115, 95→118, 96→116), sem campo `bpm` — passam com AVISO.
- **Abertura com 205 faixas:** 0.18.0 226–268 ms × 0.19.0 236–245 ms, três rodadas de cinco: sem diferença.
- A lista de formas está no app (`RAMP_RE`) e no `validate.py` (`RAMP_RE`), com comentário cruzado.

## Riscos

- **Reconhecer demais:** «from 95 bpm intro to 120 bpm drop» atravessa trechos e não é pego; é o comportamento
  certo (dois números soltos são erro de autoria). O C2 testa os dois lados.
- **Reconhecer de menos:** uma forma que o autor usar e não estiver na lista cai no caso da DEC-020 e o
  `validate.py` reprova — falha alta, não silenciosa. A lista cresce por decisão.
- **O aviso âmbar incomodar:** aparece só nas faixas com rampa (três, hoje), e diz o que fazer.

## Fora de escopo

- **Converter a rampa por um botão** (trocar por um BPM e «gradual build»): o ponto 3 discute; mexer no texto do
  acervo é curadoria, e o app não edita o Style.
- **Campo de esquema para a rampa** (`bpmEnd`).
- **A i-029** (palavra de andamento que contradiz o BPM).

## Pontos para o dono decidir

**Decididos pelo dono em 2026-11-11: os quatro como recomendados (1a, 2a, 3a, 4a) — DEC-036.**

1. **O que é rampa.**
   - **(a) Só texto: dois BPM no mesmo trecho ligados por uma das seis formas (recomendado).** O esquema não muda.
   - (b) Um campo novo no esquema (`bpmEnd`): explícito, mas muda o contrato dos chats e o prompt-modelo.
2. **O controle de BPM numa faixa com rampa.**
   - **(a) Vira rótulo, sem mexer (recomendado):** a rampa sai como foi escrita.
   - (b) Desloca os dois números juntos (−5 nos dois): mais poder, mais código, e a rampa já rende pouco no Suno.
3. **O aviso.**
   - **(a) Âmbar na linha de qualidade, com a recomendação de trocar por um BPM e descrever (recomendado).**
   - (b) Sem aviso: a rampa é escolha do autor e pronto.
   - (c) Aviso e um botão que troca a rampa por um BPM e «gradual build» no rascunho (o app passaria a editar o Style).
4. **O `validate.py`.**
   - **(a) Rampa reconhecida = AVISO, exit 0 (recomendado).**
   - (b) Continua ERRO: força trocar as três faixas à mão.
