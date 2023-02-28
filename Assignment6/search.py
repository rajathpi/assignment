from node import MCTSNode


class MonteCarloTreeSearch:

    def __init__(self, node: MCTSNode):
        # Initialize the Monte Carlo Tree Search object with a root node.
        self.root = node

    def get_best_move(self, iterations=1):
        # Run the MCTS algorithm for a specified number of iterations.
        for i in range(0, iterations):
            
            # Traverse the tree to select a child node to explore/exploit.
            selected_child_node = self.traverse()
            
            # Simulate a random game from the selected child node to the end.
            game_result = selected_child_node.rollout()
            
            # Update the stats (score and visit count) of the selected node and all its ancestors.
            selected_child_node.backprop(game_result)

        # Return the best move and the corresponding child node based on the UCT formula.
        best_child = self.root.get_best_child(trade_off_param=0)
        best_move = best_child.corresponding_move
        return best_move, best_child

    def traverse(self):
        
        # Starting from the root, traverse the tree until a non-terminal, unexpanded node is found.
        current_node = self.root
        while not current_node.is_terminal_node():
            if not current_node.is_fully_expanded():
                # If the current node is not fully expanded, expand it by creating a new child node.
                return current_node.expand()
            else:
                # Otherwise, select the best child node to explore/exploit based on the UCT formula.
                current_node = current_node.get_best_child()
        return current_node