a = int(input("Введите число: "))
sumCh=0
sumNch=0
while a > 0:
    x = int(a%10)
    if x % 2 == 0:
        sumCh+=x
    else:
        sumNch+=x
    a=a//10
print("Сумма нечетных", sumNch)   
print("Сумма четных",sumCh)


