Num1 = float(input("Введите первую переменную: "))
while True:
    oper = input("Введите знак операции, которая требуется: \n + \n - \n / \n * \n ^ \n 0 - Сброс операции ")
    if oper in ('+',  '-', '/', '*', '^'):
        if oper == '+':
            Num2 = float(input('Введите вторую переменную: '))
            Num1 += Num2
            print(Num1)
        if oper == '-':
            Num2 = float(input('Введите вторую переменную: '))
            Num1 = Num1 - Num2
            print(Num1)
        if oper == '*':
            Num2 = float(input('Введите вторую переменную: '))
            Num1 = Num1 * Num2
            print(Num1)
        if oper == '/':
            Num2 = float(input('Введите вторую переменную: '))
            if Num2 == 0:
                print("Делить на ноль нельзя!")
            elif Num2 > 0:
                Num1 = Num1 / Num2
                print(Num1)
        if oper == '^':
            Num2 = float(input('Введите вторую переменную: '))
            Num1 = pow(Num1,Num2)
            print(Num1)
        if oper == '0':
            print ("Значение сброшено на ноль")
            Num1 = 0
            Num1 = float(input("Введите первую переменную: "))
    else:
        print ("Операция невозможна")
             
            
        




