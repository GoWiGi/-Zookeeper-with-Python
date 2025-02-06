# Read the user's age
age = int(input())

# Check the age and print the corresponding category
# TODO: Write your if statement here
if age <= 18:
    result = "Minor"
elif 18 <= age <= 64:
    result = "Adult"
elif age > 65:
    result = "Senior"

print(result)
