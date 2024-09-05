def calcular_percentuais(faturamento):
    
    total_faturamento = sum(faturamento.values())
    percentuais = {}
    
    for estado, valor in faturamento.items():
        percentual = (valor / total_faturamento) * 100
        percentuais[estado] = percentual
    
    return percentuais

faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

percentuais = calcular_percentuais(faturamento)

print("Percentual de representação por estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")