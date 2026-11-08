# SPEC — Salvar no arquivo (frente de interface, entrega I4)

> **Status:** Pronta — aplicação pela `meta/workorders/261106-wo0030-salvar-no-arquivo.md` (0.17.0, DEC-033)
> **Decidida em:** a frente, em 2026-11-05 (DEC-030: a I4 é «salvar no arquivo», 0.17.0). Esta é a I4.
> **Data:** 2026-11-06 (data de criação; não muda depois)
> **Ideia de origem:** i-043 (gravar direto no arquivo do acervo, File System Access).
> **Protótipo:** telas «I4 · computador» e «I4 · celular» no canvas «Cancioneiro: nova interface»
> (`https://claude.ai/artifact/Sk1Xf5Rpr26WfGLbZJ2GAD`). A do computador é navegável: clique na alça ⋮⋮ de uma linha
> para criar uma alteração, depois em «Salvar» e no ▾ ao lado. Os quatro cenários («primeira vez», «reaberto», «mudou
> fora», «Firefox») ficam em Tweaks › cenario. As janelas do Windows e o aviso do Chrome são simulados.
> **Sonda:** `../261106-sonda-i4-salvar.html`, na pasta-pai, para o dono rodar no Chrome (roteiro no fim).
> **Depende de:** 0.16.0 (`6a07bfd`).

---

## Problema

Desde a 0.13.0 o acervo se organiza pela tela, num rascunho guardado no navegador. Para o arquivo `.json` voltar a ser
a fonte (DEC-028), o dono clica «Salvar .json», o navegador baixa uma cópia em Downloads, e ele substitui o arquivo
antigo à mão, tirando o «(1)» quando o navegador o acrescenta. São três passos fora do app a cada sessão de curadoria,
e o passo esquecido deixa o rascunho meses à frente do arquivo (DEC-029). A I4 tira esses passos onde o navegador
deixa: «Salvar» grava no próprio arquivo.

## O que já se sabe (pesquisa e medição)

- **Onde a API existe** (web-features, consultado em 2026-11-06): Chrome e Edge 86 no computador (2020), Chrome
  Android 132 (2025-01). Firefox tem posição **negativa** e Safari **contrária**; não há previsão. O «Baixar .json»
  continua sendo o caminho permanente nesses dois, não um atalho provisório.
- **No Chrome 156 do dono** existem `showSaveFilePicker`, `showOpenFilePicker` e `getAsFileSystemHandle` (sonda de
  2026-11-04) `[medido por instrumento]`.
- **`file://` conta como contexto seguro** no Chromium 153 headless: `isSecureContext` = true, e as três APIs existem
  (medido pelo chat em 2026-11-06). A pasta privada do navegador (`navigator.storage.getDirectory`) é recusada no
  `file://` com `SecurityError` — não é ela que a I4 usa, mas mostra que o `file://` tem restrições próprias. **Abrir
  a janela, gravar, guardar o vínculo e reabrir não dá para medir sem tela:** é o que a sonda pergunta.
- **A permissão de gravar vale até fechar a última aba.** Ao reabrir, o vínculo guardado no IndexedDB volta como
  «perguntar», e o primeiro «Salvar» mostra um aviso do Chrome. Desde o Chrome 122 esse aviso pode trazer «Permitir em
  todas as visitas», quando o vínculo foi guardado no IndexedDB e o site o pede de novo (Chrome for Developers,
  «Persistent permissions»). Se isso vale para o `file://`, a sonda diz.
- **Gravar não deixa arquivo pela metade no computador:** o Chrome escreve num `.crswap` ao lado e só troca pelo
  arquivo no fim. No Android a troca não é atômica e a janela de «salvar como» não cria arquivo novo (intent to ship
  do Chrome Android, 2024).
- **Padrão de quem já faz isso:** o VS Code na web guarda os vínculos no IndexedDB e pede a permissão de novo ao
  reabrir; o exemplo do web.dev detecta a API e cai no download onde ela não existe — o mesmo desenho desta spec.

## O que construir

### 1. «Salvar» grava no arquivo vinculado

- **O botão do rascunho chama-se «Salvar»** (era «Salvar .json») onde a API existe, e `Ctrl+S` (`⌘S` no Mac) faz o
  mesmo (ponto 4). Ao lado, um ▾ abre:
  - **Salvar no arquivo** · `Ctrl+S`;
  - **Salvar em outro arquivo…**: a janela do sistema; o acervo passa a ficar vinculado ao arquivo escolhido;
  - **Baixar .json**: uma cópia em Downloads, como hoje. Com vínculo, o arquivo vinculado não muda e o rascunho
    **continua** marcado como não salvo; sem vínculo, é o «Salvar .json» de hoje.
