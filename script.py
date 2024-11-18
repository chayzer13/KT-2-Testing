import csv
import json

def calculate_average(file_path):
    with open(file_path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        reader.fieldnames = [field.strip() for field in reader.fieldnames]
        
        total_grades = 0
        count = 0
        for row in reader:
            try:

                grades = [
                    float(row['Test1'].strip()), 
                    float(row['Test2'].strip()), 
                    float(row['Test3'].strip()), 
                    float(row['Test4'].strip()), 
                    float(row['Final'].strip())
                ]
                average = sum(grades) / len(grades)
                print(f"Средний балл для {row['First name']} {row['Last name']}: {average}")
                total_grades += average
                count += 1
            except KeyError as e:
                print(f"Ошибка: отсутствует ключ {e} в строке {row}")
            except ValueError as e:
                print(f"Ошибка: некорректные данные в строке {row}")
        return total_grades / count if count > 0 else 0


avg = calculate_average('grades.csv')
print(f"Общий средний балл: {avg}")



def add_heroes_and_sort(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    

    new_heroes = [
        {
            "name": "Captain Code",
            "age": 35,
            "secretIdentity": "Coder",
            "powers": ["Programming", "Hacking", "Cybersecurity"]
        },
        {
            "name": "Speedster",
            "age": 28,
            "secretIdentity": "Dash Runner",
            "powers": ["Super speed", "Time manipulation"]
        }
    ]
    
    data['members'].extend(new_heroes)
    

    data['members'] = sorted(data['members'], key=lambda x: x['age'])


    for hero in data['members']:
        if hero['age'] > 30:
            print(f"{hero['name']} старше 30 лет!")
    

    with open('superhero_new.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    print("Часть 1: Среднее арифметическое оценок")
    avg = calculate_average('grades.csv')
    print(f"Общий средний балл: {avg}")
    
    print("\nЧасть 2: Обновление JSON с супергероями")
    add_heroes_and_sort('SuperHero.json')
    print("Данные сохранены в superhero_new.json")
