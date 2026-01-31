import random
import os.path
import json
random.seed()

def draw_board(board):
    
    for row in board:
        print("|".join(cell if cell else " " for cell in row))
        print("-" * 5)

        
    pass

def welcome(board):
   
    print("Hello...Welcome to Noughts and Crosses Game!")
    draw_board(board)
    pass

def initialise_board(board):
   
    board = [[" " for _ in range(3)] for _ in range(3)]
    return board

def get_player_move(board):
    
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            
            if move < 0 or move >= 9:
                print("Invalid input. Please enter a number between 1 and 9.")
                continue
            
            row, col = divmod(move, 3)
            if board[row][col] != " ":
                print("Cell already occupied. Try again.")
                continue
            
            return row, col
        except ValueError:
            print("Invalid number. Please enter a valid number.")

    return row, col

def choose_computer_move(board):
    
    
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "O"
                
                if check_for_win(board, "O"):  
                    return row, col
                
                board[row][col] = " " 

   
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "X"
                
                if check_for_win(board, "X"): 
                    board[row][col] = "O"  
                    return row, col
                
                board[row][col] = " "  

  
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    
    return random.choice(empty_cells) if empty_cells else (None, None)

    return row, col
    

def check_for_win(board, mark):
    
    for i in range(3):
        if all(board[i][j] == mark for j in range(3)):  
            return True
        if all(board[j][i] == mark for j in range(3)): 
            return True
        
    if all(board[i][i] == mark for i in range(3)) or all(board[i][2 - i] == mark for i in range(3)):
        return True
    
    return False

def check_for_draw(board):
    
    return all(cell != " " for row in board for cell in row)
    return True

def play_game(board):
    
    board = initialise_board(board)
    welcome(board)

    while True:
        
        print("Your turn (X):")
        
        row, col = get_player_move(board)
        board[row][col] = "X"
        
        draw_board(board)

        if check_for_win(board, "X"):
            print("Congratulations! You win!")
            return 1

        if check_for_draw(board):
            print("It's a draw!")
            return 0

       
        print("Computer's turn (O):")
        row, col = choose_computer_move(board)

        
        if row is not None and col is not None:
            board[row][col] = "O"
        draw_board(board)

        if check_for_win(board, "O"):
            print("Sorry, the computer wins!")
            return -1

        if check_for_draw(board):
            print("It's a draw!")
            return 0

    return 0

def menu():
   
    while True:
        print("1. Play Game")
        print("2. Save Score")
        print("3. Load and Display Scores")
        print("q. Quit")
        
        choice = input("Please Enter your choice: ").strip().lower() 
        
        if choice in ["1", "2", "3", "q"]:
            return choice
        else:
            print("Invalid choice. Please enter '1', '2', '3', or 'q'.")
    return choice


def load_scores():
    
    try:
        with open("leaderboard.txt", "r") as file:
            return json.load(file)
        
    except (FileNotFoundError, json.JSONDecodeError):
        print("Leaderboard file not found or empty. Returning an empty leaderboard.")
        return {}

    
    return leaders

def save_score(score):
   
    name = input("Please Enter your name: ")
    scores = load_scores()
    
    scores[name] = scores.get(name, 0) + score
    with open("leaderboard.txt", "w") as file:
        json.dump(scores, file)
    print("Score saved successfully.")

    return

def display_leaderboard(leaders):
    
    print("Leaderboard:")
    
    for name, score in sorted(leaders.items(), key=lambda x: x[1], reverse=True):
        print(f"{name}: {score}")

    pass

def main():
    
    board = []
    while True:
        choice = menu()
        if choice == "1":
            score = play_game(board)
            print(f"Game ended with score: {score}")

            
        elif choice == "2":
            score = int(input("Enter your score to save: "))
            save_score(score)

            
        elif choice == "3":
            leaders = load_scores()
            display_leaderboard(leaders)

            
        elif choice == "q":
            print("Goodbye! See you soon...")
            break

        

if __name__ == "__main__":
    main()
