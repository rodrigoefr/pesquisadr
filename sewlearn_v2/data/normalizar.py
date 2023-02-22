import pandas as pd
dfX = pd.read_csv("data/kmeans_4_clusters.csv")
vetorEstudantesInput = dfX.values
df = dfX

softwareUnderstanding = []
understandingConcepts = []
practiceSM = []
testSM = []

for x in vetorEstudantesInput:
    id = x[0]
    softwareUnderstanding.append(x[1] * 0.06)
    understandingConcepts.append(x[2] * 0.06)
    practiceSM.append(x[3] * 0.06)
    testSM.append(x[4] * 0.06)
    print (id)

df['softwareUnderstanding'] = softwareUnderstanding
df['understandingConcepts'] = understandingConcepts
df['practiceSM'] = practiceSM
df['testSM'] = testSM

df.to_csv('data/saida.csv')
