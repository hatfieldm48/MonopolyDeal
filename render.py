import sys
##sys.path.append("..")
from deck import Deck
from PIL import Image, ImageDraw, ImageFont, ImageOps
from card import Card

## Define Globals and Colors
card_width = 250
card_height = 350
#player_width = 
#player_height = 
fill_background = '#F8F2ED'
fill_brown = '#8b4513'
fill_light_blue = '#87CEEB'
fill_pink = '#D54273'
fill_orange = '#FFA500'
fill_red = '#FF0000'
fill_yellow = '#FFFF00'
fill_green = '#008000'
fill_blue = '#0000ff'
fill_utility = '#CCFFCC'
fill_railroad = '#808080'
fill_one = '#F9EAA5'
fill_two = '#FBD9BF'
fill_three = '#E6DEB4'
fill_four = '#B6D5E4'
fill_five = '#AE82AF'
fill_ten = '#FDB52E'

## Get the color something should be based on the monetary value
def get_money_color(monetary_value):
    if monetary_value==1:
        return fill_one
    elif monetary_value==2:
        return fill_two
    elif monetary_value==3:
        return fill_three
    elif monetary_value==4:
        return fill_four
    elif monetary_value==5:
        return fill_five
    elif monetary_value==10:
        return fill_ten
    else:
        return '#000000'

## Get the color a section should be based on the property type
def get_property_color(prop_name, wild_colors=[]):
    
    if len(wild_colors) > 0:
        if wild_colors[0]=='*':
            return '#FFFFFF'
        return_colors = []
        for c in wild_colors:
            if c == 'brown':
                return_colors.append(fill_brown)
            elif c == 'light blue':
                return_colors.append(fill_light_blue)
            elif c == 'pink': 
                return_colors.append(fill_pink)
            elif c == 'orange':
                return_colors.append(fill_orange)
            elif c == 'red':
                return_colors.append(fill_red)
            elif c == 'yellow':
                return_colors.append(fill_yellow)
            elif c == 'green':
                return_colors.append(fill_green)
            elif c == 'dark blue':
                return_colors.append(fill_blue)
            elif c == 'utilities':
                return_colors.append(fill_utility)
            elif c == 'railroad':
                return_colors.append(fill_railroad)
        return return_colors
        
    if prop_name in ['baltic avenue', 'mediterranean avenue']:
        return fill_brown
    elif prop_name in ['connecticut avenue','oriental avenue', 'vermont avenue']:
        return fill_light_blue
    elif prop_name in ['st. charles place','virginia avenue','states avenue']:
        return fill_pink
    elif prop_name in ['new york avenue','st. james place','tennessee avenue']:
        return fill_orange
    elif prop_name in ['kentucky avenue','indiana avenue','illinois avenue']:
        return fill_red
    elif prop_name in ['ventnor avenue','marvin gardens','atlantic avenue']:
        return fill_yellow
    elif prop_name in ['north carolina avenue','pacific avenue','pennsylvania avenue']:
        return fill_green
    elif prop_name in ['boardwalk','park place']:
        return fill_blue
    elif prop_name in ['water works','electric company']:
        return fill_utility
    elif prop_name in ['short line','b&o railroad','reading railroad','pennsylvania railroad']:
        return fill_railroad
    else:
        return '#000000'

def render_property_card(property_card):

	font = ImageFont.truetype("./Data/GidoleFont/Gidole-Regular.ttf", size=24)
	result = Image.new('RGBA', (card_width, card_height))
	draw = ImageDraw.Draw(result)
	draw.rounded_rectangle(((0, 0), (250, 350)), 20, fill=fill_background) ## Create the rounded rectangel
	draw.rectangle(((15,15),(235,335)), fill=None, outline='#000000') ## Outside Border
	draw.rectangle(((25,25),(225,95)), fill=get_color(property_card.name), outline='#000000') ##Top Bar for Property title

	prop_text_w, prop_text_h = draw.textsize(property_card.name, font=font)
	draw.text(((card_width-prop_text_w)/2,10+(95-prop_text_h)/2), property_card.name, fill="black", font=font, align='center') ## Property Text

	draw.ellipse(((18,18),(60,60)), fill=fill_background, outline ='#000000') ## Top left money value
	monetary_value = str(property_card.monetary_value)
	mvalue_w, mvalue_h = draw.textsize(monetary_value, font=font)
	draw.text((18+(60.0-18.0-mvalue_w)/2, 18+(60.0-18.0-mvalue_h)/2), monetary_value, fill='black', font=font) ## Money Value

	font_rents = ImageFont.truetype("./Data/GidoleFont/Gidole-Regular.ttf", size=20)
	rent_text = ''
	for x in property_card.rent_amounts:
	    rent_text += f'{x[0]} .......... {x[1]}M\n'
	rent_text = rent_text[:-1]
	rent_text_w, rent_text_h = draw.textsize(rent_text,font=font_rents)
	draw.text(((card_width-rent_text_w)/2,(card_height+95-rent_text_h)/2),rent_text,fill='black',font=font_rents) ## Rent Amounts

	return result

