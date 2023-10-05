peso = float(input("Digite seu peso: "))
altura = float(input("Digite seua altura: "))

imc = peso/(altura*altura)

print(f"Este é o seu IMC: {(imc):2f}")

if imc < 18.5:
    print("magreza")
elif imc >= 18.5 and imc < 24.9:
    print("normal")
elif imc >= 25.0 and imc < 29.9:
    print("Sobrepeso")
elif imc >= 30.0 and imc < 39.0:
    print("Obesidade")
else:
    print("Obesidade grave")