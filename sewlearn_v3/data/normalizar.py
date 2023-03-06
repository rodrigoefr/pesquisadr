import pandas as pd
dfX = pd.read_csv("data/kmeans_4_clusters.csv")
vetorEstudantesInput = dfX.values
df = dfX

df['softwareUnderstanding'] = df['softwareUnderstanding'] * 0.0006
df['understandingConcepts'] = df['understandingConcepts'] * 0.0006
df['practiceSM'] = df['practiceSM'] * 0.0006
df['testSM'] = df['testSM'] * 0.0006

df.drop(["Unnamed: 0"], axis=1, inplace=True)
print (df.head())

df.to_csv('data/kmeans_4_clusters_normalizado0001p.csv')
