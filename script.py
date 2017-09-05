def multiples():
	i = 1
	while i < 1001:
		if i % 2 != 0:
			print i
		i += 1

multiples()

# ---------------------------------------------------------

def multiples2():
    i = 5
    while i < 1000001:
        if i % 5 == 0:
            print i
        i += 1

multiples2()

# ---------------------------------------------------------

a = [1, 2, 5, 10, 255, 3]
def sumList(list):
    i = 0
    sum = 0
    while i < len(list):
        sum += list[i]
        i += 1
    print sum

sumList(a)

# ---------------------------------------------------------

a = [1, 2, 5, 10, 255, 3]
def averageList(list):
    i = 0
    sum = 0
    while i < len(list):
        sum += list[i]
        i += 1
    print sum/len(list)

averageList(a)