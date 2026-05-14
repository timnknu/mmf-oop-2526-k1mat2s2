import abc
#from abc import  *
#from abc import abstractmethod

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

class BasicBeautifiedPrinter:
    def __init__(self, beautify = True):
        self._beutify = beautify
    def my_print(self, *args):
        line = ' '.join(map(str, args))
        if self._beutify:
            print('*' * (len(line) + 4))
            print(f'* {line} *')
            print('*' * (len(line) + 4))
        else:
            print(line)


#class Observer(metaclass=abc.ABCMeta):
class Observer(abc.ABC):
    @abc.abstractmethod
    def onReceive(self, line):
        pass



#Виведіть усі прочитані рядки на екран
class LinePrinter(BasicBeautifiedPrinter, Observer):
    def onReceive(self, line):
        self.my_print('LinePrinter says:', line)

#Підрахуйте v слів у текстовому файлі
class WordCounter(BasicBeautifiedPrinter, Observer):
    def onReceive(self, line):
        self.my_print('WordCounter says:', len(line.split()))

#Перевірте чи містить текстовий файл задане слово
class WordChecker(BasicBeautifiedPrinter, Observer):
    def onReceive(self, line):
        w = 'spam'
        self.my_print('WordChecker says:', w in line)

######################

class LengthEvaluator(Observer):
    def onReceive(self, line):
        print('Length is', len(line))

if __name__ == "__main__":
    fr = FileReader('inp.txt')

    obj1 = LinePrinter()
    obj2 = WordCounter()
    obj3 = WordChecker()
    le = LengthEvaluator()

    fr.subscribe(obj1)
    fr.subscribe(obj2)
    fr.subscribe(obj3)
    fr.subscribe(le)

    fr.run()



