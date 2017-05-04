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
			sucesor.nomina(opcion)
		
class ManjeadorDefault(Manejador):
	def nomina(self, opcion):
		return "No es una opcion valida"

tipoNomina=[]

tipoNomina.append(ManjeadorProfesorPlanta())	
tipoNomina.append(ManjeadorDefault)

print(len(tipoNomina))


for i in range (len(tipoNomina)
	print (i)

#print(tipoNomina[0].nomina(3))
