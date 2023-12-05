from company import departments, taxes


def get_tax(title_department):
    # получаю процент налога по отделам
    default_tax = 0
    for tax in taxes:
        if tax["department"] == None:
            default_tax = tax["value_percents"]
        if str(tax["department"]).lower() == str(title_department).lower():
            return tax["value_percents"]
    return default_tax


def average_tax():
    # Вывести список отделов со средним налогом на сотрудников этого отдела
    for department in departments:
        title = (department['title'])
        tax = get_tax(title)
        all_average_department = 0
        count = 0
        for employer in department['employers']:
            employer_tax = round((employer["salary_rub"] * tax) / (100 - tax))
            all_average_department += employer_tax
            count += 1
        print(f"Отдел {title} со средним налогом {all_average_department/count} на сотрудников")


def salary_all_employer():
    # Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов
    for department in departments:
        title = (department['title'])
        tax = get_tax(title)
        for employer in department['employers']:
            employer_tax = round((employer["salary_rub"] * tax) / (100 - tax))
            all_salary = employer["salary_rub"] + employer_tax
            print(f"{employer['first_name']} получает зарплату {employer['salary_rub']}, зарплата с учетом налога {all_salary}")


def max_tax():
    # Вывести всех сотрудников, за которых компания платит больше 100к налогов в год
    find_max_tax_employer = False
    for department in departments:
        title = (department['title'])
        tax = get_tax(title)
        for employer in department['employers']:
            employer_tax = round((employer["salary_rub"] * tax) / (100 - tax))
            employer_massive = {
                "first_name": employer["first_name"],
                "last_name": employer["last_name"],
                "tax": employer_tax
            }

            if employer_massive["tax"] > 100000:
                find_max_tax_employer = True
                print(f"За {employer_massive['first_name']} {employer_massive['last_name']} компания платит меньше всех налога {employer_massive['tax']}")
    if not find_max_tax_employer:
        print("Нет таких сотрудников")


def min_tax():
    # Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов
    min_salary = []
    for department in departments:
        title = (department['title'])
        tax = get_tax(title)
        for employer in department['employers']:
            employer_tax = round((employer["salary_rub"] * tax) / (100 - tax))
            employer_massive = {
                "first_name": employer["first_name"],
                "last_name": employer["last_name"],
                "tax": employer_tax
            }
            min_salary.append(employer_massive)
    min_tax_employer = min(user["tax"] for user in min_salary)
    for name in min_salary:
        for i in name.values():
            if i == min_tax_employer:
                print(f"{name['first_name']} {name['last_name']} платит меньше все налога {min_tax_employer}")
            else:
                continue


if __name__ == '__main__':
    average_tax()
    salary_all_employer()
    max_tax()
    min_tax()