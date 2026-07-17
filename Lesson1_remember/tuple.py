#кортеж - неизменяемый тип данных, в него нельзя добавлять/удалять элементы
numbers_tuple = (1,2,3,4,5,6,7)
my_tuple = ([1,2,3],['a','b','c'])

first_element = numbers_tuple[0]

nested_tuple = (1,2,(3,'a'),5)
print(nested_tuple[2])
print(nested_tuple[2][1])

tuple1 = (1,2,3)
tuple2 = (1,2,3)
print(tuple1==tuple2) #сравнить кортежи

tuple3 = (1,2,3)
tuple4 = (5,6,7)
print(tuple3==tuple4)

my_tuple = (1,2,3,4,5)
print(3 in my_tuple)

for el in my_tuple:
    print(el)

i=0
while i<len(my_tuple):
    print(my_tuple[i])
    i+=1

# del my_tuple
# print(my_tuple)

tuple1 = (1,2,3)
tuple2 = (4,5,6)

conc_tuple = tuple1+tuple2
print(conc_tuple)

my_tuple = (1,2,3,4,5)
length_of_tuple = len(my_tuple)
print(length_of_tuple)

sum_of_elements = sum(my_tuple)
print(sum_of_elements)

max_element = max(my_tuple)
min_element = min(my_tuple)
print(max_element)
print(min_element)

original_tuple = (3,4,5,6,7,6,5,4,3)
sorted_tuple = tuple(sorted(original_tuple))
print('original: ', original_tuple)
print('sorted: ', sorted_tuple)
sub_tuple = original_tuple[3:7] #с 3-го по 7-й (не включая 7-й)
print(sub_tuple)

my_tuple = list(original_tuple)
print(my_tuple)

my_string = "".join(map(str,original_tuple))
print(my_string)

my_tuple = (1,2,3,4,5)
my_list = list(my_tuple)
my_list[2] = 10 # заменить индекс 2 десяткой
updated_tuple = tuple(my_list) #обновить кортеж
print("Original tuple: ", my_tuple)
print("Updated tuple: ", updated_tuple)