# STATUS.md — Cancioneiro

> **O agora.** O que funciona, o que está em progresso, o que está quebrado, backlog curto.
> Rolante: item resolvido sai daqui e vai para o CHANGELOG. Médio/longo prazo vive no ROADMAP.

**Versão atual:** 0.8.0 · **Fase:** 3a, 3a.2, o BPM da 3b e o prompt-modelo com módulos concluídos e conferidos · Fase 2 com i-008 em aberto · próxima frente: a escolher (ver backlog)

---

## Última conversa (2026-10-29, reteste do prompt e fecho da 0.8.0)

- **Reteste do prompt-modelo** `[relatado pelo dono]`: dois chats Sonnet 5.5 fora de Projeto (Alto e Médio; o terceiro não veio). 6 de 6 faixas dentro do contrato de módulo e do orçamento (base 7-8 tags, recomposto 8-10), 0 rótulos, validador verde nos dois modos `[medido por instrumento]`. Tabela na spec `meta/specs/261028-prompt-modelo-e-modulos.md`.
- **Conferência na tela** `[relatado pelo dono]`: itens A1 a A5 ok, também visíveis nas capturas. 0.8.0 fechada (WO 0016).
- **Interface do Suno v6 medida nas capturas do dono:** v6-mini no plano gratuito; formulário Lyrics → Styles → opções → título; **sem campo de Exclude**. Registrado no `meta/HISTORY.md` §5.
- **Nota do dono `261029-1106.txt`** capturada como ideias: i-030 refinada, i-033 a i-036; e a i-037, achada nos `.md` exportados.
- **WO 0016 aplicada pelo Code** (`6a52111`, empurrado): os dez arquivos bateram com o hash de chegada; `validate.py` verde, só sintaxe (`jsonschema` ausente nesta máquina).
- **Este bloco substitui o anterior, de 2026-10-28, que abria o prompt-modelo.** O que ele dizia está no CHANGELOG [0.8.0], no DECISIONS (DEC-021, FIX-009) e em `logs/2026-10-28.md`.

## Funciona (pronto)

- **Ferramenta `app/index.html`:** importa/carrega JSON, cartões por álbum, copiar Style/Lyrics/Exclude por botão (o botão entrega o texto que está na tela — FIX-007), marca «usei», filtros por álbum/estado/uso, busca, módulos de estilo que recompõem o Style ao vivo, variantes e notas recolhíveis, «Baixar .json» limpo e «Importar .json» que saneia chaves internas e diz quantas removeu (FIX-004/006). A versão aparece no cabeçalho. A importação avisa quantos módulos citados não existem na coleção (FIX-009).
- **Painel de qualidade (0.5.0, DEC-018):** linha abaixo de Style, Lyrics e Exclude com caracteres contra o limite do campo, tags do Style e negações «no X». Vermelho só para truncamento.
- **Custo de cada módulo no chip (0.6.0, DEC-019):** com o painel de módulos aberto, cada chip mostra `−N`, `+N` ou `0` tags; a linha de qualidade diz quanto o style base usa sozinho quando o recomposto passa de 10.
- **Controle de BPM no cartão (0.7.0, DEC-020):** campo 20-300 com `−5`/`+5` e «voltar a N» governa todo «NN bpm» do Style principal; o chip de andamento é atalho (no máximo um ligado); variantes e «Baixar .json» não mudam; o valor é só da sessão.
- **Esquema JSON canônico** (`schema/`). Biblioteca de referência para autoria em `schema/style-modules.json` (27 módulos, sete camadas); cada acervo traz os seus (DEC-016).
- **Datasets:** `data/exemplo-cinzeiro.json` (1 faixa, com os 5 módulos que cita) e `data/demo.json` (2 álbuns, 3 faixas). O álbum de referências do dono mora fora do repo, em `../album-referencias (1).json` (7 faixas, 50 módulos).
- **Validação** (`scripts/validate.py`): sintaxe, esquema (com `jsonschema`), integridade referencial dos módulos (id ausente ou objeto no lugar do id, sem traceback — FIX-009), versão igual nos quatro lugares, um BPM só por faixa (DEC-020) e as marcações do prompt que o app lê (DEC-021); código 1 se falhar; a última linha diz se o esquema foi de fato conferido.
- **Export MD** (faixa / álbum / acervo), com o rótulo fora do bloco. A faixa sai com o Style recomposto (módulos e BPM da tela); álbum e acervo saem com o `style` base — ver i-037.
- **Prompt-modelo** (`schema/PROMPT-PARA-CHATS.md`, DEC-021): contrato de módulo, style com 6 a 8 tags e até 10 com os módulos ligados. Retestado em 2026-10-29: 6 de 6 faixas dentro do contrato e do orçamento.
- **Botões «Prompt para chats» e «Baixar exemplo»** (0.8.0, DEC-021): buscam o prompt e o `data/demo.json` do repositório no clique; a janela do prompt recebe o «Meu pedido».
- **Publicado no GitHub Pages** em `https://joaolucas-nds.github.io/cancioneiro/app/index.html` — o push em `main` publica.

