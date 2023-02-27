import EKM

class Student:
    def __init__(self):
        self.id = 0
        self.score = 0 
        self.capacity = EKM.Capacity()
        self.DMsFinished = []
        self.finish = False
        self.nTry = 0
        self.tpStudent = -1

    def __str__(self):
        ret = 'practiceSM:' + str(self.model.capacity.practiceSM) + ', softwareUnderstanding:' + str(self.model.capacity.softwareUnderstanding) + ', testSM:' + str(self.model.capacity.testSM) + ', understandingConcepts:' + str(self.model.capacity.understandingConcepts)
        return ret

    def printT(self):
        print ("**Student**")
        print ('id:',self.id)
        print ('score:',self.score)
        print ('softwareUnderstanding:',self.capacity.softwareUnderstanding )
        print ('practiceSM:',self.capacity.practiceSM )
        print ('testSM:',self.capacity.testSM )
        print ('understandingConcepts:',self.capacity.understandingConcepts )

    
    def printDMsFinished(self):
        sDM = ''
        self.DMsFinished.sort()
        for iDM in self.DMsFinished:
            sDM = sDM + str(iDM) + ', '
        print ("DMsFinished: ", sDM)
    
    def printDMsOFF(self):
        #listaDMTotal - self.DMsFinished
        conjDMs = DMs.DMs()
        allDMs = conjDMs.list
        offDMs = allDMs - self.DMsFinished
        sDM = ''
        for iDM in offDMs:
            sDM = sDM + iDM.id + ', '
        print ("DMsOff: ", sDM)


    def simulateSolve(self, dm):
        #verificar qual o tipo de demandedCapacity / knowledge dimension
        #self.printDM()

        ret = False
        if (dm.demandedCapacity.softwareUnderstanding > 0):            
            if (self.capacity.softwareUnderstanding >= dm.demandedCapacity.softwareUnderstanding - dm.score):
                    ret = True
                    #update capacity.knowledgeDimension of student
                    if (self.capacity.softwareUnderstanding < dm.demandedCapacity.softwareUnderstanding):
                        self.capacity.softwareUnderstanding = dm.demandedCapacity.softwareUnderstanding
                        
        if (dm.demandedCapacity.practiceSM > 0):            
            if (self.capacity.practiceSM >= dm.demandedCapacity.practiceSM - dm.score):
                    ret = True
                    #update capacity.knowledgeDimension of student
                    if (self.capacity.practiceSM < dm.demandedCapacity.practiceSM):
                        self.capacity.practiceSM = dm.demandedCapacity.practiceSM

        if (dm.demandedCapacity.testSM > 0):            
            if (self.capacity.testSM >= dm.demandedCapacity.testSM - dm.score):
                    ret = True
                    #update capacity.knowledgeDimension of student
                    if (self.capacity.testSM < dm.demandedCapacity.testSM):
                        self.capacity.testSM = dm.demandedCapacity.testSM

        if (dm.demandedCapacity.understandingConcepts > 0):            
            if (self.capacity.understandingConcepts >= dm.demandedCapacity.understandingConcepts - dm.score):
                    ret = True
                    #update capacity.knowledgeDimension of student
                    if (self.capacity.understandingConcepts < dm.demandedCapacity.understandingConcepts):
                        self.capacity.understandingConcepts = dm.demandedCapacity.understandingConcepts
                        
        return ret
        #if(estudanteAtende):
        #    return 1
        #else:
        #    return 0


'''
for student in listStudents:
    print (student.id,'-',student.generalGrade,'-',student.capacity.softwareUnderstanding
    ,'-', student.capacity.logicalMathematical_Intelligence)
print ('xxxxx')
'''