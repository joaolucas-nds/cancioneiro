# WO-0001 — Registrar fatos relatados no chat e pendências abertas

**Data:** 2026-07-21
**Origem:** fecho da sessão de auditoria (conversa ficou pesada; transferência para conversa nova).
**Motivo:** fatos que o dono relatou no chat e que não existem em arquivo nenhum. Para a próxima conversa, o que não está em arquivo não existe.

**Como aplicar:** `/apply-wo 260721-wo0001`
Cada edição abaixo tem a âncora exata. Se uma âncora não for encontrada, PARE e reporte — não improvise posição.

---

## Edição 1 — `meta/STATUS.md`

**Âncora (localizar esta linha exata):**
```
- **Publicado no GitHub Pages** e validado de olho pelo usuário — funcionando.
```

**Substituir por:**
```
- **Publicado no GitHub Pages** em `https://joaolucas-nds.github.io/cancioneiro/app/index.html` — validado de olho pelo dono, funcionando `[relatado pelo dono, com print da interface em 2026-07-21]`.
- **0.4.1 aplicada no repo do dono** `[verificado no mount em 2026-07-21: app com FIX-003, STATUS/CHANGELOG em 0.4.1]`.
```

---

## Edição 2 — `meta/STATUS.md`

**Âncora (localizar esta linha exata):**
```
## Notas de estado
```

**Inserir LOGO ABAIXO da âncora (antes das notas existentes):**
```

- **Repo local do dono:** `C:\Users\alexk\Tools\cancioneiro` (Windows). O repositório é a fonte de verdade; o ambiente do assistente é descartável e NÃO sincroniza sozinho — ver DEC-008.
- **Fluxo de upload:** o dono usa FlatDrop para achatar a árvore ao subir no Projeto de chat (`_MANIFEST_cancioneiro.md` e `_TREE_cancioneiro.md` são artefatos dessa ferramenta, não fazem parte do repo). Por isso os arquivos chegam achatados no mount com nomes como `index__app.html`.
- **Pendência de contexto — ASU:** o dono perguntou se o "modo ASU" do KCM seria melhor que o modo Code para este projeto. O assistente NÃO tem a definição de ASU (o CEREBRO só o cita de passagem em nomenclatura de specs, `AAMMDD-asuNNNN.yaml`). Recomendação ficou pendente até o dono colar a descrição do ASU `[relatado pelo dono, sem material de apoio]`.
```

---

## Edição 3 — `meta/DECISIONS.md`

**Âncora (localizar a ÚLTIMA linha do arquivo, fim do bloco FIX-003):**
```
**Licao:** Ao corrigir um bug de comparacao, testar explicitamente o **falso positivo** (o que NAO deve ser barrado), nao so o caso que motivou a correcao. O FIX-002 so testava "nao duplica"; faltava "nao barra o que e diferente".
```

**Acrescentar ao FINAL do arquivo (depois da âncora):**
```

---

## DEC-009 — Pensamento estendido ligado nas sessoes de trabalho deste projeto

**Data:** 2026-07-21
**Contexto:** O dono identificou que as conversas anteriores rodaram com o pensamento estendido DESLIGADO, e observou que era a causa dos problemas de desenvolvimento `[relatado pelo dono, 2026-07-21]`. A evidencia apoia: com pensamento desligado ocorreram (a) a falha de entrega da 0.4.0 — implementei e commitei no ambiente do assistente sem entregar arquivo, mandando o dono "sincronizar" algo que nao sincroniza; (b) o FIX-002 introduzindo o falso positivo do FIX-003, com teste que espelhava a premissa errada do codigo.

**Decisao:** Sessoes de trabalho deste projeto rodam com **pensamento estendido LIGADO**. O projeto envolve decisao de arquitetura, analise de dominio (Suno) e correcao de logica com armadilhas sutis — as tres coisas degradam sem raciocinio explicito.

**Consequencias:** (+) Menos erro de reflexo e menos retrabalho. (+) Auditorias e correcoes de comparacao ficam confiaveis. (−) Respostas um pouco mais lentas — custo aceitavel diante do retrabalho evitado.
```

---

## Edição 4 — `meta/CONTEXT.md`

**Âncora (localizar esta linha exata):**
```
## Produto / uso
```

**Inserir LOGO ACIMA da âncora:**
```
## Onde vive

- **Repo do dono:** `C:\Users\alexk\Tools\cancioneiro` (Windows). Fonte de verdade.
- **Publicado:** `https://joaolucas-nds.github.io/cancioneiro/app/index.html` (GitHub Pages, branch main, root). A raiz do site redireciona para o app.
- **Upload para o Projeto de chat:** via FlatDrop, que achata a árvore (por isso `app/index.html` chega como `index__app.html`).

```

---

## Verificação após aplicar

```
python3 scripts/validate.py
git diff --stat
```

Esperado: 3 arquivos alterados (`meta/STATUS.md`, `meta/DECISIONS.md`, `meta/CONTEXT.md`), acervo conforme ao esquema.

**Commit:**
```
git add -A && git commit -m "docs: registra fatos relatados, ambiente do dono e DEC-009 (pensamento ligado)"
```
