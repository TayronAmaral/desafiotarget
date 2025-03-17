def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

texto = input("Digite uma string: ")
print(f"String invertida: {inverter_string(texto)}")
