from nltk import  word_tokenize
from nltk.stem.lancaster import LancasterStemmer
from  nltk.corpus import  stopwords
from ExcelHelper import ExcelHelper
from Constants import  Constants

class NaturalLanguageProcessor:
    excelHelperObj = ExcelHelper()
    constantsObj = Constants()

    # NLP
    stemmer = LancasterStemmer()
    cumulativeStopWords = constantsObj.CUMULATIVE_STOPWORDS
    abbreviationsKeysList = constantsObj.getAbbreviationsKeyList()
    biGramsKeysList=constantsObj.getBiGramsKeysList()

    summaryListAfterStopWordsRemoval = []
    summaryListAfterAbbrExpansion = []
    summaryListAfterBiGramming = []
    summaryListAfterStemming = []

    def process(self):
        recordsList=self.excelHelperObj.getRecrodsByColumnName('Summary')

    def getAllSummaries(self):
        return  self.excelHelperObj.getRecrodsByColumnName('Summary')

    def removeStopWords(self,jiraListWithSummary):
        for summary in jiraListWithSummary:
            self.summaryListAfterStopWordsRemoval.append(self.removeStopWordsFromSingleSummary(summary))

        return  self.summaryListAfterStopWordsRemoval

    def removeStopWordsFromSingleSummary(self,summary):
        summaryAfterStopwordRemoval=''
        for word in word_tokenize(summary):
            if word not in self.cumulativeStopWords:
                word=word.lower().replace('\'','')
                summaryAfterStopwordRemoval=(summaryAfterStopwordRemoval+' '+word).lstrip()
        return summaryAfterStopwordRemoval


    def expandAbbreviations(self,inputSummaryList):
        for summary in inputSummaryList:
            self.summaryListAfterAbbrExpansion.append(self.expandAbbreviationForSingleSummary(summary))
        return self.summaryListAfterAbbrExpansion


    def expandAbbreviationForSingleSummary(self,summary):
        summaryAfterAbbreviationExpansion = ''
        for word in word_tokenize(summary):
            if word in self.abbreviationsKeysList:
                summaryAfterAbbreviationExpansion = (summaryAfterAbbreviationExpansion + ' ' + self.constantsObj.ABBREVIATIONS[word]).lstrip()
            else:
                summaryAfterAbbreviationExpansion = (summaryAfterAbbreviationExpansion + ' ' + word).lstrip()
        return summaryAfterAbbreviationExpansion


    def performBiGrammingOnSummaryList(self,inputSummaryList):
        for summary in inputSummaryList:
            self.summaryListAfterBiGramming.append(self.performBiGrammingOnSingleSummary(summary))
        return self.summaryListAfterBiGramming


    def performBiGrammingOnSingleSummary(self,summary):
        summaryAfterPerformingBiGramming = ''
        kewordsArry=str(summary).split(" ")
        maxLoop=len(kewordsArry)-1
        tempList=[]

        i=0;
        while i<maxLoop:
            bigram=kewordsArry[i]+' '+kewordsArry[i+1]

            if bigram in self.biGramsKeysList:
                tempList.append(self.constantsObj.BI_GRAMS[bigram])
                i=i+2
            else:
                tempList.append(kewordsArry[i])
                i=i+1

        return  ' '.join(tempList)

    def performStemming(self,inputSummaryList):
        for summary in inputSummaryList:
            self.summaryListAfterStemming.append(self.performStemmingForSingleSummary(summary))
        return self.summaryListAfterStemming


    def performStemmingForSingleSummary(self,summary):
        summaryAfterStemming = ''
        for word in word_tokenize(summary):
            summaryAfterStemming=(summaryAfterStemming+' '+self.stemmer.stem(word)).lstrip()
        return summaryAfterStemming