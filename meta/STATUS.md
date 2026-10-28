# STATUS.md — Cancioneiro

> **O agora.** O que funciona, o que está em progresso, o que está quebrado, backlog curto.
> Rolante: item resolvido sai daqui e vai para o CHANGELOG. Médio/longo prazo vive no ROADMAP.

**Versão atual:** 0.7.0 · **Fase:** 3a, 3a.2 e o BPM da 3b concluídos · prompt-modelo com contrato de módulos e botões de prompt/exemplo aplicados (WO 0015), à espera do reteste e da conferência na tela · Fase 2 com i-008 em aberto

---

## Última conversa (2026-10-28, prompt-modelo e módulos)

- **Teste base do prompt-modelo** `[relatado pelo dono]`: três chats Sonnet 5.5 fora de Projeto. O que o prompt ensinava saiu certo em 9 de 9 faixas (JSON puro, zero rótulos, BPM coerente); o que ele calava, não — os três inventaram um formato de módulo e o aninharam na faixa, e 5 de 9 bases saíram com 10 tags ou mais `[medido por instrumento]`. Os três JSONs ficam na pasta-pai como linha de base do reteste.
- **Spec `meta/specs/261028-prompt-modelo-e-modulos.md` decidida** (1a, 2a, 3a, 4a, e a 5 da nota do dono) e aplicada pela WO 0015: DEC-021 e FIX-009.
- **Este bloco substitui o anterior, de 2026-10-28, que fechava a 0.7.0.** O que ele dizia está no CHANGELOG [0.7.0], no DECISIONS (DEC-020, FIX-008) e em `logs/2026-10-28.md`.

## Funciona (pronto)

- **Ferramenta `app/index.html`:** importa/carrega JSON, cartões por álbum, copiar Style/Lyrics/Exclude por botão (o botão entrega o texto que está na tela — FIX-007), marca «usei», filtros por álbum/estado/uso, busca, módulos de estilo que recompõem o Style ao vivo, variantes e notas recolhíveis, «Baixar .json» limpo e «Importar .json» que saneia chaves internas e diz quantas removeu (FIX-004/006). A versão aparece no cabeçalho.
- **Painel de qualidade (0.5.0, DEC-018):** linha abaixo de Style, Lyrics e Exclude com caracteres contra o limite do campo, tags do Style e negações «no X». Vermelho só para truncamento.
- **Custo de cada módulo no chip (0.6.0, DEC-019):** com o painel de módulos aberto, cada chip mostra `−N`, `+N` ou `0` tags; a linha de qualidade diz quanto o style base usa sozinho quando o recomposto passa de 10.
- **Controle de BPM no cartão (0.7.0, DEC-020):** campo 20-300 com `−5`/`+5` e «voltar a N» governa todo «NN bpm» do Style principal; o chip de andamento é atalho (no máximo um ligado); variantes e «Baixar .json» não mudam; o valor é só da sessão.
- **Esquema JSON canônico** (`schema/`). Biblioteca de referência para autoria em `schema/style-modules.json` (27 módulos, sete camadas); cada acervo traz os seus (DEC-016).
- **Datasets:** `data/exemplo-cinzeiro.json` (1 faixa, com os 5 módulos que cita) e `data/demo.json` (2 álbuns, 3 faixas). O álbum de referências do dono mora fora do repo, em `../album-referencias (1).json` (7 faixas, 50 módulos).
- **Validação** (`scripts/validate.py`): sintaxe, esquema (com `jsonschema`), integridade referencial dos módulos (id ausente ou objeto no lugar do id, sem traceback — FIX-009), versão igual nos quatro lugares, um BPM só por faixa (DEC-020) e as marcações do prompt que o app lê (DEC-021); código 1 se falhar; a última linha diz se o esquema foi de fato conferido.
- **Export MD** (faixa / álbum / acervo), com o Style recomposto e o rótulo fora do bloco.
- **Publicado no GitHub Pages** em `https://joaolucas-nds.github.io/cancioneiro/app/index.html` — o push em `main` publica.

## Em progresso

