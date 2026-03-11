import string
import time
import multiDictionary as md

class SpellChecker:



    def __init__(self):
        self.multiDiz = md.MultiDictionary()
        pass

    def handleSentence(self, txtIn, language):

        startTime = time.time()

        testo=replaceChars(txtIn.lower())

        stringaParoleTesto = testo.split()
        #print(stringaParoleTesto)
        paroleErrate=self.multiDiz.searchWord(stringaParoleTesto,language)

        endTime = time.time()

        print(f" lista parole errate:{paroleErrate} , numero di parole errate:{len(paroleErrate)} ,tempo impiegato:{endTime-startTime}")


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text
