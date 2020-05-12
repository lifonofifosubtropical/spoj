#!/usr/bin/env python3

inn = int(input())
var = 0
for ix in range(inn):
    var += 1
	es, num = list(map(int,input().split()))
	es = {}
	pos = True
	for i in range(num):
		est, sig = input().split()

		try:
			if (sig not in es[est]):
				es[est].append(sig)
			else:
				pos = False
		except:
			es[est] = []
			es[est].append(sig)

	if pos:
		print("Scenario #" + str(var) + ": possible")
	else:
		print("Scenario #" + str(var) + ": impossible")
