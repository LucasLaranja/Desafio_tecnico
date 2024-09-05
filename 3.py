import json

def carregar_valores():
    with open("dados.json", "r") as file:
        valores = json.load(file)
    return valores

def calcular_faturamento(valores):
    valor = []
    
    for dia in valores:
        if dia["valor"] > 0:
            valor.append(dia["valor"])
            
    menor_valor = min(valor)
    maior_valor = max(valor)
    
    media = sum(valor) / len(valor)
    
    dias_acima_da_media = 0
    for v in valor:
        if v > media:
            dias_acima_da_media += 1
            
    return menor_valor, maior_valor, media, dias_acima_da_media

def formatar_moeda(valor):
    return f"R${valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

valores = carregar_valores()
menor_valor, maior_valor, media, dias_acima_da_media = calcular_faturamento(valores)

print(f"Menor faturamento do mês: {formatar_moeda(menor_valor)}")
print(f"Maior faturamento do mês: {formatar_moeda(maior_valor)}")
print(f"Dias com faturamento superior à média mensal: {dias_acima_da_media}")