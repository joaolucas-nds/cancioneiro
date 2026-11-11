# CHANGELOG.md — Cancioneiro

> Histórico de versões entregues. SemVer + Keep a Changelog. Cresce no topo.

---

## [0.19.0] — 2026-11-11

Rampa de BPM (i-042, DEC-036): o Style com rampa sai como foi escrito.

### Fixed
- **A rampa de BPM era reescrita em silêncio.** O controle de BPM (DEC-020) troca todo número de BPM pelo valor dele, e o valor inicial é o primeiro número: «95 BPM building to 115 BPM» copiava como «95 BPM building to 95 bpm», sem ninguém mexer no controle. Afetava as três faixas BR com rampa desde a 0.7.0. Agora a rampa é reconhecida e sai byte a byte.

### Added
- **Rampa reconhecida:** dois BPM no mesmo trecho do Style ligados por `to`, `building to`, `rising to`, `up to`, `climbing to` ou `→`. Dois números soltos continuam sendo o caso da DEC-020.
- Numa faixa com rampa, o controle de BPM vira o rótulo «rampa 95 → 115 bpm», os chips de andamento ficam desligados, a coluna BPM da Lista mostra «95→115 bpm» e a linha de qualidade avisa em âmbar que o Suno não segue mudança de andamento numa geração. O export `.md` leva «BPM: rampa 95 → 115».
- `validate.py`: a rampa declarada é AVISO, não erro; o campo `bpm`, se houver, é o número de partida.

### Changed
- `revisar-faixa` (conferência 7) e `macetes-suno` (§5) dizem que o Cancioneiro preserva a rampa, e continuam recomendando um BPM com a subida descrita.
- CI: o passo «Dependencias» instala o navegador sem depender do `apt` do runner, que ficou sem DNS três vezes em 2026-11-11; as bibliotecas do sistema, já presentes no runner, com três tentativas de 3 minutos.

Spec `meta/specs/261111-rampa-de-bpm.md`: 7 de 7 critérios, com 6 testes novos em `tests/test_bpm.py` (50 no total).

---

## [0.18.0] — 2026-11-09

Organizar os álbuns, não só as faixas (i-049, DEC-035).

### Added
- **O «⋯» do álbum**, no cabeçalho de cada álbum (Lista e Cartões) e ao lado de cada álbum da lateral: Renomear…, Subir álbum e Descer álbum, Juntar com…, Exportar álbum .md, Exportar álbum .json e Excluir álbum…. No celular, ele abre a folha de baixo.
- **Renomear** numa janela, com o título e a descrição do álbum (o campo `description` do esquema, que já existia e passa a aparecer no cabeçalho). O id do álbum não muda. Título igual ao de outro álbum é permitido, com aviso.
- **Reordenar os álbuns** arrastando pela alça ⋮⋮ da lateral, ou com Subir e Descer no «⋯»; `Alt+↑` e `Alt+↓` no nome do álbum da lateral.
- **Juntar com…:** as faixas vão para o fim do álbum escolhido, na ordem; o de origem sai; ficam o id, o título e a descrição do destino. O filtro de álbum acompanha.
- **Excluir álbum…** com as faixas, confirmando com a contagem no botão; saem também as marcas «usei» delas.
- **Exportar álbum .json:** um acervo com o álbum e os módulos que as faixas citam, que importa como qualquer acervo.

### Changed
- O botão «exportar álbum .md» do cabeçalho mora agora no «⋯» do álbum.

Todas as operações têm «Desfazer» e `Ctrl+Z`, como as das faixas. Spec `meta/specs/261109-organizar-os-albuns.md`: 10 de 10 critérios, com 12 testes novos em `tests/test_albuns.py` (44 no total), que reprovam no app da 0.17.0. Abrir 205 faixas: de 246 a 289 ms, contra 251 a 319 ms da 0.17.0 nas mesmas rodadas (sem diferença medível).

---

## [0.17.0] — 2026-11-06

Quarta e última entrega da frente de interface (I4, DEC-030, DEC-033): «Salvar» grava no próprio `.json`, onde o navegador deixa. Fecha a i-043.

