class Card:
	def __init__(self, deck = None, card_type=0, name='', rent_amounts=[], color = '', monetary_value=0,
		wild_rent_amounts = [], wild_colors = [], rent_colors = []):
		"""
		card_type (int):
			0 - default / invalid
			1 - action card
			2 - property card
			3 - peroperty wildcard
			4 - rent card
			5 - money
		name (string): the name of the card, used for further filtering decision on it
		rent_amounts (list of 2 item tuples):
		color (string): empty string if not property
			brown, light blue, pink, orange, red, yellow, green, dark blue
		monetary_value: the value of the card if it is banked or used to pay another player
		wild_rent_amounts (list of rent_amounts):
		wild_colors (list of strings):
		rent_colors (list of strings): the colors that a rent card can apply towards. "*" is any

		Action Matrix | Action | Property | Property Wildcard | Rent Card | Money
		-------------------------------------------------------------------------
			Bank      |    1   |    1     |                   |     1     |   1
			Board     |        |    1     |         1         |           |    
			Action    |    1   |          |                   |     1     |    
		"""

		self.card_type = card_type
		self.name = name
		self.display_name = self.name.upper()
		self.rent_amounts = rent_amounts
		self.color = color
		self.monetary_value = monetary_value
		self.wild_rent_amounts = wild_rent_amounts
		self.wild_colors = wild_colors
		self.rent_colors = rent_colors
		self.is_banked = False

		## Set this card's card_id to be the next int of len(deck.cards)
		self.card_id = len(deck.cards) ## will be zero indexed
