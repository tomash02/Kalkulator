print("Kolejność: liczba, operacja, liczba, c aby wyczyścić wynik")

num1 = int(input("Liczba "))
try:
    while True:
        oper = input("Operacja ")

        if oper == "c":
            num1 = int(input("Liczba "))
            continue

        num2 = int(input("Liczba "))

        if oper == "+":
            num1 += num2
            print(num1)
            continue

        if oper == "-":
            num1 -= num2
            print(num1)
            continue

        if oper == "*":
            num1 *= num2
            print(num1)
            continue

        if oper == "/" and num2 == 0:
            print("Nie dziel przez zero!!!")
            continue

        if oper == "/":
            num1 /= num2
            print(num1)
            continue

except ValueError:
    print("Nieodpowiedni input")