# python is dynamically typed language
# in python, we dont need to mention the datatype of the variable

my_income = 100000
my_taxrate = 0.15

my_tax_deduction = my_income * my_taxrate
my_net_income = my_income - my_tax_deduction

print(my_tax_deduction)
print(my_net_income)

print(type(my_tax_deduction))  # float
print(type(my_income))  # int
