#This function reads the file
def file_reader():
    exercises = []
    try:
        with open("result.txt") as file:
            for line in file.readlines():
                if "=" in line:
                    expression, result = line.rstrip().split('=')
                    exercises.append([expression, result])
    except FileNotFoundError as error:
        print(f'ERROR: {error}')

    return exercises

# Add user's decision to the list
def addDecision(exercise_list):

    for i in range(len(exercise_list)):
        print(f"This is question number {i + 1}: {exercise_list[i][0]}")
        decision = float(input("Please enter the result: "))
        exercise_list[i].append(decision)
    return exercise_list

# Compare user's decision with actual result
def compare(exercise_list, counter):

    for exercise in exercise_list:
        if float(exercise[1]) == exercise[2]:
            # counter for right answers
            counter += 1
            exercise.append(True)
        else:
            exercise.append(False)
    return [exercise_list, counter]

# Print wrong answers
def printWrongAnswers(exercise_list):
    for exercise in exercise_list:
        if exercise[-1] is False:
            print(f"{exercise[0]}={exercise[1]}")

def makeChoice(exercise_list):
    # Input user's choice
    choice = input("Do you want to continue or not\n 1. Continue\n 2. Quit\n")
    while choice not in ["Continue", "1", "Quit", "2"]:
        choice = input("Do you want to continue or not\n 1. Continue\n 2. Quit\n")
    if choice in ["Continue", "1"]:
        choice = True
        # Remove items from list
        for i in range(len(exercise_list)):
            exercise_list[i] = exercise_list[i][0:2]
    else:
        choice = False
    return choice

def main():

    #Read file
    exercise_list = file_reader()
    choice = True
    while choice:
        counter = 0
        exercise_list = addDecision(exercise_list)
        [exercise_list, counter] = compare(exercise_list, counter)

        #Print number of right answers and wrong answers
        print(f"The number of right answers is {counter}\nThe wrong answers are:")
        printWrongAnswers(exercise_list)

        choice = makeChoice(exercise_list)

if __name__ == '__main__':
    main()

