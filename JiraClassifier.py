from ExcelHelper import ExcelHelper
from TfIdfRanker import TfIdfRanker
from Constants import  Constants
from naiveBayesClassifier import tokenizer
from naiveBayesClassifier.trainer import Trainer
from naiveBayesClassifier.classifier import Classifier
import  pandas
import  openpyxl


excelHelper=ExcelHelper()
tfIdfRanker=TfIdfRanker()
constantsObj=Constants()


class JiraClassifier:
    file_loc = "JiraMetaData.xlsx"
    df = pandas.read_excel(file_loc)
    pandas.set_option('display.max_colwidth', -1)
    workBook = openpyxl.load_workbook("JiraMetaData.xlsx")
    activeWorkSheet = workBook.get_sheet_by_name('JIRASelectedRawData')

    nonClusteredJiraList = []
    clusteredJiraList = []
    nonClusteredJirasAfterClusteringList=[]
    issueSet=[]

    clusteredJiraFile = open("clusteredJiras.txt", "w")
    nonClusteredJiraFile = open("nonClusteredJiras.txt", "w")
    nonClusteredJirasAfterClusteringFile = open("nonClusteredJirasAfterClustering.txt", "w")
    jiraTrainer = Trainer(tokenizer)


    def getClusteredJiraList(self):

        for index, row in self.df.iterrows():
            clusterName = row['Labels']
            keyWords = row['KeyWords']

            if (clusterName  in constantsObj.INITIAL_CLUSTERS):
                self.clusteredJiraFile.write("%s --- %s\n" % (keyWords, row['Labels']))
                self.clusteredJiraList.append(keyWords)

        self.clusteredJiraFile.close()
        return self.clusteredJiraList

    def getNonClusteredJiraList(self):

        for index, row in self.df.iterrows():
            clusterName = row['Labels']
            keyWords = row['KeyWords']

            if (clusterName not in constantsObj.INITIAL_CLUSTERS):
                self.nonClusteredJiraFile.write("%s\n" % (keyWords))
                self.nonClusteredJiraList.append(keyWords)

        self.nonClusteredJiraFile.close()
        return self.nonClusteredJiraList


    def classifyNonClusteredJira(self):
        columnName = 'C'
        for index, row in self.df.iterrows():
            clusterName = row['Labels']
            keyWords = row['KeyWords']

            if (clusterName  in constantsObj.INITIAL_CLUSTERS):
                self.issueSet.append(({"class": row['Labels'], "sentence": keyWords}))

        for issue in self.issueSet:
            self.jiraTrainer.train(issue['sentence'], issue['class'])

        jiraClassifier = Classifier(self.jiraTrainer.data, tokenizer)

        for index, row in self.df.iterrows():
            clusterName = row['Labels']
            keyWords = row['KeyWords']
            if (clusterName  not in constantsObj.INITIAL_CLUSTERS):
                identifiedCluster=jiraClassifier.classify(row['KeyWords']).__getitem__(0)
                identifiedCluster = identifiedCluster.__getitem__(0)
                self.issueSet.append(({"class": identifiedCluster, "sentence": keyWords}))
                self.nonClusteredJirasAfterClusteringFile.write("%s --- %s\n" % (keyWords, identifiedCluster))
                '''writeIndex = columnName + str(index-2)
                self.activeWorkSheet[writeIndex] = identifiedCluster'''

        self.nonClusteredJirasAfterClusteringFile.close()
        return self.issueSet
        #self.workBook.save("JiraMetaData.xlsx")


    def classifyNewJiraToOneOfTheClusters(self,inputTrainingData,inputJira):
        for item in inputTrainingData:
            self.jiraTrainer.train(item['sentence'], item['class'])
        jiraClassifier = Classifier(self.jiraTrainer.data, tokenizer)
        clusterForInputJira=jiraClassifier.classify(inputJira)

        return  clusterForInputJira