### Added
- **«Salvar» grava no arquivo** no Chrome e no Edge do computador. No primeiro «Salvar» de um acervo, a janela do sistema vem com o nome do arquivo de origem; o acervo fica vinculado àquele arquivo, e os próximos «Salvar» gravam sem janela. Ao reabrir o app, o navegador pede uma vez a permissão de editar.
- **`Ctrl+S` (`⌘S`)** salva, até dentro de um campo de texto, e não abre mais o «salvar página» do navegador. Sem alterações, não faz nada.
- **O ▾ ao lado de «Salvar»:** Salvar no arquivo, Salvar em outro arquivo… (vincula ao escolhido) e Baixar .json (uma cópia em Downloads; com vínculo, o rascunho continua não salvo).
- **Importar pela janela do sistema** («Importar .json…» e «Importar outro .json…») e soltar o arquivo na tela já vinculam o acervo ao arquivo.
- **Arquivo mudado fora do app:** antes de gravar, o app compara a data e o tamanho do arquivo com os da última leitura ou gravação e pergunta: Cancelar, Salvar em outro arquivo… ou Substituir mesmo assim. Arquivo sumido: avisa e oferece salvar em outro.
- **O vínculo no seletor de acervo** («Vinculado a X», ou «Sem vínculo») e **Desvincular do arquivo**. Esquecer o acervo apaga o vínculo junto.
- Depois de gravar, a barra mostra «✓ Salvo no arquivo às HH:MM».

### Changed
- **«Desfazer» continua valendo depois de salvar** (revê a DEC-032): desfazer devolve o rascunho a «1 alteração não salva». Vale também para o «Salvar .json» que baixa.
- Firefox, Safari e o celular continuam com «Salvar .json», que baixa como antes; o seletor de acervo diz por quê.

Spec `meta/specs/261106-salvar-no-arquivo.md`: 14 de 14 critérios no Chromium headless (em `http://127.0.0.1`, com as janelas do sistema trocadas por arquivos da pasta privada do navegador), com prova de vida no app da 0.16.0. Abrir 205 faixas leva de 1 a 34 ms a mais que a 0.16.0 nas mesmas rodadas (o limite era 50); gravar 205 faixas (293 KB), de 10 a 14 ms. A sonda no Chrome 156 do dono, no `file://`, confirmou a janela de salvar, gravar de novo sem janela, guardar o vínculo e abrir pela janela. O app passa de 239 KB para 253 KB.

---

## [0.16.0] — 2026-11-06

Terceira entrega da frente de interface (I3, DEC-030, DEC-032): organizar o acervo sem ligar nada. O cartão não muda.

### Added
- **Arrastar pela alça ⋮⋮** de cada linha da Lista, dentro do álbum ou para outro, com o SortableJS 1.15.7 embutido no app (MIT, sem mudança; o `validate.py` confere o sha256). Com filtro ou busca ligados, a faixa cai logo antes da próxima visível, e o aviso diz onde («… foi para antes de «X»»). Soltar no mesmo lugar não conta alteração.
- **Soltar sobre a lateral:** num álbum, a faixa vai para o fim dele; em «+ Novo álbum», que só aparece durante o arrastar, o app pede o título e cria o álbum com ela.
- **O «⋯» de cada faixa**, na linha, no detalhe e no pé do cartão, com os mesmos itens: Mover para…, Subir, Descer, Exportar .md, Exportar .json e Excluir…. `Alt+↑` e `Alt+↓` no título sobem e descem.
- **Várias de uma vez:** uma caixa por linha e uma por álbum (marca as visíveis), `Shift`+clique para o intervalo e uma barra de lote com Mover para…, Exportar .json (um acervo com as faixas, nos álbuns de origem e com os módulos citados), Marcar usei e Excluir….
- **«Desfazer»** no aviso de cada operação, e `Ctrl+Z` fora dos campos de texto: volta o acervo, as marcas «usei» das excluídas e o número de alterações. Só a última; salvar e trocar de acervo esquecem a volta.
- **Soltar um `.json` sobre um álbum** (o cabeçalho na lista, ou o nome na lateral) abre «importar faixas» com ele escolhido; fora dele, importa como acervo, como antes.
- **Celular:** o «⋯» do detalhe e o toque na alça abrem uma folha de baixo; «Selecionar várias…» liga as caixas de 44 px e a barra de lote; tocar na linha marca. A alça só pega depois de segurar.

### Changed
- **Sem o interruptor «editar».** Organizar vale sempre que o acervo tem cópia guardada no navegador; sem ela (o exemplo do Pages), não há alça, e o «⋯» traz só os Exportar, com a explicação.
- **«Importar faixas…»** mora no «⋯» da barra, também no computador.
- O pé do cartão perde ↑ ↓, «mover…» e «excluir», e ganha o «⋯».

Spec `meta/specs/261106-organizar.md`: 15 de 15 critérios no Chromium headless, com prova de vida no app da 0.15.0. Abrir um acervo de 205 faixas leva de 148 a 159 ms, até cerca de 30 ms a mais que a 0.15.0 nas mesmas rodadas (o limite era 100), e a Lista de 300 faixas desenha em cerca de 60 ms. Os testes das entregas 1 a 3, da I1 e da I2 seguem em 15 de 15, 25 de 25, 19 de 19, 14 de 14 e 15 de 15, com o «⋯» no lugar do «editar». O app passa de 158 KB para 239 KB, 45 KB deles da biblioteca.

