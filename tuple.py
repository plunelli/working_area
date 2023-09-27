

#Trick Posso creare una copia della tupla come lista per poterla eventualmente modificare
xt=tuple((1,3,5,6))
xl=list(xt)
xl[3]=7
xt=tuple(xl)
print(xt)

#distribuire i dati della tupla in più variabili
xt=tuple((1,3,5,6))
(x1,x2,x3,x4)= xt
print(x1)
print(x2)
print(x3)
print(x4)

#se il numero delle variabili è inferiore al numero di variabile
# si può scegliere di trasformare l'ultima variabili in una lista
# è assegnarle tutti i valori che rimangono anteponendole un * 
xt=tuple((1,3,5,6,7,8))
(x1,x2,x3,*x4)= xt
print(x1)
print(x2)
print(x3)
print(x4)

#COUNT
xt=tuple((1,3,5,6,7,8,3))
print(xt.count(3))

#INDEX
print(xt.index(7))
print (xl.index(2))
