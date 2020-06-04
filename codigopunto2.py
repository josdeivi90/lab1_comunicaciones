x = [1.7 , 1.78, 1.68, 1.8, 1.67, 1.75]
y = [60, 66.3, 58, 75, 57, 62.3]

def Efuncion(a):
        z = sum(a)/len(a)
        return z
        
x2 = [0]*len(x)
media = Efuncion(x)

for i in range(0,len(x)):
	x2[i]=x[i]*x[i]

mediacuadratica = Efuncion(x2)

## varianza

x3 = [0]*len(x)

for h in range(0,len(x)):
        x3[h]=pow((x[h]-media),2)

varianza = Efuncion(x3)       

## correlacion

x4 = [0]*len(x)
for k in range(0,len(x)):
        x4[k]=(x[k]*y[k])

correlacion = Efuncion(x4)

cadena =" \nla media = {0} \n la mediacuadratica = {1}\n la varianza = {2}\n la correlacion = {3} "


print (cadena.format(media,mediacuadratica,varianza,correlacion))
