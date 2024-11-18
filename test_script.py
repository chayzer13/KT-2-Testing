import pytest
from script import calculate_average, add_heroes_and_sort
import json

def test_calculate_average():
    result = calculate_average('grades.csv')
    expected_result = 49.787499999999994  
    assert abs(result - expected_result) < 0.01, f"Expected {expected_result}, but got {result}"

def test_superhero_age():
    add_heroes_and_sort('SuperHero.json')
    with open('superhero_new.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    for hero in data['members']:
        assert hero['age'] >= 0, f"{hero['name']} имеет отрицательный возраст {hero['age']}"
