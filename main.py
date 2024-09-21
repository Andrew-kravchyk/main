name = "Andry"
surname = "Kravcik"
age = 15
hello = 'Hello world!'

print(hello)
print(name)
print(surname)
print(age)

print(type(hello))
print(type(name))
print(type(surname))
print(type(age))


count_int = 0
count_str = 0
count_bool = 0
count_set = 0
count_list = 0
count_tuple = 0
count_float = 0
lst_notnull = []
max_value = -1
types_count = {str, int, bool, set, list, tuple, float}
lst_count_types = [count_set, count_bool, count_tuple, count_list, count_float, count_str, count_int]
lst_name_type = [set, tuple, list, bool, float, str, int]
lst = [name, surname, age, float_z, float_z2, float_z3]
for item in lst:
    if type(item) == int:
        lst_count_types[-1] +=1
    elif type(item) == str:
        lst_count_types[-2] +=1
    elif type(item) == float:
        lst_count_types[-3] +=1



for item in lst_count_types:
    if item != 0:
        lst_notnull.append(item)
    if len(lst_notnull) == 0:
        print('Good')
    else:
        if item == max_value:
            print('Not')
            break
            
        elif item > max_value:
            max_value = item

inndex = lst_count_types.index(max_value)

print(lst_name_type[inndex])

for item in lst:
    if type(item) != lst_name_type[inndex]:
        lst.remove(item)
