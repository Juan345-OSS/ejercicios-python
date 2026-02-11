from collections import Counter

def anagrama(palabra1,palabra2):
    
    if  Counter(palabra1.lower()) == Counter(palabra2.lower()):
        print(True)
    else:
        print('error')

anagrama('eeer','Roma')

#anagrama descubrir palabras