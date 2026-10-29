# STATUS.md — Cancioneiro

> **O agora.** O que funciona, o que está em progresso, o que está quebrado, backlog curto.
> Rolante: item resolvido sai daqui e vai para o CHANGELOG. Médio/longo prazo vive no ROADMAP.

**Versão atual:** 0.9.1 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveniências de uso concluídos e conferidos · i-008 em andamento: família BR convertida (fora do repo), `Albuns/` à espera dos grupos
---

## Última conversa (2026-10-29, conversão da família BR, WO 0019)

- **Decisões da conversão: 1A, 2A, 3A, 4A** (DEC-026) — conversor determinístico por família; o acervo convertido é produto do dono e fica fora do repo.
- **Família BR convertida:** `scripts/convert_br.py` nos dez volumes, 151 de 151 faixas, gravada em `../acervos/rainha-da-preguica.json` e importada no app sem erro. O relatório mede 72 letras acima de 5.000 caracteres e 138 styles acima de 10 tags `[medido por instrumento]` — trabalho para o projeto de refino da Rainha da Preguiça, que o dono vai abrir à parte.
- **0.9.1:** os ajustes de tela da DEC-025 (vistos pelo dono) e o conversor.
- **Abertas:** grupos de `Albuns/` (i-038, proposta na pasta-pai) e o kit de música para o KCM (i-039, análise em discussão). A nota `261029-1825.txt` virou i-040 e i-041.
- **Este bloco substitui o anterior, de 2026-10-29, que fechava a 0.9.0.** O que ele dizia está no CHANGELOG [0.9.0] e [0.9.1], na DEC-025 e em `logs/2026-10-29.md` (Conversas 5 e 6).

## Funciona (pronto)

- **Ferramenta `app/index.html`:** importa/carrega JSON, cartões por álbum, copiar Style/Lyrics/Exclude por botão (o botão entrega o texto que está na tela — FIX-007), marca «usei», filtros por álbum/estado/uso, busca, módulos de estilo que recompõem o Style ao vivo, variantes e notas recolhíveis, «Baixar .json» limpo e «Importar .json» que saneia chaves internas e diz quantas removeu (FIX-004/006). A versão aparece no cabeçalho. A importação avisa quantos módulos citados não existem na coleção (FIX-009).
- **Painel de qualidade (0.5.0, DEC-018):** linha abaixo de Style, Lyrics e Exclude com caracteres contra o limite do campo, tags do Style e negações «no X». Vermelho só para truncamento.
- **Custo de cada módulo no chip (0.6.0, DEC-019):** com o painel de módulos aberto, cada chip mostra `−N`, `+N` ou `0` tags; a linha de qualidade diz quanto o style base usa sozinho quando o recomposto passa de 10.
- **Controle de BPM no cartão (0.7.0, DEC-020):** campo 20-300 com `−5`/`+5` e «voltar a N» governa todo «NN bpm» do Style principal; o chip de andamento é atalho (no máximo um ligado); variantes e «Baixar .json» não mudam; o valor é só da sessão.
- **Esquema JSON canônico** (`schema/`). Biblioteca de referência para autoria em `schema/style-modules.json` (27 módulos, sete camadas); cada acervo traz os seus (DEC-016).
- **Datasets:** `data/exemplo-cinzeiro.json` (1 faixa, com os 5 módulos que cita) e `data/demo.json` (2 álbuns, 3 faixas). Os acervos do dono moram fora do repo (DEC-026): `../album-referencias (1).json` (7 faixas, 50 módulos) e `../acervos/rainha-da-preguica.json` (10 álbuns, 151 faixas, gerado pelo conversor).
- **Conversor da família BR** (`scripts/convert_br.py`, 0.9.1, DEC-026): guias `..._VOL<n>_GUIA.md` → coleção no esquema, um álbum por volume, rótulos fora do copiável, variantes e referência levadas; relata o que passa do limite do Suno sem cortar. Teste: `python3 scripts/test_convert_br.py`.
- **Validação** (`scripts/validate.py`): sintaxe, esquema (com `jsonschema`), integridade referencial dos módulos (id ausente ou objeto no lugar do id, sem traceback — FIX-009), versão igual nos quatro lugares, um BPM só por faixa (DEC-020) e as marcações do prompt que o app lê (DEC-021); código 1 se falhar; a última linha diz se o esquema foi de fato conferido.
- **Export MD** (faixa / álbum / acervo), com o rótulo fora do bloco e o Style da tela nos três (0.9.0, D5).
- **Prompt-modelo** (`schema/PROMPT-PARA-CHATS.md`, DEC-021, DEC-023): contrato de módulo, style com 6 a 8 tags e até 10 com os módulos ligados; pede o JSON como arquivo e, sem arquivo, em bloco de código. Dois retestes em 2026-10-29: 6 de 6 faixas dentro do contrato e do orçamento, nos dois.
- **Botões «Prompt» e «Exemplo»** (0.8.0, DEC-021): buscam o prompt e o `data/demo.json` do repositório no clique; a janela do prompt recebe o «Meu pedido».
- **Conveniências (0.9.0, DEC-022, DEC-023):** «Estrutura» do cartão (ordem e blocos visíveis, no navegador); copiar o título; arrastar o `.json` para importar; o último acervo importado volta ao abrir, com origem, data e «esquecer»; a importação aceita a resposta do chat colada inteira e avisa.
- **Publicado no GitHub Pages** em `https://joaolucas-nds.github.io/cancioneiro/app/index.html` — o push em `main` publica.

## Em progresso

