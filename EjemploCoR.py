class Manejador(object):
	def __init__(self):
		self.sucesor=None
	def getSucesor(self):
		return self.sucesor
	def setSucesor(self, sucesor):
		self.sucesor=sucesor
	def nomina(self):pass
	
class ManjeadorProfesorPlanta(Manejador):
	def nomina(self, opcion):
		if(opcion==1):
			return "Se esta calculando la nomina para un profesor de planta"
		else:
			return self.sucesor.nomina(opcion)
            
class ManjeadorProfesorVEspecial(Manejador):
	def nomina(self, opcion):
		if(opcion==2):
			return "Se esta calculando la nomina para un profesor de Vinculacion especial"
		else:
			return self.sucesor.nomina(opcion)            
class ManjeadorRector(Manejador):
	def nomina(self, opcion):
		if(opcion==2):
			return "Se esta calculando la nomina para un profesor de Vinculacion especial"
		else:
			return self.sucesor.nomina(opcion)            

		
class ManjeadorDefault(Manejador):
	def nomina(self, opcion):
		return opcion,"No es una opcion valida"

tipoNomina=[]

#creamos un array de manejadores
tipoNomina.append(ManjeadorProfesorPlanta())
tipoNomina.append(ManjeadorProfesorVEspecial())

tipoNomina.append(ManjeadorRector())

tipoNomina.append(ManjeadorDefault())


for i in  range(len(tipoNomina)-1):
    tipoNomina[i].setSucesor(tipoNomina[i+1])
    print ( tipoNomina[i]," + \n",  tipoNomina[i].getSucesor());

    
print("\tSeleccione una opcion para calcular la nomina")
print("1. Profesor Planta")
print("2. Profesor Vinculacion especial")
print("3. Rector")
x=int(input())

print(tipoNomina[0].nomina(x))
