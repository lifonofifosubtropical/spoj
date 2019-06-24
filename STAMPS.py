#!/usr/bin/env python3

"""
STAMPS: solved by sorting the vector of people to borrow from
and then calculating how many of them it is required to beat
that Raymond dude.
"""

import sys

t = int(sys.stdin.readline().rstrip())

for i in range(t):
    need, nfr = sys.stdin.readline().rstrip().split()
    frst = sys.stdin.readline().rstrip().split()
    frst = list(map(int, frst))
    frst.sort(reverse = True)
    need = int(need)

    count = 0
    addr = 0
    for nstmp in frst:
        count += nstmp
        addr += 1
        if(count >= need):
            break
    if(count < need):
        addr = "impossible"
    print("Scenario #" + str(i+1) + ":", file=sys.stdout)
    print(addr, file=sys.stdout)
    print("")
