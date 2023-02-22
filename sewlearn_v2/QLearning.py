# import numpy as np
import random

class QLearning:
    
    def __init__(self):
        #use of variables algorithm
        self.listActions = []
        self.listStates = []        
        self.rewardPositie  = 0 
        self.rewardNegative = 0
        self.learningRate = 0
        self.discountFactor = 0
        self.tableQ = []
        self.explorationI = 1
        
        ''' 
         # o array possui listas
         self.tabelaQ = np.array(
            [ [0, 0, 0] , 
              [0, 0, 0] ,
              [0, 0, 0] ]
         )
        '''

    def configExploration(self, explorationInd):
        self.explorationInd = explorationInd

    def configActions(self,listActions):
        #self.listActions = []
        self.listActions = listActions

    def configStates(self,listStates):
        #self.listStates = []
        self.listStates = listStates
    
    def printActions(self):
        for act in self.listActions:
            print (act.cod, act.activityType.cod)

    def configReward(self, positive, negative):
        self.rewardPositie  = positive
        self.rewardNegative = negative

    def configLearningRate(self, x):
        self.learningRate = x

    def configDiscountFactor(self, x):
        self.discountFactor = x

    #def setStudentsEpisodes(self, x):
    #    self.listStudentsEpisodes = x
    
    def startQTable(self):
        print ('nStates: ', len(self.listStates), ' - nActions:', len(self.listActions) )
        
        #estados em linhas e ações em colunas
        for iState in self.listStates:
            line = []
            for iAction in self.listActions:
                n1 = random.random()
                n2 = random.randrange(0, 11)
                
                line.append( n1 * n2 )
            self.tableQ.append(line)
        
        #print (len(self.listActions)," ", len(self.listStates), "teste")
        
        
    def printQTable(self):
        
        lineA = ' ; '
        i = 0
        for iA in self.listActions:
            lineA = lineA + format(i, '.0f') + '; '
            i = i + 1
        print (lineA)
        
        i = 0
        for line in self.tableQ:
            linePrint = format(i, '.0f') + '; '
            i = i + 1
            for col in line:
                linePrint = linePrint +  format(col, '.6f') + '; '
                
            print(linePrint)
        
        #print(self.tableQ[1][1])
        
    
        
        
    def recommend(self, stateStudent, listActionsOff):
        
        #for iStudent in self.listStudentsEpisodes:    
        #    print (iStudent.id)
        
        #identificar a linha que cont�m as a��es e escolher a melhor a��o, excluindo a listActionsOff
        #a linha representa o estado do estudante ()

        #verificar se ir� recomendar de forma racional ou explorar
        
        if self.explorationInd == self.explorationI:
            self.explorationI = 0
            pos = self.findActionRandom(listActionsOff)
            print ("findActionRandom")
        else:
            #linha = self.tableQ[stateStudent]
            pos = self.findMaxAction(stateStudent, listActionsOff)
            print ("findMaxAction")

        self.explorationI = self.explorationI + 1
        

        
        
        ''' maior = -1
        i = -1
        pos = -1
        for valor in linha:
            #print ('--', i)
            i = i + 1
            if (i in listActionsOff): 
                #print (i)
                continue
                
            if (maior<valor):
                maior = valor
                pos = i
        
        print ('_', maior)
        '''
        
        #RETORNAR O ID DO MATERIAL DID�TICO
        return pos
    
    
    def findActionRandom(self,listActionsOff):
        
        # olhar o tamanho da lista de acoes restantes
        nActionsRemaining = len(self.listActions) - len(listActionsOff)
        
        #codigo de teste
        print ("nActionsRemaining;",nActionsRemaining)
        if nActionsRemaining <= 0:
            return 0

        # sortear um numero dentro deste conjunto de acoes restantes
        num = random.randrange(0, nActionsRemaining)
        
        #devolver este id (removendo as acoes ja usadas)
        cont = 0
        retorno = 0
        for i in self.listActions:
            if (i.id in listActionsOff): 
                #print (i)
                continue
            if cont == num:
                retorno = i.id
        
        return retorno
        
        print ("aqui---")
        sys.exit()
    
    def findMaxAction(self, iState, listActionsOff):
        linha = self.tableQ[iState]
        maior = -1
        i = -1
        pos = -1
        for valor in linha:
            #print ('--', i)
            i = i + 1
            if (i in listActionsOff): 
                #print (i)
                continue
                
            if (maior<valor):
                maior = valor
                pos = i
        return pos
    
    def updateQTable(self, iStateOld, iStateNew, iAction, trueReward, listActionsOff):
        
        reward = self.rewardNegative
        if (trueReward):
            reward = self.rewardPositie 
            
        #encontrar o maxQ
        pos = self.findMaxAction(iStateNew, listActionsOff)
        maxQQ = self.tableQ[iStateNew][pos]
        #print ('maxQQ:', maxQQ)
        #encontrar a "celula" a alterar na tabelaQ
        #alterar celula na tabelaQ
        
        #atualizar
        qSA = self.tableQ[iStateOld][iAction] 
        #print ('qSA:',qSA)
        #print ('reward:',reward)
        parte =  self.learningRate * (reward + self.discountFactor * maxQQ - qSA)
        qSA = qSA    +  parte 
        #print ('parte:',parte)
        #print ('qSA+:',qSA)
        self.tableQ[iStateOld][iAction] = qSA
        
        return 0