
file = open("10.txt", "r", encoding= 'utf-8')
string_list = file.readlines()

texto= ''
file = open("10line.txt", "w", encoding= 'utf-8')
for line in string_list:
    #line = line.replace('  ','\n')
    line = line.replace('\n','  ')
    texto += line
    
file.write(texto)
file.close()