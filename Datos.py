import pandas as pd
import matplotlib.pyplot as plt

#obtiene los datos del archivo
#datos=pd.read_csv('Datos.txt',header=0,delim_whitespace=True)
datos=pd.read_csv('Insumo 2.csv')

#define las columnas a utilizar
x1=datos.ix[:,3]
x2=datos.ix[:,5]
x3=datos.ix[:,6]
y=datos.ix[:,0]

#print(datos)

#elabora la grafica
plt.plot(y,x1,'ro',y,x2,'g^',y,x3,'bs')
#plt.plot(y,'g^')
#plt.xlabel('Precio')
plt.ylabel('Precios')
plt.show()
#print(y.describe())

