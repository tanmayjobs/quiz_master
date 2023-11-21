from src.utils.crypt import hash_password, check_password


def test_check_password_positive():
    actual_password = "12345"
    hashed_password = hash_password(actual_password)
    expected = True

    assert expected == check_password(actual_password, hashed_password)


def test_check_password_negative():
    wrong_password = "1234"

    actual_password = "12345"
    hashed_password = hash_password(actual_password)
    expected = False

    assert expected == check_password(wrong_password, hashed_password)
