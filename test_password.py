# IMPORTS
import pytest
from password import main # IMPORT FILE WITH ORIGINAL CODE
import string


# GLOBAL VARIABLES
password_length = 16
valid_characters = list(string.ascii_letters + "0123456789!@#$%^&*()-_=+[]{};:,.<>?/")

# TEST 01 - LENGTH OF THE PASSWORD:
def test_length():
    password = main("", password_length, valid_characters)
    assert len(password) == password_length, f"ERROR: {len(password)} is not correct. Must be 16"
    print("LENGTH TEST PASS")

# TEST 02 - CHAR COMBINATIONS:
def test_char():
    password = main("", password_length, valid_characters)
    assert any(char.islower() for char in password), "ERROR: The password does not have lowercase letters."
    assert any(char.isupper() for char in password), "ERROR: The password does not have uppercase letters."
    assert any(char.isdigit() for char in password), "ERROR: The password does not have numbers."
    assert any(char in "!@#$%^&*()-_=+[]{};:,.<>?/" for char in password), "ERROR: The password does not have symbols."
    print("CHAR, NUMS AND SYMBOLS TEST PASS")
    
    
# TEST 03 - COMMON PATTERNS:
def test_patterns():
    pattern_list = [
    "123", "abc", "password", "qwerty", "1111", "letmein", "1234", "qwertyuiop", 
    "asdf", "welcome", "dragon", "monkey", "iloveyou", "sunshine", "qazwsx", 
    "1qaz2wsx", "password1", "qwerty123", "123qwe", "1q2w3e4r", "qwerty1", "123123",
    "qwerty1234", "letmein123", "abc123", "123abc", "qwertyuiop1", "qwerty12345", 
    "12345", "abc12345", "123qwerty", "iloveyou123", "welcome123", "dragon123", 
    "admin123", "iloveme", "1234abcd", "password123", "123qwertyuiop", "qwerty1abc","12345", "password", "123456", "123456789", "qwerty", "abc123", "letmein", 
    "monkey", "1234", "123123", "welcome", "sunshine", "iloveyou", "admin", 
    "welcome123", "qwerty123", "trustno1", "password1", "123qwe", "1q2w3e4r", 
    "shadow", "qwertyuiop", "123321", "password123", "111111", "abc12345", 
    "princess", "football", "123qwerty", "123abc", "qazwsx", "1qaz2wsx", "letmein123", 
    "dragon", "starwars", "qwerty1", "sunshine1", "hello123", "123abc123", "welcome1", 
    "password1", "iloveu", "password1234", "1password", "monkey123", "123qwertyuiop", 
    "iloveyou123", "test123", "admin123", "qwertyuiop1", "1qazxsw2", "1234abcd", 
    "letmein1234", "qwerty1234", "1password1", "football1", "master", "superman", 
    "princess123", "welcome1234", "qwerty12345", "abc12345", "123qwe123"
    ]
    password = main("", password_length, valid_characters)
    assert not any(pattern in password for pattern in pattern_list), "ERROR: The password contains a common word or pattern."
    print("COMMON PATTERNS TEST PASS")


# TEST 04 - RANDOMNESS:
def test_random():
    password1 = main("", password_length, valid_characters)
    password2 = main("", password_length, valid_characters)
    assert password1 != password2, "ERROR: The generated passwords are the same."
    print("RANDOMNESS TEST PASS")

