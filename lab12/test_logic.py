from logic import validate_records, add_record, find_records, set_completed, delete_record, statistics

def test_all():
    records = []
    
    r = add_record(records, "Маршрут 1", "лес", 5)
    assert r["id"] == 1
    r2 = add_record(records, "Маршрут 2", "горы", 10)
    assert r2["id"] == 2
    
    assert find_records(records, "маршрут")[0]["id"] == 1
    assert find_records(records, "") == []
    
    assert set_completed(records, 1, True) == True
    assert set_completed(records, 99, True) == False
    
    assert delete_record(records, 1) == True
    assert delete_record(records, 99) == False
    
    total, done, not_done, amount, cats = statistics(records)
    assert total == 1
    assert amount == 10

test_all()
print("Все тесты пройдены!")
