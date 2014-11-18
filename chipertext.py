import math

def chipertext(string):
    
    length = len(string)
    output = ''
    k = 0
    R = int(math.sqrt(length + 0.5))
    C = int(math.ceil(length/float(R)))
    for i in range(R+1):
        for j in range(C+1):
            if (i+j*C >= length) or (k >= length):
                continue
            k += 1
            output += string[i+j*C]
    return output

print chipertext('helloworld')
