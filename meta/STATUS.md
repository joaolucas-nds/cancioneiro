# STATUS.md — Cancioneiro

> **O agora.** O que funciona, o que está em progresso, o que está quebrado, backlog curto.
> Rolante: item resolvido sai daqui e vai para o CHANGELOG. Médio/longo prazo vive no ROADMAP.

**Versão atual:** 0.8.0 · **Fase:** 3a, 3a.2, o BPM da 3b e o prompt-modelo concluídos · conveniências de uso aplicadas (WO 0017), à espera da tela e do reteste curto do prompt · Fase 2 com i-008 desbloqueada

---

## Última conversa (2026-10-29, conveniências de uso)

- **Decisões do dono** sobre a nota `261029-1106.txt`: D1 acervo guardado no navegador, D2 estrutura do cartão completa, D3 aviso de negação some com o Exclude oculto, D4 prompt pede arquivo (e, sem arquivo, o JSON em bloco de código), D5 export de álbum segue a tela. Spec `meta/specs/261029-conveniencias-de-uso.md`; DEC-022 e DEC-023; aplicadas pela WO 0017, testadas pelo chat numa cópia (34 de 34).
- **Fecho do chat (DEC-024):** a linha `/apply-wo` vem antes do «Próximo». CEREBRO e Instruções mudaram — o dono cola as Instruções novas no painel do Projeto.
- **Álbuns antigos chegaram** à pasta-pai (`../Album Rainha da Preguiça/`, `../Albuns/`, 19 arquivos, ~44 mil linhas): a i-008 está desbloqueada; ainda não lidos.
- **Este bloco substitui o anterior, de 2026-10-29, que fechava a 0.8.0.** O que ele dizia está no CHANGELOG [0.8.0], na spec do prompt-modelo e em `logs/2026-10-29.md`.

## Funciona (pronto)

- **Ferramenta `app/index.html`:** importa/carrega JSON, cartões por álbum, copiar Style/Lyrics/Exclude por botão (o botão entrega o texto que está na tela — FIX-007), marca «usei», filtros por álbum/estado/uso, busca, módulos de estilo que recompõem o Style ao vivo, variantes e notas recolhíveis, «Baixar .json» limpo e «Importar .json» que saneia chaves internas e diz quantas removeu (FIX-004/006). A versão aparece no cabeçalho. A importação avisa quantos módulos citados não existem na coleção (FIX-009).
- **Painel de qualidade (0.5.0, DEC-018):** linha abaixo de Style, Lyrics e Exclude com caracteres contra o limite do campo, tags do Style e negações «no X». Vermelho só para truncamento.
- **Custo de cada módulo no chip (0.6.0, DEC-019):** com o painel de módulos aberto, cada chip mostra `−N`, `+N` ou `0` tags; a linha de qualidade diz quanto o style base usa sozinho quando o recomposto passa de 10.
- **Controle de BPM no cartão (0.7.0, DEC-020):** campo 20-300 com `−5`/`+5` e «voltar a N» governa todo «NN bpm» do Style principal; o chip de andamento é atalho (no máximo um ligado); variantes e «Baixar .json» não mudam; o valor é só da sessão.
- **Esquema JSON canônico** (`schema/`). Biblioteca de referência para autoria em `schema/style-modules.json` (27 módulos, sete camadas); cada acervo traz os seus (DEC-016).
- **Datasets:** `data/exemplo-cinzeiro.json` (1 faixa, com os 5 módulos que cita) e `data/demo.json` (2 álbuns, 3 faixas). O álbum de referências do dono mora fora do repo, em `../album-referencias (1).json` (7 faixas, 50 módulos).
- **Validação** (`scripts/validate.py`): sintaxe, esquema (com `jsonschema`), integridade referencial dos módulos (id ausente ou objeto no lugar do id, sem traceback — FIX-009), versão igual nos quatro lugares, um BPM só por faixa (DEC-020) e as marcações do prompt que o app lê (DEC-021); código 1 se falhar; a última linha diz se o esquema foi de fato conferido.
- **Export MD** (faixa / álbum / acervo), com o rótulo fora do bloco. Na 0.8.0 a faixa sai com o Style recomposto e álbum/acervo com o `style` base; a WO 0017 faz os três seguirem a tela (D5, à espera da conferência).
- **Prompt-modelo** (`schema/PROMPT-PARA-CHATS.md`, DEC-021): contrato de módulo, style com 6 a 8 tags e até 10 com os módulos ligados. Retestado em 2026-10-29: 6 de 6 faixas dentro do contrato e do orçamento.
- **Botões «Prompt para chats» e «Baixar exemplo»** (0.8.0, DEC-021): buscam o prompt e o `data/demo.json` do repositório no clique; a janela do prompt recebe o «Meu pedido».
- **Publicado no GitHub Pages** em `https://joaolucas-nds.github.io/cancioneiro/app/index.html` — o push em `main` publica.

## Em progresso

