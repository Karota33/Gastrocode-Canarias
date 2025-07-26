import os, pathlib, openai

openai.api_key = os.environ["OPENAI_API_KEY"]
MODEL = "gpt-3.5-turbo-16k"      # modelo de 16 000 tokens

MAX_CHARS = 35000                # ~16k tokens ≈ 32-36k caracteres

TEMPLATE = """Corrige ortografía y añade al principio:
---
title: "{title}"
tags: [consultoria, gastronomia]
---
No cambies el sentido del texto; responde solo con el documento corregido."""

for md in pathlib.Path("docs").rglob("*.md"):
    original = md.read_text(encoding="utf-8")

    # Si el archivo es demasiado grande, lo saltamos
    if len(original) > MAX_CHARS:
        print(f"⚠️  {md} supera {MAX_CHARS} caracteres. Revísalo manualmente.")
        continue

    prompt = TEMPLATE.format(title=md.stem.replace("-", " ").title())
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt + "\n\n" + original}],
        temperature=0
    ).choices[0].message.content

    md.write_text(response, encoding="utf-8")
    print(f"✔️ Curado {md}")
