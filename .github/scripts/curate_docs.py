import os, pathlib, openai
from openai.error import InvalidRequestError

openai.api_key = os.environ["OPENAI_API_KEY"]
MODEL = "gpt-3.5-turbo-16k"

TEMPLATE = """Corrige ortografía y añade al principio:
---
title: "{title}"
tags: [consultoria, gastronomia]
---
No cambies el sentido del texto; responde solo con el documento corregido."""

for md in pathlib.Path("docs").rglob("*.md"):
    texto = md.read_text(encoding="utf-8")
    prompt = TEMPLATE.format(title=md.stem.replace("-", " ").title())

    try:
        respuesta = openai.ChatCompletion.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt + "\n\n" + texto}],
            temperature=0
        ).choices[0].message.content
        md.write_text(respuesta, encoding="utf-8")
        print(f"✔️ Curado {md}")
    except InvalidRequestError as e:
        print(f"⚠️  {md} SALTADO – demasiado grande: {e}")
