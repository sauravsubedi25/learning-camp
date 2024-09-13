#Write a Python function to merge two dictionaries.
#Input: {'a': 1, 'b': 2}, {'b': 3, 'c': 4}
#Output: {'a': 1, 'b': 3, 'c': 4}


def merge_dictionary(dict_a, dict_b):
   for x in dict_b:
       dict_a[x]=dict_b[x]
   return dict_a


if __name__ == '__main__':
    a= {'a': 1, 'b': 2}
    b= {'b': 3, 'c': 4}
    print(merge_dictionary(a,b))
