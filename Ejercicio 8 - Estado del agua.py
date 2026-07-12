#estado del agua
temp = int(input("Ingrese la temperatura del agua en Celcius: "))

if temp <= 0:
    print("Solido (hielo)")
elif temp > 0 and temp < 100:
    print("Liquido (agua)")
elif temp >= 100:
    print("Gaseoso (vapor)")