## Em progresso

- (nada)

## Quebrado / pendências que travam

- (nada quebrado)

## Pendências do dono

- **Instalar o validador de esquema nesta máquina.** Sem `jsonschema` e `referencing`, o `validate.py` só confere sintaxe e diz `ESQUEMA NAO CONFERIDO` na última linha. Uma vez, no CMD: `pip install jsonschema referencing --break-system-packages`. Depois, `python3 scripts/validate.py` deve terminar em `Tudo conforme ao esquema.`
- **Trazer os álbuns antigos** para a pasta-pai, quando quiser; desbloqueiam a i-008.

## Backlog curto (próximas ações concretas)

1. **Conveniências de uso** — da nota do dono de 2026-10-29: estrutura do cartão configurável e salva no navegador (i-030), copiar o título (i-033), arrastar o `.json` (i-034), acervo que sobrevive ao fechar o navegador (i-035, pede DEC), prompt que entrega arquivo (i-036, pede reteste). Uma spec com as decisões do dono.
2. **Export de álbum e acervo com o Style da tela?** (i-037) — decidir junto da 1.
3. **Pesquisar outras plataformas de música por IA** (i-032) — um turno de pesquisa antes de qualquer mudança de esquema.
4. **Converter 1 álbum real** (i-008) — quando os `.md` de origem chegarem à pasta-pai.
5. **Avisar palavra de andamento que contradiz o BPM** (i-029) — pede uma tabela palavra → faixa de BPM, com fonte e data.
6. **Importar prompts prontos dos álbuns como módulos** — o último ⬜ da 3b no ROADMAP; ainda sem spec.

## Notas de estado

- **Repo local do dono:** `C:\Users\alexk\Tools\cancioneiro\cancioneiro` (Windows). O chat lê e grava na pasta vinculada; commit e push são do Code (DEC-010). A pasta-pai guarda relatórios, notas e o acervo do dono, fora do Git; o lido vai para `../notas-arquivadas/`.
- **Canal:** pasta vinculada é o padrão; a cópia achatada (FlatDrop) é reserva (DEC-017).
- **Limites do Suno:** o v6 saiu em 2026-09-09 e a nota oficial não documenta limite de campo; os números do painel vêm de fonte secundária, com fonte e data no `QUALITY_LIMITS` (DEC-018). Outra fonte secundária (2026-08) põe o ideal em 4 a 7 descritores; o prompt usa 6 a 8. Reconferir quando houver documentação oficial. O `meta/HISTORY.md` §5 ganhou a interface do v6 vista na conta (2026-10-29); o resto do arquivo ainda descreve o v5.5.
- **Exclude no v6-mini:** o formulário gratuito não tem o campo (capturas de 2026-10-29). O app segue mostrando o bloco Exclude e o painel segue sugerindo levar «no X» para lá; o dado continua útil para quem tem o campo. Decidir na spec das conveniências (i-030: ocultar campos).
- **Botões de prompt e exemplo:** dependem de rede e do Pages. No `file://`, só funcionam se o Pages aceitar o `fetch` de uma página local — não conferido (o dono abriu o `file://` em 2026-10-29, sem relatar o resultado do botão); sem isso, a janela mostra o link para a versão publicada (DEC-021).
- **Estado de sessão** (módulos ligados e BPM escolhido) sobrevive a filtro, busca e «marcar usei»; volta ao acervo ao recarregar a página ou importar de novo (FIX-008, DEC-020).
- **Limite conhecido:** `tryAutoLoad` (carregamento automático pelo Pages) não saneia chaves internas — só a importação por arquivo faz isso. Inócuo enquanto nenhum acervo contaminado for para `data/`.
- **Pendência de contexto — ASU:** o dono perguntou se o «modo ASU» do KCM seria melhor que o modo Code para este projeto; ficou pendente até ele trazer a descrição do ASU `[relatado pelo dono, sem material de apoio]`.
- Design: na recomposição do Style a base manda — desligar um módulo não remove o que já está no style base; módulos só somam. O dedup compara sequências de palavras (FIX-003). Os módulos de gênero e de andamento costumam custar 0 tag por isso (DEC-019). O chip de andamento é atalho do controle de BPM, no máximo um ligado (DEC-020).
