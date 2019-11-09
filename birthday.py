year = input("Enter Birth Year : ")
month = input("Enter Birth Month : ")
date = input("Enter Birth date : ")

def sum_digit(n):
    num_str = str(n)
    sum = 0
    for i in range(0, len(num_str)):
        sum += int(num_str[i])
    return sum


luky_number = sum_digit(year) + sum_digit(month) + sum_digit(date)

print("Your Lucky Number is : " + str(luky_number))
