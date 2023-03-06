import EKM
import Student
import QLearning
import pandas as pd
import Generator
from datetime import datetime
import random

class ComponentExec:

    def __init__(self):
        self.generator = Generator.Generator()

    def exec(self, nExec):
        dh1 = datetime.today()
        print ('início:',dh1)
        self.nExec = nExec
        self.genDMs()
        self.uploadStudents()
        self.configQLearning()
        self.configTryResolution()
        self.execQLearning()
        self.printResult()
        
        dh2 = datetime.today()
        tempo_gasto =  dh2 - dh1
        print ('fim:',dh2)
        print ('tempo_gasto:',tempo_gasto)


    def configQLearning(self):
        self.posReward = 13
        self.negReward = -13
        self.learningRate = 0.7
        self.discountFactor = 0.7
        self.explorationInd = 8
        self.qLearning = QLearning.QLearning()
        # Acoes
        self.qLearning.configActions(self.conjDM.list) #qLearning.printActions()
        # Estados
        i=0
        listStates = []
        listStates.append(i)
        for iDm in self.conjDM.list:
            i = i + 1
            listStates.append(i)

        #Configuracoes
        self.qLearning.configStates(listStates)
        self.qLearning.configExploration(self.explorationInd)
        self.qLearning.configReward(self.posReward, self.negReward)
        self.qLearning.configLearningRate(self.learningRate)
        self.qLearning.configDiscountFactor(self.discountFactor)
        self.qLearning.startQTable()
        #qLearning.printQTable()



    def genStudentsOld(self):
        self.numStudents=10
        generator = Generator.Generator()
        listStudents = []
        listStudents = self.generator.genStudents(self.numStudents)

    def uploadStudents(self):
        self.numStudents = 8489 #10

        # Carregar base de estudantes / Enade
        # Escolher o arquivo indicado pela análise do artigo
        # --- Gerar Conjunto de Estudantes ---
        #dfX = pd.read_csv("sewlearn_v2/data/kmeans_4_clusters_normalizado.csv")
        dfX = pd.read_csv("data/kmeans_4_clusters_normalizado06.csv")
        vetorEstudantesInput = dfX.values

        listStudents = []
        self.listStudents = self.generator.genStudents(self.numStudents)
        i = 0
        for x in vetorEstudantesInput:
            self.listStudents[i].capacity.softwareUnderstanding = x[1]
            self.listStudents[i].capacity.understandingConcepts = x[2]
            self.listStudents[i].capacity.practiceSM = x[3]
            self.listStudents[i].capacity.testSM = x[4]
            i = i + 1
            #print(x)
            #print( type(x) )
            #print( x[3] )
            #print ('id, softwareUnderstanding, understandingConcepts, practiceSM, testSM' )
            #if (i == 10):
            #    break

        for x in self.listStudents:
           print (x.id, x.capacity.softwareUnderstanding, x.capacity.understandingConcepts, x.capacity.practiceSM, x.capacity.testSM )
        #print ( type(x))

        


    def genDMs(self):
        # --- Gear Conjunto de DMs  ---
        self.conjDM = EKM.Set_DMs()
        self.conjDM.list = self.generator.genDMs(10)

    def configTryResolution(self):
        # --- Planejar número de tentativas (secoes de aprendizagem) -> sequencial ---
        self.numTry1MD = 2  #6        
        self.maxTryMDStudent = self.numTry1MD * len(self.conjDM.list)
        self.filaEstudantesAleatoria = True

    def execQLearning(self):
        # ---  Recomendar DM  ---
        if (self.filaEstudantesAleatoria):

            # episodes - considerar que cada episodio consiste no aluno sorteado 
            # resolvendo a tentativa 
            self.numRecomend = 0

            self.numAcertosTotal = 0
            haEstudantesParaExec = True
            while (haEstudantesParaExec): #episodios
                #print ('------ 1')
                # Sortear estudante 
                nEstudanteSort = random.randrange(1, self.numStudents)
                nEstudanteSort = nEstudanteSort - 1

                # Caso o estudante sorteado tiver sido finalizado, executar o próximo da lista
                # Percorrer o vetor de estudantes enquanto estiverem finalizados para achar o próximo
                nEstudantesFinalizados = 0
                #print ('------ 2')
                while (self.listStudents[nEstudanteSort].finish  and haEstudantesParaExec):
                    nEstudanteSort = nEstudanteSort + 1
                    #if (self.numStudents-1 < self.listStudents[nEstudanteSort].id ):
                    if (self.numStudents-1 < nEstudanteSort):
                        nEstudanteSort = 0
                    nEstudantesFinalizados = nEstudantesFinalizados + 1
                    if (nEstudantesFinalizados == self.numStudents):
                        haEstudantesParaExec = False

                #print ('------ 3')
                # Executar enquanto houver estudantes a serem executados
                if (self.listStudents[nEstudanteSort].nTry >= self.maxTryMDStudent):
                    self.listStudents[nEstudanteSort].finish = True

                if (not self.listStudents[nEstudanteSort].finish):

                    self.listStudents[nEstudanteSort].nTry = self.listStudents[nEstudanteSort].nTry + 1
                    #print ('------ 4')                    
                    idMD = self.qLearning.recommend(self.listStudents[nEstudanteSort].score, self.listStudents[nEstudanteSort].DMsFinished )
                    self.numRecomend = self.numRecomend + 1
                    #print ('------ 5')
                    print ('Exec:', self.numRecomend)

                    #if (self.numRecomend == 3470):
                    #    zzz = 0
                    
                    # ---   Simular Estudante Resolvendo ---
                    correct = self.listStudents[nEstudanteSort].simulateSolve(self.conjDM.list[idMD])

                    iStateOld = self.listStudents[nEstudanteSort].score
                    iStateNew = self.listStudents[nEstudanteSort].score
                    trueReward = False #recompensa negativa
                    
                    #print ('------ 6')
                    if (correct):
                        iStateNew = iStateNew + 1
                        #self.listStudents[nEstudanteSort].DMsFinished.append(self.conjDM.list[idMD])
                        self.listStudents[nEstudanteSort].DMsFinished.append(idMD)
                        trueReward = True #recompensa positiva
                        #print ('val-qLearning:', qLearning.tableQ[iStateOld][idMD], ' idMD:', idMD)
                        self.numAcertosTotal = self.numAcertosTotal + 1

                    #print ('------ 7')
                    self.qLearning.updateQTable(iStateOld, iStateNew, idMD, trueReward, self.listStudents[nEstudanteSort].DMsFinished)
                    self.listStudents[nEstudanteSort].score = iStateNew
                    #print ('------ 8')
                    if self.listStudents[nEstudanteSort].score >= 110:
                        self.listStudents[nEstudanteSort].finish = True

                    #self.gerarTrace(self.listStudents[nEstudanteSort].id, self.listStudents[nEstudanteSort].score, idMD, correct)
                    print ('Student: ', self.listStudents[nEstudanteSort].id, " - Score: ", self.listStudents[nEstudanteSort].score, " - DM: ", self.conjDM.list[idMD].id, ' Response correct:', correct)

                    #print ('------ 9')
                    print (' - - - - - - - - - - - - -')

        else:
            #episodes - considerar que cada episodio consiste em um unico aluno resolvendo n tentativas  (ordenado por estudante 1, 2, 3..)
            self.numRecomend = 0
            
            self.numAcertosTotal = 0
            for student in self.listStudents:  #episodios
                #student = Student.Student()
                #student.model = iStudent
                student.nTry = 0
                student.finish = False

                while((student.nTry < self.maxTryMDStudent) and (not student.finish)):
                    
                    student.nTry = student.nTry + 1
                    idMD = self.qLearning.recommend(student.score, student.DMsFinished )
                    self.numRecomend = self.numRecomend + 1
                    print ('Exec:', self.numRecomend) 

            # ---   Simular Estudante Resolvendo ---
                    correct = student.simulateSolve(self.conjDM.list[idMD])
                    print ('Student: ', student.id, " - Score: ", student.score, " - DM: ", self.conjDM.list[idMD].id, ' Response correct:', correct)
                    iStateOld = student.score
                    iStateNew = student.score
                    trueReward = False #recompensa negativa
                    if (correct):
                        iStateNew = iStateNew + 1
                        student.DMsFinished.append(self.conjDM.list[idMD])
                        trueReward = True #recompensa positiva
                        #print ('val-qLearning:', qLearning.tableQ[iStateOld][idMD], ' idMD:', idMD)
                        self.numAcertosTotal = self.numAcertosTotal + 1

                    self.qLearning.updateQTable(iStateOld, iStateNew, idMD, trueReward, student.DMsFinished)                
                    student.score = iStateNew

                    if student.score >= 110:
                        student.finish = True
                    
                    print (' - - - - - - - - - - - - -')


    def gerarTrace(self, idEstudante, scoreEstudante, idMD, correct):
        #gerar log
        arquivo = open('trace/log.txt','a')
        texto = "idEstudante:"+ str(idEstudante)+", score:"+ str(scoreEstudante)+ ", DM:"+ str(idMD)+ ", Estudante_Acertou:" + str(correct)+ "\n"
        arquivo.write(texto)
        arquivo.close()
        print (texto)

        #gerar arquivo 
        arq = open('trace/res/res_estud' +str(self.numRecomend)+ '.txt','a')
        texto = "idEstudante \ DMs \n"
        for estudante in self.listStudents:
            tx = "idEstudante:" + str(estudante.id) + "; "

            for dm in estudante.DMsFinished:
                tx = tx + str(dm) + " " #dm.id
            texto = texto + tx + "\n"

        arq.write(texto)

    def salvarTexto(self, texto, tipo):
        #if tipo==1: #log
        if (tipo==2): #resultado
            arquivo = open('trace/result2semClus_'+ str(self.nExec)+'.txt','a')
            texto = texto + '\n'
            arquivo.write(texto)
            arquivo.close()

    def printResult(self):
        idpe = self.numAcertosTotal / self.numRecomend
        # --- Imprimir Resumo da Execucao ---
        
        self.salvarTexto("*** Experimento Teste ***", 2)
        x = "Indicador de Exploracao: " + str(self.explorationInd)
        self.salvarTexto(x, 2)
        x = "Modo de Sequenciamento da Resolucao (Estudantes/MDs): () Sequencial,  (X) Aleatoria"
        self.salvarTexto(x, 2)
        x = "Numero de Estudantes: "+ str(self.numStudents)
        self.salvarTexto(x, 2)
        x = "Numero de MDs: "  + str(len(self.conjDM.list))
        self.salvarTexto(x, 2)
        x = "Numero de tentativas (Estudante/MD): "+ str(self.numTry1MD)
        self.salvarTexto(x, 2)
        x = "-Configuracoes q-Learning"
        self.salvarTexto(x, 2)
        x = "Reforco Positivo: "+ str(self.posReward)+ " - Reforco Negativo: "+ str(self.negReward)
        self.salvarTexto(x, 2)
        x = "Taxa de Aprendizagem: "+ str(self.learningRate)
        self.salvarTexto(x, 2)
        x = "Fator de Disconto: "+ str(self.discountFactor)
        self.salvarTexto(x, 2)

        scoreTotal= 0
        for student in self.listStudents:
            x = "Estudante: "+ str(student.id)+ " - Score: "+ str(student.score)+ " - N Recomend: "+ str(student.nTry)
            self.salvarTexto(x, 2)
            #student.printDMsFinished()
            #student.printDMsOFF()
            scoreTotal=scoreTotal+student.score
            
        x = "Media-Score: "+ str(scoreTotal/self.numStudents)
        self.salvarTexto(x, 2)
        x = "Numero Recomendacoes: "+ str(self.numRecomend)
        self.salvarTexto(x, 2)
        x = "Indicador de Desempenho Ponderado do Experimento (IDPE): "+ str(idpe)
        self.salvarTexto(x, 2)
        x = 'Finish'
        self.salvarTexto(x, 2)  

