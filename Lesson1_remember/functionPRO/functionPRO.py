def greet(name):
    return f"Hi, {name}!"
result = greet("Maria")
print(result)
# result_1 = greet() что, если пустой аргумент?
# print(result_1)

def create_user(name,role="user"):
    return {
        "name":name,
        "role":role
    }
print(create_user("Maria"))
print(create_user("Maria", "admin"))

print()

def calculate_discount(price,discount_percent=10): #параметры без значений всегда идут первыми
    return price - (price*discount_percent/100)
print(calculate_discount(1000))
print(calculate_discount(1000,25))

# def foo(a=1,b): #выдаст ошибку: параметр со значением не должен быть первым
#     return a+b
# print(foo(5))

def add_test_result(name,results=[]):
    results.append(name)
    return results
print(add_test_result("test_login"))
print(add_test_result("test_logout"))

def add_test_result(name,results=None):
    if results is None:
        results = []
    results.append(name)
    return results
print(add_test_result("test_login"))
print(add_test_result("test_logout"))

def create_user_1(username,email,role):
    return f"{username} ({email}) - {role}"
print(create_user_1("Maria", "maria@gmail.com","admin"))

print(create_user_1(role="admin", username="Maria", email="maria@gmail.com"))

print(create_user_1("Maria", role="admin", email="maria@gmail.com"))

