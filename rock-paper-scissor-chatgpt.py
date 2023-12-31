import random

def get_user_choice():
    """
    Prompt the user to input their choice and return the user's choice.

    Returns:
    str: The user's choice ("rock", "paper", or "scissor").
    """
    return input('\nSelect your choice "rock", "paper" or "scissor": ')

def get_pc_choice(choices):
    """
    Randomly select the computer's choice from the given list of choices.

    Args:
    choices (list): List of possible choices.

    Returns:
    str: The computer's choice.
    """
    return random.choice(choices)

def determine_winner(player, pc):
    """
    Determine the winner of the game based on the choices of the player and the computer.

    Args:
    player (str): The player's choice.
    pc (str): The computer's choice.

    Returns:
    str: The result of the game ("Draw!", "You won! 👍", or "You lose! 👎").
    """
    if player == pc:
        return 'Draw!'
    elif (player == "rock" and pc == "scissor") or (player == "scissor" and pc == "paper") or (player == "paper" and pc == "rock"):
        return 'You won! 👍'
    else:
        return 'You lose! 👎'

def main():
    """
    The main function that orchestrates the Rock, Paper, Scissors game.
    """
    choices = ['rock', 'paper', 'scissor']
    
    # Get user's choice
    player = get_user_choice()
    
    # Get computer's choice
    pc = get_pc_choice(choices)
    
    # Display choices
    print(f'\nYour choice is "{player}", and the PC choice is: "{pc}"')
    
    # Determine the winner and display the result
    result = determine_winner(player, pc)
    print(f'\n{result}\n')

if __name__ == "__main__":
    # Run the game when the script is executed
    main()
