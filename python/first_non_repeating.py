#Write a Python function to find the first non-repeating character in a given string
#and return its index.
#Input: "swiss"
#Output: 1 (for 'w' in "swiss")


def dictionary_counter(str_a):
    dict_counter = {}
    for x in str_a:
        if x in dict_counter:
            dict_counter[x] = dict_counter[x] + 1
        else:
            dict_counter[x] = 1
    return dict_counter


def first_non_repeat_index(str_word,dict_a):
    for i in range(len(str_word)):
        if dict_a[str_word[i]] == 1:
            return i



if __name__ == '__main__':
    input_a = "swissabaawc"
    dict_count = dictionary_counter(input_a)
    print(first_non_repeat_index(input_a,dict_count))


