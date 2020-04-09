import sys

direction = [1, 0]
position = [0, 0]
repeat = 1
flag  = 1

if (len(sys.argv) == len(sys.argv[1]) + 1):
    if (sys.argv[1].isalnum() and sys.argv[2].isalnum() and sys.argv[3].isalnum() and len(sys.argv[1]) == len(sys.argv[2]) and len(sys.argv[2]) == len(sys.argv[3])):
        i = 0
        j = 0
        len = len(sys.argv[1])
        recorrido = 0
        while(len > 0):
            print(sys.argv[position[1] + 1][position[0]], end = "")
            recorrido = recorrido + 1
            if (recorrido == len):
                repeat = repeat + 1
                if (repeat == 2):
                    len = len - 1
                    repeat = 0
                else:
                    flag = -flag
                recorrido = 0
                if(direction[0] != 0):
                    direction[1] = flag 
                    direction[0] = 0
                else:
                    direction[0] = flag 
                    direction[1] = 0
            position[0] += direction[0]
            position[1] += direction[1]
            if(len != 0):
                print("," ,end = "")
    else:
        print("usage: ./gmartine.py <1-9 squared_rows...>")
else:
    print("usage: ./gmartine.py <1-9 squared_rows...>")

        