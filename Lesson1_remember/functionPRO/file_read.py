with open("users.txt", "w", encoding="utf-8") as file:
    file.write("tony\n")
    file.write("ivan\n")
    file.write("anna\n")

# read() читает весь файл целиком в одну строку, включая все переносы строк изнутри

with open("users.txt","r",encoding="utf-8") as file:
    content = file.read()
print(content)

# readlines() возвращает список, где каждый его элемент - отдельная строка.


with open("users.txt","r",encoding="utf-8") as file:
    lines = file.readlines()

print(lines)

for line in lines:
    print(line.strip()) # Когда будем подставлять данные из файла в тест парами (логин = пассворд), удобно, когда strip убрал лишние пробелы

with open("users.txt","r",encoding="utf-8") as file:
    lines = file.readlines()
print(lines)

with open("users.txt","r",encoding="utf-8") as file:
    for line in file:
        print(line.strip())



