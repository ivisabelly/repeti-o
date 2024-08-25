while True:
    try:
        nota = float(input("digita a tua nota entre zero e dez: "))
        if 0 <= nota <= 10:
            break  
        else:
            print("digita outra nota válida entre zero e dez")
    except ValueError:
        print("por favor, digita um valor numérico")

print(f"massa")