---

## [0.15.0] — 2026-11-06

Segunda entrega da frente de interface (I2, DEC-030, DEC-031): as faixas numa lista, com o cartão ao lado da escolhida. O cartão não muda.

### Added
- **Visão Lista** (a padrão) e **Cartões** (a de antes), num par de botões na barra; no celular, no «⋯». A escolha fica no navegador (`view` em `cancioneiro:ui`).
- **A lista:** uma linha de 44 px por faixa, agrupada por álbum, com o cabeçalho do álbum fixo ao rolar. Colunas: título, estado, idioma, BPM, saúde e os botões **Style**, **Lyrics** e ✓ «usei». Os dois botões copiam só o conteúdo, o Style recomposto na hora, igual ao «copiar» do cartão.
- **Saúde da faixa:** o pior nível do painel de qualidade do cartão, com marca e texto («● tudo dentro», «▲ Style 12 tags», «■ Lyrics passa de 5.000»).
- **O detalhe à direita:** clicar no título abre o cartão de hoje ao lado da lista, com ‹ › para andar pela lista filtrada e × ou `Esc` para fechar. `↓` e `↑` no título andam de faixa. O endereço guarda a faixa (`#faixa=<id>`): recarregar reabre, e o «Voltar» do navegador fecha. Entre 720 e 959 px, o detalhe abre por cima da lista.
- **A lateral** (a partir de 1280 px): os álbuns, com a contagem dos outros filtros (clicar filtra), e os acervos guardados (clicar abre).
- **Celular:** linhas de 64 px com o ✓ de 44; o detalhe em tela cheia, com «Copiar Style», «Copiar Lyrics» e «Título» fixos no pé; voltar devolve a lista na mesma rolagem.
- Um aviso de uma linha na primeira abertura diz onde está cada coisa (`tour15`).

### Changed
- Na Lista, clicar no título da faixa abre o detalhe; copiar o título fica no cartão, como antes. Em Cartões, nada muda.
- Abaixo de 1180 px de largura, o nome «Cancioneiro» sai da barra para caber o par Lista | Cartões; a versão segue no «⋯».

Spec `meta/specs/261106-lista-e-detalhe.md`: 15 de 15 critérios no Chromium headless, com prova de vida no app da 0.14.0; a Lista de 300 faixas desenha em cerca de 50 ms. Os testes das entregas 1 a 3 e da I1 seguem em 15 de 15, 25 de 25, 19 de 19 e 14 de 14, rodados em Cartões onde medem o cartão.

---

## [0.14.0] — 2026-11-05

Primeira entrega da frente de interface (I1, DEC-030): uma barra única no topo. O cartão não muda.

### Added
- **Barra única**, fixa no topo, de 48 px (no celular, 51): o nome e a versão, o seletor de acervo, a busca, «Filtros», o rascunho, «editar» e o «⋯».
- **Seletor de acervo:** mostra o título, o arquivo e a contagem do acervo aberto. Abre um menu com os acervos guardados (abrir; × para esquecer), «Importar outro .json…», «Esquecer este acervo», a origem da cópia e o estado do armazenamento. Substitui «acervos (N)», a janela de acervos e a linha de origem.
- **Filtros num painel** (Álbum, Estado, Uso), com o número de filtros ligados no botão, e uma fileira de etiquetas removíveis com «N de M faixas» e «Limpar tudo». A tecla `/` leva à busca (fora de um campo de texto).
- **«⋯»:** Importar .json…, Baixar .json, Exportar .md, Prompt para chats, Baixar exemplo e Estrutura do cartão. Na primeira abertura, um aviso de uma linha diz para onde eles foram; some em «entendi» e fica guardado no navegador (`tour14`).
- **Celular:** botões de 44 px; a busca abre numa linha própria; o rascunho fica no pé da tela. O topo, com um filtro ligado, passou de 469 px de controles para 95 px.

### Changed
- O rascunho aparece na barra como «● N alterações não salvas», com **Salvar .json**: o mesmo «Baixar .json» da DEC-028, com o nome de origem.
- Os seis botões do cabeçalho foram para o «⋯»; «editar» e «importar faixas…» foram da linha de origem para a barra.

### Fixed
- Sem acervo, a barra de filtros não fica mais na tela: a regra `[hidden]` vale para o app todo (i-044).

Spec `meta/specs/261105-barra-unica.md`: 14 de 14 conferências dos 13 critérios no Chromium headless, com prova de vida no app da 0.13.0; os testes das entregas 1 a 3 seguem em 15 de 15, 25 de 25 e 19 de 19, com os seletores dos botões que mudaram de lugar.

