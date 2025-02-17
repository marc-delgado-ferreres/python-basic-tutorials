### Control Structure ###

# What is its purpose #

# The "if", "elif", and "else" statements are used to make decisions based on a condition.
# They allow you to execute one block of code if the condition is true and another block of code if the condition is false.

# If #

# The "if" statement is used to execute a block of code if a condition is true.
# The block of code within the "if" is executed only if the condition is met. If the condition is not met, the "if" block is skipped.

if 10 > 5:
    print("Ten is greater than five")
if 3 != 4:
    print("Three is different from four")
if 7 <= 2:
    print("Seven is less than or equal to two")
if "Python" != "Cpp":
    print("Python is different from Cpp")

# In this example, we can observe four consecutive "if" statements.
# The third "if" statement is not met, so its respective block is not executed.
# The other "if" statements are met, so their blocks are executed and the respective messages are printed.
# The result will be:
# Ten is greater than five
# Three is different from four
# Python is different from Cpp

# Else #

# The "else" statement is used in conjunction with "if" to provide an alternative block of code that is executed when the "if" condition is not met.
# The block of code within the "else" is executed only if the "if" condition is not met.

age = 20

if age % 10 == 0:
    print("You have a round age")
if age < 18:
    print("You are underage")
else:
    print("You are an adult")

# In this example, we can observe three statements: two "if" statements and one "else" statement.
# The first "if" statement is met, so its block is executed and the respective message is printed.
# The second "if" statement is not met, so its block is not executed.
# The third "else" statement is activated by default, so its block is executed and the respective message is printed.
# The result will be:
# You have a round age
# You are an adult

# Elif #

# The "elif" statement is short for "else if" and is used to check multiple conditions in sequence.
# It can be used after "if" or another "elif" to provide additional blocks of code that are executed when certain conditions are met.
# Only the block of code corresponding to the first condition that is met will be executed.

temperature = 25

if temperature < 0:
    print("The temperature is very low")
elif temperature < 15:
    print("The temperature is low")
elif temperature < 30:
    print("The temperature is medium")
elif temperature < 50:
    print("The temperature is high")
else:
    print("The temperature is very high")

# In this example, we can observe five statements: one "if", three "elif", and one "else".
# The first "if" statement is not met, so its block is not executed.
# The second "elif" statement is not met, so its block is not executed.
# The third "elif" statement is met, so its block is executed and the respective message is printed.
# The fourth "elif" statement is not executed because a previous block has already been activated.
# The fifth "else" statement is not executed because a previous block has already been activated.
# The result will be:
# The temperature is medium

# Marc Delgado Ferreres