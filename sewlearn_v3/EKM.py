'''class StudentM:
    def __init__(self):
        self.id = 0
        self.score = 0 
        self.capacity = Capacity()
    
    def printT(self):
        print ("**Student**")
        print ('id:',self.id)
        print ('score:',self.score)
        print ('softwareUnderstanding:',self.capacity.softwareUnderstanding )
        print ('practiceSM:',self.capacity.practiceSM )
        print ('testSM:',self.capacity.testSM )
        print ('understandingConcepts:',self.capacity.understandingConcepts )
'''


class Capacity:    
    def __init__(self):
        self.softwareUnderstanding = 0
        self.practiceSM = 0
        self.testSM = 0
        self.understandingConcepts = 0
        #self.socialDimension = 0
        #self.logicalMathematical_Intelligence = 0
        #self.linguistic_Intelligence = 0


#ActivityCategory
#A) Compreens�o de Software
#B) Pr�ticas de MS
#C) Testes de Software
#D) Compreens�o de conceitos


class ActivityType:
    def __init__(self):
        self.id = ""
        self.categoryActivity=""
        self.description=""
        self.numBloomCategory=0


class Set_ActivityTypes:
    def __init__(self):
        listActTypes = [ 
        #ActivityCategory / ActivityType-COD / ActivityType-DESCRIPTION / numBloomCategory (N� A��ES APREND. BLOOM)
        ['A', 'A1',   'A1 - Compreender o resultado da execucao (codigo-fonte)', 2], 
        ['A', 'A2',   'A2 - Ordenar o programa (parson puzzles)', 4], 
        ['A', 'A3_1', 'A3_1 - Responder o resumo (codigo-fonte)', 4], 
        ['A', 'A3_2', 'A3_2 - Responder o resumo (modelos UML)', 4], 
        ['B', 'B1',   'B1 - MS do tipo Correcao de Defeitos', 6], 
        ['B', 'B2',   'B2 - MS do tipo Adaptacao Ambiental', 6], 
        ['B', 'B3',   'B3 - MS do tipo Adicao de Funcionalidade', 6], 
        ['B', 'B4',   'B4 - Refatoracao', 4], 
        ['C', 'C1',   'C1 - Testes', 5], 
        ['D', 'D1',   'D1 - Processo de MS', 2], 
        ['D', 'D2',   'D2 - Manutenibilidade de Software', 2] ];

        self.listActTypes = []
        
        for activTyp in listActTypes:
            activType = ActivityType()
            activType.cod = activTyp[1]
            activType.categoryActivity = activTyp[0]
            activType.description = activTyp[2]
            activType.numBloomCategory = activTyp[3]
            self.listActTypes.append(activType)


class DM:
    def __init__(self):
        self.id = 0
        self.demandedCapacity = Capacity()
        self.activityType = ActivityType()
        self.score = 0

class Set_DMs:
    def __init__(self):
        self.list = []

    def printDMs(self):
        print ( )
        print ( 'DM-list')
        print ( 'cod; description; softwareUnderstanding; practiceSM; testSM; understandingConcepts; score')
        for dm in self.list:
            print(dm.id, "; ", dm.activityType.description, "; ", dm.demandedCapacity.softwareUnderstanding, "; ", dm.demandedCapacity.practiceSM, "; ", dm.demandedCapacity.testSM, "; ", dm.demandedCapacity.understandingConcepts, "; ", dm.score )

