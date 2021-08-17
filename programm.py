import tkinter
from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile#Функции сохранить как и открыть файл
from tkinter.messagebox import showerror #Показ всех ошибок
from tkinter import messagebox #Уведомления приложения
from settings import *

class Text():
    def __init__(self):
        self.file_name = tkinter.NONE

    def new_file(self):
        self.file_name = 'Без названия'
        text.delete('1.0',tkinter.END)

    def open_file(self):
        inp = askopenfile(mode='r')
        if inp is None:
            return
        data = inp.read()
        text.delete('1.0',tkinter.END)
        text.insert('1.0',data)

    def save_file(self):
        data = text.get('1.0',tkinter.END)
        output = open(self.file_name,'w',encoding='utf-8')
        output.write(data)
        output.close()

    def save_as_file(self):
        output = asksaveasfile(mode='w',defaultextension='txt')
        data = text.get('1.0',tkinter.END)
        try:
            output.write(data.rstrip())
        except Exception:
            showerror(title='Ошибка!',message='Ошибка при сохранении файла')

    def get_info(self):
        messagebox.showinfo('Справка','Спасибо, что используете наше приложение =) ')

app = tkinter.Tk() #Окно нашего приложения
app.title(APP_NAME)# Название нашего приложения
app.minsize(width=WIDTH,height=HEIGHT)
app.maxsize(width=WIDTH,height=HEIGHT)

menuBar = tkinter.Menu(app) # Создаём меню

editor = Text()

app_menu = tkinter.Menu(menuBar) #выпадающее меню для Файл

app_menu.add_command(label='Новый', command=editor.new_file)
app_menu.add_command(label='Открыть', command=editor.open_file)
app_menu.add_command(label='Сохранить', command=editor.save_file)
app_menu.add_command(label='Сохранить как', command=editor.save_as_file)

menuBar.add_cascade(label='Файл',menu=app_menu)
menuBar.add_cascade(label='Справка',command=editor.get_info)
menuBar.add_cascade(label='Выход',command=app.quit)

text = tkinter.Text(app,width=WIDTH - 100,height = HEIGHT-10,wrap='word')# Создали поле с текстом
scroll = Scrollbar(app,orient=VERTICAL, command=text.yview)# Создали скрол
scroll.pack(side='right',fill='y')#Разместили скрол
text.configure(yscrollcommand=scroll.set) #Связь текста со скролом
text.pack()#Разместили поле с текстом
app.config(menu=menuBar)# Публикуем меню

app.mainloop()
