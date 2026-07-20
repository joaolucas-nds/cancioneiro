---
name: apply-spec
description: Aplica uma spec de meta/specs/ ao repo — localiza cada âncora exatamente, substitui, e para se não achar. Use quando o usuário pedir /apply-spec ou para aplicar uma spec nomeada.
disable-model-invocation: true
---
Leia o arquivo de spec indicado em `meta/specs/` e execute-o.
Localize cada âncora EXATAMENTE; se não achar uma, PARE e reporte — não chute um lugar próximo.
Não toque em nada fora das edições nomeadas. Ao fim, rode `git diff` e confira a forma esperada antes de commitar.
Spec: $ARGUMENTS
