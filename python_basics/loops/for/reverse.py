# reverse a list in python
# The nTH value can also dictate which direction the loop will count DOWN "-1" / UP "1"
sentence = "sucoP sucoH"
refactor = ""

print("Identifying...")

for index in range(len(sentence)-1, -1, -1):
    refactor = refactor + sentence[index]

print(refactor)
