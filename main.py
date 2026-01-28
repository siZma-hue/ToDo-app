from task_list import TaskList
from task import Task

def main():
    todo = TaskList()
    todo.load_file()

    while True:
        print(f'\n ----ToDo APP----')

        if not todo.tasks:
            print('\n Task List is empty')
        else:
            for i, task in enumerate(todo.tasks, 1):
                print(f'{i}. {task}')

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

if __name__ == "__main__":
    main()




