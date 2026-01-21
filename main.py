
# Para convertir de Ascii a binario primero se convierte el texto a un arreglo de caracteres donde cada caracteres es un valor númerico

text = "krnwenwrmxbjlroamxb"

alfabeto = 26

arreglo = list(text)


for i in range( 0  , len(arreglo) ):
    arreglo[i] = ord(arreglo[i])


def decimal_a_binario(n):
    if n == 0:
        return "0"
    
    binario = ""

    while n > 0:
        binario = str(n % 2) + binario
        n //= 2

    return binario


string_binario = ""



for i in arreglo:
    binario = decimal_a_binario(i)
    string_binario = string_binario +" "+  binario


print("texto en binario "  ,string_binario)