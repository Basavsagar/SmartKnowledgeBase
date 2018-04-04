from JiraClassifier import  JiraClassifier
from NaturalLanguageProcessor import NaturalLanguageProcessor
from TfIdfRanker import  TfIdfRanker
from JiraClassifier import  JiraClassifier

classifierObj=JiraClassifier()
nlpObj=NaturalLanguageProcessor()
tfIdfRankerObj=TfIdfRanker()
jiraClassifierOnj=JiraClassifier()

finalTrainingData=[]
finalTrainingData=classifierObj.classifyNonClusteredJira()

newJira=input("enter the jira description\n")

newJiraAfterStopWOrdsRemoval=nlpObj.removeStopWordsFromSingleSummary(newJira)
newJiraAfterAbbrExpansion=nlpObj.expandAbbreviationForSingleSummary(newJiraAfterStopWOrdsRemoval)
newJiraAfterBiGramming=nlpObj.performBiGrammingOnSingleSummary(newJiraAfterAbbrExpansion)
newJiraAfterStemming=nlpObj.performStemmingForSingleSummary(newJiraAfterBiGramming)

print("Key words generated for new Jira : {0}\n".format(newJiraAfterStemming))

clusterForNewJira=jiraClassifierOnj.classifyNewJiraToOneOfTheClusters(finalTrainingData,newJiraAfterStemming)

print("Probability of The New Jira w.r.t each Cluster\n")
print(clusterForNewJira)
print("\n")


clusterForNewJira=clusterForNewJira.__getitem__(0)
clusterForNewJira=clusterForNewJira.__getitem__(0)
print("Cluster with higest probability : {0}\n".format(clusterForNewJira))

inputToRankingAlgo=[]
for word in newJiraAfterStemming:
    inputToRankingAlgo.append(word)

tfIdfRankerObj.calculateRank(clusterForNewJira,inputToRankingAlgo)



