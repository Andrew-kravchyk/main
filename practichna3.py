lst_unique = []





def function_lst_unique():

    lst = [1,2,3,4,5,6,3,4,5,7,6,5,4,3,4,5,4,3, 'Привіт', 'анаконда']
    str = ''
    for a in lst:
        if type(a) == int:
            lst[-2] = str.lower()
  
    print(lst)
    global lst_unique 
    lst_in_set = set()    
    for item in lst :
     if item  not in lst_in_set:
         lst_unique.append(item)
         lst_in_set.add(item)
     
    print(lst_unique)
   

function_lst_unique()

def function_lst_sort():
    
    global lst_unique
    lst_sorted = lst_unique.copy()
    
    lst_sorted.sort(key=str)
    print(lst_sorted)
    
function_lst_sort()



    


    
