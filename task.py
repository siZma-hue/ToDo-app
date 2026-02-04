class Task:
    def __init__(self, text, completed=False):
        self.text = text
        self.completed = completed

    def toggle(self):
        self.completed = not self.completed

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f'{status}   {self.text}'

