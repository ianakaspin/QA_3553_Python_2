name = 'Alice'
age = 30
formatted_string = f"Hello my name is {name} and I am {age} years old"
print(formatted_string)

#find() и rfind()- принимает сабстроку, возвращает ее индекс начала и индекс конца
s= 'AbrakadabraAbrakadabra'
str='bra'
print(s.find(str))
print(s.rfind(str))
print(s.find('add')) # если запрашивается то, чего нет, возвращается -1

#count() - сколько раз искомое находится в строке: count(sub[start,end])
print(s.count(str))
print(s.count(str,4))
print(s.count(str,4,16)) #не включая концевой

#str.upper() и str.lower() - преобразовывает в верхний или нижний регистр
s= 'AbrakaDabRaAbrakaDabRa'
print(s.lower())
print(s.upper())
print(s)

#split()
s = 'Cat, Dog,Humster Rabbit, Pig'
print(s.split()) #разделяет по пробелу или знаку табуляции
print(s.split(','))
print(s.split(',', 3)) #разделяет по запятой, макс. число сепараторов - 3

#rjust() & ljust() - заполняет указанными символами слева или справа, увеличивая длину строки до указанного знач-я и
s = 'Hi'
print(s.rjust(10,'*'))
print(s.ljust(10,'*'))

#где может пригодиться: оформить список пройденных тестов с ОК на одном уровне
test = ["Login", "Cart", "API"]
for t in test:
    print(t.ljust(15), "OK")

#где может пригодиться: генерация тестовых данных. Номер заказа - 8 символов, чтобы добавлялось до восьми
order = "125"
print(order.rjust(8,"0"))

#is() - метод, показывающий, из каких символов состоит строка (им также можно искать элемент)
s= 'AbrakaDabRaAbrakaDabRa'
print(s.isalpha()) # только из букв
print(s.isdigit()) # только из цифр

#index() - ищет позицию первого вхождения подстроки, возвр. ошибку, если неверно
text = "QA automation with Python"
pos = text.index("automation") #ищи, с какого индекса начинается указанный текст
print(pos)

# pos = text.index("automation",10) - ищи указанный текст, начиная с 10 индекса

#replace() - использ. для замены
text = 'I like Java'
print(text.replace("Java", "Python"))

text = "2026-07-03"
new_text = text.replace("-", "/")
print(text)
print(new_text)


