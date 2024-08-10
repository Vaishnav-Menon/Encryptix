import random

users_score = 0;
computers_score = 0;

def repeat():
    def computers_choice():
        computers_choice = random.choice([1, 2, 3]);
        computers_choice = str(computers_choice);
        return computers_choice;

    def result(users_choice, computers_choice):
        global users_score;
        global computers_score;

        if (users_choice == computers_choice):
            print("It's a Tie!\n");
            print("Your score: ", users_score);
            print("Computer's score: ", computers_score);
        elif (users_choice == '1' and computers_choice == '3') or \
                (users_choice == '2' and computers_choice == '1') or \
                (users_choice == '3' and computers_choice == '2'):
            print("You win!\n");
            users_score += 1;
            print("Your score: ", users_score);
            print("Computer's score: ", computers_score);
        else:
            print("Computer wins!\n");
            computers_score += 1;
            print("Your score: ", users_score);
            print("Computer's score: ", computers_score);

    print("\nEnter your choice:\n1. Rock\n2. Paper\n3. Scissor");
    users_choice = str(input());

    if (users_choice == '1'):
        print("\nYour choice: Rock");
    elif (users_choice == '2'):
        print("\nYour choice: Paper");
    elif (users_choice == '3'):
        print("\nYour choice: Scissor");

    computers_choice = computers_choice();

    if (computers_choice == '1'):
        print("Computer's choice: Rock\n");
    elif (computers_choice == '2'):
        print("Computer's choice: Paper\n");
    elif (computers_choice == '3'):
        print("Computer's choice: Scissor\n");

    result(users_choice, computers_choice);

    print("\nDo you want to play again?\n1. Yes\n2. No");
    choice = str(input());
    if (choice == '1'):
        repeat();

    else:
        print("\nThanks for playing!\n");
        print("Your Final Score: ", users_score);
        print("Computer's Final Score: ", computers_score);
        if (users_score == computers_score):
            print("It's a Tie!\n");
        elif (users_score > computers_score):
            print("\nYou are the final Winner!\n");
        else:
            print("\nComputer is the final Winner!\n");

repeat();