---

## [0.13.0] — 2026-11-05

Terceira e última entrega da curadoria no app (i-040, DEC-028): editar o acervo pela tela.

### Added
- **Modo «editar»**, na linha de origem: liga a curadoria. Desligado, o cartão fica como antes. Ligado, cada cartão ganha ↑, ↓, «mover…» (para outro álbum ou para um álbum novo) e «excluir» (com confirmação), e a linha de origem ganha «importar faixas…».
- **Rascunho:** cada operação grava a cópia do acervo no navegador e soma uma alteração. A linha de origem mostra «alterado: N alterações não baixadas» com o botão «Baixar .json», que baixa com o **nome do arquivo de origem**, para substituir o antigo, e zera a contagem. Esquecer ou reimportar com alterações pendentes pedem confirmação.
- **Importar faixas** de outro `.json`, inclusive uma faixa exportada solta: uma janela lista as faixas, todas marcadas, e o destino (por padrão, o álbum de origem de cada uma). Faixa idêntica é pulada; mesmo id com conteúdo diferente entra com sufixo (`-2`). Módulo citado: o que falta entra; o diferente entra com sufixo, e a faixa passa a citá-lo; o que não existe em lugar nenhum fica citado. O toast conta cada caso.

### Changed
- «Baixar .json» de um acervo guardado sai com o nome do arquivo de origem, não com o título.
- Álbum que fica sem faixa sai do acervo.
- Fechar a aba não avisa: o rascunho já está gravado. Só avisa se a gravação no navegador falhar (DEC-029).

Spec `meta/specs/261105-curadoria-pela-tela.md`: 19 de 19 conferências dos 18 critérios no Chromium headless, com prova de vida no app da 0.12.0; os testes das entregas 1 e 2 seguem em 15 de 15 e 25 de 25.

---

## [0.12.0] — 2026-11-05

Segunda das três entregas da curadoria no app (i-041, DEC-028): vários acervos guardados no navegador.

### Added
- **Vários acervos no navegador:** cada `.json` importado fica guardado no IndexedDB (banco `cancioneiro`), pelo nome do arquivo; reimportar o mesmo arquivo substitui a cópia, e o toast diz de quando era a anterior. O botão «acervos (N)», na linha de origem, abre a janela com os guardados — título, arquivo, data, álbuns e faixas — para abrir outro sem seletor de arquivo ou esquecer um. O app reabre no último acervo aberto. Na primeira gravação, pede ao navegador para guardar de forma persistente; a janela mostra o resultado.

### Changed
- **Marcas «usei» por acervo.** Até a 0.11.0 eram só por id, e o mesmo id em dois acervos (`brv-04` na Rainha e no demo, `cinzeiro-01` no demo e no exemplo) marcava nos dois. A migração copia cada marca antiga para todo acervo guardado que tem aquele id, então nada some da tela.
- **Migração da cópia antiga** (`cancioneiro:acervo`, da 0.9.0 à 0.11.0): é gravada no IndexedDB, lida de volta e comparada, e só então apagada. Se falhar, ela fica, e o app segue como na 0.11.0. Sem IndexedDB, o app guarda só o último, como antes, e avisa uma vez.
- **Esquecer** apaga só aquele acervo; as marcas dele ficam, e reimportar o arquivo as traz de volta.
- **Importar um `.json` que não é acervo** (sem `albums`) não guarda mais a cópia. Antes, o toast de erro era coberto por «Acervo importado».

Spec `meta/specs/261104-varios-acervos.md`: 25 de 25 conferências dos 16 critérios no Chromium headless, com acervos sintéticos do tamanho dos reais (960 mil, 430 mil e 22 mil caracteres) e prova de vida no app da 0.11.0; o teste da entrega 1 continua em 15 de 15.

---

## [0.11.0] — 2026-11-02

Primeira das três entregas da curadoria no app (i-040, DEC-028): exportar uma faixa como `.json`.

### Added
- **Exportar faixa como `.json`:** botão «exportar .json» no rodapé de cada cartão, depois de «exportar .md». A faixa sai como um acervo completo — o álbum de origem (id e título), a faixa e os módulos que ela cita, cada um uma vez — e importa como qualquer acervo, sem aviso de módulo faltando. O arquivo leva o id da faixa no nome (`brv-04.json`). Sai o dado do acervo, nunca os módulos ligados nem o BPM da tela (a regra do «Baixar .json»); citação de módulo que não existe no acervo segue citada, e o toast conta. Spec `meta/specs/261102-exportar-faixa-json.md`: 15 de 15 critérios no Chromium headless, com prova de vida no app da 0.10.0.

