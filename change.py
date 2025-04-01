def change():
    expense = 23.75
    money = 100
    print("Ingresar gasto:")
    Vuelto = (money-expense)
    print(expense)
    print("Dinero recibido")
    print(money)
    print("\nVuelto")
    print("\nPesos:")
    print(int(Vuelto))
    print("Centavos:")
    print(round((Vuelto-int(Vuelto))*100))

change()