- **Conveniências de uso (DEC-022, DEC-023; i-030, i-033 a i-037)** — aplicadas pela WO 0017. Falta: (1) a conferência na tela, no app publicado; (2) o reteste curto do prompt (só a «Saída» mudou). Com os dois, fecha a 0.9.0 (CHANGELOG, README já descreve).
  - «Estrutura do cartão» (ordem e mostrar/ocultar de 6 blocos, no navegador; padrão = ordem antiga); «copiar título»; arrastar o `.json` para a tela; o último acervo importado volta ao abrir, com a origem e «esquecer» na barra; export de álbum e acervo com o Style da tela.
  - Prompt: pede um `.json` para baixar; sem arquivo, o JSON num único bloco de código. A importação aceita a resposta colada inteira e avisa que extraiu.

## Quebrado / pendências que travam

- (nada quebrado)

## Pendências do dono

- **Colar as Instruções novas no painel do Projeto** — `INSTRUCOES-DO-PROJETO.md` mudou na WO 0017 (DEC-024).
- **Conferir na tela e retestar o prompt** — roteiro entregue pelo chat na conversa de 2026-10-29, depois do push da WO 0017.
- **Instalar o validador de esquema nesta máquina.** Sem `jsonschema` e `referencing`, o `validate.py` só confere sintaxe e diz `ESQUEMA NAO CONFERIDO` na última linha. Uma vez, no CMD: `pip install jsonschema referencing --break-system-packages`. Depois, `python3 scripts/validate.py` deve terminar em `Tudo conforme ao esquema.`

## Backlog curto (próximas ações concretas)

1. **Fechar as conveniências** na 0.9.0, depois do roteiro do dono.
2. **Converter os álbuns antigos** (i-008) — chegaram em 2026-10-29; começar por medir o formato deles (sonda) e converter um.
3. **Pesquisar outras plataformas de música por IA** (i-032) — um turno de pesquisa antes de qualquer mudança de esquema.
4. **Avisar palavra de andamento que contradiz o BPM** (i-029) — pede uma tabela palavra → faixa de BPM, com fonte e data.
5. **Importar prompts prontos dos álbuns como módulos** — o último ⬜ da 3b no ROADMAP; combina com a 2.

## Notas de estado

- **Repo local do dono:** `C:\Users\alexk\Tools\cancioneiro\cancioneiro` (Windows). O chat lê e grava na pasta vinculada; commit e push são do Code (DEC-010). A pasta-pai guarda relatórios, notas e o acervo do dono, fora do Git; o lido vai para `../notas-arquivadas/`.
- **Canal:** pasta vinculada é o padrão; a cópia achatada (FlatDrop) é reserva (DEC-017).
- **Limites do Suno:** o v6 saiu em 2026-09-09 e a nota oficial não documenta limite de campo; os números do painel vêm de fonte secundária, com fonte e data no `QUALITY_LIMITS` (DEC-018). Outra fonte secundária (2026-08) põe o ideal em 4 a 7 descritores; o prompt usa 6 a 8. Reconferir quando houver documentação oficial. O `meta/HISTORY.md` §5 ganhou a interface do v6 vista na conta (2026-10-29); o resto do arquivo ainda descreve o v5.5.
- **Exclude no v6-mini:** o formulário gratuito não tem o campo (capturas de 2026-10-29). Com a WO 0017, o bloco pode ser ocultado em «Estrutura do cartão», e o aviso «no X → Exclude» some junto (D3); o dado continua no JSON.
- **Navegador (DEC-004, DEC-022):** guarda as marcas «usei», a estrutura do cartão e a cópia do último acervo importado. A cópia é cache: se o arquivo mudou fora, importe de novo; a linha de origem diz quando a cópia foi feita.
- **Botões de prompt e exemplo:** dependem de rede e do Pages. No `file://`, só funcionam se o Pages aceitar o `fetch` de uma página local — não conferido (o dono abriu o `file://` em 2026-10-29, sem relatar o resultado do botão); sem isso, a janela mostra o link para a versão publicada (DEC-021).
- **Estado de sessão** (módulos ligados e BPM escolhido) sobrevive a filtro, busca e «marcar usei»; volta ao acervo ao recarregar a página ou importar de novo (FIX-008, DEC-020).
- **Limite conhecido:** `tryAutoLoad` (carregamento automático pelo Pages) não saneia chaves internas — só a importação por arquivo faz isso. Inócuo enquanto nenhum acervo contaminado for para `data/`.
- **Pendência de contexto — ASU:** o dono perguntou se o «modo ASU» do KCM seria melhor que o modo Code para este projeto; ficou pendente até ele trazer a descrição do ASU `[relatado pelo dono, sem material de apoio]`.
- Design: na recomposição do Style a base manda — desligar um módulo não remove o que já está no style base; módulos só somam. O dedup compara sequências de palavras (FIX-003). Os módulos de gênero e de andamento costumam custar 0 tag por isso (DEC-019). O chip de andamento é atalho do controle de BPM, no máximo um ligado (DEC-020).
