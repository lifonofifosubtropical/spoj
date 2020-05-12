#!/usr/bin/env python3

length = int(input())

while length != 0:
    perm = list(map(int, input().strip().split()))
    amb = True
    for i in range(length):
        if (i+1) != perm[i] and (i+1) != perm[perm[i] -1]:
            amb = False
            break
    if amb:
        print("ambiguous")
    else:
        print("not ambiguous")

    length = int(input())

