import time

import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
       self.parole_errate=[]
       self.dizionario = d.Dictionary()

       pass

    def printDic(self, language ):
        print(self.dizionario.loadDictionary(language))


    def searchWord(self, words, language):
        dic=self.dizionario.loadDictionary(language)

        self.parole_errate.clear()
        for word in words:
           word=rw.RichWord(word)
           #print(f"parola nel ciclo : {word.__str__()}")
           if word.__str__() in dic:
               word.corretta=True
            #   print(f"{word.__str__()} corretta")
           else:
               word.corretta=False
             #  print(f"{word.__str__()} errata")
               self.parole_errate.append(word.__str__())
              # print(self.parole_errate)

        return self.parole_errate

    def searchWordLinear(self, words, language):
        startTime=time.time()
        dic=self.dizionario.loadDictionary(language)
        numParole=len(words)
        contatore=0
        while contatore<numParole:
            for word in words:
                if word.__str__() in dic :

                    contatore+=1

                else:
                    contatore += 1
                    endTime=time.time()
                    print(f"ricerca finita , parola {word.__str__()} non trovata STOP! , tempo: {endTime-startTime}")




    def searchWordModular(self, words, language):
        dic = self.dizionario.loadDictionary(language)

        return self.parole_errate