- **Prompt-modelo e módulos (DEC-021, FIX-009; i-028, i-031)** — aplicado pela WO 0015, testado pelo chat numa cópia (Desfecho da spec). Falta: (1) a conferência na tela, no app publicado; (2) o reteste do prompt com três chats nas condições do teste base. Com os dois, fecha a 0.8.0 (CHANGELOG, README e CONTEXT).
  - Prompt (`schema/PROMPT-PARA-CHATS.md`): contrato de módulo da DEC-016 (módulos na coleção, faixa cita ids, citado = ligado), style com 6 a 8 tags e até 10 com os módulos ligados, BPM só em módulo de andamento.
  - App: botões «Prompt para chats» (janela com «Meu pedido») e «Baixar exemplo», que buscam o prompt e o `data/demo.json` no clique — fonte única; e o aviso na importação quando um módulo citado não existe na coleção.

## Quebrado / pendências que travam

- (nada quebrado)

## Pendências do dono

- **Conferir na tela e retestar o prompt** — roteiro entregue pelo chat na conversa de 2026-10-28, depois do push da WO 0015.
- **Instalar o validador de esquema nesta máquina.** Sem `jsonschema` e `referencing`, o `validate.py` só confere sintaxe e diz `ESQUEMA NAO CONFERIDO` na última linha. Uma vez, no CMD: `pip install jsonschema referencing --break-system-packages`. Depois, `python3 scripts/validate.py` deve terminar em `Tudo conforme ao esquema.`
- **Trazer os álbuns antigos** para a pasta-pai, quando quiser — o dono disse que vai trazer; desbloqueiam a i-008.

## Backlog curto (próximas ações concretas)

1. **Fechar a frente do prompt-modelo** na 0.8.0, depois do roteiro do dono.
2. **Ordem dos campos no cartão** (i-030) — Lyrics acima do Style, como no Suno, configurável.
3. **Pesquisar outras plataformas de música por IA** (i-032) — um turno de pesquisa antes de qualquer mudança de esquema.
4. **Converter 1 álbum real** (i-008) — quando os `.md` de origem chegarem à pasta-pai.
5. **Avisar palavra de andamento que contradiz o BPM** (i-029) — pede uma tabela palavra → faixa de BPM, com fonte e data.
6. **Importar prompts prontos dos álbuns como módulos** — o último ⬜ da 3b no ROADMAP; ainda sem spec.

## Notas de estado

- **Repo local do dono:** `C:\Users\alexk\Tools\cancioneiro\cancioneiro` (Windows). O chat lê e grava na pasta vinculada; commit e push são do Code (DEC-010). A pasta-pai guarda relatórios, notas e o acervo do dono, fora do Git; o lido vai para `../notas-arquivadas/`.
- **Canal:** pasta vinculada é o padrão; a cópia achatada (FlatDrop) é reserva (DEC-017).
- **Limites do Suno:** o v6 saiu em 2026-09-09 e a nota oficial não documenta limite de campo; os números do painel vêm de fonte secundária, com fonte e data no `QUALITY_LIMITS` (DEC-018). Outra fonte secundária (2026-08) põe o ideal em 4 a 7 descritores; o prompt usa 6 a 8. Reconferir quando houver documentação oficial. O `meta/HISTORY.md` ainda descreve o v5.5 e precisa de uma atualização sobre o v6.
- **Botões de prompt e exemplo:** dependem de rede e do Pages. No `file://`, só funcionam se o Pages aceitar o `fetch` de uma página local — não conferido; sem isso, a janela mostra o link para a versão publicada (DEC-021).
- **Estado de sessão** (módulos ligados e BPM escolhido) sobrevive a filtro, busca e «marcar usei»; volta ao acervo ao recarregar a página ou importar de novo (FIX-008, DEC-020).
- **Limite conhecido:** `tryAutoLoad` (carregamento automático pelo Pages) não saneia chaves internas — só a importação por arquivo faz isso. Inócuo enquanto nenhum acervo contaminado for para `data/`.
- **Pendência de contexto — ASU:** o dono perguntou se o «modo ASU» do KCM seria melhor que o modo Code para este projeto; ficou pendente até ele trazer a descrição do ASU `[relatado pelo dono, sem material de apoio]`.
- Design: na recomposição do Style a base manda — desligar um módulo não remove o que já está no style base; módulos só somam. O dedup compara sequências de palavras (FIX-003). Os módulos de gênero e de andamento costumam custar 0 tag por isso (DEC-019). O chip de andamento é atalho do controle de BPM, no máximo um ligado (DEC-020).
