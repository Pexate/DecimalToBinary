number = int(input("Input an integer: "))
ostatak = 0 # ostatak == remainder in croatian
string = ""
broj = [] # broj == number in croatian
while True:
    ostatak = number % 2 
    broj.append(ostatak)
    if number<1:
        break
    number = number//2
broj.reverse()
broj.pop(0)
for i in range(len(broj)):
    string = string+str(broj[i])
print("Binary number:",string)