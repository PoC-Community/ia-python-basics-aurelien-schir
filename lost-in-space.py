# There's still some trace of corruptions..
# Apparently they seems to be called commentaries...

def robotProgram():
    max_value = 15
    goal = 15
    victory = "Success !"
    retry = "Not yet"

    for i in range(0, max_value + 1):
        if i == goal:
            return victory
        print(i, retry)

# Testing
assert(robotProgram() == 'Success !'), "File is still corrupted"
print("The file isn't corrupted anymore, good job !")
