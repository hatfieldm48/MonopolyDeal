import random
import numpy as np
import itertools

class Player:

	def __init__(self, name, game=None):

		self.player_name = name
		self.cards_in_hand = []
		self.cards_on_table = []
		self.cards_in_bank = []
		self.cards_discarded = [] #To be reset each turn
		self.game = game

		"""
		self.wildcolors_dict = {
			0: ('dark blue', 'green'),
			1: ('light blue', 'brown'),
			2: ('orange', 'pink'),
			3: ('green', 'railroad'),
			4: ('light  blue', 'railroad'),
			5: ('utilities', 'railroad'),
			6: ('yellow', 'red'),
			7: ('brown', 'light blue', 'pink', 'orange', 'red', 'yellow', 'green', 'dark blue', 'utilities', 'railroad')
		}
		self.wildcolors_nums = []"""
		self.wildcolors_options = []

	def print_my_bank(self):

		output = self.player_name + ' - BANK' + '\n'
		output += '-'*20 + '\n'

		for c in self.cards_in_bank:
			if c.card_type in [1,2]:
				output += f'{c.card_id} | {c.name} | ${c.monetary_value}\n'
			elif c.card_type in [3]:
				output += f'{c.card_id} | {c.name} | {"-".join(c.wild_colors)} | ${c.monetary_value}\n'
			elif c.card_type in [4]:
				output += f'{c.card_id} | {c.name} | {"-".join(c.rent_colors)} | ${c.monetary_value}\n'
			else: ##Money
				output += f'{c.card_id} | ${c.monetary_value}\n'

		print (output)

	def print_my_table(self):

		output = self.player_name + ' - TABLE' + '\n'
		output += '-'*20 + '\n'

		for c in self.cards_on_table:
			if c.card_type in [1,2]:
				output += f'{c.card_id} | {c.name} | ${c.monetary_value}\n'
			elif c.card_type in [3]:
				output += f'{c.card_id} | {c.name} | {"-".join(c.wild_colors)} | ${c.monetary_value}\n'
			elif c.card_type in [4]:
				output += f'{c.card_id} | {c.name} | {"-".join(c.rent_colors)} | ${c.monetary_value}\n'
			else: ##Money
				output += f'{c.card_id} | ${c.monetary_value}\n'

		print (output)

	def print_hand(self):

		output = self.player_name + '- HAND' + '\n'
		output += '-'*20 + '\n'

		for c in self.cards_in_hand:
			if c.card_type in [1,2]:
				output += f'{c.card_id} | {c.name} | ${c.monetary_value}\n'
			elif c.card_type in [3]:
				output += f'{c.card_id} | {c.name} | {"-".join(c.wild_colors)} | ${c.monetary_value}\n'
			elif c.card_type in [4]:
				output += f'{c.card_id} | {c.name} | {"-".join(c.rent_colors)} | ${c.monetary_value}\n'
			else: ##Money
				output += f'{c.card_id} | ${c.monetary_value}\n'

		print (output)

	def find_combinations(self, combinations, index, result=''):

		if index < 0:
			combinations.add(result[:-1])
			return

		#color_idx = self.wildcolors_nums[index]
		#colors = self.wildcolors_dict[color_idx]
		colors = self.wildcolors_options[index]


		for i in range(len(colors)):
			self.find_combinations(combinations, index-1, result+colors[i]+',')

	def find_all_combinations(self):

		combinations = set()
		#find_combinations(combinations, len(self.wildcolors_nums)-1)
		self.find_combinations(combinations, len(self.wildcolors_options)-1)

		return combinations

	def check_for_game_win(self):
		""" Need to check the cards_on_table to see if this player won the game
		    Ideas for how:
		    - Just have rules for the wildcard and the 2 color wildcards
		    - Create the full permutation of color combinations
		    - Check each one for a set of 3 against the proper numbers
		"""

		accurate_counts = {
			'brown': 2, 
			'light blue': 3, 
			'pink': 3,
			'orange': 3,
			'red': 3,
			'yellow': 3,
			'green': 3,
			'dark blue': 2,
			'utilities': 2,
			'railroad': 4
		}

		self.wildcolors_options = []
		property_cards = [x for x in self.cards_on_table if x.card_type==2]
		two_way_wildcards = [x for x in self.cards_on_table if len(x.wild_colors)==2]
		full_wildcards = [x for x in self.cards_on_table if x.wild_colors=='*']
		for c in two_way_wildcards:
			self.wildcolors_options.append(c.wild_colors)
		for c in full_wildcards:
			self.wildcolors_options.append(['brown', 'light blue', 'pink', 'orange', 'red', 'yellow', 'green', 'dark blue', 'utilities', 'railroad'])

		wild_combinations = list(self.find_all_combinations())
		wild_combinations = [x.split(',') for x in wild_combinations]

		##print (wild_combinations)
		if wild_combinations[0][0]=='':
			## Then no wilds, just check frequency of normal property cards
			color_freqs = {}
			for c in property_cards:
				if c.color in color_freqs.keys():
					color_freqs[c.color] += 1
				else:
					color_freqs[c.color] = 1
			## For each key, check if the value is >= the accurate_counts one
			monopolies = 0
			for k in color_freqs.keys():
				if color_freqs[k] >= accurate_counts[k]:
					monopolies += 1

			if monopolies >= 3:
				return True
		else:
			for combo in wild_combinations:
				## Now for each one of these create a color frequency dictionary, 
				color_freqs = {}
				for c in property_cards:
					if c.color in color_freqs.keys():
						color_freqs[c.color] += 1
					else:
						color_freqs[c.color] = 1
				for color in combo:
					if color in color_freqs.keys():
						color_freqs[color] += 1
					else:
						color_freqs[color] = 1

				## For each key, check if the value is >= the accurate_counts one
				monopolies = 0
				for k in color_freqs.keys():
					if color_freqs[k] >= accurate_counts[k]:
						monopolies += 1

				if monopolies >= 3:
					return True

		return False

	def find_card_idx(self, card_id):
		""" Given a card's ID, find the index of it in hand
		"""

		for i in range(len(self.cards_in_hand)):
			if self.cards_in_hand[i].card_id == card_id:
				return i

		print ('Error: Card Not Found')
		return None

	def bank_card(self, card_id):
		""" When a player chooses to play a card into their bank
		"""

		card_in_hand_idx = self.find_card_idx(card_id)
		card_to_play = self.cards_in_hand.pop(card_in_hand_idx)
		self.cards_in_bank.append(card_to_play)
		card_to_play.is_banked = True

		return True

	def board_card(self, card_id):
		""" When a player chooses to play a card onto their board
		"""

		card_in_hand_idx = self.find_card_idx(card_id)
		card_to_play = self.cards_in_hand.pop(card_in_hand_idx)
		self.cards_on_table.append(card_to_play)

		return True

	def action_card(self, card_id):
		""" When a player chooses to play an action card into the discard pile
		"""

		card_in_hand_idx = self.find_card_idx(card_id)
		card_to_play = self.cards_in_hand.pop(card_in_hand_idx)
		
		## Execute the card's action
		placeholder = 0

		self.cards_discarded.append(card_to_play)

		return

	def take_turn(self, deck):

		## Reset self.cards_discarded back to an empty list
		self.cards_discarded = []

		return_dict = {
			'game_won': False,
			'cards_discarded': [],
		}

		## Draw 2 cards
		for i in range(2):
			card_drawn = deck.draw_card()
			self.cards_in_hand.append(card_drawn)


		## Get the game state
		print(self.game.get_game_state(self))


		"""## Play a random card
		rnd_idx = random.randint(0, len(self.cards_in_hand)-1)
		card_to_play = self.cards_in_hand.pop(rnd_idx)
		return_dict['cards_discarded'].append(card_to_play)
		"""

		## Create the array of action indicators
		# list of tuples s.t. (card_in_hand_idx, action_func)
		decision_pointers = []
		for c in self.cards_in_hand:
			if c.card_type==1:
				decision_pointers.append((c.card_id, 'bank'))
				decision_pointers.append((c.card_id, 'action'))
			elif c.card_type==2:
				#decision_pointers.append((c.card_id, 'bank'))
				decision_pointers.append((c.card_id, 'board'))
			elif c.card_type==3:
				decision_pointers.append((c.card_id, 'board'))
			elif c.card_type==4:
				decision_pointers.append((c.card_id, 'bank'))
				decision_pointers.append((c.card_id, 'action'))
			elif c.card_type==5:
				decision_pointers.append((c.card_id, 'bank'))

		decisions = np.zeros((len(decision_pointers)), dtype=int)

		## For now, randomly select up to 3 of them
		# [ ] - This allows for 1 card to be chosen for multiple actions, which isn't legal
		#     - following the same thought, defining this game in terms of "game state"
		#         instead of decisions might make more sense...
		num_actions_chosen = random.randint(0, 3)
		#selected_actions = np.random.choice(len(decisions), num_actions_chosen, replace=False)
		selected_cards = np.random.choice(len(self.cards_in_hand), num_actions_chosen, replace=False)
		selected_cards_ids = [self.cards_in_hand[x].card_id for x in selected_cards]
		print (selected_cards, selected_cards_ids)
		##selected_actions = 0
		for selected_card_id in selected_cards_ids:
			possible_actions = [x for x in decision_pointers if x[0]==selected_card_id]
			chosen_action = possible_actions[random.randint(0, len(possible_actions)-1)]
			decision_idx = decision_pointers.index(chosen_action)
			decisions[decision_idx] = 1
			#print (chosen_action, decision_idx)

		#for action in selected_actions:
		#	decisions[action] = 1
		print ('  ', decisions)


		## Now execute the actions for those decisions
		for i in range(len(decisions)):
			if decisions[i]==1:
				if decision_pointers[i][1]=='bank':
					self.bank_card(decision_pointers[i][0])
				elif decision_pointers[i][1]=='board':
					self.board_card(decision_pointers[i][0])
				elif decision_pointers[i][1]=='action':
					self.action_card(decision_pointers[i][0])

		## Append any discarded cards to return_dict element
		for c in self.cards_discarded:
			return_dict['cards_discarded'].append(c)

		## End of turn, all actions (or non-action decided)
		## now the player must discard until their hand is <=7
		## this while loop is fine for random selection, but,
		##  for RL-decided actions, it should probably be an if-else
		##  going all the way from 1 discard require to 6 discards 
		##  required, so that decisions can be considered as a whole
		while len(self.cards_in_hand) > 7:
			rnd_idx = random.randint(0, len(self.cards_in_hand)-1)
			card_to_discard = self.cards_in_hand.pop(rnd_idx)
			return_dict['cards_discarded'].append(card_to_discard)


		## Check if you won the game
		self.print_my_table()
		self.print_my_bank()
		return_dict['game_won'] = self.check_for_game_win()


		self.print_hand()
		return return_dict

