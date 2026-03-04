
# Assert Statements

def deposit(amount):
    #In order for this program to work correctly
    # and for the bank records to be correct, we must not
    # allow somrone to deposit a zero or negative amount.#
    assert amount > 0


# Valid Python comparison in an assert statement

# assert temperature < 0 
# assert len(given_name) > 0
# assert balance  == 0
# assert school_year ! = "senior"
        

# The pytest Module

def test_min():
    assert min(7, -3, 0, 2) == -3

    