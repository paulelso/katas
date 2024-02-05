# Description: This is a simple implementation of the zip function in Python.
def my_zip(list1, list2):
    zip_list = []
    for i in range(len(list1)):
        zip_list.append((list1[i], list2[i]))
        
    return zip_list
        

if __name__ == "__main__":
   print(my_zip([1, 2, 3], "abc"))# [(1, 'a'), (2, 'b'), (3, 'c')]
   print(my_zip([10, 20, 30], "abc"))# [(10, 'a'), (20, 'b'), (30, 'c')]