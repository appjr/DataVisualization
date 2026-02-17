from openai import OpenAI
client = OpenAI()
models = [m.id for m in client.models.list().data]
print([m for m in models if "image" in m or "dall" in m])
