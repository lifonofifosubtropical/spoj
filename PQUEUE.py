#!/usr/bin/env python3

inn = int(input())
while(inn):
	n, m = list(map(int, input().split()))
	works = list(enumerate(list(map(int, input().split()))))
	aux = sorted(works, key=lambda tup: tup[1], reverse = True)
	con = 1
	for i in works:
		if i[1] == aux[0][1]:
			del(aux[0])
			if i[0] == m:
				print(con)
				break
			con+=1
		else:
			works.append(i)


	inn -=1
