def makestr(dic, l):
    yo = ""
    for i in l:
        try:
            yo += str(dic[i])
        except KeyError:
            yo += "0"
    return yo


t = int(input())

for i in range(1, t+1):
    c = {}
    _ = input()
    l = input().strip().split()
    for j in l:
        try:
            c[j] += 1
        except KeyError:
            c[j] = 1
    ll = input().strip().split()

    print(f"Scenario #{i}: {makestr(c, ll)}")
