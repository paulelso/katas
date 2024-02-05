# Description: This is a simple implementation of the zip function in Python.
def my_zip(list1, list2):
    for i in range(len(list1)):
        print(f"{list1[i]}, {list2[i]}")
        

if __name__ == "__main__":
   my_zip([1, 2, 3], "abc")