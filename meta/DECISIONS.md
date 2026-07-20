# DECISIONS.md — Cancioneiro

> Por que as coisas são como são. Decisões de arquitetura (DEC) e bugs graves resolvidos (FIX).
> Cresce devagar. Formato ADR: contexto, decisão, alternativas, consequências.

---

## DEC-001 — JSON canônico como fonte de verdade; Markdown como export

**Data:** 2026-07-19
**Contexto:** Os chats hoje entregam cada canção em `.md` com convenção livre, e cada álbum inventou a sua (`[ESTILO SUNO]`, `[LETRA]`, `[VAR A]`, emojis de bandeira, tabelas diferentes). Para a ferramenta fazer copy-por-campo, marcar "já copiado", trocar módulos de estilo e filtrar por bloco, ela precisa de **campos discretos e nomeados**, não de prosa formatada.

**Decisão:** O dado canônico do acervo é **JSON** validável por JSON Schema. Os chats passam a gerar nesse esquema. O **Markdown** deixa de ser entrada e vira **export** gerado pela ferramenta (uma canção, um álbum, ou tudo), para quem precisa do formato legível (colar num chat, subir num Projeto, ler humano).

**Alternativas consideradas:**
- *MD com front-matter YAML por canção:* legível, mas o corpo (style/lyrics) ainda seria texto livre a parsear, e o front-matter não cobre bem estruturas aninhadas (variantes, módulos). Meio-termo que herda a fragilidade do parser.
- *Parser universal de MD:* tentaria ler os álbuns antigos direto. Rejeitado: convenções divergentes tornam o parser um poço de exceções (é a causa da bagunça, não a solução).

**Consequências:** (+) Elimina ambiguidade na raiz; a ferramenta lê campos, não adivinha. (+) Um contrato único para todos os chats. (−) Converter o acervo existente é trabalho semi-manual/assistido, não automático. (−) JSON é menos amigável de editar à mão que MD — mitigado pela ferramenta e pelo export MD.

---

## DEC-002 — Ferramenta em HTML+JS single-file (sem framework, sem build)

**Data:** 2026-07-19
**Contexto:** Uso pessoal em Windows, copiar-colar rápido enquanto se gera música no Suno. O usuário não quer manter ambiente de dev (Node/Python) só para rodar a ferramenta.

**Decisão:** A ferramenta é **um único `app/index.html`** com JS vanilla e CSS embutido. Abre com duplo-clique no navegador, sem servidor, sem instalação, sem passo de build.

**Alternativas consideradas:**
- *Python (CLI/script):* exigiria Python instalado e não dá interface visual de cartões/botões naturalmente. Rejeitado para a ferramenta principal (pode voltar como utilitário de conversão em lote, se necessário).
- *App com framework (React/Vue) + build:* mais poder, mas introduz toolchain, `node_modules`, passo de build — contra o requisito de zero setup. Reavaliar só se a complexidade da UI crescer muito (ROADMAP).

**Consequências:** (+) Zero fricção de execução no Windows. (+) Portável (um arquivo). (−) Sem ecossistema de componentes; UI feita à mão. (−) Limite prático de complexidade antes de doer — aceitável para o escopo atual.

---

## DEC-003 — Nome "cancioneiro" (agnóstico de plataforma)

**Data:** 2026-07-19
**Contexto:** Nome vira raiz do repo e prefixo dos meta. O usuário pediu explicitamente algo não amarrado a "Suno", já que a ferramenta pode servir para outras plataformas de geração (Udio etc.) e o foco é *criar/compor/organizar canções*.

**Decisão:** **`cancioneiro`** — palavra portuguesa para coletânea de canções. Descreve o que a ferramenta faz (reúne e organiza canções) sem citar marca.

**Alternativas consideradas:** `suno-forge`, `suno-deck` (rejeitados: prendem à marca Suno); `cancioneiro` venceu por ser agnóstico e evocativo.

**Consequências:** (+) Sobrevive a troca de plataforma-alvo. (+) Nome curto e memorável. (−) Menos "descobrível" por quem busca "suno tool" — irrelevante para uso pessoal.

---

## DEC-004 — Dado canônico em arquivo versionado, nunca em localStorage

**Data:** 2026-07-19
**Contexto:** A pesquisa mostrou ferramentas concorrentes que guardam a biblioteca no `localStorage` do navegador. Isso significa perder tudo ao limpar o navegador ou trocar de máquina.

**Decisão:** O acervo real vive em **arquivo JSON versionado** (`data/`). A ferramenta **importa** o JSON e **exporta** o JSON/MD; o `localStorage` guarda apenas **estado efêmero** (marcações de "já copiei" da sessão, filtros ativos). Fonte de verdade = arquivo, sempre.

**Alternativas consideradas:** *localStorage como store principal* (rejeitado: frágil, não versionável, não compartilhável entre máquinas). *IndexedDB* (mais robusto que localStorage, mas ainda preso ao navegador; mesmo problema de fundo).

