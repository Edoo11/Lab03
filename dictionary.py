
class Dictionary:
    def __init__(self):
        self.vocabolario = []
        pass



    def loadDictionary(self, language):

        diz = ""
        vocabolario = []
        if language == "italian":
            x="Italian"
            diz=f"resources/{x}.txt"
        elif language == "english":
            x="English"
            diz =f"resources/{x}.txt"
        elif language == "spanish":
            x="Spanish"
            diz = f"resources/{x}.txt"

        with(open(diz, 'r')) as f:

            for line in f:
                strippata=line.strip()
                vocabolario.append(strippata)

            f.close()


        return vocabolario


    def printAll(self):
        print(self.vocabolario)



    @property
    def dict(self):
        return self._dict