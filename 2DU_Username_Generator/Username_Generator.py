data = {
    "students": ["Adam Levine", "Monica Muller", "John Deere", "John Deere", "Adam Peichl", "Martin Novak", "Michal Kuchař", "John Deere","Adam Levine","Adam Levine"],
    "active": [True, False, True, True, True, False, True, True, True, True]
}


def CleanStudentsList(list: 'dictionary') -> 'list':
    CleanList = []
    for student in range(0, len(list["students"])):
        if list["active"][student] == True:
            CleanList.append(list["students"][student])
    return CleanList


def CreateLoginsForStudents(students_list: 'list', dictionary: 'dictionary') -> 'dictionary':
    logins = []
    for student in students_list:
        iterator_through_same_names = 2
        student_name_and_surname_array = student.split()
        temp_login = student_name_and_surname_array[1][0:5] + student_name_and_surname_array[0][0:3]
        temp_login = temp_login.lower()
        already_exists_flag = 0
        for login in logins:
            if login == temp_login:
                already_exists_flag = 1

        if already_exists_flag == 1:
            for login2 in logins:
                if temp_login == login2:
                    temp_login = temp_login[:-len(str(iterator_through_same_names))] + str(iterator_through_same_names)
                    iterator_through_same_names += 1
        logins.append(temp_login)
    dictionary['usernames'] = logins
    return dictionary


clean_list = CleanStudentsList(data)
dictionary_of_all_users = CreateLoginsForStudents(clean_list, data)
print(dictionary_of_all_users)
