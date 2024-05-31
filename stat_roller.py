import random
def roll(dice: int, sides: int):
	return sum(random.randint(1, sides) for _ in range(dice))
stats = ['STR', 'DEX', 'CON', 'INT','WIS','CHA']
stat_dict = {}
def get_stats():
	for stat in stats:
		die_1 = roll(1,4); die_2 = roll(1,4)
		die_3 = roll(1,4); die_4 = roll(1,4)
		rolls = [die_1, die_2, die_3, die_4]
		rolls.remove(min(rolls))
		return sum(rolls)
def assign_stats():
	for stat in stats:
		stat_dict[stat] = get_stats()
print('################')
print('#### STATS #####')
print('################')
assign_stats()
for stat in stats:
	print(f'## {stat}: {stat_dict.get(f'{stat}'):5} ##')
print('################')
print('################')