from analysis import validate_todos, completion_counts, top_users, select_tasks

todos = [
    {"id": 1, "userId": 5, "title": "Ввод", "completed": True},
    {"id": 2, "userId": 5, "title": "Циклы", "completed": False},
    {"id": 3, "userId": 10, "title": "Строки", "completed": True},
    {"id": 4, "userId": 10, "title": "Файлы", "completed": True},
    {"id": 5, "userId": 5, "title": "Списки", "completed": True}
]

validate_todos(todos)

counts = completion_counts(todos)
assert counts == {5: 2, 10: 2}
assert top_users(counts) == [5, 10]

assert select_tasks(todos, 5, "и") == [2, 5]
assert select_tasks(todos, 5, None) == [1, 2, 5]
assert select_tasks(todos, 99, "и") == []

print("Все тесты пройдены!")
