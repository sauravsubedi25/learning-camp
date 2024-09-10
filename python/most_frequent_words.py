#Problem Statement:
#Write a Python function that counts the frequency of each word in a given paragraph. 
# The function should return the result as a dictionary. 
# Additionally, provide a way to retrieve the most frequently occurring word(s) from this dictionary
#input_paragraph = "Hello world Hello world This world is full of surprises Surprises are everywhere; surprises are fun"

#Frequency counter method that returns dictionary of words and its frequency
#Input list
#returns dictionary
def frequecy_counter(listWords):
    frequency_counter = {}
    for x in listWords:
        if x in frequency_counter:
            frequency_counter[x] = frequency_counter[x] + 1
        else:
            frequency_counter[x] = 1
    return frequency_counter

#Max Frequency counter method that returns list of words with highest frequency
#Input dictionary
#returns list
def find_max_frequent_words(adict):
    a=0
    for x in adict:
        if a == 0:
            maxvalue = adict[x]
            maxkey = x
            a = a+1
        if adict[x] > maxvalue:
            maxvalue = adict[x]
            maxkey = x
    word_list = []
    for y in adict:
        if adict[y]==maxvalue:
            word_list.append(y)
    return word_list


if __name__ == '__main__':
    input_paragraph = "Hello world Hello world This world is full of surprises Surprises are everywhere surprises are fun"
    split_words = input_paragraph.lower().split(" ")
    word_counter = frequecy_counter(split_words)
    print(word_counter)
    max_word_list = find_max_frequent_words(word_counter)
    print("most frequent words",max_word_list)
