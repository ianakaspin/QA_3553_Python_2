age = 25
name = 'Ivan'


# int - целые числа
# float - дробные
# str - строки
# bool - логический
# строка - последовательность символов любой длины

said = "She said 'Hello'"
print(said)

my_string = '''This is my multy-line string.
We`ve wrapped the text to the next line'''
print(my_string)

raw_string = r"C:\Program Files\Mariia\Python"
print(raw_string)

# Типы переменных (возвращает тип)
s1 = "Hello world"
print(type(s1))
s2 = 5
print(type(s2))
s3 = 3.8
print(type(s3))
s4 = False
print(type(s4))

s1 = 'Zeleno'
s2 = 'glazka'
s3 = s1+s2 #concatenation - склеивание
print(s3)

words = ["Hello", "World", "and", "Python"]
result = "".join(words) #join - объединение, применяется к строке-разделителю, аргументом является список words
print(result)

st = 'ab' * 7 #сколько раз печатать сочетание ab
print(st)

st=35*'*'  #сколько раз печатать *
print(st)

s1 = 'Vasya Pupkin'
s2 = 'Vasya'
if s2 in s1:
    print('User Vasya is in our database')
else:
    print('Usre Vasya is not in the DB')

st = 'a'
if st=='a' or st=='b' or st=='c' or st=='d':
    print('YES')

if st in 'abcd':
    print('YES')

#len() - длина строки
ln = len('Zelenoglazka')
print(ln)

s1 = 'Zelenoglazka'
print(len(s1))

#P Y T H O N
#0 1 2 3 4 5
st = 'Python'
print(st[0])
print(st[1])
print(st[2])
print(st[3])
print(st[4])
print(st[5])

#P  Y  T  H  O  N
#-6 -5 -4 -3 -2 -1 - индексация с конца начинается с -1

#my_string[start:end]
print(st[0:3]) #с 0 по 2, 3-й символ не включается
print(st[2:5])  #со 2 по 4, 5-й символ не включается
print(st[4:6])  #с 4 по 5, 6-й символ не включается

# H E L L O   W O R L D
# 0 1 2 3 4 5 6 7 8 9 10 - пробел тоже символ

my_string = "Hello world!"
every_second_char = my_string[::2] #печатать каждый второй символ
print(every_second_char)

reversed_string = my_string[::-1] #печатать с конца, шаг будет отрицательный
print(reversed_string)

from_second = my_string[1::2] # со второго символа (после 0) до конца через 1
print(from_second)

my_substring = my_string[1:10:3] # с 1 по 10 с шагом 3
print(my_substring)