def render_money_card(money_card):

	result = Image.new('RGBA', (card_height, card_width))
	draw = ImageDraw.Draw(result)
	fill_money = get_money_color(money_card.monetary_value)
	draw.rounded_rectangle(((0, 0), (350, 250)), 20, fill=fill_money)
	draw.rectangle(((15,15),(335, 235)), fill=None, outline='#000000')

	draw.ellipse(((350-60,18),(350-18,60)), fill=fill_money, outline ='#000000')
	draw.ellipse(((18,250-60),(60,250-18)), fill=fill_money, outline ='#000000')
	draw.ellipse(((175-80,125-80),(175+80,125+80)), fill=fill_money, outline ='#000000')

	monetary_value = str(money_card.monetary_value)
	mvalue_w, mvalue_h = draw.textsize(monetary_value, font=font)
	font_large = ImageFont.truetype("./Data/GidoleFont/Gidole-Regular.ttf", size=80)
	mlargevalue_w, mlargevalue_h = draw.textsize(monetary_value, font=font_large)
	draw.text((350-60+(60.0-18.0-mvalue_w)/2, 18+(60.0-18.0-mvalue_h)/2), monetary_value, fill='black', font=font)
	draw.text((18+(60.0-18.0-mvalue_w)/2, 250-60+(60.0-18.0-mvalue_h)/2), monetary_value, fill='black', font=font)
	draw.text((175-(mlargevalue_w/2), 125-(mlargevalue_h/2)), monetary_value, fill='black', font=font_large)

	return result

