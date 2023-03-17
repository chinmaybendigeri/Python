
# write a function that returns true if a list contains any even number

def check_even_list(num_list):
    for num in num_list:
        if num % 2 == 0:
            return True
        else:
            pass
    return False

print(check_even_list([1,2,5]))
print(check_even_list([1,3,5]))

# write a function that returns new list of even numbers from a list

def even_numbers_list(num_list):
    even_nums_list = []
    for num in num_list:
        if num % 2 == 0:
            even_nums_list.append(num)
        else:
            pass
    return even_nums_list

print(even_numbers_list([1,2,3,4,5]))
print(even_numbers_list([1,3,5]))

# create a function that returns tuple of employee name and his/her work hours from
# list of tuples( employees and their work hours)

def check_employee_of_month(employee_list):
    current_max = 0
    employee_of_month = ''

    for employee,hours in employee_list:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee

    return (employee_of_month,current_max)

emp_work_list = [('Chinmay',100),('Vivek',400),('Jeeva',800)]
print(check_employee_of_month(emp_work_list))

e,h = check_employee_of_month(emp_work_list)
print(e)
print(h)


