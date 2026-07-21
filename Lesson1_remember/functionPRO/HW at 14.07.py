#1
def create_profile(name, age=18, city='Unknown'): #ф-я с позиционным аргументом name
    return {  #верни словарь:
        "name": name,
        "age": age,
        "city": city
    }

print(create_profile("Anna")) # проверка от Марии
print(create_profile("Tom",25))
print(create_profile(city="Haifa", name="Igor"))

# name = input("Enter name ") # мой вариант без проверки
# age = input("Enter age ")
# city = input("Enter city ")
#
# profile = create_profile(name, age, city)
# for key,value in profile.items():
#      print(f"{key}: {value}")

#2
def sum_even_numbers(*numbers):
    even_numbers = []
    for n in numbers:
        if n % 2 == 0:
            even_numbers.append(n)
    return sum(even_numbers)

numbers = (1,2,3,4,5,6)
print(sum_even_numbers(*numbers))

#3
def print_pet_info(name, **info):
    print(f"Name: {name}")
    for key, value in info.items():
        if value:
            print(f"{key}: {value}")

name = input("Enter name ")
age = input("Enter age ")
color = input("Enter color ")
breed = input("Enter breed ")

print_pet_info(name, age=age, color=color,breed=breed)

#4
def merge_lists(*lists):
    result = []

    for current_list in lists:
        for item in current_list:
            result.append(item)
    return result

print(merge_lists(
    [1, 25],
    [3, 8, 3],
    [4, 5, 456],
    []
))
print()

#5
def build_message(*words, separator=" "):
    return separator.join(words)
print(build_message("Hello", "world"))
print(build_message("2026", "07", "15", separator=" "))
print(build_message())