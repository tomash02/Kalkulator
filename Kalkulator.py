while True:
    czynnik_a = input("Podaj pierwszy czynnik\n")
    czynnik_b = input("Podaj drugi czynnik\n")
    operacja = input("Podaj rodzaj operacji\n")
    if operacja == "+":
        print(czynnik_a, operacja, czynnik_b,"=",int(czynnik_a) + int(czynnik_b))
        continue
    if operacja == "-":
        print(czynnik_a, operacja, czynnik_b, "=",int(czynnik_a) - int(czynnik_b))
        continue
    if operacja == "*":
        print(czynnik_a, operacja, czynnik_b,"=",int(czynnik_a) * int(czynnik_b))
        continue
    if operacja == "/":
        print(czynnik_a, operacja, czynnik_b,"=",int(czynnik_a) / int(czynnik_b))
        continue
    if operacja == "**":
        print(czynnik_a, operacja, czynnik_b,"=",int(czynnik_a) ** int(czynnik_b))
        continue
    if operacja == "//":
        print(czynnik_a, operacja, czynnik_b,"=",int(czynnik_a) // int(czynnik_b))
        continue