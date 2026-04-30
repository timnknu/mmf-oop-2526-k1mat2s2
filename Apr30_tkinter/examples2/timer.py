# Приклад програми "таймера" (відліку часу)
# Очікується, що користувач вводить кількість секунд, після чого запускає відлік часу кнопкою "Пуск". Відлік часу відбувається з інтервалом 1 секунда, і коли час вийде, користувачеві пропонується запустити відлік знову. Кнопка "Стоп" дозволяє зупинити відлік часу в будь-який момент.
# (для простоти, у цьому прикладі припускається, що користувач діє лише за "правильним" сценарієм)
# Однак, користувач вправі взаємодіяти з програмою у будь-який спосіб - не обов'язково дотримуючись "правильного" сценарію - наприкдад, натискати "Стоп" ще до запуску відліку, або змінювати кількість секунд під час відліку.
# Тож загалом за наявності графічного інтерфейсу, програму потрібно зробити "стійкою" до будь-яких дій користувача (або - заблокувати деякі дії, якщо вони не відповідають "правильному" сценарію).


import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("My Timer")
        # встановлення розміру вікна та його центрування на екрані
        width=348
        height=192
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        #root.resizable(width=False, height=False)

        # поля для введення кількості секунд та змінна-контейнер для зберігання цього значення
        self.s = tk.StringVar()
        time_entry = tk.Entry(root, textvariable=self.s)
        time_entry.place(x=70,y=40,width=186)
        self.s.set("10") # встановити початкове значення кількості секунд

        # мітка для поля введення
        lbl1 = tk.Label(root, text = "Кількість секунд")
        lbl1.place(x=0,y=0)

        # кнопки "Пуск" та "Стоп", які викликають відповідні методи при натисканні
        start_btn = tk.Button(root, text = "Пуск",
                              command = self.start_bnt_onclick)
        start_btn.place(x=30,y=110,width=70,height=25)

        stop_btn = tk.Button(root, text = "Стоп",
                             command = self.stop_btn_onclick)
        stop_btn.place(x=220,y=110,width=70,height=25)

        # початковий стан спеціальної змінної, яка вказує поточний "стан" програми - чи відлік часу активний, чи ні
        self.is_active = False

    # метод, який викликається tkinter'ом "автоматично" (як наслідок запланованого виклику через .after())
    # Він використовується для оновлення і перевірки кількості секунд, що залишилися
    def update_time(self):
        if not self.is_active: # на випадок, якщо користувач натиснув "Стоп", а метод update_time() вже запланований до виклику через .after()
            tk.messagebox.showwarning(title="відповідь",
                                      message="відлік часу зупинений")
            return
        #

        old_text = self.s.get() # отримати поточний текст з поля введення (який має бути кількістю секунд, що залишилися)
        old_val = int(old_text)
        if old_val == 0: # якщо час вийшов
            #tk.messagebox.askyesno(title="питання",
            #                       message="Час вийшов. Запустити знову?")
            ans = tk.messagebox.askquestion(title="питання",
                                            message="Час вийшов. Запустити знову?",
                                            type=tk.messagebox.YESNO)
            tk.messagebox.showwarning(title="відповідь",
                                      message=ans)

        else: # якщо час ще не вийшов
            self.s.set( str(old_val - 1) )  # змінити текст у полі введення на кількість секунд, що залишилися (на 1 менше, ніж було до цього)
            root.after(1000, self.update_time) # запланувати повторний виклик цього ж методу через 1 секунду (1000 мс)
    #

    # метод, який викликається при натисканні кнопки "Пуск"
    def start_bnt_onclick(self):
        self.is_active = True
        root.after(1000, self.update_time) # методом .after() ми ініціюємо виклик методу update_time() з затримкою 500 мс (0.5 сек)

    # метод, який викликається при натисканні кнопки "Стоп"
    def stop_btn_onclick(self):
        self.is_active = False



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
#        ft = tkFont.Font(family='Times',size=10)
