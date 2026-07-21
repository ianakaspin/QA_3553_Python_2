import csv
# def save_shopping_list(items):
#     with open("shopping.txt","w", encoding="utf-8") as file:
#         for item in items:
#             file.write(item + "\n")
#
# items=[
#     "Milk",
#     "Bread",
#     "Apples",
#     "Coffee"
# ]
# print(save_shopping_list(items))


# def save_shopping_list(items):
#     with open("shopping.txt", "w", encoding="utf-8") as file:
#         file.write("\n".join(items) + "\n")
#
# items=[
#      "Milk",
#      "Bread",
#      "Apples",
#      "Coffee"
# ]
# print(save_shopping_list(items))

# with open("students.csv", "r", encoding="utf-8") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row)
#         print(row["name"], ":", row["age"])

def write_students(filename, students):
    with open(filename, "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "age"])
        for name, age in students:
            writer.writerow([name, age])

def read_students(filename):
    students = []
    with open("students.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append((row["name"], row["age"]))
    return students

students = [
    ("Anna", 21),
    ("Tom", 19),
    ("Kate", 22)
]
 
write_students("students.csv", students)

result = read_students("students.csv")
print(result)

import json

def save_profile(name, age, city):
    profile = {
        "name": name,
        "age": age,
        "city": city
    }

    with open("profile.json", "w", encoding="utf-8") as f:
        json.dump(profile, f, ensure_ascii=False)

save_profile("Maria", 30, "Haifa")