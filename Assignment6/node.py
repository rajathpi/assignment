import numpy as np

class MCTSNode:
    def __init__(self, game_state, parent=None, move=None):
        """
        Initializes an MCTSNode object.
        :param game_state: object representing the current state of the game
        :param parent: parent node of the current node (if any)
        :param move: move that led to the current node (if any)
        """
        self.game_state = game_state
        self.parent = parent
        self.children = []

        # number of times the node has been visited
        self._n_visits = 0  
        
        # total score of all simulations that passed through this node
        self._score = 0

        # move that led to this node (if any)
        self._move = move

        self._untried_moves = None

    @property
    def q(self):
        """
        Returns the average score of all simulations that passed through this node.
        """
        return self._score

    @property
    def n(self):
        """
        Returns the number of times this node has been visited.
        """
        return self._n_visits

    @property
    def corresponding_move(self):
        """
        Returns the move that led to this node (if any).
        """
        return self._move

    @property
    def untried_moves(self):
        """
        Returns a list of untried moves from this node.
        """
        if self._untried_moves is None:
            self._untried_moves = self.game_state.legal_moves()
        return self._untried_moves

    def is_fully_expanded(self):
        """
        Returns True if all possible moves from this node have been explored, False otherwise.
        """
        return len(self.untried_moves) == 0

    def is_terminal_node(self):
        """
        Returns True if the game is over at this node, False otherwise.
        """
        return self.game_state.is_game_over()

    def add_child_node(self, child_node):
        """
        Adds a child node to the current node.
        :param child_node: child node to be added
        """
        self.children.append(child_node)

    def get_best_child(self, trade_off_param=2.0):
        """
        Returns the child node with the highest UCT score, where UCT = Q/N + c*sqrt(log(P)/N).
        :param trade_off_param: exploration/exploitation trade-off parameter c
        """
        # Upper bound confidence trees
        child_scores = []
        for child in self.children:
            score = (child.q / child.n) + trade_off_param * np.sqrt((2 * np.log(self.n) / child.n))
            child_scores.append(score)
        return self.children[np.argmax(child_scores)]

    def expand(self):
        """
        Expands the current node by adding a new child node.
        :return: the new child node
        """
        untried_move = self.untried_moves.pop()
        child_game_state = self.game_state.make_move(untried_move)
        child_node = MCTSNode(game_state=child_game_state, parent=self, move=untried_move)
        self.add_child_node(child_node)
        return child_node

    def rollout(self):
        """
        Simulates a random game from the current node until a terminal state is reached.
        :return: result of the simulated game
        """
        simulation_state = self.game_state #copy.deepcopy(self.game_state)
        # Simulate game until terminal state
        while not simulation_state.is_game_over():
            legal_moves = simulation_state.legal_moves()
            move = self.rollout_policy_choose_move(legal_moves)
            simulation_state = simulation_state.make_move(move)
        # Return result of match
        return simulation_state.get_game_result()

    def rollout_policy_choose_move(self, possible_moves):
        # Random uniform policy
        return possible_moves[np.random.randint(len(possible_moves))]

    def backprop(self, game_result):
        self._n_visits += 1
        self._score += game_result
        if self.parent:
            self.parent.backprop(game_result)
