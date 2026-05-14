class FileReader:
    def __init__(self, fname):
        self._fname = fname
        self._subs = []

    def subscribe(self, obj):
        self._subs.append(obj)

    def run(self):
        with open(self._fname) as f:
            for line in f:
                s = line.rstrip('\r\n')
                for obj in self._subs:
                    obj.onReceive(s)


#Виведіть усі прочитані рядки на екран
class LinePrinter:
    def onReceive(self, line):
        #....
        pass

#Підрахуйте v слів у текстовому файлі
class WordCounter:
    def onReceive(self, line):
        #....
        pass

#Перевірте чи містить текстовий файл задане слово
class WordChecker:
    def onReceive(self, line):
        #....
        pass

######################

if __name__ == "__main__":
    fr = FileReader('inp.txt')

    obj1 = LinePrinter()
    obj2 = WordCounter()
    obj3 = WordChecker()

    fr.subscribe(obj1)
    fr.subscribe(obj2)
    fr.subscribe(obj3)

    fr.run()



