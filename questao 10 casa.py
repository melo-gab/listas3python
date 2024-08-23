while True:
    op=str(input("Insira uma operação (+, -, * ou /) ou S para encerrar: "))
    if op=="S" or op=="s":
        print("Encerrando...")
        break
    a=float(input("Insira o valor A: "))
    b=float(input("Insira o valor B: "))
    if op=="+" or op=="-" or op=="*" or op=="/":
        if op=="+":
            r=a+b
        elif op=="-":
            r=a-b
        elif op=="*":
            r=a*b
        else:
            if b!=0:
                r=a/b
            else:
                print("O divisor B não pode ser 0.")
        print(a, op, b, "=", "%.2f" %r)
    else:
        print("Operador inválido.")
   
