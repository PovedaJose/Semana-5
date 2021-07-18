class Operaciones:
    def __init__(self, n1,n2):
        self.num1=n1
        self.num2=n2
    
    def suma(self):
        suma= self.num1 + self.num2
        return suma

    def resta(self):
        #if self.num1>= self.num2:
            #return self.num1 - self.num2
        #return 0
        return self.num1 - self.num2
        
    def multiplicacion(self):
        return self.num1* self.num2
    
    def division(self):
        if self.num2 !=0: return self.num1/self.num2
        return 0

    def divisionEntera(self):
        return self.num1 // self.num2
    
    def residuo(self):
        return self.num1 % self.num2
    
    def exponente(self):
        return self.num1**self.num2
    
    def mostrar(self):
        print("Numero 1: {}, Numero 2: {}" .format(self.num1, self.num2))

print("MENU OPERACIONES MATEMÁTICAS")
print("1) Suma\n2) Resta\n3) Multiplicacion\n4) Division\n5) Division Entera\n6) Residuo\n7) Exponente\n8) Salir")
opc= "0"
while opc != "8" :
    opc= input("Digame su opción [1.....8]: ")
    n1= int(input("Ingrese Numero 1: "))
    n2= int(input("Ingrese Numero 2: "))
    operacion= Operaciones(n1, n2)
    if opc=="1":
        print("{} + {}={}".format(operacion.num1, operacion.num2,operacion.suma()))
    elif opc =="2":
        print("{} - {}={}".format(operacion.num1, operacion.num2,operacion.resta()))
    elif opc =="3":
        print("{} * {}={}".format(operacion.num1, operacion.num2,operacion.multiplicacion()))
    elif opc =="4":
        print("{} / {}={}".format(operacion.num1, operacion.num2,operacion.division()))
    elif opc =="5":
        print("{} // {}={}".format(operacion.num1, operacion.num2,operacion.divisionEntera()))
    elif opc =="6":
        print("{} % {}={}".format(operacion.num1, operacion.num2,operacion.residuo()))
    elif opc =="7":
        print("{} ** {}={}".format(operacion.num1, operacion.num2,operacion.exponente()))

print("Gracias por su visita")