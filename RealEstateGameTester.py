# Author:           Marcos Valdez
# GitHub username:  MHValdez
# Date:             05/27/2022
# Description:      A tester for RealEstateGame.py


# import unittest
from RealEstateGame import Space, GO, Property, Player, RealEstateGame


# class TestSpace(unittest.TestCase):
#     """Contains unit tests for the Space class"""
#     def test_space(self):
#         """ """
#         pass


space = Space("test space", 200)
print(space.get_name())
print()

go = GO(200)
print(go.get_name())
print(go.get_payout())
print()

prop = Property("test prop", 200)
print(prop.get_name())
print(prop.get_rent())
print(prop.get_price())
print(prop.get_owner())
print()

player = Player("p1", 2000)
print(player.get_name())
print(player.get_balance())
print(player.get_pos())
print()

prop.set_owner(player)
print(prop.get_owner().get_name())
print()

player.set_pos(1)
print(player.get_pos())
player.update_balance(-1000)
print(player.get_balance())
player.update_balance(-1200)
print(player.get_balance())
print()

game = RealEstateGame()
print(game._board)
print(game._players)
print()

game.display()

rents = [50, 50, 50, 75, 75, 75, 100, 100, 100, 150, 150, 150,
         200, 200, 200, 250, 250, 250, 300, 300, 300, 350, 350, 350]
game.create_spaces(50, rents)
print(f"{game._board[0].get_name()}      : {game._board[0].get_payout()}")
for prop in game._board[1:]:
    print(f"{prop.get_name()} : {prop.get_rent()} / {prop.get_price()} : {prop.get_owner()}")
print()

game.create_spaces(50, rents)

game.display()
print()

game.create_player("Player 1", 1100)
game.create_player("Player 1", 1200)
game.create_player("Player 2", 1200)
game.create_player("Player 3", 1300)
for player in game._players:
    print(f"{player.get_name()} : {player.get_balance()}")
print()

game.display()
print()

print(game.get_space(1).get_name())
print(game.get_space(1).get_rent())
print(game.get_space(1).get_price())
print(game.get_space(1).get_owner())
print()

print(game.get_player("Player 0"))
print(game.get_player("Player 1").get_name())
print()

print(game.get_player_account_balance("Player 0"))
print(game.get_player_account_balance("Player 1"))
print(game.get_player_current_position("Player 0"))
print(game.get_player_current_position("Player 1"))
print()

game.buy_space("Player 1")

game.display()
print()

game.move_player("Player 1", 6)
print(game.get_player_current_position("Player 1"))
game.move_player("Player 1", 6)
print(game.get_player_current_position("Player 1"))
game.move_player("Player 1", 6)
print(game.get_player_current_position("Player 1"))
game.move_player("Player 1", 3)
print(game.get_player_current_position("Player 1"))
print(game.get_player_account_balance("Player 1"))
game.move_player("Player 1", 6)
print(game.get_player_current_position("Player 1"))
print(game.get_player_account_balance("Player 1"))
print()

game.display()
print()

game.buy_space("Player 1")
print(game.get_player_account_balance("Player 1"))
print(game.get_space(2).get_owner().get_name())
print()

game.display()
print()

print(game.get_player_account_balance("Player 2"))
game.move_player("Player 2", 2)
print(game.get_player_account_balance("Player 2"))
print()

game.display()
print()

print(game.get_player_account_balance("Player 3"))
game.move_player("Player 3", 5)
print(game.get_player_current_position("Player 3"))
print(game.get_player_account_balance("Player 3"))
game.buy_space("Player 3")
print(game.get_player_account_balance("Player 3"))
print(game.get_space(5).get_owner().get_name())
print()

game.display()
print()

print(game.get_player_account_balance("Player 1"))
game.get_player("Player 1").update_balance(-900)
print(game.get_player_account_balance("Player 1"))
print(game.get_player_current_position("Player 1"))
game.move_player("Player 1", 3)
print(game.get_player_current_position("Player 1"))
print(game.get_player_account_balance("Player 1"))
game.move_player("Player 1", 3)
print(game.get_player_current_position("Player 1"))
print()

game.display()
print()

print(f'Game Over: "{game.check_game_over()}"')
game.get_player("Player 2").update_balance(-1150)
print(game.get_player_account_balance("Player 2"))
print(f'Game Over: "{game.check_game_over()}"')
print()

game.create_player("Player 4", 1000)
game.create_player("Player 5", 1000)

game.display()
print()

print(f'Game Over: "{game.check_game_over()}"')
print()

game.move_player("Player 2", 3)
game.move_player("Player 4", 5)
game.move_player("Player 5", 5)

game.display()
print()

game.create_player("Player 6", 1000)
game.move_player("Player 6", 5)

game.display()
print()
