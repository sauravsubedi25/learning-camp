#Compress a String Using the Counts of Repeated Characters
#Write a Python function to perform basic string compression using the counts of repeated characters.
#Input: "aabcccccaaa"
#Output: "a2b1c5a3"

def compress_string(str_a):
    comp_str = ''
    x = 1
    for i in range(len(str_a)-1):
        if str_a[i]==str_a[i+1]:
            x = x+1
        else:
            comp_str = comp_str + str_a[i] +str(x)
            x=1
    comp_str = comp_str + str_a[i] + str(x)
    return comp_str



if __name__ == '__main__':
    a = "aabcccccaaa"
    print(compress_string(a))