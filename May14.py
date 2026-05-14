class FileReader:
    #......
    pass

#Виведіть усі прочитані рядки на екран
class LinePrinter:
    #....
    pass

#Підрахуйте v слів у текстовому файлі
class WordCounter:
    #....
    pass

#Перевірте чи містить текстовий файл задане слово
class WordChecker:
    #....
    pass

######################

if __name__ == "__main__":
    fr = FileReader()

    obj1 = LinePrinter()
    obj2 = WordCounter()
    obj3 = WordChecker()

    fr.subscribe(obj1)
    fr.subscribe(obj2)
    fr.subscribe(obj3)

    fr.run()



