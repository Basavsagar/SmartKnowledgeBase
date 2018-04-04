import pandas as pd
import math

class TfIdfRanker():
    file_loc = "JiraMetaData.xlsx"
    df = pd.read_excel(file_loc, useCols = "A,C,D")
    pd.set_option('display.max_colwidth',-1)

    def tf(self,word,blob):
        termFreq = blob.upper().count(word.upper())
        if termFreq > 0:
            termFreq = 1 + math.log(termFreq)
        return termFreq

    def n_containing(self,word, bloblist):
        return sum(1 for blob in bloblist if word.upper() in blob.upper())

    def idf(self,word, bloblist):
        containingDocuments = self.n_containing(word,bloblist)
        wordIdf = 0
        if containingDocuments > 0:
            wordIdf = math.log(len(bloblist) / containingDocuments)
        return wordIdf

    def tfIdf(self,word, blob, bloblist):
        return (self.tf(word, blob) * self.idf(word, bloblist))

    def calculateRank(self, label, search_doc):
        Col_Keyword = self.df.loc[self.df['Labels'] == label, 'KeyWords']
        Col_JIRANo = self.df.loc[self.df['Labels'] == label, 'JIRA NO']
        my_dict = dict(zip(Col_JIRANo, Col_Keyword))

        Result_Dict = {}
        finalDictToReturn = {}

        for key, value in my_dict.items():
            docTfIdf = 0
            if pd.notnull(value):
                for word in search_doc:
                    docTfIdf = docTfIdf + self.tfIdf(word, value, my_dict.values())

            Result_Dict[key] = docTfIdf

        Ordered_Dict = dict(sorted(Result_Dict.items(), key=lambda x: x[1], reverse=True))
        first3pairs = {k: Ordered_Dict[k] for k in list(Ordered_Dict)[:3]}

        for jiraKey in first3pairs:
            Col_Summary = self.df.loc[self.df['JIRA NO'] == jiraKey, 'Summary']
            finalDictToReturn[jiraKey] = list(Col_Summary)[0]

        #return finalDictToReturn

        print("List of Smiliar Jiras\n")
        print(finalDictToReturn)

