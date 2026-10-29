# SPEC — Conveniências de uso: estrutura do cartão, título, arrastar, acervo no navegador, prompt em arquivo

> **Status:** Implementada (0.9.0, 2026-10-29)
> **Decidida em:** 2026-10-29 pelo dono — **D1 sim, D2 completa, D3 some, D4 sim, D5 segue a tela**; na D4,
> a alternativa ao arquivo é o JSON **dentro de um bloco de código** (refinamento do dono, mesma mensagem).
> Aplicação: `meta/workorders/261029-wo0017-conveniencias-de-uso.md`.
> **Data:** 2026-10-29 (data de criação; não muda depois)
> **Ideias de origem:** i-030, i-033, i-034, i-035, i-036 (nota do dono `261029-1106.txt`) e i-037 (achada nos
> `.md` exportados). Decisões propostas no turno de 2026-10-29 e respondidas na mensagem seguinte.
> **Depende de:** 0.8.0 (DEC-021). Toca a DEC-004 (navegador) — ver DEC-022.

---

## Problema

A nota do dono de 2026-10-29 junta atritos de uso, medidos nas capturas da conta dele:

1. **O título não se copia.** O formulário do v6 tem campo de título (o último, antes de «Save to»).
2. **A ordem do cartão é fixa.** Título → Style → Lyrics serve a quem preenche o Suno de baixo para cima (o
   dono faz assim), mas ele quer controlar a estrutura e guardar a escolha, com a ordem atual como padrão.
3. **O Exclude não tem destino na conta dele:** o formulário do v6-mini gratuito não tem o campo. O bloco e o
   aviso «no X → Exclude» do painel mandam para um campo que não existe ali.
4. **Carregar exige o botão e o seletor de arquivo**, e **o acervo some ao fechar o navegador** — só as marcas
   «usei» sobrevivem.
5. **A resposta do chat vem como texto para copiar** e colar no Bloco de notas.
6. **O export de álbum/acervo saía com o `style` base**, o de faixa com o recomposto (i-037) — sem estar escrito.

## Decisões

**D1 — Acervo guardado no navegador (i-035) → DEC-022.** O último acervo **importado** (botão ou arrastar) fica
numa cópia no `localStorage` e volta ao abrir. É cache, não fonte (DEC-004 segue): o app nunca edita o acervo
(FIX-004), então a cópia é igual ao arquivo. Contra o risco de a cópia ficar velha sem ninguém ver, uma **linha de
origem** na barra de controles diz de onde veio e quando («Acervo importado de X em dd/mm/aaaa hh:mm · guardado
neste navegador») e tem o botão **«esquecer»**. A cópia vence a carga automática do Pages; esquecer volta a ela.
Se o navegador recusar (cota, modo privado), importa assim mesmo e o toast avisa.

**D2 — Estrutura do cartão completa (i-030) → DEC-023.** Botão «Estrutura do cartão» abre uma janela com os seis
blocos — Style, Lyrics, Exclude, Módulos, Variantes, Notas —, cada um com «mostrar» e ↑/↓, mais «Restaurar
padrão». Vale para todos os cartões, guardado no navegador (`App.ui.layout`, estado de interface). **Escolhas
técnicas:** o título e a linha de metadados (BPM, tom, contexto) ficam sempre no topo; os módulos são bloco
próprio, para a ordem padrão ser **exatamente** a de antes; o export `.md` **não** segue a estrutura (é documento
do acervo, ordem fixa, e mostra tudo).

**D3 — Exclude oculto leva junto o aviso de negação.** Com o bloco Exclude oculto, a linha de qualidade deixa de
dizer ««no X»: mais confiável no campo Exclude». O dado continua no JSON.

**D4 — O prompt pede arquivo; a alternativa é bloco de código (i-036) → DEC-023.** A seção «Saída» passa a pedir um
`.json` para download com o nome do `id` do álbum; quem não puder criar arquivo responde com o JSON inteiro em
**um único bloco de código `json`**, sem texto fora. O botão de copiar do bloco entrega só o JSON. Rede de
segurança no app: se o arquivo importado não for JSON puro (resposta colada inteira), a importação extrai o
bloco de código — ou o trecho do primeiro `{` ao último `}` — e **diz no toast** que extraiu (FIX-006: limpar
calado apaga o sinal). Lixo continua recusado.

