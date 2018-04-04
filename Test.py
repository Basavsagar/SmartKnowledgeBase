from NaturalLanguageProcessor import NaturalLanguageProcessor
from ExcelHelper import  ExcelHelper
from JiraClassifier import  JiraClassifier


nlpObj=NaturalLanguageProcessor()
excelHelperObj=ExcelHelper()
classifierObj=JiraClassifier()


from Constants import  Constants

summaryList=[]
summaryListAfterStopWordsRemoval=[]
summaryListAfterAbbrExpansion=[]
summaryListAfterByGramming=[]
summaryListAfterStemming=[]
nonClusteredJiraList = []
clusteredJiraList = []
finalTrainingData=[]


'''summaryList=nlpObj.getAllSummaries()

summaryListAfterStopWordsRemoval=nlpObj.removeStopWords(summaryList)
summaryListAfterAbbrExpansion=nlpObj.expandAbbreviations(summaryListAfterStopWordsRemoval)
summaryListAfterByGramming=nlpObj.performBiGrammingOnSummaryList(summaryListAfterAbbrExpansion)
summaryListAfterStemming=nlpObj.performStemming(summaryListAfterByGramming)

excelHelperObj.wirteKeywordsToExcel(summaryListAfterStemming)'''

clusteredJiraList=classifierObj.getClusteredJiraList()
onClusteredJiraList=classifierObj.getNonClusteredJiraList()

finalTrainingData=classifierObj.classifyNonClusteredJira()

print("success")


