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
           if dic.__contains__(word.__str__()) :
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
        self.parole_errate.clear()
        numParole=len(words)
        contatore=0
        while contatore<numParole:
            for word in words:
                word = rw.RichWord(word)
                if word.__str__() in dic :
                    contatore+=1

                else:
                    self.parole_errate.append(word.__str__())
                    contatore+=1

        endTime=time.time()

        print(f"ricerca finita , parole {self.parole_errate} non trovate STOP! , tempo: {endTime-startTime}")



    def searchWordModular(self, words, language):

        startTime = time.time()

        dic = self.dizionario.loadDictionary(language)
        self.parole_errate.clear()

        for w in words:

            word = rw.RichWord(w)

            left = 0
            right = len(dic) - 1
            found = False

            while left <= right:

                mid = (left + right) // 2

                if word._parola == dic[mid]:
                    word.corretta = True
                    found = True
                    break

                elif word._parola < dic[mid]:
                    right = mid - 1

                else:
                    left = mid + 1

            if not found:
                word.corretta = False
                self.parole_errate.append(word._parola)

        endTime = time.time()

        print(
            f"ricerca finita, parole {self.parole_errate} non trovate STOP!, tempo: {endTime-startTime}"
        )