### Changed
- **Decisão da curadoria (DEC-028):** o app vai editar um rascunho marcado do acervo, guardado no IndexedDB; o arquivo baixado é a fonte, e o `.json` curado passa a mandar sobre os conversores. Os dois conversores e o README dizem isso.

---

## [0.10.0] — 2026-10-31

Os álbuns antigos de `Albuns/` convertidos e reagrupados (i-008, i-038), e o kit de música para os projetos do KCM (i-039, DEC-027).

### Added
- **Conversor dos guias de `Albuns/` (`scripts/convert_guides.py`):** lê os oito guias de formatos mistos — rótulo no bloco, «Style — Opção A/B», «Style Prompt»/«Letra», letra em Markdown fora de bloco, «Variações para» — e grava uma coleção no esquema. Com `--groups`, um mapa (fora do repo) reagrupa as faixas em álbuns e reprova faixa perdida ou id inexistente. Teste com guias sintéticos em `scripts/test_convert_guides.py` (8 casos). Medido no acervo do dono: 205 de 205 faixas, 12 álbuns por cena de uso; o arquivo fica fora do repo.
- **Kit de música (`kit-musica/`, DEC-027):** `BLOCO-SUNO.md` (cinco linhas para as Instruções de um projeto de música do KCM e uma seção para o CEREBRO dele), skill `macetes-suno` (o que tem efeito no Suno, com exemplo bom e ruim) e skill `revisar-faixa` (oito conferências por faixa, com script que conta). A revisão acha nos acervos do dono o que o painel do app acha: 72 letras acima de 5.000 caracteres e 138 styles acima de 10 tags na Rainha da Preguiça.
- **Validação:** o `validate.py` confere que os limites da skill `revisar-faixa` são os do `QUALITY_LIMITS` do app.

---

## [0.9.1] — 2026-10-29

Ajustes de tela pedidos pelo dono depois de conferir a 0.9.0 (nota `261029-1618.txt`, DEC-025), vistos na tela. E o primeiro conversor dos guias antigos (i-008, DEC-026).

### Added
- **Conversor da familia BR (`scripts/convert_br.py`, DEC-026):** le os guias `..._VOL<n>_GUIA.md` da «Rainha da Preguiça» e grava uma colecao no esquema, um album por volume. Tira os rotulos `[ESTILO SUNO]` e `[LETRA]` do que e copiavel, leva as variantes `VAR A/B` e os campos de referencia (Conceito, Voz, Instrumentos, conversa de origem). Conversao fiel: letra longa e style com tags demais nao sao cortados, o relatorio conta. Teste com guia sintetico em `scripts/test_convert_br.py` (8 casos, sem letra real no repo). Medido no acervo do dono: 151 de 151 faixas, 10 albuns; o arquivo gerado fica fora do repo.

### Changed
- **Cabecalho:** a versao fica pequena abaixo do nome, sem o subtitulo; «Prompt», «Exemplo» (icone de baixar) e «Estrutura» (icone de camadas) ficam ao lado do nome; importar, baixar e exportar ficam na ponta direita.
- **Titulo:** clicar no nome da faixa copia o titulo, com «copiado ✓» ao lado; sai o botao «copiar titulo», que quebrava a linha.
- **Estrutura do cartao:** as linhas se arrastam para mudar a ordem (os ↑ ↓ ficam, para o teclado). O padrao passa a **esconder o Exclude** — o formulario gratuito do Suno v6 nao tem o campo; o aviso «no X → Exclude» some junto (D3). Quem tinha salvo o padrao antigo passa ao novo; estrutura personalizada fica como estava.

---

## [0.9.0] — 2026-10-29

Conveniencias de uso, conferidas na tela e retestadas pelo dono.

### Added
- **Estrutura do cartao (DEC-023, i-030):** ordem e mostrar/ocultar de seis blocos (Style, Lyrics, Exclude, Modulos, Variantes, Notas), guardada no navegador; «Restaurar padrao».
- **Copiar o titulo da faixa (i-033).**
- **Arrastar o `.json` para a tela importa (i-034)**, pelo mesmo caminho do botao.
- **O ultimo acervo importado volta ao abrir (DEC-022, i-035):** copia em cache no navegador; a barra mostra de onde veio e quando, com «esquecer». Vence a carga automatica do Pages.

