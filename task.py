class Task:
    def __init__(self, text, completed=False):
        self.text = text
        self.completed = completed

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f'{status} {self.text}'