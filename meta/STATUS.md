# STATUS.md — Cancioneiro

> **O agora.** O que funciona, o que está em progresso, o que está quebrado, backlog curto.
> Rolante: item resolvido sai daqui e vai para o CHANGELOG. Médio/longo prazo vive no ROADMAP.

**Versão atual:** 0.5.0 · **Fase:** 3a (painel de qualidade) concluída e conferida na tela · Fase 2 com i-008 em aberto · próxima: 3a.2 ou BPM

---

## Última conversa (2026-10-27, fecho da Fase 3a e da 0.5.0)

- **Fase 3a conferida na tela pelo dono:** os cinco itens do roteiro da WO 0009 ok `[relatado pelo dono, 2026-10-27]` — o painel mede o Style recomposto (298 em ar-01, não os 164 do base), acompanha o clique no chip, o botão copia o que se vê (FIX-007), o vermelho aparece em 1.271 com todos os módulos ligados, e a faixa instrumental avisa «no drums» sem avisar «no vocals».
- **0.5.0 fechada no CHANGELOG:** tudo o que entrou no app desde a 0.4.1 — painel de qualidade (DEC-018), FIX-004 a FIX-007, acervo autossuficiente (DEC-016).
- **Este STATUS foi reescrito, não acrescido.** Saíram os seis blocos «Última conversa» de 2026-07-21 a 2026-10-24: o que foi entregue está no CHANGELOG (0.4.1 e 0.5.0), as decisões no DECISIONS (DEC-010 a DEC-018, FIX-003 a FIX-007), e o detalhe de cada dia em `logs/`. As pendências de tela que eles declaravam abertas foram **todas fechadas pelo dono** (WO 0006 item 1; WO 0007 itens 1-3; WO 0009 itens 1-5), e a pergunta de 2026-10-17 está fechada desde a WO 0007. Nada único se perdeu: o que só existia aqui foi para «Notas de estado».

## Funciona (pronto)

- **Ferramenta `app/index.html`:** importa/carrega JSON, cartões por álbum, copiar Style/Lyrics/Exclude por botão (o botão entrega o texto que está na tela — FIX-007), marca «usei», filtros por álbum/estado/uso, busca, módulos de estilo que recompõem o Style ao vivo, variantes e notas recolhíveis, «Baixar .json» limpo e «Importar .json» que saneia chaves internas e diz quantas removeu (FIX-004/006).
- **Painel de qualidade (0.5.0, DEC-018):** linha abaixo de Style, Lyrics e Exclude com caracteres contra o limite do campo, tags do Style e negações «no X». Vermelho só para truncamento.
- **Esquema JSON canônico** (`schema/`). Biblioteca de referência para autoria em `schema/style-modules.json` (27 módulos, sete camadas); cada acervo traz os seus (DEC-016).
- **Datasets:** `data/exemplo-cinzeiro.json` (1 faixa, com os 5 módulos que cita) e `data/demo.json` (2 álbuns, 3 faixas). O álbum de referências do dono mora fora do repo, em `../album-referencias (1).json` (7 faixas, 50 módulos).
- **Validação** (`scripts/validate.py`): sintaxe, esquema (com `jsonschema`) e integridade referencial dos módulos; código 1 se falhar; a última linha diz se o esquema foi de fato conferido.
- **Export MD** (faixa / álbum / acervo), com o Style recomposto e o rótulo fora do bloco.
- **Prompt-modelo** (`schema/PROMPT-PARA-CHATS.md`) para chats gerarem JSON no esquema.
- **Publicado no GitHub Pages** em `https://joaolucas-nds.github.io/cancioneiro/app/index.html` — o push em `main` publica.

## Em progresso

- (nada)

## Quebrado / pendências que travam

- (nada quebrado)

## Pendências do dono

- **Instalar o validador de esquema nesta máquina.** Sem `jsonschema` e `referencing`, o `validate.py` só confere sintaxe e diz `ESQUEMA NAO CONFERIDO` na última linha. Uma vez, no Git Bash ou no CMD: `pip install jsonschema referencing --break-system-packages`. Depois, `python3 scripts/validate.py` deve terminar em `Tudo conforme ao esquema.` — o arquivo do álbum já foi validado fora daqui com 0 erros.
- **Colar as Instruções no painel do Projeto.** O painel ainda tem a versão anterior à WO 0008 e diverge do `INSTRUCOES-DO-PROJETO.md` em duas linhas: `**Config:**` (falta `/ultracode`) e `**Commit:**` (falta «Bloco git parcial (só `add`) não serve.»). Abrir o arquivo, copiar tudo, colar no painel.

## Backlog curto (próximas ações concretas)

1. **3a.2 — sugerir o que cortar quando há tags demais** (i-026). 7 de 7 faixas do álbum já acendem âmbar; aviso que sempre acende vira paisagem.
2. **Controle de BPM** (i-005) — pedido explícito na premissa original, ainda não feito.
3. **O app declarar a própria versão** (i-027) — pequeno; torna todo print datável.
4. **Testar o prompt-modelo ponta a ponta:** colar num chat, gerar uma faixa, importar.
5. **Converter 1 álbum real** (i-008) — depende de o dono trazer um `.md` de origem para a pasta-pai.

## Notas de estado

- **Repo local do dono:** `C:\Users\alexk\Tools\cancioneiro\cancioneiro` (Windows). O chat lê e grava na pasta vinculada; commit e push são do Code (DEC-010). A pasta-pai guarda relatórios, notas e o acervo do dono, fora do Git; o lido vai para `../notas-arquivadas/`.
- **Canal:** pasta vinculada é o padrão; a cópia achatada (FlatDrop) é reserva (DEC-017).
- **Limites do Suno:** o v6 saiu em 2026-09-09 e a nota oficial não documenta limite de campo; os números do painel vêm de fonte secundária, com fonte e data no `QUALITY_LIMITS` (DEC-018). Reconferir quando houver documentação oficial. O `meta/HISTORY.md` ainda descreve o v5.5 e precisa de uma atualização sobre o v6.
- **Limite conhecido:** `tryAutoLoad` (carregamento automático pelo Pages) não saneia chaves internas — só a importação por arquivo faz isso. Inócuo enquanto nenhum acervo contaminado for para `data/`.
- **Pendência de contexto — ASU:** o dono perguntou se o «modo ASU» do KCM seria melhor que o modo Code para este projeto; ficou pendente até ele trazer a descrição do ASU `[relatado pelo dono, sem material de apoio]`.
- Os álbuns antigos de julho não estão na pasta. Para converter um (i-008), trazer o `.md` de origem para a pasta-pai.
- Design: na recomposição do Style a base manda — desligar um módulo não remove o que já está no style base; módulos só somam. O dedup compara sequências de palavras (FIX-003).
