def sequencia_fibonacci(s):
    a, b = 0, 1
    
    lista_fibonacci = [a, b]
    
    while b < s:
        a, b = b, a + b
        lista_fibonacci.append(b)
        
    return lista_fibonacci, s in lista_fibonacci

num = 51

sequence, pertence = sequencia_fibonacci(num)

print(f"A sequencia gerada é: {sequence}")

if pertence:
    print("O número pertence a seguência de fibonacci gerada")
    
else:
    print("O número não pertence a sequência")