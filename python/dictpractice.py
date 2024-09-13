
def print_dictionarycounter(listWords):
    distCounter = {}
    for x in listWords:
        if x in distCounter:
            distCounter[x] = distCounter[x] + 1
        else:
            distCounter[x] = 1
    print(distCounter)

def return_dictionarycounter(listWords):
    distCounter = {}
    for x in listWords:
        if x in distCounter:
            distCounter[x] = distCounter[x] + 1
        else:
            distCounter[x] = 1
    return distCounter


if __name__ == '__main__':
    ll = ["aa", "aa", "ten", "b", "c", "ten", "d", "d"]
    print_dictionarycounter(ll)
    listNum = [1, 2, 2, 5, 10, 10, 10, 11, 3, 2, 5]
    dd = return_dictionarycounter(listNum)
    print(dd)
    line = "Hello World hi world"
    words = line.split(" ")
    print(words)
    line1 = "hello world how are you world test counter hello i am counter"
    words1 = line1.split(" ")
    print_dictionarycounter(words1)