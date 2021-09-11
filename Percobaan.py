x = 70

if(x <= 70):
	print("Mengikuti Ujian Ulang")
if(x >= 70):
	print("Tidak Perlu Tidak Perlu Ujian Ulang")

num , u, a = [[1]], 0, 0
print(len(num), u, a)
for i in range(30):
	num[u][a] = i
	if len(num[u]) <= 4:
		a += 1
	else :
		a = 0
		u += 1

print(num)
	