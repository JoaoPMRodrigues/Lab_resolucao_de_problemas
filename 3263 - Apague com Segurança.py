n = int(input())
binario = str(input())
binario_final = str(input())
auxiliar = ""
if n%2==1:
    for i in range(len(binario)):
        if binario[i] == "1":
            auxiliar += "0"
        else:
            auxiliar += "1"
else:
    auxiliar = binario

if auxiliar == binario_final:
    print("Deletion succeeded")    
else:
    print("Deletion failed")