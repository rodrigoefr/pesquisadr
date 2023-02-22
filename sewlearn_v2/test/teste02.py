'''
with open('test/arq01.txt', 'w') as arquivo:
    arquivo.write('xTexto adicionado à primeira linha.\n')
    arquivo.write('xTexto que vai na segunda linha.\n')
'''

arquivo = open('test/arq01.txt','a')
arquivo.write('texto X Y z' + "\n")
arquivo.close()