### Changed
- **Prompt-modelo (DEC-023, i-036):** a «Saida» pede um `.json` para baixar; sem arquivo, o JSON num unico bloco de codigo. Reteste do dono com dois chats: 6 de 6 faixas no contrato e no orcamento; os arquivos vieram com o nome do `id` do album, como o prompt pede para o arquivo.
- **Importacao:** aceita a resposta do chat colada inteira — extrai o bloco de codigo (ou do primeiro `{` ao ultimo `}`) e avisa no toast.
- **Export de album e de acervo com o Style da tela (D5, i-037):** modulos ligados e BPM do controle, como o da faixa. Conferido no `.md` exportado pelo dono: 18 tags em ar-01, igual ao cartao.
- **Painel de qualidade:** com o Exclude oculto, nao sugere levar «no X» para ele.

---

## [0.8.0] — 2026-10-29

Prompt-modelo com contrato de modulos e o prompt pela interface do app, conferidos na tela e retestados pelo dono.

### Added
- **Botoes «Prompt para chats» e «Baixar exemplo» (DEC-021, i-031):** a janela do primeiro recebe o «Meu pedido» e copia o prompt-modelo inteiro com o pedido no lugar; o segundo baixa `cancioneiro-exemplo.json`. Os dois buscam `schema/PROMPT-PARA-CHATS.md` e `data/demo.json` no clique — o app nao guarda copia; falhando a busca, a janela mostra o link da versao publicada.
- **`scripts/validate.py` confere o prompt (sexta checagem):** reprova se sumirem as marcacoes que o botao le (`--- INÍCIO ---`, `--- FIM ---` e a linha entre parenteses abaixo de `## Meu pedido`).

### Changed
- **Prompt-modelo (DEC-021, i-028):** ensina o contrato de modulo da DEC-016 (modulos no `styleModules` da colecao com `id`, `category`, `label`, `fragment`, `notes`; a faixa cita ids; citado = ligado), o orcamento (style com 6 a 8 tags; ate 10 com os modulos ligados) e que BPM em modulo so vai na camada `tempo`. Reteste do dono com dois chats: 6 de 6 faixas dentro do orcamento, 0 modulos fora do contrato, 0 rotulos — contra 0 de 3 chats no contrato antes.
- **Toast:** dura conforme o tamanho da mensagem (2,2 a 6 s), para os avisos longos darem tempo de ler.

### Fixed
- **FIX-009:** modulo declarado dentro da faixa sumia em silencio no app (painel com 0 chips) e derrubava o `validate.py` com traceback. Agora o validador reprova com mensagem por item, e a importacao — por arquivo ou pela carga automatica — diz quantos modulos citados nao existem na colecao.

---

## [0.7.0] — 2026-10-28

Fase 3b: o controle de BPM no cartao, conferido na tela pelo dono.

### Added
- **Controle de BPM (DEC-020, i-005):** o «128 BPM» da linha de metadados virou um campo (20 a 300, `−5`/`+5`, «voltar a N») que governa todo «NN bpm» do Style principal — base e modulos —, reescrito no lugar, antes da dedup. Botao copiar, linha de qualidade, recomposto e export MD («BPM: N» e o bloco) usam o valor do controle. Variantes e o «Baixar .json» nao mudam; o valor e so da sessao, como os modulos. Valor invalido nao chega ao Style.
- **Chip de andamento como atalho:** ligar um chip da camada Andamento move o controle para o numero dele e desliga o outro; no maximo um ligado. Antes, 49 de 49 cliques punham um segundo BPM no prompt.
- **`scripts/validate.py` confere o BPM (quinta checagem):** reprova faixa com dois BPM diferentes no style, ou com campo `bpm` diferente do numero do style (ou sem numero nele).

### Fixed
- **FIX-008:** filtro, busca e «marcar usei» religavam os chips do acervo enquanto o bloco de Style seguia com o clique — o botao copiar entregava um texto que os chips nao explicavam. O estado de sessao sobrevive ao re-render e so volta ao acervo ao importar de novo.

---

## [0.6.0] — 2026-10-27

Fase 3a.2: o custo de cada modulo no chip, conferido na tela. E a versao passa a aparecer no app.

### Added
- **Custo de cada modulo no chip (DEC-019):** com o painel de modulos aberto, cada chip mostra quantas tags ele muda no Style daquele cartao — `−N` ligado, `+N` desligado, `0` quando nao muda o prompt (o chip que antes acendia sem efeito nenhum). Recalculado em todos os chips a cada clique, so com o painel aberto. A linha de qualidade passa a dizer quanto o style base usa sozinho quando o recomposto passa de 10 tags. A lista de corte automatica foi descartada: medida, ela mandaria cortar a voz de rap em faixas de rap-pop.
- **A versao na tela (i-027):** o cabecalho do app mostra `v0.6.0`. Todo print passa a ser datavel.
- **`scripts/validate.py` confere a versao:** o topo do CHANGELOG, o app, o README e o STATUS tem de dizer a mesma; senao, codigo 1.

