import pandas as pd
import matplotlib.pyplot as plt

#obtiene los datos del archivo
#datos=pd.read_csv('Datos.txt',header=0,delim_whitespace=True)
datos=pd.read_csv('Insumo 2.csv')

#define las columnas a utilizar
x1=datos.ix[:,3]
x2=datos.ix[:,5]
x3=datos.ix[:,6]
#y=datos.ix[:,0]

#print(datos)

#tutorial
#plt.plot([1,2,3,4,5], [1,3,9,12,15],'ro')

#elabora la grafica
#plt.plot(y,x1,'ro',y,x2,'g^',y,x3,'bs')
#plt.plot(y,'g^')
#plt.xlabel('Precio')

#plt.ylabel('Algunos números')

#Grafico circular
y = [10,20,15,20,15,20]
plt.style.use('fast')
plt.figure(figsize=(10,5),dpi=80)
plt.pie(y)
plt.xlabel('Dato 1',fontsize=14)
plt.title('Grafico Circular')
plt.legend(('10 %','20 %','15 %', '20 %', '15 %','20 %'), prop = {'size': 12}, loc='center left', bbox_to_anchor=(1,0,0.5,1))

plt.show()
#print(y.describe())

