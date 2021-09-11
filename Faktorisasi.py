print('Enter your Faktor:')
x = input()

arr, inp, arrH = [], int(x), []
for i in range(inp):
    var = inp / (i+1)
    if(var.is_integer()):
        arr.append(i+1)
        arrH.append(int(var))
        print(i+1, 'x', int(var))
    if(i == inp - 1):
        pass
arrH.sort()

# print("Hasilnya : ", arr)
print("Hasilnya : ", arrH)
