s=""
max=100
min=1
answer = int((max+min)//2)
print(answer)
while (s!="Верно"):
    s = input("Верно?   ")
    if s=="Больше":
        min = answer+1
    elif s=="Меньше":
        max = answer - 1
    elif s=="Верно":
        break
    answer = int((max+min)//2)
    print(answer)


