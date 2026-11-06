# STATUS.md — Cancioneiro

> **O agora.** O que funciona, o que está em progresso, o que está quebrado, backlog curto.
> Rolante: item resolvido sai daqui e vai para o CHANGELOG. Médio/longo prazo vive no ROADMAP.

**Versão atual:** 0.16.0 · **Fase:** 3a, 3a.2, o BPM da 3b, o prompt-modelo e as conveniências de uso concluídos e conferidos · os álbuns antigos convertidos (i-008, fora do repo) · curadoria no app concluída nas três entregas (DEC-028, DEC-029) · frente de interface na I3 de quatro (DEC-030 a DEC-032) · kit de música lido pelo KCM, à espera da resposta (i-039)

---

## Última conversa (2026-11-06, I3: protótipo, spec e implementação, WO 0027)

- **I2 conferida na tela pelo dono** (roteiro OK `[relatado pelo dono]`): lista e detalhe (0.15.0) estão fechados.
- **I3, organizar (0.16.0):** protótipo no canvas «Cancioneiro: nova interface» (fileira da I3), spec `meta/specs/261106-organizar.md` e os três pontos decididos pelo dono como recomendados (DEC-032): arrastar com filtro pela regra da próxima visível, Cartões só com o «⋯», seleção no celular pelo «⋯». 15 de 15 critérios no Chromium headless, testados pelo chat.
- **WO 0027 aplicada e empurrada** (`6a07bfd`, 0.16.0): validação verde; falta só a conferência da I3 na tela pelo dono.
- **Este bloco substitui o anterior, da WO 0026** (I2). O que ele dizia está no CHANGELOG [0.15.0], na spec `meta/specs/261106-lista-e-detalhe.md` e em `logs/2026-11-06.md` (Conversas 1 a 3).

## Funciona (pronto)

