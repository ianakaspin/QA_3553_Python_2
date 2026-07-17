def print_list_reverse(lst):
    if lst is None or not isinstance(lst, list) or len(lst) == 0:
        print("Wrong list")
        return
    reversed_lst = lst[::-1] #исходный не меняется, на выходе получаем новый список
    print(reversed_lst)

print_list_reverse([1, 2, 3, 4, 5])
print_list_reverse([])

def is_valid_point(point):
    if point is None:
        return None
    if isinstance(point,tuple) and len(point)==0: #если он кортеж и длина его =0
        return None
    if not isinstance(point,tuple):
        return False
    if len(point)!=2:
        return False
    x,y = point
    if not isinstance(x,(int,float)) or not isinstance(y,(int,float)):
        return False
    return True

# print(is_valid_point(3, 5))
# print(is_valid_point(3, "5"))
# print(is_valid_point([3, 5]))
# print(is_valid_point(1, 2, 3))

def print_sublist_reverse(lst, start, finish):
    if lst is None or not isinstance(lst,list) or len(lst)==0:
        print("Wrong")
        return
    if (
        not isinstance(start,int)
        or not isinstance(finish,int)
    ):
        print("Wrong")
        return
    if start<0 or finish >=len(lst) or start>finish:
        print("Wrong")
        return
    beginning = lst[:start]
    middle_reversed = lst[start:finish+1][::-1]
    ending = lst[finish+1:]
    print(beginning + middle_reversed + ending)

print_sublist_reverse([10, 20, 30, 40, 50, 60], 1,3)

def get_students_by_grade(students):
    if students is None or not isinstance(students,dict) or len(students)==0:
        return {}
    result = {}
    for name,grade in students.items():
        result.setdefault(grade,[]).append(name)

        if grade not in result:
            result[grade]=[]
        result[grade].append(name)
        return result

print(get_students_by_grade({"alice": 90, "bob": 85, "diana": 90, "charlie": 85}))
