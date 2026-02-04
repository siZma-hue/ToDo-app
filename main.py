from PyInstaller.lib.modulegraph.modulegraph import entry

from task_list import TaskList
from task import Task
from tkinter import *

task_labels = []


def main():
    todo = TaskList()
    todo.load_file()

    root = Tk()

    root['bg'] = '#fafafa'
    root.title('ToDo')
    root.geometry('500x700')
    root.resizable(False, False)

    frame1 = Frame(root, bg='black')
    frame1.place(relx=0, rely=0, relwidth=1, relheight=0.7)

    tasks_var = StringVar(value=todo.tasks)

    list_box = Listbox(frame1, listvariable=tasks_var, bg='black', fg='white',
                       font=('arial', 17))
    list_box.pack(fill='both', expand=True, pady=30, padx=30)

    def toggle_done(event):
        index = list_box.curselection()[0]
        todo.tasks[index].toggle()
        tasks_var.set(todo.tasks)

    list_box.bind("<Double-Button-1>", toggle_done)

    canvas1 = Canvas(frame1, bg='black', highlightthickness=0)
    canvas1.pack(fill='both', expand=True)

    frame2 = Frame(root, bg='light blue')
    frame2.place(relx=0, rely=0.7, relwidth=1, relheight=0.3)

    entry = Entry(frame2, bg='white', fg='black', width=40)
    entry.place(x=30, y=540)

    canvas2 = Canvas(frame2, bg='light blue', highlightthickness=0)
    canvas2.pack(fill='both', expand=True)


    root.mainloop()



#btn2 = Button(root, text='Сохранить и выйти', font=('Arial', 15))
#btn2.place(x=PlaceManage.x_x1, y=PlaceManage.y1_y1)

"""print(f'\n1. Добавить задачу')
        print(f'2. Отметить задачу выполненной')
        print(f'3. Сохранить и выйти')

        choice = input("Выберите действие: ")

        if choice == '1':
            text = input("Введите задачу: ")
            todo.add_task(Task(text))

        elif choice == '2':
            num = int(input("Номер задачи: "))
            todo.tasks[num - 1].completed = True

        elif choice == '3':
            todo.save_file()
            print("До скорой встречи!")
            break """

if __name__ == "__main__":
    main()




