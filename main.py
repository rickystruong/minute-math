from re import M
import random
import time
import pickle
import os.path

# Generate and print a problem and return its solution
def problem(operation, difficulty):
    # Generate numbers based on difficulty
    if difficulty == "easy":
        myNum1 = random.randint(1, 12)
        myNum2 = random.randint(1, 12)
    elif difficulty == "medium":
        myNum1 = random.randint(1, 50)
        myNum2 = random.randint(1, 50)
    elif difficulty == "hard":
        myNum1 = random.randint(1, 100)
        myNum2 = random.randint(1, 100)
    # Generate, print, and solve problems based on operation
    if operation == "+":
        myNum3 = myNum1 + myNum2
        mySolution = myNum3
        print(f"\nProblem: {myNum1} {operation} {myNum2}")
    elif operation == "-":
        myNum3 = myNum1 + myNum2
        mySolution = myNum1
        print(f"\nProblem: {myNum3} {operation} {myNum2}")
    elif operation == "*":
        myNum3 = myNum1 * myNum2
        mySolution = myNum3
        print(f"\nProblem: {myNum1} {operation} {myNum2}")
    elif operation == "/":
        myNum3 = myNum1 * myNum2
        mySolution = myNum1
        print(f"\nProblem: {myNum3} {operation} {myNum2}")
    elif operation == "%":
        myNum3 = myNum1 * myNum2
        myNum4 = random.randint(1, myNum2)
        myNum5 = myNum3 + myNum4
        mySolution = myNum5 % myNum2   
        print(f"\nProblem: {myNum5} {operation} {myNum2}")
    return mySolution

# Update and print leaderboard
def leaderboard(name, time): 
    # Loop to ensure pickle file exists before proceeding
    while True:
        # Each run, see if pickle file exists
        path = './data_pick.pkl'
        check_file = os.path.isfile(path)
        # If pickle file does exist
        if check_file:
            # Proceed with code
            break
        # If pickle file doesn't exist
        else:
            # Initialize a dictionary, store the file, and loop again
            dictionary = {}
            with open("data_pick.pkl", "wb") as pickle_file:
                pickle.dump(dictionary, pickle_file)
    # Retrive current file
    with open("data_pick.pkl", "rb") as pickle_file:
        dictionary = pickle.load(pickle_file)
    # Update dictionary with name and time
    dictionary.update({name: time}) 
    # Store updated file for future use
    with open("data_pick.pkl", "wb") as pickle_file:
        pickle.dump(dictionary, pickle_file)
    # Create a sorted dictionary in ascending order of time
    sort = sorted(dictionary.items(), key = lambda x:x[1])
    sort_dictionary = dict(sort)
    # Print top 5 times as leaderboard
    print("\nLeaderboard: \n")
    n = 0
    for key in sort_dictionary.keys():
        print(f"{key}: {sort_dictionary[key]} seconds")
        n += 1
        if n == 5:
            break

# Print results of a game
def result(name, operation, difficulty, start, end, correct, wrong):
    # Calculate variables of interest
    total = correct + wrong
    accuracy = round(((correct / total) * 100), 2)
    time = round(end - start, 2)
    # Convert operation to word
    if operation == "+":
        word = "addition"
    elif operation == "-":
        word = "subtraction"
    elif operation == "*":
        word = "multiplication"
    elif operation == "/":
        word = "division"
    elif operation == "%":
        word = "modulo"
    # Print results
    print(f"\nResults for {name}:")
    print(f"\nOperation: {word} \nDifficulty: {difficulty}")
    print(f"Time: {time} seconds \nAccuracy: {accuracy}%")
    # Call leaderboard() to print leaderboard
    leaderboard(name, time)

# Main method
def main():
    print("Welcome to Minute Math! How quickly can you answer 5 questions?\n")
    # Grab a name from the player
    while True:
        name = input("Please enter 3 letters for your name: ").upper()
        # If input is valid, break from loop to proceed with game
        if len(name) == 3:
            break
        # If not, loop will keep going
        print("Name is invalid. Try again...\n")
    # Grab an operation from the player
    operations = ["+", "-", "*", "/", "%"]
    print() # Print an empty line
    while True:
        myOperation = input("Pick an operation [+, -, *, /, or %]: ")
        # If input is valid, break from loop to proceed with game
        if myOperation in operations:
            break
        # If not, loop will keep going
        print("Operation is invald. Try again...\n")
    # Grab a difficulty from the player
    difficulties = ["easy", "medium", "hard"]
    print() # Print an empty line
    while True:
        myDifficulty = input("Pick a difficulty [easy, medium, or hard]: ").casefold()
        # If input is valid, break from loop to proceed with game
        if myDifficulty in difficulties:
            break
        # If not, loop will keep going
        print("Difficulty is invald. Try again...\n")
    # Intialize variables and start timer
    correct = 0
    wrong = 0
    start = time.time()
    # Game loop (5 problems)
    while correct < 5:
        # Call problem() to generate and print a problem and return its solution
        mySolution = problem(myOperation, myDifficulty)
        # Grab an answer from the player
        while True:
            try:
                player_input = int(input('Answer: '))
                # If correct, break from loop
                if player_input == mySolution:
                    print("That's right!")
                    break
                # If not, loop keeps going
                else:
                    print("That's not right. Try again...")
                    wrong += 1
            # If answer is garbage, loop keeps going
            except ValueError:
                print('Answer must be an integer. Try again...')
        # If correct and loop was broken, add one to correct
        correct += 1
    # End game and call result() to print results
    end = time.time()
    result(name, myOperation, myDifficulty, start, end, correct, wrong)

if __name__ == '__main__':
    main()
