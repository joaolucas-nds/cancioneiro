# ROADMAP.md — Cancioneiro

> Plano deliberado de evolução em fases. Estado: ✅ concluída · 🔨 em curso · ⬜ próxima · 💭 futura.
> Detalhe de execução vive no STATUS; ideias soltas no IDEAS. Aqui é só a direção.

---

## ✅ Fase 1 — Fundação (2026-07-19)
Arquitetura, esquema e documentação.
- ✅ Estudo do fluxo existente (Cinzeiro-OST + guias de álbum) e do estado do Suno (v5.5).
- ✅ Decisões de arquitetura (DEC-001 a 005).
- ✅ Esquema JSON canônico (`schema/`).
- ✅ Dataset de prova (1 faixa convertida).
- ✅ Documentação de contexto (`meta/`) e arquivos-raiz.

## 🔨 Fase 2 — Ferramenta v0 (MVP de leitura + cópia)
O mínimo que já é útil: ler o acervo e copiar sem procurar.
- ✅ `app/index.html`: importar/carregar JSON, renderizar álbuns → canções como cartões (i-001).
- ✅ Botão copiar por campo (Style / Lyrics separados), com marcação de "já copiado" + "usei" manual (i-003).
- ✅ Filtro por estado da canção + álbum + uso + busca textual (i-007).
- ✅ Export MD de faixa / álbum / acervo (i-006).
- ✅ Prompt-modelo para chats gerarem no esquema (i-002).
- ✅ Prompt-modelo com contrato de modulos e orcamento de tags; prompt e exemplo pelos botoes do app (DEC-021, i-028, i-031) — 0.8.0, retestado pelo dono.
- ✅ Script de validação de acervo `scripts/validate.py`.
- 🔨 Conveniências de uso: estrutura do cartão configurável, copiar título, arrastar o `.json`, acervo guardado no navegador, prompt que entrega arquivo, export de álbum com o Style da tela (DEC-022, DEC-023; i-030, i-033 a i-037) — aplicadas, falta a tela e o reteste do dono.
- ⬜ Converter `album_guia_suno.md` inteiro como segundo dataset (i-008).
**Marco:** conseguir usar a ferramenta de verdade numa rodada de geração no Suno.

## 🔨 Fase 3 — Qualidade de prompt e modularidade
O diferencial real sobre os builders genéricos: a ferramenta não só organiza, ela **impede prompt ruim**. Fundamentado em constraints verificados (HISTORY §9-11). Núcleo modular já entregue no v0.

**3a — Painel de qualidade — ✅ concluída em 0.5.0 (DEC-018), conferida na tela pelo dono em 2026-10-27:**
- ✅ Contador de caracteres do Style e do Exclude (1.000) e do Lyrics (5.000, aviso a partir de ~3.000), medindo o Style **recomposto** e atualizando a cada chip (i-017).
- ✅ Contador de tags: âmbar acima de ~10, nunca vermelho (i-018).
- ✅ «no X» no style detectado por fronteira de palavra; **só avisa** — migrar num clique ficou fora (DEC-018); `no vocals` não dispara em faixa instrumental (i-019).
- ⏸ Aviso de ordem: gênero nas primeiras palavras (i-020) — **adiado**: dispara em 0 de 10 faixas reais; gatilho no IDEAS.

**3a.2 — ✅ concluída em 0.6.0 (DEC-019), conferida na tela pelo dono em 2026-10-27:**
- ✅ O custo de cada módulo em tags, no próprio chip, e a folga do style base na linha de qualidade (i-026). A lista de corte automática foi descartada pela medição: mandaria cortar a voz de rap em faixas de rap-pop.

**3b — Modularidade (continuação):**
- ✅ Módulos de estilo ligáveis/desligáveis por menu, recompondo o style (i-004) — v0 entregue, refinar UX na iteração.
- ✅ Controle de BPM no cartão (i-005, DEC-020) — 0.7.0, conferido na tela pelo dono em 2026-10-28; campo numérico, não slider, e o chip de andamento vira atalho.
- ✅ Campo de exclusão de estilos (i-009) — no esquema e com botão de copiar na ferramenta.
- ✅ Export MD completo (i-006).
- ⬜ Importar prompts prontos dos álbuns como módulos.

## 💭 Fase 4 — Refino e escala (futura, sob demanda)
Só se o uso pedir.
- 💭 Validação do JSON contra o schema em runtime.
- 💭 Suporte a `layers[]` para OST de jogo (duas camadas sincronizadas) (i-010).
- 💭 Reavaliar stack (framework + build) se a UI ficar complexa demais para single-file (revisita DEC-002).
- 💭 Suporte a outras plataformas além do Suno (Udio etc.) — o nome já é agnóstico.
