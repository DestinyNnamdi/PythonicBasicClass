"""
your first assignment on conditional statements 
analogy: Microsoft has contracted several companies in nigeria to give jobs to several quolified candidates, and SLNCOnline is in charge of those living with disability because their case is special. But there is a problem.
SLNCOnline do not have the developers to write the code that checks for what microsoft ask them to, and so you are contacted as a python developer that you are. because of some peculiarities, some certain things will be ignored.
For example: the usual age limit is between 18 to 35, but in this case, it's between 18 to 50.
So, your code must meet the following:
tcollect their user-names and age.
if the persons age is less than 18, tell them to try when their of age.
if the age is within 18 to 50, congradulate them! But also, if the age is within 36 to 50, still congradulate them and add that they are lucky! If not because of their disability, they are already grater than 35 which is greater than the job age limit by Microsoft.
and finally, if the age is greater than 50, tell them they are too old for the job by Microsoft.
"""
# write your name at the end of this line, not below it: Destiny Nnamdi

# start writing your code below this line: Good luck!
Name=input("What is your name?")
age = int(input("What is your age? "))
age = 50
if age < 18:
    print("Try when you're of age.")
if age >= 18:
    print("Congratulations! You qualify.")
if age>=36:
    print("Congratulations! You are lucky! Though you're above Microsoft's usual employment age limit, your disability qualifies you for this momentous project.")
if age > 50:
     print("Microsoft considers you too old for this job.")

