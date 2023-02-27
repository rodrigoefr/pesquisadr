import pandas as pd
dfX = pd.read_csv("data/kmeans_4_clusters.csv")
vetorEstudantesInput = dfX.values
df = dfX
'''
softwareUnderstanding = []
understandingConcepts = []
practiceSM = []
testSM = []

for x in vetorEstudantesInput:
    id = x[0]
    softwareUnderstanding.append(x[1] * 0.03)
    understandingConcepts.append(x[2] * 0.03)
    practiceSM.append(x[3] * 0.03)
    testSM.append(x[4] * 0.03)
    print (id)

df['softwareUnderstanding'] = softwareUnderstanding
df['understandingConcepts'] = understandingConcepts
df['practiceSM'] = practiceSM
df['testSM'] = testSM
'''

df['softwareUnderstanding'] = df['softwareUnderstanding'] * 0.03
df['understandingConcepts'] = df['understandingConcepts'] * 0.03
df['practiceSM'] = df['practiceSM'] * 0.03
df['testSM'] = df['testSM'] * 0.03

df.drop(["Unnamed: 0"], axis=1, inplace=True)
print (df.head())

df.to_csv('data/kmeans_4_clusters_normalizado3__v2.csv')
