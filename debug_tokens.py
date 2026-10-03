import json
with open("skt-morph-data/01/01.1096.json", "r") as f:
    data = json.load(f)

def extract_all_text_tokens(obj):
    tokens = set()
    if isinstance(obj, dict):
        for v in obj.values():
            tokens.update(extract_all_text_tokens(v))
    elif isinstance(obj, list):
        for v in obj:
            tokens.update(extract_all_text_tokens(v))
    elif isinstance(obj, str):
        if obj and obj != "-":
            for x in obj.split("/"):
                tokens.add(x.strip())
    return tokens

tokens = extract_all_text_tokens(data["upasarga_forms"]["vi"])
print("Is vijayate in tokens?", "vijayate" in tokens)
print("Some tokens:", list(tokens)[:10])
