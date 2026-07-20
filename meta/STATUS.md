# STATUS.md — Cancioneiro

> **O agora.** O que funciona, o que está em progresso, o que está quebrado, backlog curto.
> Rolante: item resolvido sai daqui e vai para o CHANGELOG. Médio/longo prazo vive no ROADMAP.

**Versão atual:** 0.3.0 · **Fase:** 2 — Ferramenta v0 + tooling de acervo

---

## Última sessão (2026-07-19, parte 3)

Verifiquei a integridade do repo (2 commits, JSON conformes ao schema por validação estrutural, lógica 11/11, HTML são). Entreguei o **prompt-modelo para chats** (`schema/PROMPT-PARA-CHATS.md`) — fecha o ciclo chat→ferramenta — e um **script de validação** (`scripts/validate.py`) que checa datasets contra o schema (migrado para a API nova do jsonschema, testado com caso negativo).


## Funciona (pronto)

- **Ferramenta `app/index.html` v0:** importa/carrega JSON, renderiza álbuns→canções como cartões, copia Style/Lyrics/Exclude por botão, marca "usei" (auto ao copiar + toggle manual), filtra por álbum/estado/uso, busca por texto, painel de módulos de estilo que liga/desliga e recompõe o Style ao vivo, variantes e notas recolhíveis, export/import e "Baixar .json".
- **Esquema JSON canônico** (`schema/`) + biblioteca de 27 módulos nas cinco camadas.
- **Datasets:** `data/exemplo-cinzeiro.json` (1 faixa) e `data/demo.json` (2 álbuns, 3 faixas, módulos embutidos — instrumental + vocal + variantes).
- **Hospedagem:** `index.html` raiz redireciona para o app; pronto para GitHub Pages.
- **Prompt-modelo** (`schema/PROMPT-PARA-CHATS.md`): texto colável que faz um chat gerar JSON no esquema (cinco camadas + regra copiável/referência + saída JSON pura).
- **Validação** (`scripts/validate.py`): valida `data/*.json` contra o schema; código 1 se falhar. Comando no CLAUDE.md.

## Em progresso

- Validação visual da ferramenta (aguarda você abrir e dar o olhar de dono).

## Quebrado / pendências que travam

- (nada quebrado — lógica testada, fetch validado nos dois layouts)

## Backlog curto (próximas ações concretas)

1. **Publicar no GitHub Pages** e abrir o link para validar de olho (passo seu — instruções na entrega).
2. **Ajustes de UI pós-validação visual** — melhor levar para o Claude Code (iteração fina por spec).
3. **Converter 1 álbum inteiro** (candidato: `album_guia_suno.md`) como dataset real, validando com `scripts/validate.py`.
4. **Testar o prompt-modelo na prática:** colar num chat, gerar 1 faixa, importar na ferramenta, ver se fecha o ciclo.

## Notas de estado

- Os álbuns antigos NÃO estão mais no mount desta sessão (o Projeto foi atualizado com os arquivos do cancioneiro). Para converter um álbum real, subir o `.md` de origem de novo.
- Nota de design registrada: na recomposição de style, se um fragmento já está no style base, desligar o módulo correspondente não o remove do texto — a base é a fonte, módulos só aumentam. Comportamento correto e intencional.
