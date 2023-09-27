a="oggi è molto caldo; il termometro segna {} gradi"
gradi = 35
print(a.format(gradi))
a="oggi è molto caldo; il termometro segna " + str(35) + " gradi"
print(a)
#per dividere in sottostringhe dove trova un simbolo ;
print (a.split(";"))
#per estrapolare sottostringhe trattando la stringa come una collection di caratteri
print (a[:5])     