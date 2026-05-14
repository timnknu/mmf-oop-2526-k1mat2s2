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

#class Observer(metaclass=abc.ABCMeta):
class Observer(abc.ABC):
    @abc.abstractmethod
    def onReceive(self, line):
        pass

class BasicBeautifiedPrinter:
    def __init__(self, beautify = True):
        self._beutify = beautify
    def my_print(self, line):
        if self._beutify:
            print('*' * (len(line) + 4))
            print(f'* {line} *')
            print('*' * (len(line) + 4))
        else:
            print(line)



b = BasicBeautifiedPrinter(False)
b.my_print('Hello world')

#Виведіть усі прочитані рядки на екран
class LinePrinter(Observer):
    def onReceive(self, line):
        print('LinePrinter says:', line)

#Підрахуйте v слів у текстовому файлі
class WordCounter(Observer):
    def onReceive(self, line):
        print('WordCounter says:', len(line.split()))

#Перевірте чи містить текстовий файл задане слово
class WordChecker(Observer):
    def onReceive(self, line):
        w = 'spam'
        print('WordChecker says:', w in line)

######################

class LengthEvaluator:
    def get_length(self, line):
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



