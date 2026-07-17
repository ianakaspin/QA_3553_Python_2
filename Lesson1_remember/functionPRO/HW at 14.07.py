# #1
# def create_profile(name, age, city):
#     return {
#         "name": name,
#         "age": age,
#         "city": city
#     }
#
# name = input("Enter name ")
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


