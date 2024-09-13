#Invert a Dictionary
#Write a Python function to invert a dictionary (swap keys and values).
#Input: {'a': 1, 'b': 2, 'c': 3}
#Output: {1: 'a', 2: 'b', 3: 'c'}


def invert_dictionary(dict_a):
    dict_a_inv = {}
    for x in dict_a:
        dict_a_inv[dict_a[x]]=x
    return dict_a_inv

if __name__ == '__main__':
    a = {'a': 1, 'b': 2, 'c': 3}
    print(invert_dictionary(a))