def render_property_wildcard(property_wildcard):

	font = ImageFont.truetype("./Data/GidoleFont/Gidole-Regular.ttf", size=24)
	result = Image.new('RGBA', (card_width, card_height))
	draw = ImageDraw.Draw(result)
	draw.rounded_rectangle(((0, 0), (250, 350)), 20, fill=fill_background)
	draw.rectangle(((15,15),(235,335)), fill=None, outline='#000000')

	if (property_wildcard.wild_colors[0]=='*'):
	    ## Make the top bar and write Property Wild Card
	    draw.rectangle(((25,25),(225,95)), fill=fill_background, outline='#000000')
	    
	    wildcard_text = 'Property Wild Card'
	    prop_text_w, prop_text_h = draw.textsize(wildcard_text, font=font)
	    draw.text(((card_width-prop_text_w)/2,10+(95-prop_text_h)/2), wildcard_text, fill="black", font=font, align='center')

	    return result

	else:
	    ## Making the top and bottom color blocks
	    wild_color_fills = get_color(property_wildcard.name, property_wildcard.wild_colors)
	    draw.rectangle(((25,25),(225,95)), fill=wild_color_fills[0], outline='#000000')
	    draw.rectangle(((25,350-95),(225,350-25)), fill=wild_color_fills[1], outline='#000000')

	    ## Making the top money circle
	    draw.ellipse(((18,18),(60,60)), fill=fill_background, outline ='#000000')
	    monetary_value = str(property_wildcard.monetary_value)
	    mvalue_w, mvalue_h = draw.textsize(monetary_value, font=font)
	    draw.text((18+(60.0-18.0-mvalue_w)/2, 18+(60.0-18.0-mvalue_h)/2), monetary_value, fill='black', font=font)

	    ## Making the bottom upside down money circle
	    draw.ellipse(((250-60,350-60),(250-18,350-18)), fill=fill_background, outline ='#000000')
	    txt = Image.new('L', (60-18, 60-18))
	    d = ImageDraw.Draw(txt)
	    d.text(((60-18)/2, (60-18)/2), monetary_value, font=font, fill=255)
	    w=txt.rotate(180,  expand=1)
	    result.paste( ImageOps.colorize(w, (0,0,0), (0,0,0)), (250-21-18-mvalue_w,350-21-18-int(mvalue_h/2)),  w)

	    font_rents = ImageFont.truetype("./Data/GidoleFont/Gidole-Regular.ttf", size=20)
	    ## First rent
	    rent_text = ''
	    for x in property_wildcard.wild_rent_amounts[0]:
	        rent_text += f'{x[0]} ... {x[1]}M\n'
	    rent_text = rent_text[:-1]
	    rent_text_w, rent_text_h = draw.textsize(rent_text,font=font_rents)
	    draw.text(((card_width-rent_text_w)*3/4,(card_height-rent_text_h)/2),rent_text,fill='black',font=font_rents)
	    ## Second rent
	    rent_flip = Image.new('L', (125, 350-95-95))
	    d = ImageDraw.Draw(rent_flip)
	    rent_text = ''
	    for x in property_wildcard.wild_rent_amounts[1]:
	        rent_text += f'{x[0]} ... {x[1]}M\n'
	    rent_text = rent_text[:-1]
	    rent_text_w, rent_text_h = draw.textsize(rent_text,font=font_rents)
	    #draw.text(((card_width-rent_text_w)/4,(card_height-rent_text_h)/2),rent_text,fill='black',font=font_rents)
	    d.text(((0, (350-95-95)//2)), rent_text, font=font_rents, fill=255)
	    #d.text(((0, (350-95-95)//2)), rent_text, font=font_rents, fill=255)
	    r_flip = rent_flip.rotate(180, expand=1)
	    result.paste( ImageOps.colorize(r_flip, (0,0,0), (0,0,0)), (0, 350-95-95), r_flip)

	    return result

def render_action_card(action_card):

	font = ImageFont.truetype("./Data/GidoleFont/Gidole-Regular.ttf", size=24)
	result = Image.new('RGBA', (card_width, card_height))
	draw = ImageDraw.Draw(result)
	fill_money = get_money_color(action_card.monetary_value)
	draw.rounded_rectangle(((0, 0), (250, 350)), 20, fill=fill_money)
	draw.rectangle(((15,15),(235, 335)), fill=None, outline='#000000')
	#draw.rectangle(((25,25),(225,95)), fill=fill_money, outline='#000000')

	draw.ellipse(((18,18),(60,60)), fill=fill_money, outline ='#000000')
	draw.ellipse(((250-60,350-60),(250-18,350-18)), fill=fill_money, outline ='#000000')
	draw.ellipse(((125-80,175-80),(125+80,175+80)), fill=fill_money, outline ='#000000')

	monetary_value = str(action_card.monetary_value)
	mvalue_w, mvalue_h = draw.textsize(monetary_value, font=font)
	font_large = ImageFont.truetype("./Data/GidoleFont/Gidole-Regular.ttf", size=30)
	display_name = action_card.name.replace(' ','\n')
	mlargevalue_w, mlargevalue_h = draw.textsize(display_name, font=font_large)
	draw.text((18+(60.0-18.0-mvalue_w)/2, 18+(60.0-18.0-mvalue_h)/2), monetary_value, fill='black', font=font)
	draw.text((250-60+(60.0-18.0-mvalue_w)/2, 350-60+(60.0-18.0-mvalue_h)/2), monetary_value, fill='black', font=font)
	draw.text((125-(mlargevalue_w/2), 175-(mlargevalue_h/2)), display_name, fill='black', font=font_large)

	return result

def render_rent_card(rent_card):

	font = ImageFont.truetype("./Data/GidoleFont/Gidole-Regular.ttf", size=24)
	result = Image.new('RGBA', (card_width, card_height))
	draw = ImageDraw.Draw(result)
	fill_money = get_money_color(sample_rent_card.monetary_value)
	draw.rounded_rectangle(((0, 0), (250, 350)), 20, fill=fill_money)
	draw.rectangle(((15,15),(235, 335)), fill=None, outline='#000000')

	draw.ellipse(((18,18),(60,60)), fill=fill_money, outline ='#000000')
	draw.ellipse(((250-60,350-60),(250-18,350-18)), fill=fill_money, outline ='#000000')
	draw.ellipse(((125-80,175-80),(125+80,175+80)), fill=fill_money, outline ='#000000')

	monetary_value = str(sample_rent_card.monetary_value)
	mvalue_w, mvalue_h = draw.textsize(monetary_value, font=font)
	font_large = ImageFont.truetype("./Data/GidoleFont/Gidole-Regular.ttf", size=30)
	display_name = sample_rent_card.name.replace(' ','\n')
	for c in sample_rent_card.rent_colors:
	    display_name += '\n' + c
	mlargevalue_w, mlargevalue_h = draw.textsize(display_name, font=font_large)
	draw.text((18+(60.0-18.0-mvalue_w)/2, 18+(60.0-18.0-mvalue_h)/2), monetary_value, fill='black', font=font)
	draw.text((250-60+(60.0-18.0-mvalue_w)/2, 350-60+(60.0-18.0-mvalue_h)/2), monetary_value, fill='black', font=font)
	draw.text((125-(mlargevalue_w/2), 175-(mlargevalue_h/2)), display_name, fill='black', font=font_large)

	return result


def render_player(player):

	## Need to render each of the cards in the players hand, board, and bank
	##  [ ] hand
	##  [ ] bank
	##  [ ] board

	## Create the full framing for this player
	result = Image.new('RGBA', ())


