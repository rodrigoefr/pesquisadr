import QLearning

qLearning = QLearning.QLearning();

qLearning.setNStatesAndActions(3, 5)

qLearning.execute()

#print (qLearning.tableQ)

print ("actions" , qLearning.actions)

print ("tableQ" , qLearning.tableQ)

