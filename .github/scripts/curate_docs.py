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

CHUNK_SIZE = 8000            # ~8000 caracteres ≈ 3500-4000 tokens

def limpiar_texto(titulo: str, texto: str) -> str:
    prompt = TEMPLATE.format(title=titulo)
    try:
        resp = openai.ChatCompletion.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt + "\n\n" + texto}],
            temperature=0
        )
        return resp.choices[0].message.content
    except InvalidRequestError as e:
        print(f"⚠️  Lote saltado por error: {e}")
        return texto  # devuelve el original sin cambios

for md in pathlib.Path("docs").rglob("*.md"):
    original = md.read_text(encoding="utf-8")
    titulo = md.stem.replace("-", " ").title()

    # Divide en trozos y procesa cada uno
    partes = [
        original[i : i + CHUNK_SIZE] for i in range(0, len(original), CHUNK_SIZE)
    ]
    partes_limpias = [limpiar_texto(titulo, p) for p in partes]
    resultado = "\n".join(partes_limpias)

    md.write_text(resultado, encoding="utf-8")
    print(f"✔️ Curado {md} (partes: {len(partes)})")
