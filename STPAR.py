#!/usr/bin/env python3

numc = int(input().strip())
while numc != 0:
    l = list(map(int, input().strip().split()))
    l.append(9999)
    stack = [9999]
    acum = 0
    ok = True
    while l != [9999] or stack != [9999]:
        if l[0] == acum + 1:
            acum += 1
            del l[0]
        elif stack[-1] == acum + 1:
            acum += 1
            del stack[-1]
        elif stack[-1] > l[0]:
            stack.append(l[0])
            del l[0]
        else:
            ok = False
            break
    if ok:
        print("yes")
    else:
        print("no")
    numc = int(input().strip())