### Fixed
- O cabecalho do `scripts/validate.py` dizia «checa duas coisas» desde a WO 0006, que acrescentou a terceira; agora lista as quatro.

---

## [0.5.0] — 2026-10-27

Painel de qualidade do prompt (Fase 3a) e quatro correcoes que o tornaram confiavel. Tudo o que entrou no app desde a 0.4.1.

### Added
- **Painel de qualidade (DEC-018):** abaixo de Style, Lyrics e Exclude, uma linha que mede o que vai para o Suno — caracteres contra o limite do campo (Style e Exclude 1.000; Lyrics 5.000, com aviso a partir de ~3.000), tags do Style (ambar acima de ~10, nunca vermelho) e negacoes «no X» (por fronteira de palavra; so avisa; `no vocals` nao dispara em faixa instrumental). Mede o Style **recomposto** e se atualiza a cada clique num chip de modulo. Vermelho reservado ao truncamento, o unico caso que perde texto. Limites num objeto unico, com fonte e data.
- **`scripts/validate.py`:** checagem de integridade referencial (todo id em `songs[].styleModules` existe no `styleModules[]` da propria colecao — DEC-016), e a ultima linha passa a declarar se o esquema foi de fato conferido.
- `meta/specs/` (primeira spec: o painel) e `meta/analises/` (primeira analise: o round-trip do acervo).

### Fixed
- **FIX-004:** o «Baixar .json» gravava um `Set` serializado como `{}` em cada faixa, e o «Importar .json» quebrava nele — o app estragava o proprio arquivo. O estado dos modulos ligados saiu de dentro da colecao.
- **FIX-005:** a importacao relatava qualquer falha como «nao e um JSON valido», e o `validate.py` dizia «Tudo conforme ao esquema» sem ter conferido esquema nenhum. Mensagem que nomeia um resultado so pode vir da operacao que o produz.
- **FIX-006:** arquivos ja contaminados continuavam propagando a chave interna. A importacao saneia as chaves com prefixo `_` e **diz quantas removeu**.
- **FIX-007:** o botao «copiar» do Style entregava o texto de antes do clique no chip de modulo. O que se via nao era o que se colava no Suno; a troca de estilo por modulo so chegava ao Suno pelo export MD.

### Changed
- **DEC-016 — acervo autossuficiente:** cada colecao traz os modulos que suas faixas citam; `schema/style-modules.json` e biblioteca de referencia para autoria. `data/exemplo-cinzeiro.json` recebeu os 5 modulos que citava sem ter.
- Kit de contexto atualizado de v1.74.0 para v1.131.0 (DEC-010 a DEC-015, DEC-017) — processo e documentacao, nenhuma mudanca de produto.

---

## [0.4.1] — 2026-07-21

Auditoria: correção de bug no dedup e alinhamento da documentação.

### Fixed
- **FIX-003: falso positivo no dedup do Style.** A comparação por substring crua barrava fragmentos legítimos — "female vocals" era descartado quando a base tinha "male vocals" (uma é substring da outra), e "harp" era barrado por "harpsichord". Passou a comparar **sequências de palavras**, com normalização simples de plural. 14 checks, incluindo regressão do FIX-002.
- Documentação desalinhada com o código: README anunciava "v0.1.0 — ferramenta a construir" (estava em 0.4.0 e publicada); CONTEXT dizia que o export MD ficaria para a Fase 3 (já entregue); ROADMAP e IDEAS marcavam o campo de exclusão como pendente (já implementado); STATUS listava no backlog a publicação no Pages (já feita) e a validação visual (já ocorrida).

### Added
- **HISTORY §9-13:** limites de campo verificados (Style ~1.000 chars, Lyrics 5.000 com ponto doce em ~3.000, título 100) e o achado central de que **o Suno trunca em silêncio**; teto prático de tags (~5-10, acima de 10 o modelo ignora as finais); ordem de tags (gênero primeiro); campo de exclusão mais confiável que negação no texto; mudanças de interface de jul/2026 (Lyrics Editor, Lyricist); contexto do processo GEMA.
- README: seções de validação do acervo e de geração por chat.

---

## [0.4.0] — 2026-07-21

Export para Markdown e correção do Style recomposto.

### Added
- **Export MD** (i-006): botões para exportar em Markdown a faixa (rodapé do cartão), o álbum (cabeçalho do álbum) e o acervo inteiro (cabeçalho). O `.md` mantém a regra inviolável — rótulo fora, conteúdo copiável em bloco limpo. Export de faixa usa o Style recomposto com os módulos ligados.

