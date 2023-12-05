from company import departments


def min_salary_department():
    # Вывести названия отделов с указанием минимальной зарплаты в нём
    for department in departments:
        employer = department['employers']
        print(f'Минимальная зарплата {min(user["salary_rub"] for user in employer)} в отделе {department["title"]} ')


def all_salary_department():
    # Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём
    for department in departments:
        sum_department = 0
        count = 0
        for employer in department["employers"]:
            sum_department += employer["salary_rub"]
            count += 1
        employer = department['employers']
        print(f'Отдел {department["title"]} с минимальной зарплатой {min(user["salary_rub"] for user in employer)}')
        print(f'Отдел {department["title"]} со средней зарплатой {sum_department/count}')
        print(f'Отдел {department["title"]} с максимальной зарплатой {max(user["salary_rub"] for user in employer)}')


def all_salary_company():
    # Вывести среднюю зарплату по всей компании
    sum_salary = 0
    count = 0
    for department in departments:
        for employer in department["employers"]:
            sum_salary += employer["salary_rub"]
            count += 1
    print(f'Средняя зарплата по всей компании {sum_salary/count}')


def high_position():
    # Вывести названия должностей, которые получают больше 90к без повторений
    position = []
    for department in departments:
        for employer in department['employers']:
            if employer['salary_rub'] > 90000:
                position.append(employer['position'])
    unique_position = list(dict.fromkeys(position))
    for position in unique_position:
        print(f"Должность сотрудника {position}, который получает больше 90к")


def average_salary_girl():
    # Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин)
    girl = ["Michelle", "Nicole", "Christina", "Caitlin"]
    for department in departments:
        average_salary = 0
        count = 0
        for employer in department['employers']:
            if employer['first_name'] in girl:
                average_salary += employer["salary_rub"]
                count += 1
        print(f"Средняя зарплата среди девушек в {department['title']} {round(average_salary/count, 2)}")


def last_letter():
    # Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву
    name_massive = []
    letters = set("aeiouy")
    for department in departments:
        for employer in department['employers']:
            if employer["last_name"][-1] in letters:
                name_massive.append(employer["first_name"])
            else:
                continue
    result = ", ".join(set(name_massive))
    print(f"{result} - имена сотрудников, чья фамилия заканчивается на гласную букву")


if __name__ == '__main__':
    min_salary_department()
    all_salary_department()
    all_salary_company()
    high_position()
    average_salary_girl()
    last_letter()
