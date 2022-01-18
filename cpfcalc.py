#age integer checker
def getAge(age):
  while True:
    try:
       ageInput = int(input(age))
    except ValueError:
       print("Please enter a valid integer.")
       continue
    else:
       return ageInput
       break

#salary integer checker
def getSalary(salary):
  while True:
    try:
       salInput = int(input(salary))
    except ValueError:
       print("Please enter a valid integer.")
       continue
    else:
       return salInput
       break

age = getAge("Enter your age: ")
salary = getSalary("Enter your salary: $")

#assigns youCPF and employerCPF based on age
#youCPF is how much you contribute to your CPF
#employerCPF is how much employer contributes to your CPF

if age <= 55:
    youCPF = 0.2
    employerCPF = 0.17
elif age <= 60:
        youCPF = 0.13
        employerCPF = 0.13
elif age <= 65:
        youCPF = 0.075
        employerCPF = 0.09
elif age > 65:
        youCPF = 0.05
        employerCPF = 0.075

#age in ranges
range1 = [36, 37, 38, 39, 40, 41, 41, 43, 44, 45]
range2 = [46, 47, 48, 49, 50]
range3 = [51, 52, 53, 54, 55]
range4 = [56, 57, 58, 59, 60]
range5 = [61, 62, 63, 64, 65]
# >65 OA 1%, SA 1%, Medisave 10.5% of total salary

if age in range1:
    oa = 0.21
    sa = 0.07
    ms = 0.09
if age in range2:
    oa = 0.19
    sa = 0.08
    ms = 0.10
if age in range3:
    oa = 0.15
    sa = 0.115
    ms = 0.105
if age in range4:
    oa = 0.12
    sa = 0.035
    ms = 0.105
if age in range5:
    oa = 0.035
    sa = 0.025
    ms = 0.105
if age > 65:
    oa = 0.01
    sa = 0.01
    ms = 0.105
if age <= 35:
    oa = 0.23
    sa = 0.06
    ms = 0.08

youC = youCPF * salary
employerC = employerCPF * salary

#printings
print(f"Your monthly CPF Contribution is ${youC:.2f}",sep='')
print(f"Your employer will contribute ${employerC:.2f}",sep='')
totalC = youC + employerC

#calculate oa, sa, Medisave
x = oa * salary
y = sa * salary
z = ms * salary

print(f"Total CPF contribution is ${totalC:.2f}",sep='')

print(f"${x:.2f} will be credited into your Ordinary Account.",sep='')
print(f"${y:.2f} will be credited into your Special Account.",sep='')
print(f"${z:.2f} will be credited into your Medisave.",sep='')

dollar = 1
#total deduction from salary
deduct = dollar + youC
ths = salary - deduct
print(f"Your nett(take-home) salary is ${ths:.2f} with your $1 contribution deducted.",sep='')

input("Press Enter to exit...")
