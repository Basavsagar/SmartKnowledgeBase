import pandas
import openpyxl
from naiveBayesClassifier import tokenizer
from naiveBayesClassifier.trainer import Trainer
from naiveBayesClassifier.classifier import Classifier


class ExcelHelper:
    jiraDataFile="JiraMetaData.xlsx"
    workBook = openpyxl.load_workbook("JiraMetaData.xlsx")
    activeWorkSheet = workBook.get_sheet_by_name('JIRASelectedRawData')
    # Reading excel
    df = pandas.read_excel("JiraMetaData.xlsx")

    def getNumberOfRows(self):
        return  self.df.values.shape[0]

    def getNumberOfColumns(self):
        return self.df.values.shape[1]

    def getRecrodsByColumnName(self,columnName):
        recordsList=[]
        temp=self.df[columnName].values
        for row in temp:
            recordsList.append(row)
        return recordsList

    def wirteKeywordsToExcel(self,inputList):
        k = 2
        columnName = 'D'
        for item in inputList:
            index = columnName + str(k)
            self.activeWorkSheet[index] = str(item)
            k += 1
        self.activeWorkSheet['D1'] = 'KeyWords'
        self.workBook.save("JiraMetaData.xlsx")
