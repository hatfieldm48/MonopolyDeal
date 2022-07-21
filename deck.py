from card import Card
import random

class Deck:
	def __init__(self, game=None):

		self.cards = []

		## Initialize the deck cards
		self.create_deck_of_cards()

		## Shuffle the deck
		self.shuffle_deck()

		## Set the Game Pointer
		self.game = game

		return

	def test_valid_deck(self):

		## Number of Action Cards = 34
		action_cards = [x for x in self.cards if x.card_type==1]
		if len(action_cards)==34:
			print ("Number of action cards:            PASS")
		else:
			print (f"FAIL: Number of action cards is {len(action_cards)}, should be 34")
			return False

		## Number of Property Cards = 28
		property_cards = [x for x in self.cards if x.card_type==2]
		if len(property_cards)==28:
			print ("Number of property cards:          PASS")
		else:
			print (f"FAIL: Number of property cards is {len(property_cards)}, should be 28")
			return False

		## Number of Property Wild Cards = 11
		property_wildcards = [x for x in self.cards if x.card_type==3]
		if len(property_wildcards)==11:
			print ("Number of property wild cards:     PASS")
		else:
			print (f"FAIL: Number of property wild cards is {len(property_wildcards)}, should be 11")
			return False

		## Number of Rent Cards = 13
		rent_cards = [x for x in self.cards if x.card_type==4]
		if len(rent_cards)==13:
			print ("Number of rent cards:              PASS")
		else:
			print (f"FAIL: Number of rent cards is {len(rent_cards)}, should be 13")
			return False

		## Number of Money Cards = 20
		money_cards = [x for x in self.cards if x.card_type==5]
		if len(money_cards)==20:
			print ("Number of money cards:             PASS")
		else:
			print (f"FAIL: Number of money cards is {len(money_cards)}, should be 20")
			return False

		## Number of cards = 106
		if len(self.cards) == 106:
			print ("Number of cards:                   PASS")
		else:
			print (f"FAIL: Number of cards is {len(self.cards)}, should be 106")
			return False

		## Total Money = 57
		money_cards = [x for x in self.cards if x.card_type==5]
		if sum([x.monetary_value for x in money_cards])==57:
			print ("Total money:                       PASS")
		else:
			print (f"FAIL: Total money is {sum([x.monetary_value for x in money_cards])}, should be 57")
			return False

		## Property Colors Test
		accurate_properties = {
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
		deck_properties = {}
		for c in property_cards:
			if c.color in deck_properties.keys():
				deck_properties[c.color] += 1
			else:
				deck_properties[c.color] = 1
		if accurate_properties == deck_properties:
			print ("Property Colors Test:              PASS")
		else:
			print (f"FAIL: Property frequencies don't match. Here is the wrong one: {deck_properties}")
			return False

		return True


	def create_deck_of_cards(self):

		## Create the 34 Action Cards
		for i in range(2):
			new_card = Card(deck=self, card_type=1, name='deal breaker', monetary_value=5)
			self.cards.append(new_card)
		for i in range(3):
			new_card = Card(deck=self, card_type=1, name='debt collector', monetary_value=3)
			self.cards.append(new_card)
		for i in range(2):
			new_card = Card(deck=self, card_type=1, name='double the rent', monetary_value=1)
			self.cards.append(new_card)
		for i in range(3):
			new_card = Card(deck=self, card_type=1, name='forced deal', monetary_value=3)
			self.cards.append(new_card)
		for i in range(2):
			new_card = Card(deck=self, card_type=1, name='hotel', monetary_value=4)
			self.cards.append(new_card)
		for i in range(3):
			new_card = Card(deck=self, card_type=1, name='house', monetary_value=3)
			self.cards.append(new_card)
		for i in range(3):
			new_card = Card(deck=self, card_type=1, name='its my birthday', monetary_value=2)
			self.cards.append(new_card)
		for i in range(3):
			new_card = Card(deck=self, card_type=1, name='just say no!', monetary_value=4)
			self.cards.append(new_card)
		for i in range(10):
			new_card = Card(deck=self, card_type=1, name='pass go', monetary_value=1)
			self.cards.append(new_card)
		for i in range(3):
			new_card = Card(deck=self, card_type=1, name='sly deal', monetary_value=3)
			self.cards.append(new_card)

		## Create the 28 Property Cards
		self.cards.append(Card(deck=self, card_type=2, name = 'baltic avenue', 
			rent_amounts = [(1,1),(2,2)], 
			color = 'brown', monetary_value=1))
		self.cards.append(Card(deck=self, card_type=2, name = 'mediterranean avenue', 
			rent_amounts = [(1,1),(2,2)], 
			color = 'brown', monetary_value=1))

		self.cards.append(Card(deck=self, card_type=2, name = 'connecticut avenue', 
			rent_amounts = [(1,1),(2,2),(3,3)], 
			color = 'light blue', monetary_value=1))
		self.cards.append(Card(deck=self, card_type=2, name = 'oriental avenue', 
			rent_amounts = [(1,1),(2,2),(3,3)], 
			color = 'light blue', monetary_value=1))
		self.cards.append(Card(deck=self, card_type=2, name = 'vermont avenue', 
			rent_amounts = [(1,1),(2,2),(3,3)], 
			color = 'light blue', monetary_value=1))

		self.cards.append(Card(deck=self, card_type=2, name = 'st. charles place', 
			rent_amounts = [(1,1),(2,2),(3,4)], 
			color = 'pink', monetary_value=2))
		self.cards.append(Card(deck=self, card_type=2, name = 'virginia avenue', 
			rent_amounts = [(1,1),(2,2),(3,4)], 
			color = 'pink', monetary_value=2))
		self.cards.append(Card(deck=self, card_type=2, name = 'states avenue', 
			rent_amounts = [(1,1),(2,2),(3,4)], 
			color = 'pink', monetary_value=2))

		self.cards.append(Card(deck=self, card_type=2, name = 'new york avenue', 
			rent_amounts = [(1,1),(2,3),(3,5)], 
			color = 'orange', monetary_value=2))
		self.cards.append(Card(deck=self, card_type=2, name = 'st. james place', 
			rent_amounts = [(1,1),(2,3),(3,5)], 
			color = 'orange', monetary_value=2))
		self.cards.append(Card(deck=self, card_type=2, name = 'tennessee avenue', 
			rent_amounts = [(1,1),(2,3),(3,5)], 
			color = 'orange', monetary_value=2))

		self.cards.append(Card(deck=self, card_type=2, name = 'kentucky avenue', 
			rent_amounts = [(1,2),(2,3),(3,6)], 
			color = 'red', monetary_value=3))
		self.cards.append(Card(deck=self, card_type=2, name = 'indiana avenue', 
			rent_amounts = [(1,2),(2,3),(3,6)], 
			color = 'red', monetary_value=3))
		self.cards.append(Card(deck=self, card_type=2, name = 'illinois avenue', 
			rent_amounts = [(1,2),(2,3),(3,6)], 
			color = 'red', monetary_value=3))

		self.cards.append(Card(deck=self, card_type=2, name = 'ventnor avenue', 
			rent_amounts = [(1,2),(2,4),(3,6)], 
			color = 'yellow', monetary_value=3))
		self.cards.append(Card(deck=self, card_type=2, name = 'marvin gardens', 
			rent_amounts = [(1,2),(2,4),(3,6)], 
			color = 'yellow', monetary_value=3))
		self.cards.append(Card(deck=self, card_type=2, name = 'atlantic avenue', 
			rent_amounts = [(1,2),(2,4),(3,6)], 
			color = 'yellow', monetary_value=3))

		self.cards.append(Card(deck=self, card_type=2, name = 'north carolina avenue', 
			rent_amounts = [(1,2),(2,4),(3,7)], 
			color = 'green', monetary_value=4))
		self.cards.append(Card(deck=self, card_type=2, name = 'pacific avenue', 
			rent_amounts = [(1,2),(2,4),(3,7)], 
			color = 'green', monetary_value=4))
		self.cards.append(Card(deck=self, card_type=2, name = 'pennsylvania avenue', 
			rent_amounts = [(1,2),(2,4),(3,7)], 
			color = 'green', monetary_value=4))

		self.cards.append(Card(deck=self, card_type=2, name = 'boardwalk', 
			rent_amounts = [(1,3),(2,8)], 
			color = 'dark blue', monetary_value=4))
		self.cards.append(Card(deck=self, card_type=2, name = 'park place', 
			rent_amounts = [(1,3),(2,8)], 
			color = 'dark blue', monetary_value=4))

		self.cards.append(Card(deck=self, card_type=2, name = 'water works', 
			rent_amounts = [(1,1),(2,2)], 
			color = 'utilities', monetary_value=2))
		self.cards.append(Card(deck=self, card_type=2, name = 'electric company', 
			rent_amounts = [(1,1),(2,2)], 
			color = 'utilities', monetary_value=2))

		self.cards.append(Card(deck=self, card_type=2, name = 'short line', 
			rent_amounts = [(1,1),(2,2),(3,3),(4,4)], 
			color = 'railroad', monetary_value=2))
		self.cards.append(Card(deck=self, card_type=2, name = 'b&o railroad', 
			rent_amounts = [(1,1),(2,2),(3,3),(4,4)], 
			color = 'railroad', monetary_value=2))
		self.cards.append(Card(deck=self, card_type=2, name = 'reading railroad', 
			rent_amounts = [(1,1),(2,2),(3,3),(4,4)], 
			color = 'railroad', monetary_value=2))
		self.cards.append(Card(deck=self, card_type=2, name = 'pennsylvania railroad', 
			rent_amounts = [(1,1),(2,2),(3,3),(4,4)], 
			color = 'railroad', monetary_value=2))

		## Create the 11 Property Wildcards
		self.cards.append(Card(deck=self, card_type=3, name = 'property wild card',
			wild_rent_amounts = [],
			wild_colors = ['dark blue', 'green'], monetary_value=4))
		self.cards.append(Card(deck=self, card_type=3, name = 'property wild card',
			wild_rent_amounts = [],
			wild_colors = ['light blue', 'brown'], monetary_value=1))
		for i in range(2):
			self.cards.append(Card(deck=self, card_type=3, name = 'property wild card',
				wild_rent_amounts = [],
				wild_colors = ['*'], monetary_value=0))
		for i in range(2):
			self.cards.append(Card(deck=self, card_type=3, name = 'property wild card',
				wild_rent_amounts = [],
				wild_colors = ['orange', 'pink'], monetary_value=2))
		self.cards.append(Card(deck=self, card_type=3, name = 'property wild card',
			wild_rent_amounts = [],
			wild_colors = ['green', 'railroad'], monetary_value=4))
		self.cards.append(Card(deck=self, card_type=3, name = 'property wild card',
			wild_rent_amounts = [],
			wild_colors = ['light blue', 'railroad'], monetary_value=4))
		self.cards.append(Card(deck=self, card_type=3, name = 'property wild card',
			wild_rent_amounts = [],
			wild_colors = ['utilities', 'railroad'], monetary_value=2))
		for i in range(2):
			self.cards.append(Card(deck=self, card_type=3, name = 'property wild card',
				wild_rent_amounts = [],
				wild_colors = ['yellow', 'red'], monetary_value=3))

		## Create the 13 Rent Cards
		for i in range(3):
			self.cards.append(Card(deck=self, card_type=4, name = 'rent wildcard',
				rent_colors=['*'], monetary_value=3))
		for i in range(2):
			self.cards.append(Card(deck=self, card_type=4, name = 'rent',
				rent_colors=['green', 'dark blue'], monetary_value=1))
		for i in range(2):
			self.cards.append(Card(deck=self, card_type=4, name = 'rent',
				rent_colors=['brown', 'light blue'], monetary_value=1))
		for i in range(2):
			self.cards.append(Card(deck=self, card_type=4, name = 'rent',
				rent_colors=['pink', 'orange'], monetary_value=1))
		for i in range(2):
			self.cards.append(Card(deck=self, card_type=4, name = 'rent',
				rent_colors=['red', 'yellow'], monetary_value=1))
		for i in range(2):
			self.cards.append(Card(deck=self, card_type=4, name = 'rent',
				rent_colors=['utilities', 'railroad'], monetary_value=1))

		## Create the Money Cards
		self.cards.append(Card(deck=self, card_type=5, name = '10M', monetary_value=10))
		for i in range(2):
			self.cards.append(Card(deck=self, card_type=5, name = '5M', monetary_value=5))
		for i in range(3):
			self.cards.append(Card(deck=self, card_type=5, name = '4M', monetary_value=4))
		for i in range(3):
			self.cards.append(Card(deck=self, card_type=5, name = '3M', monetary_value=3))
		for i in range(5):
			self.cards.append(Card(deck=self, card_type=5, name = '2M', monetary_value=2))
		for i in range(6):
			self.cards.append(Card(deck=self, card_type=5, name = '1M', monetary_value=1))

		return

	def shuffle_deck(self):

		random.shuffle(self.cards)
		return True

	def get_size(self):

		return len(self.cards)

	def draw_card(self):

		card_drawn = self.cards.pop(0)

		## Check if deck is empty and needs to be reshuffled
		if self.get_size() == 0:
			## The discard gards in game.discard will become new deck
			self.cards = [x for x in self.game.discard]
			self.game.discard = []
			self.shuffle_deck()


		return card_drawn

