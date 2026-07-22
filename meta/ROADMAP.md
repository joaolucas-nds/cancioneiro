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
- ✅ Script de validação de acervo `scripts/validate.py`.
- ⬜ Converter `album_guia_suno.md` inteiro como segundo dataset (i-008).
**Marco:** conseguir usar a ferramenta de verdade numa sessão de geração no Suno.

## 🔨 Fase 3 — Modularidade (estilos e BPM trocáveis)
O diferencial sobre os builders genéricos. **Núcleo já entregue no v0** (painel de módulos recompõe o style ao vivo); resta refinar.
- ✅ Módulos de estilo ligáveis/desligáveis por menu, recompondo o style (i-004) — v0 entregue, refinar UX na iteração.
- ⬜ Controle de BPM por slider/stepper (i-005).
- ⬜ Campo de exclusão de estilos (i-009).
- ✅ Export MD completo (i-006).
- ⬜ Importar prompts prontos dos álbuns como módulos.

## 💭 Fase 4 — Refino e escala (futura, sob demanda)
Só se o uso pedir.
- 💭 Validação do JSON contra o schema em runtime.
- 💭 Suporte a `layers[]` para OST de jogo (duas camadas sincronizadas) (i-010).
- 💭 Reavaliar stack (framework + build) se a UI ficar complexa demais para single-file (revisita DEC-002).
- 💭 Suporte a outras plataformas além do Suno (Udio etc.) — o nome já é agnóstico.