### Fixed
- **FIX-002: duplicação no Style recomposto.** Ligar módulos repetia conceitos já presentes no style base (ex.: base "dark ambient cinematic intro" + módulo "dark ambient cinematic" → ambos no texto), poluindo o prompt e desperdiçando as primeiras palavras (as que mais pesam no Suno). O dedup passou a comparar **por contenção**, não só igualdade exata.

### Changed
- `downloadCollection` refatorado sobre helper genérico `downloadFile`; cabeçalho do álbum alinhado ao centro.
- DEC-008 revisada após falha real de entrega (ver DECISIONS).

---

## [0.3.0] — 2026-07-19

Fecha o ciclo chat→ferramenta e adiciona validação de acervo.

### Added
- **`schema/PROMPT-PARA-CHATS.md`**: prompt-modelo colável que instrui qualquer chat a gerar canções no esquema canônico (ensina as cinco camadas audíveis, a regra copiável/referência, os dois campos do Suno e a saída em JSON puro). Fecha o ciclo "chat gera → ferramenta lê" (i-002/i-014).
- **`scripts/validate.py`**: valida `data/*.json` contra o schema (sintaxe + conformidade estrutural via jsonschema/referencing). Retorna código 1 em erro. Testado com caso negativo (id inválido, state fora do enum, campo faltando).

### Changed
- CLAUDE.md: passo de validação agora aponta para `scripts/validate.py`.

### Notas
- Verificação de integridade do repo confirmada: datasets conformes ao schema, lógica 11/11, HTML íntegro.

---

## [0.2.0] — 2026-07-19

Ferramenta v0 construída. Modelo das cinco camadas audíveis incorporado. Hospedagem definida.

### Added
- **Ferramenta `app/index.html`** (single-file, sem build): cartões por álbum; copiar Style/Lyrics/Exclude por botão; marcação "usei" automática (ao copiar) e manual (toggle); filtros por álbum/estado/uso; busca textual; painel de módulos de estilo por camada que recompõe o Style ao vivo; variantes e notas recolhíveis; importar/baixar JSON.
- **`index.html` raiz** que redireciona para o app (URL limpa no GitHub Pages).
- **`data/demo.json`**: 2 álbuns (instrumental + vocal), 3 faixas, com a biblioteca de módulos embutida.
- Biblioteca de módulos expandida para **27 módulos** nas cinco camadas audíveis (genre/motion/instrument/vocal/mood/production/tempo).

### Changed
- Categorias de módulo agora espelham as cinco camadas audíveis do modelo usesuno (DEC-007).

### Fixed
- FIX-001: auto-load do acervo tenta múltiplos caminhos (`data/` e `../data/`), corrigindo o fetch com o app em subpasta no GitHub Pages.

### Decisões (ver DECISIONS.md)
- DEC-006: GitHub Pages + carregamento auto-detectado (fetch/import).
- DEC-007: categorias de módulo = cinco camadas audíveis.
- FIX-001: caminho relativo do fetch.

### Notas
- Validação visual da ferramenta ainda pendente (screenshot bloqueado pela rede do container; lógica testada com 11/11 checks headless).

---

## [0.1.0] — 2026-07-19

Fundação do projeto. Arquitetura definida, esquema JSON canônico criado, documentação de contexto completa.

### Added
- Repositório inicial com estrutura de pastas (`meta/`, `schema/`, `data/`, `app/`, `logs/`).
- **Esquema JSON canônico:** `schema/song.schema.json` (canção), `schema/collection.schema.json` (coleção/álbuns), `schema/style-modules.json` (biblioteca de módulos de estilo reutilizáveis).
- **Dataset de prova:** `data/exemplo-cinzeiro.json` — faixa "Abertura das Forjas" (Cinzeiro-OST) convertida para o esquema, validando cobertura dos campos.
- Documentação de contexto completa: CONTEXT, STATUS, DECISIONS, CHANGELOG, IDEAS, ROADMAP, GLOSSARY, HISTORY, LOG-TEMPLATE.
- Arquivos-raiz: INSTRUCOES-DO-PROJETO.md, CLAUDE.md, README.md, .gitignore.
- Log de sessão `logs/2026-07-19.md`.

### Decisões (ver DECISIONS.md)
- DEC-001: JSON canônico como fonte de verdade, MD como export.
- DEC-002: ferramenta em HTML+JS single-file.
- DEC-003: nome "cancioneiro" (agnóstico de plataforma).
- DEC-004: dado canônico em arquivo versionado, não em localStorage.
- DEC-005: adaptação das Instruções ao domínio música/ferramenta.

### Notas
- A ferramenta (`app/index.html`) ainda não existe — é o marco da próxima fase.
- Conhecimento técnico do Suno herdado do guia de produção do Cinzeiro-OST e refinado com pesquisa de jul/2026 (v5.5) — consolidado em HISTORY.md.
