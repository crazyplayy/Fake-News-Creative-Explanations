
i = 0

while i < 11:
    abrir = str(i) + ".txt"
    file = open(abrir, "r", encoding= 'utf-8')
    string_list = file.readlines()

    texto= ''
    file = open(abrir, "w", encoding= 'utf-8')
    for line in string_list:
        line = line.replace('  ','\n')
        #line = line.replace('\n','  ')
        texto += line
        
    file.write(texto)
    file.close()

    i += 1

print("donezo")