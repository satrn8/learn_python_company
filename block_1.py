from company import departments


def all_departments():
    # Вывести названия всех отделов
    for department in departments:
        print(f"Название отдела - {department['title']}")


def all_employers():
    # Вывести имена всех сотрудников компании
    name_massive = []
    for department in departments:
        for employer in department['employers']:
            name_massive.append(employer['first_name'])
    result = ", ".join(name_massive)
    print(f"Сотрудники компании: {result}")


def all_employers_departments():
    # Вывести имена всех сотрудников компании с указанием отдела, в котором они работают
    for department in departments:
        for employer in department['employers']:
            print(f"Cотрудник {employer['first_name']} работает работает в отделе {department['title']}")


def all_employers_max_salary():
    # Вывести имена всех сотрудников компании, которые получают больше 100к
    for department in departments:
        for employer in department['employers']:
            if employer['salary_rub'] > 100000:
                print(f"Сотрудник {employer['first_name']}, который получает больше 100к - {employer['salary_rub']}")


def all_employers_min_salary():
    # Вывести позиции, на которых люди получают меньше 80к (можно с повторениями)
    for department in departments:
        for employer in department['employers']:
            if employer['salary_rub'] < 80000:
                print(f"Позиция сотрудника {employer['position']}, который получает меньше 80к - {employer['salary_rub']}")


def sum_every_departments():
    # Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела
    for department in departments:
        sum_department = 0
        for employer in department["employers"]:
            sum_department += employer["salary_rub"]
        print(f"В месяц на отдел {department['title']} уходит {sum_department}")


if __name__ == '__main__':
    all_departments()
    all_employers()
    all_employers_departments()
    all_employers_max_salary()
    all_employers_min_salary()
    sum_every_departments()