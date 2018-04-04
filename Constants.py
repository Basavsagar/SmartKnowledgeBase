from  nltk.corpus import  stopwords

class Constants:

    # NLP
    STANDARD_STOPWORDS = list(set(stopwords.words('english')))
    CUSTOM_STOPWORDS = ['``','!', '@', '#', '$', '%', '^', '(', ')', '_', '=', '+', '\',', '|', '}', '{', ']', '[', ';',
                       ':', '/', '?', '<', ',', '>', '.', '`', '~','\"','-']
    CUMULATIVE_STOPWORDS = STANDARD_STOPWORDS + CUSTOM_STOPWORDS
    abbreviationsKeysList = []
    biGramsKeysList=[]

    ABBREVIATIONS = {'dmr': 'dischargemedicationreconciliation',
                     'amr': 'admissionmedicationreconciliation',
                     'psfo': 'partialstructuredfreetextorder',
                     'sp': 'storedprocedure',
                     'mh': 'medhistory',
                     'hm': 'homemedication',
                     'newrx': 'newprescription',
                     'epcs': 'electronicprescriptionofcontrolledsubstances',
                     'pml': 'patientmedicationlist',
                     'favorites': 'personalfavorites',
                     'medrec':'medicationreconciliation'
                     }

    BI_GRAMS =      {'med rec':'medicationreconciliation',
                     'home medications':'homemedication',
                     'home medication':'homemedication',
                     'home meds': 'homemedication',
                     'home med': 'homemedication',
                     'controlled substance': 'controllsubstance',
                     'controll substances': 'controllsubstance',
                     'control substances': 'controllsubstance',
                     'controlled substances': 'controllsubstance',
                     'new prescription': 'newprescription',
                     'new prescriptions': 'newprescription',
                     'clinical checking': 'clinicalchecking',
                     'clinicals checking': 'clinicalchecking',
                     'clinicals checkings': 'clinicalchecking',
                     'discharge rec': 'dischargemedicationre',
                     'discharge medrec': 'dischargemedicationreconciliation',
                     'discharge medicationreconciliation':'dischargemedicationreconciliation',
                     'negative charting': 'negativecharting',
                     'personal favorite': 'personalfavorites',
                     'personal favorites': 'personalfavorites',
                     'med history':'medicationhistory',
                     'medication history':'medicationhistory'
                     }

    def getAbbreviationsKeyList(self):
        for key in self.ABBREVIATIONS.keys():
            self.abbreviationsKeysList.append(key)
        return self.abbreviationsKeysList

    def getBiGramsKeysList(self):
        for key in self.BI_GRAMS.keys():
            self.biGramsKeysList.append(key.lower())
        return self.biGramsKeysList

    INITIAL_CLUSTERS = ['AMR','DaysSupply', 'MedHistory', 'PDMP','Surescripts',
                        'PML', 'PharmacyWorklist', 'ePrescription','KDI', 'DMR', 'HML', 'Security', 'Clinicalchecking',
                       'NegativeCharting', 'Formulary', 'RXFILL', 'ICD10', 'other']