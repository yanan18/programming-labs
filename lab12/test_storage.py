import os
from storage import save_records, load_records

def test_save_load():
    test_file = "temp_test.json"
    data = [{"id": 1, "title": "Тест"}]
    
    assert save_records(test_file, data) == True
    loaded = load_records(test_file)
    assert loaded == data
    
    os.remove(test_file)

test_save_load()
print("Сохранение и чтение работают!")
