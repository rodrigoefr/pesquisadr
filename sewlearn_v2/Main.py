import EKM
import Student
import QLearning
import Generator
import Set_DMs


# --- Configurar Algoritmo ---

numStudents = 10
posReward = 13
negReward = -13
learningRate = 0.7
discountFactor = 0.7
explorationInd = 8
numTry1MD = 5  #6


# --- Gerar Conjunto de Estudantes ---
generator = Generator.Generator()
listStudents = []
listStudents = generator.genStudents(numStudents)


# --- Gear Conjunto de DMs  ---
conjDM = Set_DMs.DMs()
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
for student in listStudents:  #episodios
    #student = Student.Student()
    #student.model = iStudent
    student.nTry = 0
    student.finish = False

    while((student.nTry < maxTryMDStudent) and (not student.finish)):
        nExec = nExec + 1
        print ('Exec:', nExec)        
        student.nTry = student.nTry + 1
        idMD = qLearning.recommend(student.model.score, student.DMsFinished )
        numRecomend = numRecomend + 1

# ---   Simular Estudante Resolvendo ---
        correct = student.simulateSolve(conjDM.list[idMD])
        print ('Student: ', student.model.id, " - Score: ", student.model.score, " - DM: ", conjDM.list[idMD].id, ' Response correct:', correct)
        iStateOld = student.model.score
        iStateNew = student.model.score
        trueReward = False #recompensa negativa
        if (correct):
            iStateNew = iStateNew + 1
            student.DMsFinished.append(conjDM.list[idMD])
            trueReward = True #recompensa positiva
            #print ('val-qLearning:', qLearning.tableQ[iStateOld][idMD], ' idMD:', idMD)

        qLearning.updateQTable(iStateOld, iStateNew, idMD, trueReward, student.DMsFinished)                
        student.model.score = iStateNew

        if student.model.score >= 110:
            student.finish = True
        
        print (' - - - - - - - - - - - - -')

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
    print ("Estudante: ", student.model.id, " - Score: ", student.model.score )
    #student.printDMsFinished()
    #student.printDMsOFF()
    scoreTotal=scoreTotal+student.model.score
    
print ("Media-Score: ", scoreTotal/numStudents)
print ("Numero Recomendacoes: ", numRecomend)
print ('Finish')