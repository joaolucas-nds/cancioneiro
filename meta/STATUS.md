# STATUS.md — Cancioneiro

> **O agora.** O que funciona, o que está em progresso, o que está quebrado, backlog curto.
> Rolante: item resolvido sai daqui e vai para o CHANGELOG. Médio/longo prazo vive no ROADMAP.

**Versão atual:** 0.4.0 · **Fase:** 2 — Ferramenta v0 + export MD

---

## Última sessão (2026-07-21)

Ferramenta publicada e rodando no GitHub Pages (confirmado por print do usuário). Descoberto que a entrega da sessão anterior FALHOU: implementei o export MD, commitei no ambiente do assistente e não entreguei arquivo — o usuário ficou na 0.3.0 sem saber. DEC-008 corrigida (lição registrada). Entregue agora: **export MD** (faixa/álbum/acervo) + **correção do bug de duplicação no Style recomposto** (dedup por contenção), visível no print do usuário.


## Funciona (pronto)

- **Ferramenta `app/index.html` v0:** importa/carrega JSON, renderiza álbuns→canções como cartões, copia Style/Lyrics/Exclude por botão, marca "usei" (auto ao copiar + toggle manual), filtra por álbum/estado/uso, busca por texto, painel de módulos de estilo que liga/desliga e recompõe o Style ao vivo, variantes e notas recolhíveis, export/import e "Baixar .json".
- **Esquema JSON canônico** (`schema/`) + biblioteca de 27 módulos nas cinco camadas.
- **Datasets:** `data/exemplo-cinzeiro.json` (1 faixa) e `data/demo.json` (2 álbuns, 3 faixas, módulos embutidos — instrumental + vocal + variantes).
- **Hospedagem:** `index.html` raiz redireciona para o app; pronto para GitHub Pages.
- **Prompt-modelo** (`schema/PROMPT-PARA-CHATS.md`): texto colável que faz um chat gerar JSON no esquema (cinco camadas + regra copiável/referência + saída JSON pura).
- **Validação** (`scripts/validate.py`): valida `data/*.json` contra o schema; código 1 se falhar. Comando no CLAUDE.md.
- **Export MD** (i-006): exportar faixa / álbum / acervo em `.md` legível (rótulo fora do bloco). Faixa usa o Style recomposto.
- **Publicado no GitHub Pages:** `joaolucas-nds.github.io/cancioneiro/app/index.html` — funcionando.

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