- **Álbuns antigos (i-008, DEC-026).** Família BR feita. `Albuns/` (8 arquivos, 172 faixas): proposta de 12 álbuns por cena de uso em `../261029-PROPOSTA-grupos-albuns.md` (i-038); com os grupos aprovados, conversores dos formatos e um mapa faixa → álbum.
- **Kit de música para o KCM (i-039)** — `meta/analises/261029-ANALISE-kit-de-musica.md`, em discussão: três peças (Instruções-modelo, skill de macetes, skill de revisão de faixa), fonte neste repo, adaptadas ao molde do nicho de música do KCM.

## Quebrado / pendências que travam

- (nada quebrado)

## Pendências do dono

- **Aprovar ou ajustar os grupos de `Albuns/`** — `../261029-PROPOSTA-grupos-albuns.md`, três pontos no fim.
- **Decidir o kit de música** — decisões 1 a 3 da análise; a 3 pede acesso de leitura à pasta do KCM (`C:\Users\alexk\Arquiteturas\Contexto\contexto-modular`) ou o molde do nicho trazido para a pasta-pai.
- **Instalar o validador de esquema nesta máquina.** Sem `jsonschema` e `referencing`, o `validate.py` só confere sintaxe e diz `ESQUEMA NAO CONFERIDO` na última linha. Uma vez, no CMD: `pip install jsonschema referencing --break-system-packages`. Depois, `python3 scripts/validate.py` deve terminar em `Tudo conforme ao esquema.`

## Backlog curto (próximas ações concretas)

1. **Converter `Albuns/`** (i-008, i-038) — depois dos grupos aprovados.
2. **Kit de música** (i-039) — depois das decisões; testar a skill de revisão contra a Rainha da Preguiça (deve achar as 72 e as 138).
3. **Curadoria no app e mais de um acervo** (i-040, i-041) — análise antes de spec: o app passaria de leitor a editor leve.
4. **Rampa de BPM** (i-042) — três faixas BR reprovam no `validate.py` por mudarem de andamento de propósito.
5. **Pesquisar outras plataformas de música por IA** (i-032) — um turno de pesquisa antes de qualquer mudança de esquema.
6. **Avisar palavra de andamento que contradiz o BPM** (i-029) — pede uma tabela palavra → faixa de BPM, com fonte e data.
7. **Importar prompts prontos dos álbuns como módulos** — o último ⬜ da 3b no ROADMAP; o índice-mestre da BR traz fórmulas de estilo.

## Notas de estado

- **Repo local do dono:** `C:\Users\alexk\Tools\cancioneiro\cancioneiro` (Windows). O chat lê e grava na pasta vinculada; commit e push são do Code (DEC-010). A pasta-pai guarda relatórios, notas e o acervo do dono, fora do Git; o lido vai para `../notas-arquivadas/`.
- **Canal:** pasta vinculada é o padrão; a cópia achatada (FlatDrop) é reserva (DEC-017).
- **Limites do Suno:** o v6 saiu em 2026-09-09 e a nota oficial não documenta limite de campo; os números do painel vêm de fonte secundária, com fonte e data no `QUALITY_LIMITS` (DEC-018). Outra fonte secundária (2026-08) põe o ideal em 4 a 7 descritores; o prompt usa 6 a 8. Reconferir quando houver documentação oficial. O `meta/HISTORY.md` §5 ganhou a interface do v6 vista na conta (2026-10-29); o resto do arquivo ainda descreve o v5.5.
- **Exclude no v6-mini:** o formulário gratuito não tem o campo (capturas de 2026-10-29). Desde a 0.9.1 (DEC-025) o bloco vem oculto por padrão, com o aviso «no X → Exclude» junto (D3); o dado continua no JSON e no export. Quem usa o campo liga em «Estrutura».
- **Navegador (DEC-004, DEC-022):** guarda as marcas «usei», a estrutura do cartão e a cópia do último acervo importado. A cópia é cache: se o arquivo mudou fora, importe de novo; a linha de origem diz quando a cópia foi feita.
- **Botões «Prompt» e «Exemplo»:** dependem de rede e do Pages. No `file://`, só funcionam se o Pages aceitar o `fetch` de uma página local — não conferido (o dono abriu o `file://` em 2026-10-29, sem relatar o resultado do botão); sem isso, a janela mostra o link para a versão publicada (DEC-021).
- **Estado de sessão** (módulos ligados e BPM escolhido) sobrevive a filtro, busca e «marcar usei»; volta ao acervo ao recarregar a página ou importar de novo (FIX-008, DEC-020).
- **Limite conhecido:** `tryAutoLoad` (carregamento automático pelo Pages) não saneia chaves internas — só a importação por arquivo faz isso. Inócuo enquanto nenhum acervo contaminado for para `data/`.
- **Pendência de contexto — ASU:** o dono perguntou se o «modo ASU» do KCM seria melhor que o modo Code para este projeto; ficou pendente até ele trazer a descrição do ASU `[relatado pelo dono, sem material de apoio]`.
- Design: na recomposição do Style a base manda — desligar um módulo não remove o que já está no style base; módulos só somam. O dedup compara sequências de palavras (FIX-003). Os módulos de gênero e de andamento costumam custar 0 tag por isso (DEC-019). O chip de andamento é atalho do controle de BPM, no máximo um ligado (DEC-020).

- **Aplicação da WO 0019 (Code, `d9b401f`):** empurrada; 13 hashes, teste 8/8 e conversor reproduzindo o acervo do chat conferidos. `validate.py` ainda sem o esquema (instalar `jsonschema`, pendência do dono).
