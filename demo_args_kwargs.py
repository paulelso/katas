# Description: function which uses * and ** to unpack a tuple or dictionary into the args and kwargs (respectively) 
# The example show unpacking of a dictionary to **kwargs
def my_print_args(*args, **kwargs):
    print(f"{args=} {kwargs=}")

if __name__ == "__main__":
    my_print_args(**{"a": 1, "b": 2, "y": 25, "z": 26}) # args=() kwargs={'a': 1, 'b': 2, 'y': 25, 'z': 26}