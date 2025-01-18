import pygame
import sys
import random
import os
import pickle

# Initialize Pygame
pygame.init()

# Set up display, fonts, colors, and time
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Minute Math")
font = pygame.font.SysFont('Arial', 30)
WHITE = (255, 255, 255)
TEAL = (0, 115, 90)

# Function to welcome player
def welcome():
    messages = ["Welcome to Minute Math!", "How quickly can you correctly answer 5 questions?"]
    # Calculate the total height of the text to center it vertically (with extra space between the lines)
    total_height = len(messages) * font.get_height() + 50
    start_y = (screen_height - total_height) // 2
    # Loop to display both messages
    screen.fill(WHITE)
    # Render and display each message
    for i, message in enumerate(messages):
        text = font.render(message, True, TEAL)
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, start_y + i * (font.get_height() + 20)))
    # Display instructions at the bottom
    continue_text = font.render("Press ENTER to continue", True, TEAL)
    screen.blit(continue_text, (screen_width // 2 - continue_text.get_width() // 2, screen_height - 80))
    pygame.display.flip()
    # Wait for the player to press ENTER
    waiting_for_enter = True
    while waiting_for_enter:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting_for_enter = False

# Function for player to pick name
def pick_name():
    input_text = ""
    is_inputting = True
    while is_inputting:
        for event in pygame.event.get():
            # See if player wants to quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # See if player is pressing a key
            if event.type == pygame.KEYDOWN:
                # If player presses ENTER to finalize input...
                if event.key == pygame.K_RETURN:
                    # Check if there is an input
                    if input_text:
                        # Check if input is valid
                        if len(input_text.strip()) == 3:
                            return input_text.strip()
                # If player presses BACKSPACE to delete the last character...
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                # If the player presses some other key...
                else:
                    # Add the number to the input string
                    input_text += event.unicode
        # Clear the screen
        screen.fill(WHITE)
        # Display the current input text
        input_display = font.render(f"Enter 3 characters for your name: {input_text}", True, TEAL)
        screen.blit(input_display, (screen_width // 2 - input_display.get_width() // 2, screen_height // 2))
        # Display instructions at the bottom
        continue_text = font.render("Press ENTER once you have a valid option", True, TEAL)
        screen.blit(continue_text, (screen_width // 2 - continue_text.get_width() // 2, screen_height - 80))
        pygame.display.flip()

# Function for player to pick an operation
def pick_operation():
    operations = ["+", "-", "*", "/", "%"]
    input_text = ""
    is_inputting = True
    while is_inputting:
        for event in pygame.event.get():
            # See if player wants to quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # See if player is pressing a key
            if event.type == pygame.KEYDOWN:
                # If player presses ENTER to finalize input...
                if event.key == pygame.K_RETURN:
                    # Check if there is an input
                    if input_text:
                        # Check if input is valid
                        if input_text.strip() in operations:
                            return input_text.strip()
                # If player presses BACKSPACE to delete the last character...
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                # If the player presses some other key...
                else:
                    # Add the number to the input string
                    input_text += event.unicode
        # Clear the screen
        screen.fill(WHITE)
        # Display the current input text
        input_display = font.render(f"Pick an operation [+, -, *, /, or %]: {input_text}", True, TEAL)
        screen.blit(input_display, (screen_width // 2 - input_display.get_width() // 2, screen_height // 2))
        # Display instructions at the bottom
        continue_text = font.render("Press ENTER once you have a valid option", True, TEAL)
        screen.blit(continue_text, (screen_width // 2 - continue_text.get_width() // 2, screen_height - 80))
        pygame.display.flip()

# Function for player to pick a difficulty
def pick_difficulty():
    difficulties = ["easy", "medium", "hard"]
    input_text = ""
    is_inputting = True
    while is_inputting:
        for event in pygame.event.get():
            # See if player wants to quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # See if player is pressing a key
            if event.type == pygame.KEYDOWN:
                # If player presses ENTER to finalize input...
                if event.key == pygame.K_RETURN:
                    # Check if there is an input
                    if input_text:
                        # Check if input is valid
                        if input_text.strip().lower() in difficulties:
                            return input_text.strip().lower()
                # If player presses BACKSPACE to delete the last character...
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                # If the player presses some other key...
                else:
                    # Add the number to the input string
                    input_text += event.unicode
        # Clear the screen
        screen.fill(WHITE)
        # Display the current input text
        input_display = font.render(f"Pick a difficulty [easy, medium, or hard]: {input_text}", True, TEAL)
        screen.blit(input_display, (screen_width // 2 - input_display.get_width() // 2, screen_height // 2))
        # Display instructions at the bottom
        continue_text = font.render("Press ENTER once you have a valid option", True, TEAL)
        screen.blit(continue_text, (screen_width // 2 - continue_text.get_width() // 2, screen_height - 80))
        pygame.display.flip()

# Function to display a countdown before the game
def countdown():
    words = ["Ready...", "Set...", "Go!"]
    display_time = 1000
    # Loop through each word and display it
    for word in words:
        word_start = pygame.time.get_ticks()
        while pygame.time.get_ticks() - word_start < display_time:
            # See if player wants to quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # Clear the screen and display the current word
            screen.fill(WHITE)
            text = font.render(word, True, TEAL)
            screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2))
            pygame.display.flip()
    # Clear the screen
    screen.fill(WHITE)
    pygame.display.flip()

# Function to display a problem and return player input
def problem(operation, difficulty):
    input_text = ""
    is_inputting = True
    # Generate the problem based on operation and difficulty
    if difficulty == "easy":
        b = 12
    elif difficulty == "medium":
        b = 30
    elif difficulty == "hard":
        b = 100
    if operation == "+":
        num1 = random.randint(1, b)
        num2 = random.randint(1, b)
        solution = num1 + num2
    elif operation == "-":
        num2 = random.randint(1, b)
        num3 = random.randint(1, b)
        num1 = num2 + num3
        solution = num3
    elif operation == "*":
        num1 = random.randint(1, b)
        num2 = random.randint(1, b)
        solution = num1 * num2
    elif operation == "/":
        num2 = random.randint(1, b)
        num3 = random.randint(1, b)
        num1 = num2 * num3
        solution = num3
    elif operation == "%":
        num3 = random.randint(1, b)
        num2 = random.randint(1, b)
        num4 = num3 * num2
        num5 = random.randint(1, num2)
        num1 = num4 + num5
        solution = num1 % num2
    while is_inputting:
        for event in pygame.event.get():
            # See if player wants to quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # See if player is pressing a key
            if event.type == pygame.KEYDOWN:
                # If player presses ENTER to finalize input...
                if event.key == pygame.K_RETURN:
                    # Check if there is an input
                    if input_text:
                        # Convert it to a number
                        input_num = int(input_text)
                        # Check if it is correct
                        if input_num == solution:
                            accuracy = "correct"
                        else:
                            accuracy = "incorrect"
                        return num1, num2, solution, input_num, accuracy
                # If player presses BACKSPACE to delete the last digit...
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                # If the player presses a number...
                elif event.key >= pygame.K_0 and event.key <= pygame.K_9:
                    # Add the number to the input string
                    input_text += event.unicode  
        # Clear the screen
        screen.fill(WHITE)
        # Display the current input text
        input_display = font.render(f"{num1} {operation} {num2} = {input_text}", True, TEAL)
        screen.blit(input_display, (screen_width // 2 - input_display.get_width() // 2, screen_height // 2))
        pygame.display.flip()

# Function to display individual results
def results(name, operation, difficulty, incorrect, time, score):
    screen.fill(WHITE)
    lines = [
        f"Name: {name}",
        f"Operation: {operation}",
        f"Difficulty: {difficulty}",
        f"Total incorrect: {incorrect}",
        f"Total time: {time:.2f} seconds",
        f"Score: {score:.2f} points"
    ]
    # Calculate the total height of the text to center it vertically (with extra space between lines)
    total_height = len(lines) * font.get_height() + 50
    start_y = (screen_height - total_height) // 2
    # Render and display each line
    for i, line in enumerate(lines):
        text = font.render(line, True, TEAL)
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, start_y + i * (font.get_height() + 10)))
    # Display instructions at the bottom
    continue_text = font.render("Press ENTER to continue", True, TEAL)
    screen.blit(continue_text, (screen_width // 2 - continue_text.get_width() // 2, screen_height - 80))
    pygame.display.flip()
    # Wait for the player to press ENTER
    waiting_for_enter = True
    while waiting_for_enter:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting_for_enter = False

# Function to display leaderboard
def leaderboard(name, score):
    # Loop to ensure pickle file exists before proceeding
    path = './data_pick.pkl'
    check_file = os.path.isfile(path)
    if not check_file:
        # Initialize a dictionary and store the file
        dictionary = {}
        with open("data_pick.pkl", "wb") as pickle_file:
            pickle.dump(dictionary, pickle_file)
    # Retrieve the current file
    with open("data_pick.pkl", "rb") as pickle_file:
        dictionary = pickle.load(pickle_file)
    # Update dictionary with name and score
    dictionary.update({name: score})
    # Store updated file for future use
    with open("data_pick.pkl", "wb") as pickle_file:
        pickle.dump(dictionary, pickle_file)
    # Create a sorted dictionary in ascending order of score
    sort = sorted(dictionary.items(), key=lambda x: x[1])
    sort_dictionary = dict(sort)
    # Clear the screen
    screen.fill(WHITE)
    # Display the leaderboard
    text = ["Leaderboard:"]
    n = 0
    for key, value in sort_dictionary.items():
        text.append(f"{key}: {value} points")
        n += 1
        if n == 5:
            break
    # Calculate the total height of the leaderboard text block to center it vertically (with extra space between lines)
    total_height = len(text) * font.get_height() + 50
    start_y = (screen_height - total_height) // 2
    # Render and display each line
    for i, line in enumerate(text):
        text = font.render(line, True, TEAL)
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, start_y + i * (font.get_height() + 10)))
    # Display instructions at the bottom
    continue_text = font.render("Press ENTER to quit", True, TEAL)
    screen.blit(continue_text, (screen_width // 2 - continue_text.get_width() // 2, screen_height - 80))
    pygame.display.flip()
    # Wait for the player to press ENTER
    waiting_for_enter = True
    while waiting_for_enter:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting_for_enter = False

def main():
    # Call functions before the game loop
    welcome()
    name = pick_name().upper()
    operation = pick_operation()
    difficulty = pick_difficulty()
    countdown()
    # Start the game loop
    start_time = pygame.time.get_ticks()
    incorrect = 0
    correct = 0
    while correct < 5:
        # Call problem() to print a problem and return player input
        num1, num2, solution, input_num, accuracy = problem(operation, difficulty)
        # Calculate elapsed time after the player answers the problem
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - start_time
        # Process the result and track score
        if accuracy == "correct":
            print(f"{num1} {operation} {num2} = {input_num}. Correct.")
            correct += 1
        else:
            print(f"{num1} {operation} {num2} = {input_num}. Incorrect, it should be {solution}.")
            incorrect += 1
    time = elapsed_time / 1000
    score = time + incorrect
    # Call functions after the game loop
    results(name, operation, difficulty, incorrect, time, score)
    leaderboard(name, score)

if __name__ == "__main__":
    main()