import json
from task import Task

class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def save_file(self, filename='tasks.json'):
        data = []
        for task in self.tasks:
            data.append({
                'text': task.text,
                'completed': task.completed,
            })

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load_file(self, filename='tasks.json'):
        try:
            with open(filename, encoding='utf-8') as f:
                data = json.load(f)

            self.tasks = []
            for item in data:
                self.tasks.append(Task(text=item['text'], completed=item['completed']))
        except FileNotFoundError:
            self.tasks = []

    def remove_task(self, task):
        self.tasks.remove(task)

    def search_task(self, text):
        for task in self.tasks:
            if task.text == text:
                return task
        return None
