jum = [5, 3,7,2]
kaleng = ["M", "H", "K", "B"]


nowW = ""
nomor = 0
for x in range(20):
	nx = x%3
	if (Number(jum[nx]) != 0):
		if(kaleng[nx] == nowW):
			pass
		nowW = str(kaleng[nx]).lower()
		nomor += 1

print(nomor)