- **Primeira vez num acervo (sem vínculo):** «Salvar» abre a janela «Salvar como» do sistema com o nome de origem
  (`App.source`) já preenchido. O dono vai à pasta, confirma «substituir», e o app grava. Daí em diante o acervo está
  **vinculado** àquele arquivo (ponto 1).
- **Com vínculo:** «Salvar» grava sem janela. Se o navegador não tiver mais a permissão (aba reaberta), o aviso do
  Chrome aparece uma vez; «Não permitir» não grava nada e diz como baixar.
- **Depois de gravar:** o número de alterações zera, a marca vira «✓ Salvo no arquivo às HH:MM», e o aviso diz
  «Salvo em <nome> às HH:MM». O arquivo gravado é o mesmo texto do «Salvar .json» de hoje (JSON com 2 espaços, chaves
  internas tiradas), mais uma quebra de linha no fim.

### 2. O vínculo

- **Guardado no registro do acervo no IndexedDB** (`cancioneiro`, o mesmo depósito), em dois campos novos: o
  vínculo com o arquivo e a marca do arquivo na última leitura ou gravação (data de modificação e tamanho). Sem banco
  novo e sem mudar a versão do banco. Nada vai para o `.json`.
- **Importar pela janela ou arrastando também vincula** (ponto 1): no Chrome, «Importar .json…» usa a janela do
  sistema de abrir arquivo em vez do `<input type=file>`, e soltar um `.json` pega o vínculo do arquivo solto. A
  permissão de **gravar** é pedida só no primeiro «Salvar».
- **O seletor de acervo mostra o vínculo**: «Vinculado a <nome>. «Salvar» grava nele.», ou «Sem vínculo: o primeiro
  «Salvar» pede o arquivo.». Ali mora **Desvincular do arquivo**.
- **Esquecer o acervo** apaga também o vínculo. **Reimportar** troca o vínculo pelo do arquivo novo.
- **Sem IndexedDB** (o modo de reserva, um acervo no `localStorage`): sem vínculo; «Salvar» baixa, como hoje.

### 3. O arquivo mudou fora do app (ponto 2)

- **Antes de gravar, o app relê a data e o tamanho do arquivo.** Se diferem da marca guardada, abre «<nome> mudou fora
  do app», com as duas datas, e três botões: **Cancelar**, **Salvar em outro arquivo…** e **Substituir mesmo assim**.
- **O arquivo sumiu ou foi renomeado:** o aviso diz isso e oferece «Salvar em outro arquivo…»; o vínculo continua até
  o dono desvincular ou salvar em outro.

### 4. «Desfazer» depois de salvar (ponto 3)

- **A volta da última operação continua valendo depois de «Salvar».** Desfazer depois de salvar devolve o rascunho a
  «1 alteração não salva». Revê o «salvar esquece a volta» da DEC-032, que existia porque salvar era baixar um arquivo
  e substituir à mão.

### 5. Onde não grava direto

- **Firefox, Safari e navegadores sem a API:** o botão volta a se chamar «Salvar .json» e baixa, como na 0.16.0; o ▾
  só tem «Baixar .json». O seletor de acervo diz «Este navegador não grava direto no arquivo».
- **Celular** (ponto 5): também baixa, mesmo no Chrome Android que tem a API.
- **Página do Pages** (`https://`): grava, com vínculos próprios; o `file://` e o Pages são origens diferentes, como as
  cópias guardadas.

### O que não muda

- O rascunho no IndexedDB, gravado a cada operação (DEC-028); a confirmação ao esquecer e ao reimportar com
  alterações (DEC-029).
- O que se copia e o que se exporta (os Exportar .md e .json continuam baixando).
- O formato do `.json`.

## O que muda para quem usa (a conta tem de fechar)

| Gesto de hoje (0.16.0) | Na I4 (Chrome ou Edge no computador) |
|---|---|
| «Salvar .json», abrir Downloads, mover para a pasta, substituir, tirar o «(1)» | «Salvar» (ou `Ctrl+S`); a primeira vez de cada acervo, confirmar o arquivo na janela |
| Rascunho esquecido por meses | o mesmo lembrete, mas salvar custa um clique |
| Depois de salvar, sem «Desfazer» | «Desfazer» continua até a próxima operação |
| Arquivo editado fora sem aviso | o app pergunta antes de gravar por cima |
| Firefox, Safari, celular | igual a hoje |

