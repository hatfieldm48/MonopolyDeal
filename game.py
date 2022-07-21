from deck import Deck
from card import Card
from player import Player

import random
import numpy as np


class Game:

	def __init__(self, players = ['A', 'B', 'C']):

		self.player_names = players
		self.num_players = len(self.player_names)

		## Create the players as python objects
		self.players = [Player(x, self) for x in self.player_names]
		self.set_player_order()

		## Create the deck and discard piles
		self.deck = Deck(self) ## Gets shuffled on initialization
		self.discard = [] # Will be a list of Card objects

		## Deal the cards
		self.deal_hands()

		self.turn_counter = 0
		self.game_won = False

		#while not self.game_won:
		while (not self.game_won) and (self.turn_counter < 100):

			## Print Deck and Discard Status
			print (f'Cards Left in Deck    : {self.deck.get_size()}')
			print (f'Cards Left in Discard : {len(self.discard)}')

			## Get the next Player up
			next_player = self.players[0]

			## Have the take their turn and get the return value(s)
			return_dict = next_player.take_turn(self.deck)

			## Add the played cards to the discard pile
			for c in return_dict['cards_discarded']:
				self.discard.append(c)

			## If the player won, then end the game
			if return_dict['game_won']:
				print (f'WINNER: {next_player.player_name}')
				self.game_won = True

			
			else:
				## If no, next player up, and move this player to the end of the line
				self.players = self.players[1:] + self.players[:1]

				## increment turn counter
				self.turn_counter += 1
				print (f'CARDS IN GAME: {self.count_all_cards()}')

		return

	def set_player_order(self):

		random.shuffle(self.players)
		return True

	def deal_hands(self):

		for i in range(5):
			for p in self.players:

				#card_to_deal = self.deck.cards.pop(0)
				card_to_deal = self.deck.draw_card()
				p.cards_in_hand.append(card_to_deal)

	def count_all_cards(self):

		total_cards = 0

		## Deck cards
		total_cards += self.deck.get_size()

		## Discard cards
		total_cards += len(self.discard)

		## Cards in player hands, banks, table
		for p in self.players:
			total_cards += len(p.cards_in_hand)
			total_cards += len(p.cards_on_table)
			total_cards += len(p.cards_in_bank)

		return total_cards

	def get_game_state(self, requesting_player):
		""" Return the game state as an array of integer values
		    Thoughts/Ideas:
		    - Seems like these are traditionally 0/1 booleans, but that doesn't seems possible for multiplayer games
		    - proposed setup: array of length 106 == total num cards
		    -   each card gets an integer value of the following:
		    -   0 - not seen
		    -   1 - discarded
		    -   2 - in my hand
		    -   3 - on my board
		    -   4 - in my bank
		    -   5 - on player m's board
		    -   6 - in player m's bank
		    -   7 - ...
		    -   8 - ...
		"""

		game_state = np.zeros(106, dtype=int)

		## Don't need to set the un-seen cards still in deck to zero, that's array default

		## Set discarded cards to 1
		for c in self.discard:
			game_state[c.card_id] = 1

		## Set cards in that player's hand to 2
		for c in requesting_player.cards_in_hand:
			game_state[c.card_id] = 2

		## Set cards in that player's board to 3
		for c in requesting_player.cards_on_table:
			game_state[c.card_id] = 3

		## Set cards in that player's hand to 4
		for c in requesting_player.cards_in_bank:
			game_state[c.card_id] = 4

		other_player_idx = 5
		for other_player in self.players:
			if other_player != requesting_player:
				for c in other_player.cards_on_table:
					game_state[c.card_id] = other_player_idx

				for c in other_player.cards_in_bank:
					game_state[c.card_id] = other_player_idx + 1

				other_player_idx += 2

		return game_state




