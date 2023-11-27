import labtest1


def test_calc_average_expenses():
    csv_list=labtest1.load_csv_database()
    result = labtest1.calc_average_expenses(csv_list)
    assert result == 6.0

def test_calc_total_expenses():
    csv_list=labtest1.load_csv_database()
    result = labtest1.calc_total_expenses(csv_list)
    assert result == 42.0

def test_is_price_range_valid():
    result1 = labtest1.is_price_range_valid(1,2)
    result2 = labtest1.is_price_range_valid(2,1)
    assert result1 and not result2

def test_get_items_by_price_range():
    csv_list=labtest1.load_csv_database()
    result = labtest1.get_items_by_price_range(csv_list,3.5,8)
    assert result == [{'date': '15.01.2022', 'expense_item': 'butter', 'price': '3.5'}, {'date': '19.01.2022', 'expense_item': 'apples', 'price': '4.7'}]
def test_sort_by_items():
    csv_list=labtest1.load_csv_database()
    result = labtest1.sort_by_items(csv_list)
    assert result == [{'date': '19.01.2022', 'expense_item': 'apples', 'price': '4.7'}, {'date': '15.01.2022', 'expense_item': 'butter', 'price': '3.5'}, {'date': '20.01.2022', 'expense_item': 'oranges', 'price': '3'}, {'date': '22.01.2022', 'expense_item': 'potatos', 'price': '2.5'}, {'date': '13.01.2022', 'expense_item': 'rice', 'price': '13.5'}, {'date': '30.01.2022', 'expense_item': 'rice', 'price': '12'}, {'date': '17.01.2022', 'expense_item': 'sugar', 'price': '2.8'}]