## Critérios de pronto (o chat mede no Chromium headless antes da WO)

**Como se mede o que tem janela:** o headless não abre a janela do sistema. Os testes trocam `showSaveFilePicker` e
`showOpenFilePicker` por versões que devolvem arquivos de verdade da pasta privada do navegador, e por isso rodam em
`http://127.0.0.1` (no `file://` essa pasta é recusada). A permissão é simulada trocando `queryPermission` e
`requestPermission`. A janela real e o aviso real ficam com a sonda e com o roteiro de tela do dono.

| # | Critério |
|---|---|
| C1 | Com a API: o botão diz «Salvar», o ▾ tem «Salvar no arquivo», «Salvar em outro arquivo…» e «Baixar .json». Sem a API (as funções apagadas antes de carregar): o botão diz «Salvar .json», o ▾ só «Baixar .json», e salvar baixa como na 0.16.0. |
| C2 | Sem vínculo, «Salvar» chama a janela de salvar com `suggestedName` = nome de origem; grava; o arquivo lido de volta é igual, byte a byte, ao que o «Baixar .json» baixaria, mais a quebra de linha final; zera as alterações; o vínculo fica no registro do IndexedDB. **Falso positivo:** cancelar a janela não grava, não zera, não vincula e não mostra erro. |
| C3 | Com vínculo e permissão, «Salvar» grava **sem** chamar janela nenhuma. |
| C4 | Depois de recarregar a página, o vínculo volta do IndexedDB; com a permissão em «perguntar», «Salvar» chama `requestPermission` uma vez; «granted» grava; «denied» não grava, não zera e diz como baixar. |
| C5 | Importar pela janela de abrir e soltar um `.json` deixam o acervo vinculado ao arquivo; o primeiro «Salvar» grava nele sem janela de salvar. |
| C6 | Arquivo mudado fora (data ou tamanho diferentes da marca): «Salvar» abre o aviso e não grava; «Substituir mesmo assim» grava; «Salvar em outro arquivo…» grava no outro e vincula a ele; «Cancelar» não grava. **Falso positivo:** gravar duas vezes seguidas pelo app não abre o aviso na segunda. |
| C7 | Arquivo apagado depois de vincular: «Salvar» avisa que ele sumiu, não perde o rascunho e oferece «Salvar em outro arquivo…». |
| C8 | «Baixar .json» com vínculo baixa a cópia e **não** zera as alterações nem muda o arquivo vinculado. |
| C9 | `Ctrl+S` com alterações faz o mesmo que o botão e impede o «salvar página» do navegador; sem alterações, não faz nada visível; dentro de um campo de texto, também salva. |
| C10 | Depois de «Salvar», «Desfazer» e `Ctrl+Z` voltam a última operação e o rascunho a «1 alteração não salva». |
| C11 | O seletor de acervo mostra o vínculo e «Desvincular do arquivo»; desvincular tira o vínculo do registro, e o próximo «Salvar» pede a janela; esquecer o acervo apaga o vínculo junto. |
| C12 | No celular (390×844), com a API presente: o pé mostra «Baixar .json», e salvar baixa. |
| C13 | Abrir com 205 faixas fica, no máximo, 50 ms mais lento que a 0.16.0 (média de 5, mesmas rodadas); gravar um acervo de 205 faixas leva no máximo 1 s. |
| C14 | O cabeçalho diz `v0.17.0`; nenhum erro de página; os testes das entregas 1 a 3, da I1, da I2 e da I3 continuam passando (os que clicam «Salvar .json» rodam sem a API ou pelo «Baixar .json»). Nenhum código lê ou apaga chave sem o nome `cancioneiro`. |

**Prova de vida:** o mesmo teste no app da 0.16.0 reprova, no mínimo, C1, C2 e C3.

## Resultado (medido pelo chat em 2026-11-06, Chromium headless, app de chegada da WO 0030)

**14 de 14 critérios.** Acervo de teste: o `data/demo.json` (3 faixas, 2 álbuns), gravado num arquivo da pasta privada do
navegador e aberto pela janela trocada; para o C13, um acervo de 205 faixas em 12 álbuns feito a partir dele (293 KB).

