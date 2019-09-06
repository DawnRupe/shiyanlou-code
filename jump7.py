for num in range(1,100+1):
	if num%7 == 0: ##??7??
		##print("?({})".format(num))
		continue
	elif num%10 == 7: ##????7?
		##print("?({})".format(num))
		continue
	elif num//10 == 7: ##????7?
		##print("?({})".format(num))
		continue
	else:
		print(num)