- **Ferramenta `app/index.html`:** importa/carrega JSON, cartões por álbum, copiar Style/Lyrics/Exclude por botão (o botão entrega o texto que está na tela — FIX-007), marca «usei», filtros por álbum/estado/uso, busca, módulos de estilo que recompõem o Style ao vivo, variantes e notas recolhíveis, «Baixar .json» limpo e «Importar .json» que saneia chaves internas e diz quantas removeu (FIX-004/006). A versão aparece no cabeçalho. A importação avisa quantos módulos citados não existem na coleção (FIX-009).
- **Painel de qualidade (0.5.0, DEC-018):** linha abaixo de Style, Lyrics e Exclude com caracteres contra o limite do campo, tags do Style e negações «no X». Vermelho só para truncamento.
- **Custo de cada módulo no chip (0.6.0, DEC-019):** com o painel de módulos aberto, cada chip mostra `−N`, `+N` ou `0` tags; a linha de qualidade diz quanto o style base usa sozinho quando o recomposto passa de 10.
- **Controle de BPM no cartão (0.7.0, DEC-020):** campo 20-300 com `−5`/`+5` e «voltar a N» governa todo «NN bpm» do Style principal; o chip de andamento é atalho (no máximo um ligado); variantes e «Baixar .json» não mudam; o valor é só da sessão.
- **Esquema JSON canônico** (`schema/`). Biblioteca de referência para autoria em `schema/style-modules.json` (27 módulos, sete camadas); cada acervo traz os seus (DEC-016).
- **Datasets:** `data/exemplo-cinzeiro.json` (1 faixa, com os 5 módulos que cita) e `data/demo.json` (2 álbuns, 3 faixas). Os acervos do dono moram fora do repo (DEC-026): `../album-referencias (1).json` (7 faixas, 50 módulos) `../acervos/rainha-da-preguica.json` (10 álbuns, 151 faixas) e `../acervos/albuns-reagrupados.json` (12 álbuns, 205 faixas), os dois gerados pelos conversores.
- **Conversor da família BR** (`scripts/convert_br.py`, 0.9.1, DEC-026): guias `..._VOL<n>_GUIA.md` → coleção no esquema, um álbum por volume, rótulos fora do copiável, variantes e referência levadas; relata o que passa do limite do Suno sem cortar. Teste: `python3 scripts/test_convert_br.py`.
- **Conversor dos guias de `Albuns/`** (`scripts/convert_guides.py`, 0.10.0): formatos mistos → coleção, com mapa de grupos que reprova faixa perdida. Teste: `python3 scripts/test_convert_guides.py`.
- **Kit de música** (`kit-musica/`, 0.10.0, DEC-027): bloco para Instruções e CEREBRO de um projeto de música, skills `macetes-suno` e `revisar-faixa`. Uso à mão em `kit-musica/README.md`.
- **Validação** (`scripts/validate.py`): sintaxe, esquema (com `jsonschema`), integridade referencial dos módulos (id ausente ou objeto no lugar do id, sem traceback — FIX-009), versão igual nos quatro lugares, um BPM só por faixa (DEC-020) e as marcações do prompt que o app lê (DEC-021) e os limites da skill `revisar-faixa` contra o app (DEC-027); código 1 se falhar; a última linha diz se o esquema foi de fato conferido.
- **Export MD** (faixa / álbum / acervo), com o rótulo fora do bloco e o Style da tela nos três (0.9.0, D5).
- **Exportar faixa como `.json`** (0.11.0, DEC-028): botão no rodapé do cartão; a faixa sai como acervo — o álbum de origem (id e título), a faixa e os módulos que ela cita — e importa como qualquer acervo. Sai o dado do acervo, não os módulos ligados nem o BPM da tela; o toast conta os módulos e os citados que não existem. Conferido na tela pelo dono em 2026-11-04.
- **Vários acervos no navegador** (0.12.0, DEC-028): cada importado fica no IndexedDB pelo nome do arquivo; o seletor de acervo, na barra, abre ou esquece cada um; reabre no último aberto; marcas «usei» por acervo. Sem IndexedDB, guarda só o último, como antes.
- **Curadoria pela tela** (0.13.0, DEC-028, DEC-029): mover, novo álbum, excluir e importar faixas num rascunho gravado no navegador; «● N alterações não salvas» com «Salvar .json» pelo nome de origem. Desde a 0.16.0, sem o interruptor «editar».
- **Organizar** (0.16.0, DEC-030, DEC-032): arrastar pela alça ⋮⋮ na Lista (com filtro, antes da próxima visível) e para os álbuns da lateral ou «+ Novo álbum»; o «⋯» de cada faixa (linha, detalhe e cartão) com Mover, Subir, Descer, Exportar e Excluir, e `Alt+↑`/`Alt+↓`; caixas e barra de lote; «Desfazer» e `Ctrl+Z` da última operação; soltar o `.json` sobre um álbum importa faixas nele. Só com cópia guardada no navegador. A SortableJS 1.15.7 vai embutida, com o hash no `validate.py`.
- **Lista e detalhe** (0.15.0, DEC-030, DEC-031): Lista (padrão) ou Cartões; uma linha por faixa com Style, Lyrics, ✓ e a saúde do prompt; o cartão de hoje ao lado, com ‹ ›, setas e `#faixa=<id>` no endereço; a lateral de álbuns e acervos a partir de 1280 px; no celular, o detalhe em tela própria com os botões de copiar no pé.
- **Barra única** (0.14.0, DEC-030): fixa, de 48 px; seletor de acervo como menu, busca com `/`, Filtros num painel com etiquetas removíveis e «N de M», rascunho e o «⋯» com Importar, Importar faixas, Baixar, Exportar .md, Prompt para chats, Baixar exemplo e Estrutura do cartão. No celular, 51 px, botões de 44 px, a busca numa linha própria e o rascunho no pé.
- **Prompt-modelo** (`schema/PROMPT-PARA-CHATS.md`, DEC-021, DEC-023): contrato de módulo, style com 6 a 8 tags e até 10 com os módulos ligados; pede o JSON como arquivo e, sem arquivo, em bloco de código. Dois retestes em 2026-10-29: 6 de 6 faixas dentro do contrato e do orçamento, nos dois.
- **«Prompt para chats» e «Baixar exemplo»** (0.8.0, DEC-021; no «⋯» desde a 0.14.0): buscam o prompt e o `data/demo.json` do repositório no clique; a janela do prompt recebe o «Meu pedido».
- **Conveniências (0.9.0, DEC-022, DEC-023):** «Estrutura» do cartão (ordem e blocos visíveis, no navegador); copiar o título; arrastar o `.json` para importar; o último acervo importado volta ao abrir, com origem, data e «esquecer»; a importação aceita a resposta do chat colada inteira e avisa.
- **Publicado no GitHub Pages** em `https://joaolucas-nds.github.io/cancioneiro/app/index.html` — o push em `main` publica.

## Em progresso

- **Kit de música no KCM (i-039)** — o KCM leu a carta 01 e responde por carta, sem data. Gatilho: sem resposta até o primeiro projeto de música novo, o projeto usa o kit à mão (`kit-musica/README.md`).

## Quebrado / pendências que travam

- (nada quebrado)

## Pendências do dono

- **Conferir a I3 na tela** — roteiro na conversa de 2026-11-06 (WO 0027), depois do push, no computador e no celular.
- **Instalar o validador de esquema nesta máquina.** Sem `jsonschema` e `referencing`, o `validate.py` só confere sintaxe e diz `ESQUEMA NAO CONFERIDO` na última linha. Uma vez, no CMD: `pip install jsonschema referencing --break-system-packages`. Depois, `python3 scripts/validate.py` deve terminar em `Tudo conforme ao esquema.`

## Backlog curto (próximas ações concretas)

