from Matrix import Matrix
import random

class GoldRush(Matrix):
    def __init__(self, rows, cols):
        super().__init__(rows, cols)
        self.s1 = 0
        self.s2 = 0
        self.win = ""
        self.coins = 0

    def load_board(self):
        if self.rows == 0 and self.cols == 0:
            self.matrix = []
            return

        self.matrix = []
        elements = ["coin", ".", "wall"]
        coins = 0

        for i in range(self.rows):
            self.matrix.append([])
            for j in range(self.cols):
                if i % 2 != 0:
                    rand_index = random.randint(0, 1)
                    rand_element = elements[rand_index]
                    self.matrix[i].append(rand_element)
                    if rand_element == "coin":
                        coins += 1
                else:
                    wall_index = 2
                    wall = elements[wall_index]
                    self.matrix[i].append(wall)

            rand = random.randint(1, 2)
            for k in range(1, self.cols, rand):
                rand += 1
                rand_index = random.randint(0, 1)
                rand_element = elements[rand_index]
                self.matrix[i][k] = rand_element
                if rand_element == "coin":
                    coins += 1

        self.matrix[0][0] = "player1"
        self.matrix[self.rows - 1][self.cols - 1] = "player2"
        self.coins = coins

        if coins < 10:
            return self.load_board()
        else:
            return self.matrix

    def _check_win(self, player):
        player_num = player[-1]
        score = getattr(self, f"s{player_num}")
        if score == 100:
            self.win = player
            return self.win

    def _check_other_player(self, player):
        otherPlayer = None
        if player == "player1":
            otherPlayer = "player2"
            return otherPlayer
        elif player == "player2":
            otherPlayer = "player1"
            return otherPlayer
        

    def _move(self, curr_row, curr_col, player, delta_row, delta_col):
        other_player = self._check_other_player(player)
        new_row, new_col = curr_row + delta_row, curr_col + delta_col

        if not (0 <= new_row < self.rows and 0 <= new_col < self.cols):
            return

        if self.matrix[new_row][new_col] not in ["wall", other_player]:
            if self.matrix[new_row][new_col] == "coin":
                self._score(player)

            self.matrix[curr_row][curr_col] = "."
            self.matrix[new_row][new_col] = player

        return self._check_win(player)

    def _move_down(self, curr_row, curr_col, player):
        return self._move(curr_row, curr_col, player, 1, 0)

    def _move_up(self, curr_row, curr_col, player):
        return self._move(curr_row, curr_col, player, -1, 0)

    def _move_right(self, curr_row, curr_col, player):
        return self._move(curr_row, curr_col, player, 0, 1)

    def _move_left(self, curr_row, curr_col, player):
        return self._move(curr_row, curr_col, player, 0, -1)

    def move_player(self, player, direction):
        curr_row, curr_col = None, None

        for i, row in enumerate(self.matrix):
            for j, value in enumerate(row):
                if value == player:
                    curr_row, curr_col = i, j
                    break
            if curr_row is not None:
                break

        if direction == "down":
            self._move_down(curr_row, curr_col, player)
        elif direction == "up":
            self._move_up(curr_row, curr_col, player)
        elif direction == "right":
            self._move_right(curr_row, curr_col, player)
        elif direction == "left":
            self._move_left(curr_row, curr_col, player)

    def _score(self, player):
        player_num = player[-1]
        score_attr = f"s{player_num}"
        setattr(self, score_attr, getattr(self, score_attr) + 10)
        print(getattr(self, score_attr))
