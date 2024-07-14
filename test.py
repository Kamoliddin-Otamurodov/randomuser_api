import pytest
from main import gender_user , b

a = gender_user(b)

def user_is_female(gender):
    if gender == "female":
        return True
    else:
        return False
    

def test_is_female():
    ans = True

    execute = user_is_female(a)

    assert ans == execute

test_is_female()