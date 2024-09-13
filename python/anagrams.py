#Group Anagrams Using a Dictionary
#Write a Python function to group anagrams from a list of words using a dictionary.
#Input: ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
#Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]


def group_anagrams(list_a):
    dict_a = {}
    #Map<string,list<string>> dict_a
    for a in list_a:
        sorted_word = ''.join(sorted(a))
        if sorted_word in dict_a:
            dict_a[sorted_word].append(a)
        else:
            dict_a[sorted_word] = [a]
   #print(dict_a)
    new_list =[]
    for x in dict_a:
        new_list.append(dict_a[x])
    return new_list



if __name__ == '__main__':
    a = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    print(group_anagrams(a))

