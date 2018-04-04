from Constants import  Constants

constantsObj=Constants()

def performByGrammingOnSingleSummary(self,summary):
    summaryAfterPerformingByGramming = ''
    kewordsArry = str(summary).split(" ")

    i = 0
    maxLoop = len(kewordsArry) - 1
    while True:
        byGram = kewordsArry[i] + kewordsArry[i + 1]
        if byGram in self.abbreviationsKeyToLowerList:
            summaryAfterPerformingByGramming = (
            summaryAfterPerformingByGramming + ' ' + self.constantsObj.BY_GRAMS[byGram]).lstrip()
            i = i + 2
        else:
            summaryAfterPerformingByGramming = (summaryAfterPerformingByGramming + ' ' + byGram).lstrip()
            i = i + 1

        if i >= maxLoop:
            break

    return summaryAfterPerformingByGramming

