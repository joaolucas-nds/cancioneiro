# SPEC — Salvar no arquivo (frente de interface, entrega I4)

> **Status:** Rascunho — espera a sonda no Chrome do dono e os cinco pontos para o dono decidir.
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
