#traffic light
#red = stop, yellow = warning, green = go
#any other color = invalid

color = input("Ingresa un color: ").lower()
if color == "red":
    print("stop")
elif color == "green":
    print("go")
elif color == "yellow":
    print("warning")
else:
    print("invalid")
