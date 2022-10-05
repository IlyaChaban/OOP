data = {
    "students":["Adam Levine", "Monica Muller", "John Deere", "John Deere", "John Deere", "John Deere", "John Deere", "John Deere", "John Deere", "John Deere", "John Deere", "John Deere", "John Deere", "John Deere"],
    "active":[True, False, True, True, True, True, True, True, True, True, True, True, True, True]
}



def CleanStudentsList(list:'dictionary') -> 'list':
    CleanList=[]
    for student in range(0,len(list["students"])):
        if list["active"][student] == True:
            CleanList.append(list["students"][student])
    return CleanList
    
def CreateLoginsForStudents(students_list:'list') -> 'list':
    logins = []
    for student in students_list:
        iterator_through_same_names=2
        student_name_and_surname_array = student.split()
        temp_login = student_name_and_surname_array[1][0:5] + student_name_and_surname_array[0][0:3]
        temp_login=temp_login.lower()
        already_exists_flag=0
        for login in logins:
            if login == temp_login:
                already_exists_flag=1
                
        if already_exists_flag==1:
            for login2 in logins:
                
                temp_login=temp_login[:-len(str(iterator_through_same_names))]+str(iterator_through_same_names)
                iterator_through_same_names+=1
        logins.append(temp_login)    
    return logins

clean_list=CleanStudentsList(data) 
students_login_list=CreateLoginsForStudents(clean_list)

print(students_login_list)