from task_list import TaskList
from task import Task
from tkinter import *
from place_manager import PlaceManage

def clicked():
    return


def main():
    todo = TaskList()
    todo.load_file()

    root = Tk()
    root.title('Welcome in ToDo App')
    root.geometry('500x600')


    if not todo.tasks:
        lbl1 = Label(root, text='Ваш список пустой. Задач нет!')
        lbl1.place(row=0, column=0)
    else:
        for i, task in enumerate(todo.tasks, 1):
            lbl2 = Label(root, text=f'{i}. {task}', font=('Arial', 20))
            lbl2.pack()

    btn1 = Button(root, text='Добавить задачу', command=clicked, font=('Arial', 15))
    btn1.place(x=PlaceManage.x_x, y=PlaceManage.y1_y)

    btn2 = Button(root, text='Сохранить и выйти', command=clicked, font=('Arial', 15))
    btn2.place(x=PlaceManage.x_x1, y=PlaceManage.y1_y1)

    root.mainloop()

"""
        print(f'\n1. Добавить задачу')
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
            break
            """

if __name__ == "__main__":
    main()




