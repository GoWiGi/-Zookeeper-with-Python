# You can get the input number as follows
from xml.dom.minidom import ProcessingInstruction

input_number = int(input())

# Write your if statement for number range here
if 10 <= input_number <= 20:
    result = "Inside the range"
else:
    result = "Outside the range"

print(result)

# Based on the result of your if statement, print the appropriate message