1. **I4 — Salvar no arquivo** (i-043, DEC-030) — protótipo no canvas, depois spec: gravar o rascunho direto no `.json` de origem onde o navegador deixar, sem baixar e substituir à mão.
2. **Organizar os álbuns** (i-049) — renomear, reordenar na lateral, juntar dois; candidata depois da I4.
3. **Rampa de BPM** (i-042) — três faixas BR reprovam no `validate.py` por mudarem de andamento de propósito.
4. **Pesquisar outras plataformas de música por IA** (i-032) — um turno de pesquisa antes de qualquer mudança de esquema.
5. **Avisar palavra de andamento que contradiz o BPM** (i-029) — pede uma tabela palavra → faixa de BPM, com fonte e data.
6. **Importar prompts prontos dos álbuns como módulos** — o último ⬜ da 3b no ROADMAP; o índice-mestre da BR e os «estilos originais» do VOL5 trazem fórmulas de estilo.

## Notas de estado

- **Repo local do dono:** `C:\Users\alexk\Tools\cancioneiro\cancioneiro` (Windows). O chat lê e grava na pasta vinculada; commit e push são do Code (DEC-010). A pasta-pai guarda relatórios, notas e o acervo do dono, fora do Git; o lido vai para `../notas-arquivadas/`.
- **Canal:** pasta vinculada é o padrão; a cópia achatada (FlatDrop) é reserva (DEC-017).
- **Limites do Suno:** o v6 saiu em 2026-09-09 e a nota oficial não documenta limite de campo; os números do painel vêm de fonte secundária, com fonte e data no `QUALITY_LIMITS` (DEC-018). Outra fonte secundária (2026-08) põe o ideal em 4 a 7 descritores; o prompt usa 6 a 8. Reconferir quando houver documentação oficial. O `meta/HISTORY.md` §5 ganhou a interface do v6 vista na conta (2026-10-29); o resto do arquivo ainda descreve o v5.5.
- **Exclude no v6-mini:** o formulário gratuito não tem o campo (capturas de 2026-10-29). Desde a 0.9.1 (DEC-025) o bloco vem oculto por padrão, com o aviso «no X → Exclude» junto (D3); o dado continua no JSON e no export. Quem usa o campo liga em «Estrutura».
- **Navegador (DEC-004, DEC-022, DEC-028):** guarda as cópias dos acervos importados (IndexedDB, banco `cancioneiro`), as marcas «usei» por acervo e a estrutura do cartão (`localStorage`, `cancioneiro:ui`). As cópias são cache: se o arquivo mudou fora, importe de novo; o menu do seletor de acervo diz quando a cópia foi feita. Os avisos de primeira abertura guardam `tour14` (0.14.0) e `tour15` (0.15.0), e a visão escolhida, `view`, no mesmo `cancioneiro:ui`.
- **Rascunho (DEC-028, DEC-029, DEC-032):** com alterações, a cópia guardada está à frente do arquivo até «Salvar .json» e substituir. A marca na barra é o lembrete; esquecer e reimportar pedem confirmação. O «Desfazer» guarda só a última operação, na memória da aba: recarregar a página o esquece.
- **No `file://`, todas as páginas locais dividem o armazenamento** (sonda de 2026-11-04): o app só lê e grava o que tem o nome `cancioneiro`. O `file://` e o Pages são origens diferentes — o que está guardado num não aparece no outro.
- **Conversores são de primeira geração (DEC-028):** depois de mudar um acervo (à mão ou, com a entrega 3, no app), não rode o conversor por cima dele.
- **«Prompt para chats» e «Baixar exemplo»:** dependem de rede e do Pages. No `file://`, só funcionam se o Pages aceitar o `fetch` de uma página local — não conferido (o dono abriu o `file://` em 2026-10-29, sem relatar o resultado do botão); sem isso, a janela mostra o link para a versão publicada (DEC-021).
- **Estado de sessão** (módulos ligados e BPM escolhido) sobrevive a filtro, busca e «marcar usei»; volta ao acervo ao recarregar a página ou importar de novo (FIX-008, DEC-020).
- **Limite conhecido:** `tryAutoLoad` (carregamento automático pelo Pages) não saneia chaves internas — só a importação por arquivo faz isso. Inócuo enquanto nenhum acervo contaminado for para `data/`.
- **Pendência de contexto — ASU:** o dono perguntou se o «modo ASU» do KCM seria melhor que o modo Code para este projeto; ficou pendente até ele trazer a descrição do ASU `[relatado pelo dono, sem material de apoio]`.
- Design: na recomposição do Style a base manda — desligar um módulo não remove o que já está no style base; módulos só somam. O dedup compara sequências de palavras (FIX-003). Os módulos de gênero e de andamento costumam custar 0 tag por isso (DEC-019). O chip de andamento é atalho do controle de BPM, no máximo um ligado (DEC-020).
