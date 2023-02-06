Kolvo = int(input("Введите количество чисел: "))
res = int(input("Введите число: "))
Chislo = 0
for i in range (res-1):
    Znak = input("Введите знак: ")
    if Chislo !=0:
        Chislo = int(input ("Введите число: "))
    while Chislo==0:
        Chislo = int(input ("Введите число: "))
    match Znak:
        case '+':
            res+=Chislo
        case '-':
            res-=Chislo
        case '*':
            res*=Chislo
        case '/':
            res/=Chislo
        case '^':
            res**=Chislo
print("Ваш результат: ", res)