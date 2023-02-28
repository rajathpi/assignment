import numpy as np
from gamestate import GameState
from node import MCTSNode
from search import MonteCarloTreeSearch
from move import Move


# Define the main function to run the game
def main():
    print("You play as O, computer play as X")
    print("X goes first!")
    print("")

    # Initialize game
    # Create an empty 3x3 board to start the game
    initial_board = np.zeros(shape=(3, 3))

    # Create a new game state with the initial board and set the initial player to X
    current_game_state = GameState(initial_board=initial_board, initial_player=GameState.playerX)
    

    # Create a new node with the current game state as the root of the search tree
    current_node = MCTSNode(game_state=current_game_state)

    # Print initial game board
    current_node.game_state.print_board()
    print("\n")

    # Loop until the game is over
    while not current_node.game_state.is_game_over():

        # Use Monte Carlo Tree Search to find the best move for the current player
        mcts = MonteCarloTreeSearch(node=current_node)
        best_move, new_node = mcts.get_best_move(10000)
        current_node = new_node
        
        # Print the new game board after the computer's move
        current_node.game_state.print_board()
        print("\n")

        # If the game is not over, get the player's move input
        if not current_node.game_state.is_game_over():
            player_input = [int(i) for i in input("Select move by typing 'x y' coordinates: ").strip().split(" ")]
            
            # Create a new move object for the player's input and update the game state
            player_move = Move(player=GameState.playerO, x=player_input[0], y=player_input[1])
            current_game_state = current_node.game_state.make_move(move=player_move)
            
            # Create a new node for the updated game state and add it to the search tree
            current_node = MCTSNode(game_state=current_game_state, parent=current_node, move=player_move)
            
            # Print the new game board after the player's move
            current_node.game_state.print_board()
            print("\n")

    # Print the game result
    game_result = current_node.game_state.get_game_result()
    if game_result == GameState.playerX:
        print("X wins!")
    elif game_result == GameState.playerO:
        print("O wins!")
    else:
        print("It is a tie!")

# Run the main function if this file is being executed directly
if __name__ == '__main__':
    main()