| # | O que foi conferido | Resultado |
|---|---|---|
| C1 | sem a API: «Salvar .json», sem ▾, baixa `demo.json` e zera; com a API: «Salvar», o ▾ com os três itens | OK |
| C2 | sem vínculo, a janela com `suggestedName` = nome de origem; o arquivo gravado é o JSON do acervo com 2 espaços e a quebra final; zera e vincula; cancelar a janela não grava, não zera, não vincula e só avisa «Nada foi gravado.» | OK |
| C3 | com vínculo, grava sem janela (só `queryPermission`) | OK |
| C4 | recarregar traz o vínculo; com «perguntar», «Salvar» chama `requestPermission`; negar não grava e avisa; permitir grava | OK |
| C5 | importar pela janela de abrir vincula, e o primeiro «Salvar» grava sem janela de salvar | OK |
| C6 | mudado fora: o aviso com Cancelar, Salvar em outro… e Substituir; cancelar não grava; substituir grava; outro grava e vincula ao outro; duas gravações seguidas pelo app não abrem o aviso | OK |
| C7 | arquivo apagado: avisa, oferece «Salvar em outro arquivo…», e o rascunho fica | OK |
| C8 | «Baixar .json» com vínculo baixa e não zera nem muda o arquivo | OK |
| C9 | `Ctrl+S` com o foco na busca salva e impede o padrão do navegador; sem alterações, impede o padrão e não grava | OK |
| C10 | depois de salvar (no arquivo e baixando), «Desfazer» e `Ctrl+Z` voltam a «1 alteração não salva» | OK |
| C11 | o seletor mostra «Vinculado a…» e «Desvincular»; desvincular tira o vínculo do registro e o próximo «Salvar» pede a janela; esquecer apaga o registro com o vínculo | OK |
| C12 | a 390×844, com a API presente: «Salvar .json», sem ▾, baixa sem chamar janela | OK |
| C13 | abrir 205 faixas, média de 5, três rodadas: 243, 235 e 218 ms, contra 209, 218 e 217 ms da 0.16.0 nas mesmas rodadas (no pior caso, +34 ms; o limite era +50); gravar 205 faixas: 10 a 14 ms | OK |
| C14 | `v0.17.0`; nenhum erro de página nos três cenários | OK |

**Prova de vida, medida:** no app da 0.16.0 o teste para no C1 (não há o ▾ de salvar).

**Regressão:** os testes das entregas anteriores não estão no repositório nem nesta conversa (viraram a i-051). A
regressão foi por fumaça: importar, a Lista com 3 linhas, o detalhe, Descer pelo «⋯» do detalhe (+1 alteração), Cartões
com 3 cartões, sem erro de página; soltar um `.json` sem vínculo importa como antes. O arrastar da I3 não foi refeito.
`validate.py` exit=0 com `jsonschema`.

**Onde a implementação saiu da spec:**
- **Sem a API não há ▾:** o botão já baixa, e o «⋯» da barra tem «Baixar .json». A spec previa o ▾ só com ele.
- **O aviso da primeira vez** («Escolha o arquivo X para o app gravar nele daqui em diante…») sai como aviso no pé, junto
  da janela, sem clique a mais.
- **Salvar com outro nome:** neste navegador o acervo continua com o nome de origem, e o aviso diz isso.
- **O C13 mediu a importação inteira** (ler o arquivo, guardar e desenhar), por isso os números são maiores que os da I3;
  a comparação é com a 0.16.0 nas mesmas rodadas.
- **O teste roda num perfil persistente do Chromium:** no contexto anônimo, ler do IndexedDB um handle guardado derruba a
  aba (medido). No Chrome do dono a sonda leu o handle guardado sem problema.
- **Soltar o arquivo com vínculo** não se mede no headless (um drop sintético não traz handle); a sonda viu o handle no
  Chrome do dono, com a permissão de gravar em «perguntar», que o primeiro «Salvar» pede.

**A sonda no Chrome 156 do dono (`file://`, 2026-11-06 16:27):** janela de salvar e gravação (221 ms na primeira, cerca de
100 ms depois); gravar de novo sem janela; handle guardado e lido do IndexedDB; janela de abrir com gravação; handle ao
arrastar. **Não medido:** o fechar e reabrir (a página não foi reaberta: o relatório não tem a linha «página reaberta») e o
arquivo mudado fora (o arquivo de teste não foi editado). Os dois ficam no roteiro de tela da I4.

## Riscos

- **O aviso de permissão a cada sessão.** Se o `file://` não ganhar «Permitir em todas as visitas», será um clique por
  sessão, no primeiro «Salvar». Ainda é menos que os três passos de hoje. A sonda mede.
- **Gravar por cima do arquivo errado.** A primeira gravação passa pela janela do sistema, que pede para confirmar a
  substituição; depois, o vínculo vem do próprio arquivo, não do nome. O nome no seletor de acervo e no aviso diz
  onde gravou.
