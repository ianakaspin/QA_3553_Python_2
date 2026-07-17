def login(username,password):
    print(username,password)

data = ["admin","12345"]
login(data[0],data[1])
login(*data) # * говорит: разложи по аргументам

user = {
    "username":"admin",
    "password":"12345"
}

login(**user)

user = {
    "username":"admin",
    "password":"12345",
    #"remember_me":True # неопределенный ключ, в опред-и ф-и его не было, вызовет ошибку
}
login(**user)