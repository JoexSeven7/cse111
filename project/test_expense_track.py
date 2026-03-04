import pytest
from expense_track import make_expense_record, filter_by_category, calculate_total
from expense_track import DATE_INDEX, CATEGORY_INDEX, DESC_INDEX, AMOUNT_INDEX

def test_make_expense_record():
    # Test creating a record
    record = make_expense_record("2024-01-01", "Food", "Lunch", 15.50)
    
    # Assert it returns a list with correct values at correct indexes
    assert isinstance(record, list)
    assert record[DATE_INDEX] == "2024-01-01"
    assert record[CATEGORY_INDEX] == "Food"
    assert record[DESC_INDEX] == "Lunch"
    assert record[AMOUNT_INDEX] == 15.50

def test_filter_by_category():
    # Create mock data (List of Lists)
    # Note: CSV readers usually read amounts as strings first, so we simulate that
    sample_data = [
        ["2024-01-01", "Food", "Lunch", "10.00"],
        ["2024-01-02", "Rent", "Monthly", "500.00"],
        ["2024-01-03", "Food", "Dinner", "20.00"],
        ["2024-01-04", "Gas",  "Fuel", "50.00"]
    ]
    
    # Filter for 'Food'
    food_list = filter_by_category(sample_data, "Food")
    
    # Should have 2 items
    assert len(food_list) == 2
    assert food_list[0][CATEGORY_INDEX] == "Food"
    assert food_list[1][CATEGORY_INDEX] == "Food"
    
    # Filter for 'Rent'
    rent_list = filter_by_category(sample_data, "Rent")
    assert len(rent_list) == 1
    
    # Filter for non-existent category
    fun_list = filter_by_category(sample_data, "Fun")
    assert len(fun_list) == 0

def test_calculate_total():
    # Create mock data
    sample_data = [
        ["date", "cat", "desc", "10.50"],
        ["date", "cat", "desc", "20.25"],
        ["date", "cat", "desc", "5.00"]
    ]
    
    total = calculate_total(sample_data)
    
    # Check total with approximation
    assert total == pytest.approx(35.75)

# Run tests
pytest.main(["-v", "--tb=line", "-rN", __file__])