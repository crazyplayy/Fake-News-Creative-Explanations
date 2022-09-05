
i = 11

while i < 21:
    abrir = "output" + str(i) + ".txt"
    guardar = str(i) + "normal.txt"

    file = open(abrir, "r", encoding= 'utf-8')
    string_list = file.readlines()

    texto= ''
    file = open(guardar, "w", encoding= 'utf-8')
    for line in string_list:
        line = line.replace('  ','\n')
        #line = line.replace('\n','  ')
        texto += line
        
    file.write(texto)
    file.close()

    i += 1

print("donezo")