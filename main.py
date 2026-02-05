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
        todo.save_file()

    list_box.bind("<Double-Button-1>", toggle_done)

    canvas1 = Canvas(frame1, bg='black', highlightthickness=0)
    canvas1.pack(fill='both', expand=True)

    frame2 = Frame(root, bg='#ECEBEC')
    frame2.place(relx=0, rely=0.7, relwidth=1, relheight=0.3)


    def delete_task():
        index = list_box.curselection()[0]
        todo.remove_task(todo.tasks[index])
        tasks_var.set(todo.tasks)
        todo.save_file()

    btn_delete = Button(frame2, text='Удалить', command=delete_task)
    btn_delete.place(relx=0.22, rely=0.75, anchor='e')

    entry = Entry(frame2, bg='black', fg='white', font=('arial', 12))
    entry.place(relx=0.05, rely=0.2, relwidth=0.7)

    def add_task():
        text = entry.get().strip()
        if not text:
            return

        todo.add_task(Task(text))
        tasks_var.set(todo.tasks)
        todo.save_file()

        entry.delete(0, END)


    btn2_add = Button(frame2, text='Добавить', command=add_task)
    btn2_add.place(relx=0.24, rely=0.50, anchor='e')


    root.mainloop()


if __name__ == "__main__":
    main()




