from boolean_gauss import *
import sys

sys.argv #invert f1.txt f2.txt

command=sys.argv[1]
if command=="invert":
    #recup fichier
    nameFile=sys.argv[2]
    M=from_csv(nameFile)
    print(M)
    M=inverse(M)
    M=to_csv(M)

    nameFile=sys.argv[3]
    File2=open(nameFile,"w+")
    File2.write(M)


else:
    print ("this command don't exist")