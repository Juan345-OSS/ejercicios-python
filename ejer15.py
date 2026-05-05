def es_armstrong(n):
    digitos = str(n)
    num_digitos = len(digitos)
    
    # Sumamos cada dígito elevado a la potencia num_digitos
    suma = sum(int(d) ** num_digitos for d in digitos)
    
    return suma == n


print(es_armstrong(153))  
print(es_armstrong(8208)) 