**D5 — Export de álbum e acervo segue a tela (i-037) → DEC-023.** `albumToMarkdown` passa a usar o Style
recomposto, como a faixa: módulos ligados e BPM do controle.

**Sem decisão do dono (técnico):** copiar o título (i-033) e arrastar o `.json` (i-034, mesmo caminho do botão:
saneamento, avisos, cópia guardada; só reage a arraste de arquivo).

## Critérios de aceite

Executados pelo chat em Chromium headless sobre o app de chegada, contra a 0.8.0 (`73e4a54f`):

- [x] Estrutura padrão: blocos, Style e linha de qualidade **iguais aos da 0.8.0** nos três acervos (7, 3 e 1 cartões).
- [x] «copiar título» copia só o título e mostra «copiado ✓».
- [x] A janela lista os seis blocos na ordem padrão; ↑ do primeiro e ↓ do último desabilitados.
- [x] Ocultar o Exclude o tira de todos os cartões; subir o Lyrics o põe acima do Style; o Style copiado não muda.
- [x] A estrutura sobrevive ao recarregar; «Restaurar padrão» volta à ordem da 0.8.0.
- [x] Recarregar traz o acervo importado, com toast «Acervo do navegador: …» e a linha de origem com data e «esquecer».
- [x] «esquecer» limpa a tela e a cópia; recarregar depois disso não traz o acervo.
- [x] Aviso «no drums» aparece com o Exclude visível e some com ele oculto (D3).
- [x] Com o Style oculto, clicar num chip não dá erro.
- [x] Arrastar um arquivo mostra «Solte o .json para importar»; soltar importa; arrastar texto é ignorado.
- [x] Resposta colada com cercas e texto em volta importa e avisa «JSON extraído de um bloco de código»; lixo é recusado; JSON limpo não avisa.
- [x] Export do álbum = Style da tela (18 tags em ar-01); export do acervo leva o BPM do controle (D5).
- [x] Navegador recusando a cópia: importa e avisa «não coube no navegador».
- [x] Servido por http: sem cópia, o demo carrega com origem «GitHub Pages»; com cópia, ela vence; «esquecer» traz o demo.
- [x] A janela do prompt continua abrindo; nenhum erro de página.
- [x] `validate.py` verde (as marcações do prompt seguem as mesmas).

**Resultado: 34 de 34.** Faltam, e são do dono: a tela real (layout, celular), o reteste do prompt (D4) com chats.

## Fora de escopo

- Mais de um acervo guardado ao mesmo tempo (a cópia é a do último importado).
- Guardar a estrutura ou o acervo fora do navegador (outro aparelho não vê).
- A i-008 (os álbuns antigos chegaram em 2026-10-29: frente própria).

## Riscos

- **Cópia velha:** o arquivo mudou e a cópia não. Mitigação: a linha de origem com data; importar de novo substitui.
- **`localStorage` no `file://`:** o Chrome guarda por arquivo local; outro navegador ou perfil não vê. Esperado.
- **O prompt mudou de novo:** o texto que passou no reteste de 2026-10-29 foi o anterior; esta mudança só toca a
  «Saída», mas exige reteste curto (roteiro do dono).
- **Toast longo:** o aviso do cache somado a outros pode passar de uma linha; dura até 6 s (0.8.0).

---

## Desfecho — 2026-10-29

- **Tela** `[relatado pelo dono]`: itens A1 a A7 do roteiro ok. O `.md` de álbum exportado por ele traz o Style
  de ar-01 com 18 tags, igual ao da faixa (D5 conferido no arquivo dele).
- **Reteste do prompt** (dois chats, Médio e Alto; pedido próprio do dono, não o de bancada): `validate.py`
  verde nos dois modos; 19 e 23 módulos no contrato; base 7-8 tags e recomposto 8-9 em 6 de 6 faixas; 0
  rótulos; 19 e 23 chips, toast limpo `[medido por instrumento]`. Os arquivos chegaram com o nome do `id` do
  álbum (`teste-esforco-alto.json`, `teste-esforco-medio.json`) — o nome que o prompt pede para o **arquivo**;
  indica que os chats criaram arquivo, sem confirmação de como vieram.
- **Ajustes pedidos em seguida** (nota `261029-1618.txt`, DEC-025): título que copia ao clicar, estrutura
  arrastável, Exclude oculto por padrão, cabeçalho enxuto. Testados pelo chat (23 de 23, e a bateria desta spec
  refeita: 34 de 34); vão em [Unreleased] até o dono ver.

