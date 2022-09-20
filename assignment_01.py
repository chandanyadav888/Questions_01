#1 ask a num with user and filter odd and add into the odd list
 
odd = []

def filter_odd(user_provider_num):
    for num in range(1, user_provider_num+1):
        if (num % 2 != 0):
            odd.append(num)

any_num = int(input("please provide any number:-->:"))
filter_odd(any_num)

print("odd_list:",odd)

#2 ask a num with user and filter even and add into the even list

even = []

def filter_even(user_provider_num):
    for num in range(1, user_provider_num+1):
        if (num % 2 == 0):
            even.append(num)

any_num = int(input("please enter any number:-->:"))
filter_even(any_num)
print("even_list:",even)      

 #3 ask a age with user and check he/she is elegible for vote(must be greater than 19) or not.

age = int(input("please enter your age:"))
if age>19:
   print(f"you are eligible for voting, you are {age} that is the required age for voting")

else:
    print(f"you are just a child finish your primary education first")

 #4 application of loop into the weeks of day:

week_days_list = [
    "sunday",
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday", ]

counter = 0
for day in week_days_list:
    counter += 1
    print(f" day {counter} is: -->{day}")

 #5 ask a first_name and second_name from user return its full name as:

first_name = input("please enter your first_name:")
second_name = input("please enter your second_name:")

print(f"oh! so, your fullname is: {first_name} {second_name}")

# another method

first_name, second_name = input("please enter your first_name,second_name:").split(",")

# def user_fullname( first, second): ( is it necessary to prove this def ??)
#     return f" {first} {second}"

print(f"oh! so, your fullname is: {first_name} {second_name}" )


