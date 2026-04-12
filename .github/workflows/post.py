import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

prompt = """
Escreva 1 post curto para X em português.
Tema: disciplina, foco, mentalidade e evolução pessoal.
Tom: forte, direto, impactante e natural.
Máximo: 240 caracteres.
Sem hashtags.
Sem emojis.
Retorne apenas o texto do post.
"""

response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
)

post = response.output_text.strip()

print("Post gerado:")
print(post)
