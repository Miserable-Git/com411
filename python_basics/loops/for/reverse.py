# reverse a list in python
# The nTH value can also dictate which direction the loop will count DOWN "-1" / UP "1"
sentence = "sucoP sucoH"

print("Identifying...")

for index in range(len(sentence)-1, -1, -1):
    print(sentence[index])
