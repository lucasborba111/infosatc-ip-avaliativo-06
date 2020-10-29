def parameter():
    insert = input("insira caractere em { [ ( abrindo e fechando: ")
    if(insert=="{[()]}"):
        print("Verdadeiro")
        True
    elif(insert == "[]"):
        print("Verdadeiro")
        True
    elif(insert == "()"):
        print("Verdadeiro")
        True
    elif(insert == "{}"):
        print("Verdadeiro")
        True
    else:
        print("falso")
        False
parameter()