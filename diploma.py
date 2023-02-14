from typing import List, Dict
import datetime


def load_data(file_path: str) -> List[Dict[str, str]]:
    """Load data from a file"""
    data = []
    with open(file_path, 'r') as f:
        for line in f:
            # split the line by ',' and remove the newline character
            record = line.strip().split(',')
            data.append({
                'name': record[0],
                'age': record[1],
                'gender': record[2],
                'date of birth': record[3]
            })
    return data


def save_data(file_path: str, data: List[Dict[str, str]]):
    """Save data to a file"""
    with open(file_path, 'w') as f:
        for record in data:
            f.write(f"{record['name']},{record['age']},{record['gender']},{record['date of birth']}\n")


def add_record(data: List[Dict[str, str]]):
    first_name = input("Enter the first name: ")
    if not first_name:
        print("First name cannot be empty.")
        return
    second_name = input("Enter the second name: ")
    parent_name = input("Enter the parent name: ")
    gender = input("Enter the gender: ")
    date_of_birth = input("Enter the date of birth (dd.mm.yyyy or dd mm yyyy or dd/mm/yyyy or dd-mm-yyyy): ")

    date_of_birth = date_of_birth.replace("/", ".")
    date_of_birth = date_of_birth.replace("-", ".")
    date_of_birth_parts = date_of_birth.split(".")

    if len(date_of_birth_parts) == 3:
        day = date_of_birth_parts[0].zfill(2)
        month = date_of_birth_parts[1].zfill(2)
        year = date_of_birth_parts[2]
        date_of_birth = f"{day}.{month}.{year}"

    elif len(date_of_birth_parts) == 2:
        day = date_of_birth_parts[0].zfill(2)
        month = date_of_birth_parts[1].zfill(2)
        year = input("Enter the year (yyyy): ").zfill(4)
        date_of_birth = f"{day}.{month}.{year}"
    elif len(date_of_birth_parts) == 1:
        day = input("Enter the day (dd): ").zfill(2)
        month = input("Enter the month (mm): ").zfill(2)
        year = date_of_birth_parts[0].zfill(4)
        date_of_birth = f"{day}.{month}.{year}"
    else:
        print("Invalid date of birth format.")
        return
        # Call the calculate_age function here
    age = calculate_age(date_of_birth)
    print(first_name, second_name, "You current age is ", age)
    data.append({
        'first_name': first_name,
        'second_name': second_name,
        'parent_name': parent_name,
        'gender': gender,
        'date of birth': date_of_birth
    })


def search_records(data: List[Dict[str, str]]):
    #Search records by name"
    name = input("Enter name to search: ")
    for record in data:
        if record['name'] == name:
            print(record)


def calculate_age(date_of_birth: str) -> int:
    """Calculate the age of a person in years based on their date of birth or today's date"""
    today = datetime.datetime.now().date()
    date_of_birth = datetime.datetime.strptime(date_of_birth, '%d.%m.%Y').date()
    age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    return age




def main():
    data = []
    file_path = 'people.txt'
    choice = 0
    while choice != 5:
        print("1. Load data from file")
        print("2. Save data to file")
        print("3. Add new record")
        print("4. Search records")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            data = load_data(file_path)
        elif choice == 2:
            save_data(file_path, data)
        elif choice == 3:
            add_record(data)
        elif choice == 4:
            search_records(data)


if __name__ == '__main__':
    main()
