# SPEC — Exportar uma faixa como .json (curadoria, entrega 1)

> **Status:** Decidida — aplicação pela `meta/workorders/261102-wo0022-exportar-faixa-json.md` (0.11.0)
> **Decidida em:** 2026-11-02 pelo dono: F1 + G1, entregas 1 → 2 → 3, o `.json` curado manda sobre os conversores
> (análise `meta/analises/261102-ANALISE-curadoria-no-app.md`, DEC-028).
> **Data:** 2026-11-02 (data de criação; não muda depois)
> **Ideia de origem:** i-040 (nota do dono `261029-1825.txt`: «no exportar md de cada faixa, seria interessante a
> opção de exportar a faixa como json»).

---

## Problema

Hoje uma faixa só sai do app em `.md`, que é leitura. Para levar uma faixa a um chat que trabalha no esquema, ou
juntá-la a outro acervo, o dono precisa do JSON dela, e o único JSON que o app entrega é o do acervo inteiro
(«Baixar .json»: 959 mil caracteres na Rainha da Preguiça). A entrega 3 da curadoria («importar faixas») vai ler
exatamente este formato; definir agora o que uma faixa exportada contém é o que deixa a entrega 3 sem decisão de
formato pendente.

## O que construir

Um botão **«exportar .json»** no rodapé de cada cartão, depois de «exportar .md». O clique baixa `<id da faixa>.json`
com uma coleção completa no esquema:

| Campo | Valor |
|---|---|
| `schemaVersion` | o do acervo aberto (sem ele, `"1.0"`) |
| `title` | o título da faixa |
| `targetTool` | o do acervo aberto, se ele tiver; senão, o campo não sai |
| `albums` | um álbum: `id` e `title` do álbum de origem (sem `description`), e `songs` com a faixa |
| `styleModules` | os módulos que a faixa cita e que existem no acervo, na ordem da citação, cada um uma vez; sem nenhum, o campo não sai |

**Regras:**

1. **O dado do acervo, não o da sessão.** Módulos ligados ou desligados no painel e o BPM do controle não entram:
   a faixa sai igual à do acervo, campo por campo. É a regra do «Baixar .json»; o Style da tela continua sendo do
   `.md`.
2. **Citação que não resolve segue citada.** Id que não existe no acervo, ou objeto no lugar do id, fica na faixa
   como está (conversão fiel), não leva módulo, e o toast conta: «N módulo(s) citado(s) não existe(m) no acervo —
   a faixa os cita assim mesmo». Sem saneamento mudo (FIX-006).
3. **Cópia profunda.** O arquivo nunca compartilha objeto com o acervo aberto; exportar não muda nada na tela.
4. **Chave interna nunca sai.** O objeto exportado passa pelo `stripInternalKeys` (FIX-004).
5. **O nome do arquivo é o id** (ASCII pelo esquema). Sem id, o `slug` do título.
6. **O toast diz o que foi:** «Faixa exportada em .json: brv-04.json · 1 módulo».

O arquivo importa como qualquer acervo (botão ou arrastar), sem aviso de módulo faltando quando a faixa cita só
módulos que existem.

## Critérios de pronto (medidos pelo chat no Chromium headless, `file://`, app de chegada da WO 0022)

| # | Critério | Resultado |
|---|---|---|
| C1 | Todo cartão tem no rodapé «marcar usei», «exportar .md», «exportar .json», nessa ordem (demo + 3 faixas sintéticas: 6 cartões; exemplo: 1) | OK, 2 de 2 |
| C2 | Para cada faixa: nome `<id>.json`; título, `schemaVersion` e `targetTool` do acervo; um álbum com id e título de origem; a faixa idêntica à do acervo; os módulos citados que existem, únicos e na ordem; toast com a contagem; o arquivo passa no esquema (a faixa sintética com objeto no lugar do id reprova, como deve) | OK, 7 de 7 faixas |
| C3 | Com todos os módulos desligados e BPM 222 na sessão, o `.json` traz a faixa do acervo | OK |
| C7 | Chave `_` posta na faixa e num módulo em memória não sai no arquivo; o acervo aberto continua com ela (cópia, não mutação) | OK |
| C8 | O `.json` exportado, reimportado, abre 1 cartão sem aviso de módulo faltando nem de chave removida | OK |
| C9 | «Baixar .json» do acervo inteiro continua igual ao importado | OK |
| C10 | O cabeçalho diz `v0.11.0` | OK |
| C11 | Nenhum erro de página | OK |

**Total: 15 de 15.** Faixas sintéticas: `borda-01` cita `["nao-existe", {objeto}, <id existente>]` (2 faltando,
1 módulo), `borda-02` cita o mesmo módulo duas vezes (1 módulo), `borda-03` não cita nenhum (sem `styleModules`).
**Prova de vida:** o mesmo teste no app da 0.10.0 reprova C10 e C1 e para em `exportSongJson is not defined`.

## Fora de escopo

- Importar faixas para o acervo aberto, excluir, mover, reordenar (entrega 3).
- Vários acervos no navegador e marcas «usei» por acervo (entrega 2).
- Exportar o Style recomposto em `.json` (o recomposto é estado de sessão; está no `.md`).
- Exportar um álbum como `.json` (não pedido; o acervo inteiro já sai pelo «Baixar .json»).

## Roteiro do dono (tela)

Vai inteiro no fecho do chat do turno que entrega a WO 0022.
