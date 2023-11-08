m1 = int(input("Choissisez un nombre entre 1 et 10 : "))
i = 0
tab = []
while i <= m1 - 1:
    m2 = int(input("Choissisez un nombre entre 10 et 100 : "))
    tab.append(m2)
    i = i + 1
print(sum(tab)/m1)