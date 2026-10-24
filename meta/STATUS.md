# STATUS.md — Cancioneiro

> **O agora.** O que funciona, o que está em progresso, o que está quebrado, backlog curto.
> Rolante: item resolvido sai daqui e vai para o CHANGELOG. Médio/longo prazo vive no ROADMAP.

**Versão atual:** 0.4.1 · **Fase:** 2 concluída · Fase 3 (qualidade de prompt) a iniciar

---

## Última conversa (2026-10-24, WO 0008 — merge do kit v1.131.0)

- Kit v1.131.0 aplicado numa fatia só (`db0e234`, DEC-017): CEREBRO no template novo (pasta vinculada como canal padrão, achatado como reserva) com as 3 especializações reinjetadas — «Técnicas específicas» agora com **8 itens** (medido: `sed ... | grep -c "^- \*\*"` = 8). `INSTRUCOES-DO-PROJETO.md` em 6.438 caracteres (teto 7.450). `CLAUDE.md` deliberadamente fora de sincronia (motivo na DEC-017). Modelo de WO e as 3 skills adotados, com a regra de idempotência pelo texto novo INTEIRO.
- Medido pelo chat (não reconferido aqui): o `album-referencias (1).json` baixado pelo app corrigido tem 0 chaves `_`, 7 faixas, 50 módulos, idêntico ao antigo menos as 7 chaves (27.862 → 27.638 bytes). Primeira validação de esquema real do projeto, feita no ambiente do chat: 0 erros de esquema, 0 ids de módulo órfãos.
- **Pendência:** na máquina do dono `jsonschema`/`referencing` continuam ausentes e o `validate.py` segue dizendo `ESQUEMA NAO CONFERIDO`. Pendências de tela da WO 0006/0007 seguem abertas.

## Última conversa (2026-10-23, WO 0007 — sanear na importação)

- FIX-006 aplicado (`131f900`): `stripInternalKeys` remove, na importação por arquivo, as chaves com prefixo `_` que versões antigas vazaram para o JSON, e o toast de sucesso diz quantas saíram. O saneamento roda FORA do `try` da carga. Corrige o que o FIX-004 deixou: parou de GRAVAR `_activeModules`, mas devolvia a que já estava no arquivo.
- A pergunta de 2026-10-17 (`../261017-2231.txt`) está **fechada** nas duas metades: o que havia de errado com o arquivo (FIX-004 e FIX-006) e como evitar que erros assim continuem (FIX-005, nas duas pontas: o `catch` do app e o rodapé do `validate.py`).
- **Pendência do dono:** conferência na tela — importar o `album-referencias.json` e ver o toast dizer 7 campos removidos; baixar de novo e conferir 0 `_activeModules`. Os 4 itens da WO 0006 seguem sem carimbo. `jsonschema` segue não instalado: conformidade de esquema NÃO CONFERIDA.
- Limite conhecido: `tryAutoLoad` não sanea (só a importação por arquivo).

## Última conversa (2026-10-22, WO 0006 — round-trip do acervo)

- Round-trip corrigido (FIX-004/005): o estado dos módulos ligados saiu de dentro da coleção (`App.activeModules[song.id]`) e o `importFromFile` separa o `try` do parse do `try` da carga. `data/exemplo-cinzeiro.json` completado com os 5 módulos que citava (DEC-016); `scripts/validate.py` ganha checagem de referência cruzada e passa a declarar quando o esquema NÃO foi conferido (sem `jsonschema`).
- A pergunta de 2026-10-17 sobre o `album-referencias.json` está **fechada**. A resposta ao «como evitar que erros como esse continuem» é o FIX-005 (mensagem que nomeia causa só pode vir da operação que a produz), não o FIX-004.
- **Pendência do dono:** os 4 itens do roteiro de conferência na tela da WO 0006 (importar, baixar, reimportar, chip) — não carimbados como feitos.

## Última conversa (2026-10-20, kit v1.127.0 — fatias 1 a 4)

- Kit: as quatro fatias do v1.127.0 aplicadas (WOs 0002-0005). Skills `apply-wo`, `wrap`, `sondar` instaladas e `apply-spec` removida; `.claude/settings.json` com `Write` e `additionalDirectories`; `CLAUDE.md`, `.gitignore` e `.flatdropignore` atualizados. `meta/CEREBRO.md` adotado do template com três especializações (DEC-013); `INSTRUCOES-DO-PROJETO.md` fundido preservando o domínio (DEC-014); `meta/LOG-TEMPLATE.md` alinhado à cadência de turno e à DEC-010. Fatia 4: os demais `meta/` ficam na forma do projeto, entra `meta/SPEC.md`, a pasta morta `meta/specs/` sai (DEC-015); ideias i-022 a i-024 capturadas.
- **Pendência do dono:** o painel do Projeto no claude.ai ainda manda as três linhas revogadas — colar nele o conteúdo novo de `INSTRUCOES-DO-PROJETO.md`.
- Varredura de cadência «sessão→turno»: **ENCERRADA na primeira classe** («manda» = zero ocorrências em arquivo que dirige comportamento). O total medido continua alto porque as outras quatro classes são legítimas: relato histórico datado, domínio (sessão do navegador/Suno), contraste deliberado do kit e meta-documentação da própria correção. Números do fecho no relatório da WO 0005.
- Pendente de produto: a pergunta de 2026-10-17 sobre o `album-referencias.json` (pasta-pai) continua aberta.

## Última conversa (2026-07-21, auditoria)

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
