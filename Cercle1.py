from pylab import *
#Cercle de rayon 1 
x=linspace(-1,1,100)
#print(x)
y=sqrt(1 - x**2)
plot(x,y, 'r')
#Pour obtenir la symétrie
plot(x,-y, 'r')
#Forcer le graphique d'avoir la mm échelle en x et y
axis("equal")
grid()


show()
