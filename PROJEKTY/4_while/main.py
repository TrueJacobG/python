i = 0
while i < 3:
    i += 1
    print("Hi! " + str(i))

i = 0
while True:
    i += 1
    if i % 2 != 0:#reszta z dzielenia to 0
        continue#pomija dalsze instrunkcje w pętli, idzie do następnego skoku
    print(i)
    if  i > 10:
        break

