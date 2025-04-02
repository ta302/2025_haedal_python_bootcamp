n=int(input("input:\n"))

for i in range(1,n+1):
    if i%7==0:
        continue
    if i>100:
        break
    print(i)