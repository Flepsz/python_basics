val = list()

for i in range(0, 5):
    n = int(input('Digite o {}º número : '.format(i + 1)))
    if i == 0 or n > val[-1]:
        val.append(n)
    else:
        pos = 0
        while pos < len(val):
            if n <= val[pos]:
                val.insert(pos, n)
                break
            pos += 1
print(val)