**Consequências:** (+) Acervo sobrevive a limpeza de navegador e é versionável no Git. (+) Portável entre máquinas. (−) Exige um passo explícito de import/export (não "salva sozinho") — mitigável com um botão de "baixar JSON atualizado" bem visível.

---

## DEC-005 — Adaptação das Instruções do Projeto ao nicho música/ferramenta

**Data:** 2026-07-19
**Contexto:** As Instruções do Projeto vêm do Kit no nicho "Desenvolvimento" genérico. Este projeto é dev, mas com um domínio específico (prompts de IA de música) que tem armadilhas próprias.

**Decisão:** Manter a base de Desenvolvimento (é um repositório de código real) e acrescentar, quando as Instruções forem refinadas, a regra específica do domínio: *"conteúdo copiável para o Suno nunca leva rótulo de referência dentro do bloco"*. Registrado também em «Feedback para o Kit» no IDEAS. Refino das Instruções fica para quando a ferramenta existir e o padrão de trabalho se firmar (evitar encurtar cedo demais).

**Consequências:** (+) Instruções permanecem fiéis ao processo enquanto o projeto amadurece. (−) Ainda genéricas por ora — aceitável na fundação.

---

## DEC-006 — Hospedagem em GitHub Pages + carregamento auto-detectado (fetch/import)

**Data:** 2026-07-19
**Contexto:** A ferramenta e um `index.html`. Aberta por duplo-clique (`file://`), o navegador PROIBE `fetch` de arquivos locais (trava de seguranca) — entao ela nao consegue ler `data/*.json` sozinha nesse modo. Servida por `http(s)://` (GitHub Pages), o `fetch` funciona. O usuario ja versiona no GitHub e quer o fluxo mais pratico.

**Decisao:** Publicar no **GitHub Pages** como fluxo principal (abrir um link, funciona em qualquer maquina, ate no celular). A ferramenta **auto-detecta o ambiente**: se servida por http(s), carrega `data/demo.json` sozinha (tenta `data/` e `../data/`); se em `file://`, pula o fetch e espera import manual. Em qualquer modo, os botoes "Importar .json" e "Baixar .json" estao sempre disponiveis. Um `index.html` na raiz redireciona para `app/index.html` (URL limpa no Pages).

**Alternativas consideradas:**
- *Vercel/Netlify:* servem para apps com build. Nosso HTML estatico nao precisa — seria toolchain a mais. Rejeitado.
- *So import manual (sem fetch):* funcionaria em file://, mas joga fora a conveniencia de "abrir o link e o acervo ja esta la" no Pages. O modo hibrido cobre os dois sem custo.

**Consequencias:** (+) Fluxo principal e so abrir um link; funciona multiplataforma. (+) Modo local (offline, file://) segue funcionando via import. (−) Trocar o acervo padrao exige commit no repo (coerente com DEC-004: JSON versionado e a fonte). (−) O caminho do acervo padrao (`demo.json`) esta fixo no codigo — trocavel por import ou editando uma linha.

---

## DEC-007 — Categorias de modulo espelham as cinco camadas audiveis

**Data:** 2026-07-19
**Contexto:** O guia do usesuno.com consolida um modelo de prompt em **cinco camadas audiveis** (musical lane, motion, sound sources, voice/lead, production space) + andamento. E um modelo mais forte e testavel que as categorias ad-hoc que o esquema tinha na fundacao (mood/instrument/vocal/genre/tempo soltos).

**Decisao:** As `category` dos modulos de estilo passam a espelhar essas camadas: `genre` (lane), `motion` (movimento/pulso), `instrument` (fontes), `vocal` (voz/lead), `mood` (clima), `production` (espaco de mix), `tempo` (andamento). A ferramenta agrupa os chips por camada nessa ordem. A biblioteca-semente foi expandida de 14 para 27 modulos cobrindo as camadas.

**Alternativas consideradas:** *Manter categorias livres* (rejeitado: sem modelo, a biblioteca vira bag desorganizada). *Copiar a taxonomia de genero de 10 categorias do usesuno* (adiado: util para submenu de genero na Fase 3, nao para as camadas de composicao).

**Consequencias:** (+) Menu de troca organizado por decisao audivel, alinhado a um modelo testado. (+) Ensina o usuario (e os chats) a pensar em camadas. (−) Modulos antigos precisam de category valida — ja migrados.

---

## FIX-001 — Caminho relativo do fetch quebrava com o app em subpasta

**Data:** 2026-07-19
**Sintoma:** Teste local (http.server) mostrou que o app em `app/index.html` buscando `data/demo.json` resolvia para `app/data/demo.json` (inexistente) — o auto-load falhava no GitHub Pages, onde o app fica em `/app/`.
**Causa raiz:** Caminho relativo unico e fragil; nao considerava a profundidade da pasta do app.
**Solucao:** O auto-load tenta uma lista de caminhos candidatos (`data/demo.json` e `../data/demo.json`), adotando o primeiro que responder 200. Validado com servidor local nos dois layouts.
**Licao:** Testar o fetch no layout real de deploy (app em subpasta) antes de assumir que "funciona local". O teste pegou o bug antes da entrega.
