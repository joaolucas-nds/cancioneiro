# STATUS.md — Cancioneiro

> **O agora.** O que funciona, o que está em progresso, o que está quebrado, backlog curto.
> Rolante: item resolvido sai daqui e vai para o CHANGELOG. Médio/longo prazo vive no ROADMAP.

**Versão atual:** 0.4.1 · **Fase:** 2 concluída · Fase 3 (qualidade de prompt) a iniciar

---

## Última conversa (2026-10-20, fatia 3 do kit v1.127.0)

- Kit: fatia 3 aplicada (WO 0004). `meta/CEREBRO.md` adotado do template v1.127.0 com três especializações (DEC-013); `INSTRUCOES-DO-PROJETO.md` fundido preservando o domínio (DEC-014); `meta/LOG-TEMPLATE.md` alinhado à cadência de turno e à DEC-010.
- **Pendência do dono:** o painel do Projeto no claude.ai ainda manda as três linhas revogadas — colar nele o conteúdo novo de `INSTRUCOES-DO-PROJETO.md`.
- Pendente do kit: fatia 4 (demais `meta/`, `meta/specs/`, títulos `## Última sessão` deste arquivo).

## Última sessão (2026-10-20, kit v1.127.0 — fatias 1 e 2)

- Kit: fatias 1 e 2 do v1.127.0 aplicadas. Skills `apply-wo`, `wrap`, `sondar` instaladas e `apply-spec` removida; `.claude/settings.json` com `Write` e `additionalDirectories`; `CLAUDE.md`, `.gitignore` e `.flatdropignore` atualizados.
- Pendente do kit: os demais `meta/` (fatia 4); a pasta morta `meta/specs/`. (CEREBRO e Instruções saíram da pendência: fatia 3 aplicada, ver bloco acima.)
- Pendente de varredura: cadência «sessão→turno» — **46 ocorrências varridas** (`grep -rnoiE` em `meta/ CLAUDE.md INSTRUCOES-DO-PROJETO.md README.md .claude/ .gitignore .flatdropignore logs/`; medida nas fatias 1-2: 52): **corrigidas nesta fatia 20** (CEREBRO 11, Instruções 3, LOG-TEMPLATE 6), **legítimas e justificadas 17**, **a corrigir 2** (os dois títulos `## Última sessão` do próprio STATUS, que viram `## Última conversa` na fatia 4). Declarada **PENDENTE**, não encerrada.
- Pendente de produto: a pergunta de 2026-10-17 sobre o `album-referencias.json` (pasta-pai) continua aberta.

## Última sessão (2026-07-21, auditoria)

Auditoria completa do projeto contra a premissa original + pesquisa de refinamento. Resultado: **7 divergências de documentação** corrigidas (README dizia "v0.1.0, ferramenta a construir"; i-009 já implementado mas marcado aberto; backlog com item já feito) e **1 bug real corrigido** (FIX-003: dedup por substring barrava "female vocals" quando a base tinha "male vocals"). Pesquisa trouxe constraints verificáveis e acionáveis: limite de ~1.000 caracteres no Style com **truncamento silencioso**, teto prático de ~10 tags, e campo de exclusão mais confiável que negação no texto. Consolidado no HISTORY (seções 9-13) e vira a Fase 3.


## Funciona (pronto)

- **Ferramenta `app/index.html` v0:** importa/carrega JSON, renderiza álbuns→canções como cartões, copia Style/Lyrics/Exclude por botão, marca "usei" (auto ao copiar + toggle manual), filtra por álbum/estado/uso, busca por texto, painel de módulos de estilo que liga/desliga e recompõe o Style ao vivo, variantes e notas recolhíveis, export/import e "Baixar .json".
- **Esquema JSON canônico** (`schema/`) + biblioteca de 27 módulos nas cinco camadas.
- **Datasets:** `data/exemplo-cinzeiro.json` (1 faixa) e `data/demo.json` (2 álbuns, 3 faixas, módulos embutidos — instrumental + vocal + variantes).
- **Hospedagem:** `index.html` raiz redireciona para o app; pronto para GitHub Pages.
- **Prompt-modelo** (`schema/PROMPT-PARA-CHATS.md`): texto colável que faz um chat gerar JSON no esquema (cinco camadas + regra copiável/referência + saída JSON pura).
- **Validação** (`scripts/validate.py`): valida `data/*.json` contra o schema; código 1 se falhar. Comando no CLAUDE.md.
- **Export MD** (i-006): exportar faixa / álbum / acervo em `.md` legível (rótulo fora do bloco). Faixa usa o Style recomposto.
- **Publicado no GitHub Pages** em `https://joaolucas-nds.github.io/cancioneiro/app/index.html` — validado de olho pelo dono, funcionando `[relatado pelo dono, com print da interface em 2026-07-21]`.
- **0.4.1 aplicada no repo do dono** `[verificado no mount em 2026-07-21: app com FIX-003, STATUS/CHANGELOG em 0.4.1]`.

## Em progresso

- (nada em execução — aguardando escolha da Fase 3)

## Quebrado / pendências que travam

- (nada quebrado — lógica testada, fetch validado nos dois layouts)

## Backlog curto (próximas ações concretas)

1. **Painel de qualidade do prompt** (Fase 3, recomendado): contador de caracteres do Style (limite ~1.000, o Suno trunca em silêncio), contador de tags com aviso acima de ~10, e detecção de "no X" no style sugerindo migrar para `excludeStyles`. Fundamentado no HISTORY §9-11.
2. **Controle de BPM** (i-005) — pedido explícito na premissa original, ainda não feito.
3. **Converter 1 álbum real** (i-008) — depende de subir um `.md` de origem.
4. **Testar o prompt-modelo ponta a ponta:** colar num chat, gerar, importar.


## Notas de estado

- **Repo local do dono:** `C:\Users\alexk\Tools\cancioneiro` (Windows). O repositório é a fonte de verdade; o ambiente do assistente é descartável e NÃO sincroniza sozinho — ver DEC-008.
- **Fluxo de upload:** o dono usa FlatDrop para achatar a árvore ao subir no Projeto de chat (`_MANIFEST_cancioneiro.md` e `_TREE_cancioneiro.md` são artefatos dessa ferramenta, não fazem parte do repo). Por isso os arquivos chegam achatados no mount com nomes como `index__app.html`.
- **Pendência de contexto — ASU:** o dono perguntou se o "modo ASU" do KCM seria melhor que o modo Code para este projeto. O assistente NÃO tem a definição de ASU (o CEREBRO só o cita de passagem em nomenclatura de specs, `AAMMDD-asuNNNN.yaml`). Recomendação ficou pendente até o dono colar a descrição do ASU `[relatado pelo dono, sem material de apoio]`.
- Os álbuns antigos NÃO estão mais no mount desta sessão (o Projeto foi atualizado com os arquivos do cancioneiro). Para converter um álbum real, subir o `.md` de origem de novo.
- Nota de design: na recomposição de style, se um fragmento já está no style base, desligar o módulo não o remove — a base é a fonte, módulos só aumentam. Correto e intencional.
- O dedup compara **sequências de palavras** (não substring), após FIX-003. Plural simples é normalizado.
