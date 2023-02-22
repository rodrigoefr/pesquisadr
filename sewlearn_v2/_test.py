import DMs
import Generator

generator = Generator.Generator()
conjDM = DMs.DMs()
conjDM.list = generator.genDMs(10) 

allDMs = conjDM.list

#print(allDMs)

for dm in allDMs:
    print (dm.id, " - ", dm.activityType.description)