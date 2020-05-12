count = 0

def execute(ins, item, dic):
    global count
    if ins == "insert":
        if item in dic:
            dic[item] += 1
            if dic[item] == 2:
                count += 1;
        else:
            dic[item] = 1
    else:
        if item in dic:
            dic[item] -= 1
            if dic[item] == 0:
                del dic[item]
            elif dic[item] == 1:
                count -= 1

def homo(dic):
    global count
    if len(dic.keys()) > 1:
        he = True
    else:
        he = False
    if count != 0:
        ho = True
    else:
        ho = False
    if he and ho:
        print("both")
    elif ho:
        print("homo")
    elif he:
        print("hetero")
    else:
        print("neither")

def main():
    i = int(input().strip())
    d = {}
    for t in range(i):
        ins, item = input().strip().split()
        execute(ins, item, d)
        homo(d)

if __name__ == '__main__':
    main()
