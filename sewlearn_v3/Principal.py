for i in range(30):

    nExec = i + 1   #i inicia de 0
    import ComponentExec

    exec = ComponentExec.ComponentExec()

    exec.exec(nExec)

'''
#try:
#except:
#print ('erro001')

import EKM
import Student
import QLearning
import pandas as pd
import Generator

numStudents = 8489

# Carregar base de estudantes / Enade
# Escolher o arquivo indicado pela análise do artigo
# --- Gerar Conjunto de Estudantes ---
dfX = pd.read_csv("data/kmeans_4_clusters.csv") 
vetorEstudantesInput = dfX.values
generator = Generator.Generator()
listStudents = []
listStudents = generator.genStudents(numStudents)
i = 0
for x in vetorEstudantesInput:
  listStudents[i].capacity.softwareUnderstanding = x[1]
  listStudents[i].capacity.understandingConcepts = x[2]
  listStudents[i].capacity.practiceSM = x[3]
  listStudents[i].capacity.testSM = x[4]
  i = i + 1
  #print(x)
  #print( type(x) )
  #print( x[3] )
print ('id, softwareUnderstanding, understandingConcepts, practiceSM, testSM' )
for x in listStudents:
  print (x.id, x.capacity.softwareUnderstanding, x.capacity.understandingConcepts, x.capacity.practiceSM, x.capacity.testSM )
  #print ( type(x))
 


# --- Configurar Algoritmo ---

posReward = 13
negReward = -13
learningRate = 0.7
discountFactor = 0.7
explorationInd = 8
numTry1MD = 5  #6


# --- Gear Conjunto de DMs  ---
conjDM = EKM.Set_DMs()
conjDM.list = generator.genDMs(10)
#dmS.printDMs()


# --- Planejar número de tentativas (secoes de aprendizagem) -> sequencial ---
maxTryMDStudent = numTry1MD * len(conjDM.list)


#--- Preparar Algoritmo QLearning---
qLearning = QLearning.QLearning()
# Acoes
qLearning.configActions(conjDM.list) #qLearning.printActions()

# Estados
i=0
listStates = []
listStates.append(i)
for iDm in conjDM.list:
    i = i + 1
    listStates.append(i)

#Configuracoes
qLearning.configStates(listStates)
qLearning.configExploration(explorationInd)
qLearning.configReward(posReward, negReward)
qLearning.configLearningRate(learningRate)
qLearning.configDiscountFactor(discountFactor)
qLearning.startQTable()


qLearning.printQTable()
#print("parei")
#exit

# ---  Recomendar DM  ---
#episodes - considerar que cada episodio consiste em um unico aluno resolvendo n tentativas  (ordenado por estudante 1, 2, 3..)

numRecomend = 0
nExec = 0
numAcertosTotal = 0
for student in listStudents:  #episodios
    #student = Student.Student()
    #student.model = iStudent
    student.nTry = 0
    student.finish = False

    while((student.nTry < maxTryMDStudent) and (not student.finish)):
        nExec = nExec + 1
        print ('Exec:', nExec)        
        student.nTry = student.nTry + 1
        idMD = qLearning.recommend(student.score, student.DMsFinished )
        numRecomend = numRecomend + 1

# ---   Simular Estudante Resolvendo ---
        correct = student.simulateSolve(conjDM.list[idMD])
        print ('Student: ', student.id, " - Score: ", student.score, " - DM: ", conjDM.list[idMD].id, ' Response correct:', correct)
        iStateOld = student.score
        iStateNew = student.score
        trueReward = False #recompensa negativa
        if (correct):
            iStateNew = iStateNew + 1
            student.DMsFinished.append(conjDM.list[idMD])
            trueReward = True #recompensa positiva
            #print ('val-qLearning:', qLearning.tableQ[iStateOld][idMD], ' idMD:', idMD)
            numAcertosTotal =  numAcertosTotal + 1

        qLearning.updateQTable(iStateOld, iStateNew, idMD, trueReward, student.DMsFinished)                
        student.score = iStateNew

        if student.score >= 110:
            student.finish = True
        
        print (' - - - - - - - - - - - - -')

idpe = numAcertosTotal / numRecomend
# --- Imprimir Resumo da Execucao ---
print ("*** Experimento Teste ***")
print ("Indicador de Exploracao: ", explorationInd)
print ("Modo de Sequenciamento da Resolucao (Estudantes/MDs): (X) Sequencial,  ( ) Aleatoria")
print ("Numero de Estudantes: ", numStudents)
print ("Numero de MDs: "  , len(conjDM.list))
print ("Numero de tentativas (Estudante/MD): ", numTry1MD)
print ("-Configuracoes q-Learning")
print ("Reforco Positivo: ", posReward, " - Reforco Negativo: ", negReward)
print ("Taxa de Aprendizagem: ", learningRate)
print ("Fator de Disconto: ", discountFactor)

scoreTotal= 0
for student in listStudents:
    print ("Estudante: ", student.id, " - Score: ", student.score, " - N Recomend: ", student.nTry)
    #student.printDMsFinished()
    #student.printDMsOFF()
    scoreTotal=scoreTotal+student.score
    
print ("Media-Score: ", scoreTotal/numStudents)
print ("Numero Recomendacoes: ", numRecomend)
print ("Indicador de Desempenho Ponderado do Experimento (IDPE): ", idpe)
print ('Finish')
'''