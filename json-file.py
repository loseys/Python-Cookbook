import json

# content =[1, 2, 3, 4, 5]
# dados_json = json.dumps()

content = [1, 2, 3, 4, 5]
with open('file.json', 'w') as arquivo:
    json.dump(content, arquivo)

with open('file.json' ,'r') as arquivo:
    new_content = json.load(arquivo)
