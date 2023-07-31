import json

with open("appsettings.json") as user_file:
  file_contents = user_file.read()

recomendacoes = json.loads(file_contents) 