- **O `.crswap`:** se o navegador fechar no meio da gravação, pode sobrar um arquivo `.crswap` ao lado do
  arquivo; o arquivo em si fica inteiro. Inofensivo; apaga-se à mão.
- **Pasta sincronizada (OneDrive e afins):** a troca do arquivo pode gerar conflito de sincronização. As pastas do
  dono hoje são locais (`C:\Users\alexk\Tools`).
- **Comportamento do Chrome muda entre versões** (a permissão já mudou no 122). O teste usa a API, não a janela; a
  sonda e o roteiro de tela é que pegam mudança de comportamento.
- **O app passa a pedir permissão de arquivo** — algo que nunca pediu. O texto do aviso é do Chrome; o app diz antes,
  na primeira vez, o que vai acontecer («Escolha o arquivo do acervo para o app gravar nele daqui em diante»).

## Fora de escopo

- **Salvar sozinho a cada operação** (autosave). O rascunho no IndexedDB já guarda tudo a cada operação; gravar no
  arquivo a cada clique tornaria o «Desfazer» e o aviso de arquivo mudado mais confusos, e faria o aviso de permissão
  aparecer no meio da curadoria. Pode virar ideia depois de usar a I4.
- **Mesclar** a versão de fora com o rascunho, quando o arquivo mudou fora: só avisar e deixar escolher.
- **Gravar no celular** (ponto 5).
- **Abrir uma pasta inteira de acervos** (`showDirectoryPicker`): cada acervo continua sendo um arquivo.
- **Organizar os álbuns** (i-049) e **arrastar faixa para outro acervo** (i-050).

## Pontos para o dono decidir

**Decididos pelo dono em 2026-11-06, os cinco como recomendados** (DEC-033), depois da sonda.

1. **Como o acervo se vincula ao arquivo.**
   - **(a) Nos dois caminhos (recomendado):** no primeiro «Salvar» de cada acervo, pela janela de salvar, e também ao
     importar pela janela ou arrastando. Os três acervos que já estão no navegador se vinculam no primeiro «Salvar»,
     sem reimportar.
   - (b) Só no primeiro «Salvar»: menos código, mas importar e salvar logo em seguida sempre passa por duas janelas.
   - (c) Só ao importar: exige reimportar os acervos que já estão no navegador.
2. **Arquivo mudado fora do app.**
   - **(a) Conferir data e tamanho e perguntar antes de gravar (recomendado):** custa uma leitura antes de cada
     gravação; protege o caso de editar o `.json` à mão, ou num chat, e esquecer o rascunho aberto.
   - (b) Gravar sem conferir: mais simples; a versão de fora some em silêncio.
3. **«Desfazer» depois de salvar.**
   - **(a) Continua valendo (recomendado):** salvar fica barato (`Ctrl+S`), e perder a rede de segurança a cada
     salvar ensinaria a não salvar.
   - (b) Esquece, como hoje (DEC-032): mais simples de explicar, mas `Ctrl+S` passa a apagar a volta.
4. **`Ctrl+S`.**
   - **(a) Salva, em qualquer navegador e até dentro de um campo de texto (recomendado):** onde não grava direto,
     baixa, como o botão.
   - (b) Só onde grava direto; nos outros, fica o «salvar página» do navegador, que não serve para nada aqui.
5. **Celular.**
   - **(a) Só «Baixar .json» (recomendado):** no Android a gravação não é atômica, a janela não cria arquivo novo, e o
     uso no celular hoje é consulta e cópia.
   - (b) Gravar direto também no Chrome Android, com o risco de arquivo pela metade se a gravação cair.

## Sonda — roteiro para o dono (antes de decidir os pontos)

1. Na pasta `C:\Users\alexk\Tools\cancioneiro`, abra `261106-sonda-i4-salvar.html` com duplo-clique no **Chrome**.
2. Faça os passos 1 a 5 na ordem que a página mostra. No passo 3, feche **todas** as abas da sonda antes de reabrir.
   Marque na página o que o Chrome mostrou.
3. No passo 6, salve o relatório na mesma pasta, com o nome sugerido (`261106-sonda-i4-relatorio.txt`).
4. Clique o passo 7 e apague à mão o `sonda-i4-teste.json`.

**Esperado quando está certo:** o passo 1 abre a janela «Salvar como» e grava; o passo 2 grava sem janela; o passo 3
mostra um aviso do Chrome e grava; o passo 4 diz «mudou fora = true»; o relatório chega à pasta-pai. Se o passo 1 der
erro, a I4 não serve no `file://` e a spec muda antes de qualquer código.
