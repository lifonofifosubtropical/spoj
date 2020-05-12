#!/usr/bin/env python3

x, y = map(int, input().strip().split())

while x != 0 and y != 0:
    att = list(map(int, input().strip().split()))
    att.sort()
    dff = list(map(int, input().strip().split()))
    dff.sort()

    if(att[0] < dff[1]):
        print("Y")
    else:
        print("N")
    x, y = map(int, input().strip().split())

