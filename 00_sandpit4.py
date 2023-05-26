import random


#  Functions go here

def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print()
            print("Please answer yes / no")


def instructions():
    print()
    print("**** How To Play ****")
    print()
    print("Choose either a number of rounds or press <enter> for infinite mode")
    print()
    print(
        "Then for each round, choose from rock / paper / scissors (or xxx to quit) You can type r / p / s / x if you don't want to type the entire word.")
    print()
    print("The rules are...")
    print()
    print("- Rock beats scissors")
    print("- Scissors beats paper")
    print("- Paper beats rock")
    print()
    print("*** Have fun ***")
    print()

    return ""


def choice_checker(question, valid_list, error):
    valid = False
    while not valid:

        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item
        # in the list (or the first letter of an item), the
        # full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item not in list
        print(error)
        print()


def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> or an integer that is more than 0\n"

        # If infinite mode not chosen, check response
        # is an integer that is more than 0
        if response != "":
            try:
                response = int(response)

                # If response is too low, go back to
                # start of loop
                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


def statement_generator(statement, decoration):
    sides = decoration * 3

    statement = " {} {} {} ".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Main routine goes here...

game_summary = []

rounds_lost = 0
rounds_drawn = 0
rounds_played = 0

statement_generator("Welcome to Rock Paper Scissors", "*")
print()

played_before = yes_no("Have you played the game before? ")
if played_before == "no":
    instructions()

print()
print("Let's get started...")
print()

rounds_played = 0
print()
choose_instruction = "Please choose rock (r), paper (p), or scissors (s)"

# List of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Start of Game Play Loop

    # Rounds Heading

    if rounds == "":
        heading = "Continuous Mode: Round {}".format(rounds_played + 1)
    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)

    print(heading)
    choose_instruction = "Please choose rock (r), paper (p), or scissors (s)"
    choose_error = "Please choose from rock / paper / scissors (or xxx too quit)"

    # Ask user for choice and check it's valid
    user_choice = choice_checker(choose_instruction, rps_list, choose_error)

    # End game if exit code is typed
    if user_choice == "xxx":
        break

    # get computer choice
    comp_choice = random.choice(rps_list[:-1])

    # compare choices
    if comp_choice == user_choice:
        result = "tie"
        rounds_drawn += 1
    elif user_choice == "rock" and comp_choice == "scissors":
        result = "won"
    elif user_choice == "paper" and comp_choice == "rock":
        result = "won"
    elif user_choice == "scissors" and comp_choice == "paper":
        result = "won"
    else:
        result = "lost"
        rounds_lost += 1

    if result == "tie":
        feedback = "It's a tie"
    else:
        feedback = "{} vs {} - you {}".format(user_choice, comp_choice, result)

    # outcome goes here, include round number and feedback
    outcome = "Round {}: {}".format(rounds_played + 1, feedback)
    game_summary.append(outcome)

    # Output results...
    print(feedback)

    rounds_played += 1

    # end game if requested # of rounds has been played
    if rounds_played == rounds:
        break

# Ask user if they want to see their game history
# If 'yes' show game history

