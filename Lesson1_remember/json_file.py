import json

#dumps() - берет объект python и превращает его в json-строку, работает со строкой
#loads() - превращает текст json в объект python, работает со строкой
#dump() - сохраняет python-объект в файл в формате .json, работает с файлом
#load() - json-файл превращает в python-файл, работает с файлом

user = {"username":"Egor", "age":30, "is_admin":True} #это словарь

json_string = json.dumps(user)
print(json_string)
print(type(json_string))

user = json.loads(json_string)
print()
print(user)
print(type(user))
print(user["username"])

test_config = {
    "base_url":"https://api.example.com",
    "timeout":10,
    "retries":3
}

with open("config.json","w", encoding="utf-8") as file:
    json.dump(test_config,file,indent=2,ensure_ascii=False)

with open("config.json","r", encoding="utf-8") as file:
    loaded_config = json.load(file)

print(loaded_config)
print(loaded_config["base_url"])