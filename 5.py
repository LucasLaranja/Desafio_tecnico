def inverter_string(s):

    resultado = ""
    
    for i in range(len(s) - 1, -1, -1):
        resultado += s[i]
    
    return resultado

def main():

    nome = input("Digite seu nome para ver como ele fica invertido: ")
    
    nome_invertido = inverter_string(nome)
    
    print(f"Seu nome invertido é {nome_invertido}")

main()
