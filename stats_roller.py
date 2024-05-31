import random

def roll(dice: int, sides: int):
	return sum(random.randint(1, sides) for _ in range(dice))

def get_rolls():
	return [roll(1, 6) for _ in range(4)]

stats = ('str', 'dex', 'con', 'int', 'wis', 'cha')
stat_dict = {}

def modify_rolls():
	for stat in stats:
		rolls = get_rolls()
		cull = min(rolls)
		rolls.remove(min(rolls))
		rolls.append(sum(rolls)) 
		rolls.append(cull)
		stat_dict[stat] = rolls
		
modify_rolls()
print(f'###################################')
print(f'# Result  = d1  + d2  + d3 # cull #')
for stat in stats:
	print(f'# {stat.upper()}: {stat_dict[stat][3]:<3}\
=  {stat_dict[stat][0]}  +  {stat_dict[stat][1]}  +  \
{stat_dict[stat][2]} #  ({stat_dict[stat][4]}) #')
print(f'###################################')
