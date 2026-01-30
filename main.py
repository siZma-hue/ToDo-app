from task_list import TaskList
from task import Task
from tkinter import *
from place_manager import PlaceManage

task_labels = []


def main():
    todo = TaskList()
    todo.load_file()

    root = Tk()
    root.title('Welcome in ToDo App')
    root.geometry('500x600')
    root.configure(bg='dark slate gray')



# начало работы с кнопкой

    def clicked():
        entry = Entry(root, font=('Arial', 15))
        entry.place(x=46, y=112)

        def on_add_click():

            text = entry.get()
            if text.strip() == '':
                return

            new_task = Task(text=text)

            todo.add_task(new_task)
            todo.save_file()

            entry.delete(0, END)
            refresh_tasks()

        btn3 = Button(root, text='Добавить', command=on_add_click)
        btn3.place(x=146, y=202)

    btn1 = Button(root, text='Добавить задачу', command=clicked, font=('Inter', 15))
    btn1.place(x=PlaceManage.x_x, y=PlaceManage.y1_y)

    def refresh_tasks():
        for lbl in task_labels:
            lbl.destroy()

        task_labels.clear()

        y = 36
        for i, task in enumerate(todo.tasks, 1):
            lbl = Label(root, text=f"{i}. {task}", font=('Inter', 15), bg='dark slate gray')
            lbl.place(x=20, y=y)
            task_labels.append(lbl)
            y += 28

    refresh_tasks()
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




