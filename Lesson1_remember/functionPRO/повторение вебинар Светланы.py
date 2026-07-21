# **kwargs - собирает в словарь именованные аргументы
# *args - собирает позиционные аргументы в кортеж

def register_student(name, course = "Python", *grades, **info):
    print(name)
    print(course)
    print(grades)
    print(info)

register_student("Anna", "QA", 98,100,95, city="Haifa", online = True)

file = open("f1.txt", "w", encoding="utf-8") #без with open нужно этот файл закрывать отдельной командой
file.write("Hello")
file.close()

with open("f2.txt", "w", encoding="utf-8") as new_file:
    new_file.write("Bye") #закрывает автоматически файл и сохраняет переменную

 #write w
 #read r
 #add a - добавление в конец


with open("f2.txt", "w", encoding="utf-8") as new_file:
    new_file.write("bye")

with open("f3.txt", "w") as f: #открывай и записывай заново
    f.write("learn")
    f.write("\npractice")
    f.write("\nread")

with open("f3.txt", "a") as f: #Не переписывай, а дописывай - add
    f.write("\nJSON")

with open("f3.txt", "r") as file:
    content = file.read()
print(content)

with open("f3.txt", "r") as file:
    for line in file:
        print(line.strip())

#csv
import csv
from pathlib import Path

students = [
    ["name", "age", "city"],
["name1", 34, "Haifa"],
["name2", 19, "Karmiel"],
["name3", 25, "Rehovot"],
]

with open("students.csv","w", encoding="utf-8", newline="") as file_csv:
    w = csv.writer(file_csv) #это создает объект, который умеет записывать данные в нужном нам формате
    w.writerows(students)

with open("students.csv","r", encoding="utf-8") as file_csv:
    r = csv.reader(file_csv)
    for row in r:
        print(row)

def create_folder():
    r_path = Path("rep") #создает папку
    r_path.mkdir(exist_ok=True) #создает папку; если есть - ладно 
    res_file = r_path/"res.txt"
    with open(res_file,"w") as f:
        f.write("success")
create_folder()