from boolean_gauss import *
import sys

command = sys.argv[1]

if command == "invert":
    # input file
    file_name = sys.argv[2]
    mat = from_csv(file_name)
    
    # printing
    print('initial matrix :')
    print(mat)
    
    # inverse
    mat = inverse(mat)
    mat_csv = to_csv(mat)
    
    # printing
    print('inverse matrix :')
    print(mat)
    
    # output file
    file_name = sys.argv[3]
    open(nameFile,"w+").write(mat_csv)
    exit(0)

else:
    print (f'command "{command}" does\'nt exist')
    exit(1)
