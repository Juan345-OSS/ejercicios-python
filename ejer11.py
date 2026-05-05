#  * Crea un programa que comprueba si los paréntesis, llaves y corchetes
#  * de una expresión están equilibrados.
#  * - Equilibrado significa que estos delimitadores se abren y cieran
#  *   en orden y de forma correcta.
#  * - Paréntesis, llaves y corchetes son igual de prioritarios.
#  *   No hay uno más importante que otro.
#  - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
#  - Expresión no balanceada: { a * ( c + d ) ] - 5 }


expresion = "{ [ a * ( c + d ) ] - 5 }"

pila = []
es_valido = True


pares = {')': '(', '}': '{', ']': '['}

for caracter in expresion:
    if caracter in "({[":
        pila.append(caracter)
    
    elif caracter in ")}]":
        if len(pila) > 0:
            ultimo = pila.pop()
            if ultimo != pares[caracter]:
                es_valido = False
                break
        else:
            es_valido = False
            break

if es_valido and len(pila) == 0:
    print(f"La expresión '{expresion}' está balanceada.")
else:
    print(f"La expresión '{expresion}' NO está balanceada.")
