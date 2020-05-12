#!/usr/bin/env python3

ind = int(input())

for i in range(ind):
    num, num1 = input().split()

    num = int(num[::-1])
    num1 = int(num1[::-1])

    print(int(str(num + num1)[::-1]))
