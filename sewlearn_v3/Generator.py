import EKM
import random
import Student

class Generator:
    
    def genStudents(self, nStudents):
        listStudents = []
        for x in range(nStudents):
            #student  = Model.StudentM()
            student = Student.Student()
            student.id = x
            
            #student.capacity.socialDimension = random.randrange(0, 4)
            #student.capacity.logicalMathematical_Intelligence = random.randrange(0, 4)
            #student.capacity.linguistic_Intelligence = random.randrange(0, 4)
            
            listStudents.append(student)
        return listStudents
        

    def genDMs(self, nDMsForActivityType):
        listDMs = []
        cod = 0
        actTypes = EKM.Set_ActivityTypes()

        for actType in actTypes.listActTypes:
            for i in range(nDMsForActivityType):
                dm = EKM.DM()
                dm.id = cod
                cod = cod + 1
                ii=i+1
                if (actType.categoryActivity=='A'):
                    dm.demandedCapacity.softwareUnderstanding = ii * (actType.numBloomCategory / nDMsForActivityType)
                if (actType.categoryActivity=='B'):
                    dm.demandedCapacity.practiceSM = ii * (actType.numBloomCategory / nDMsForActivityType)
                if (actType.categoryActivity=='C'):
                    dm.demandedCapacity.testSM = ii * (actType.numBloomCategory / nDMsForActivityType)
                if (actType.categoryActivity=='D'):
                    dm.demandedCapacity.understandingConcepts = ii * (actType.numBloomCategory / nDMsForActivityType)

                dm.activityType = actType
                dm.score = actType.numBloomCategory / nDMsForActivityType
                
                listDMs.append(dm)
        
        return listDMs

