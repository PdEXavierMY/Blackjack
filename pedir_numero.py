def pedir_entrada_numero(invitacion):
    while True:
        print(invitacion, end = ": ")
        entrada = input()
        try:
            entrada = int(entrada)
        except:
            print("Solo los caracteres [0-9] están autorizados.", file = sys.stderr)
        else:
            return entrada

def pedir_entrada_numero_delimitado(invitacion, minimo=MIN, maximo=MAX):
    while True:
        invitacion = "{} entre {} y {} incluidos".format(invitacion, minimo, maximo)
        entrada = pedir_entrada_numero(invitacion)
        if minimo <= entrada <= maximo:
            return entrada