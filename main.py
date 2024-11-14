from game import GoldRush


def play_game():
    print("Welcome to Gold Rush!")
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    game = GoldRush(rows, cols)
    game.load_board()
    game.print()

    while not game.win:
        player = "player1"
        direction = input(f"{player}, enter your move (up, down, left, right): ").strip().lower()
        game.move_player(player, direction)
        game.print()
        if game._check_win(player):
            print(f"{player} wins!")
            break

        player = "player2"
        direction = input(f"{player}, enter your move (up, down, left, right): ").strip().lower()
        game.move_player(player, direction)
        game.print()
        if game._check_win(player):
            print(f"{player} wins!")
            break

if __name__ == "__main__":
    play_game()