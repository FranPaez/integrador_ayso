numeros = list(map(float, input("Ingrese números separados por espacios: ").split()))
promedio = sum(numeros) / len(numeros) if numeros else 0
print(f"El promedio es: {promedio}")
