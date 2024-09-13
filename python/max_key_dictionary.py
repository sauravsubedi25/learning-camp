# Find Key with Maximum Value
#Write a Python function to find the key with the maximum value in a dictionary.
#Input: {'a': 10, 'b': 20, 'c': 5}
#Output: 'b'
#from test import maxkey, maxvalue


def find_max_key(dict_a):
    count=0
    for x in dict_a:
        if count==0:
            maxkey = x
            maxvalue = dict_a[x]
            count = count+1
        if dict_a[x]>maxvalue:
            maxvalue = dict_a[x]
            maxkey = x
    return  maxkey


if __name__ == '__main__':
    a = {'a': 10, 'b': 20, 'c': 5}
    print("maxkey",find_max_key(a))
