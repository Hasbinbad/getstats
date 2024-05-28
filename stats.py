import random

# edit to allow pull request

strength1 = random.randint(1, 6); strength2 = random.randint(1, 6)
strength3 = random.randint(1, 6); strength4 = random.randint(1, 6)
strength_list = [strength1, strength2, strength3, strength4]
strength_removed = min(strength_list)
strength_list.remove(min(strength_list))
strength = sum(strength_list)
 
dexterity1 = random.randint(1, 6); dexterity2 = random.randint(1, 6)
dexterity3 = random.randint(1, 6); dexterity4 = random.randint(1, 6)
dexterity_list = [dexterity1, dexterity2, dexterity3, dexterity4]
dexterity_removed = min(dexterity_list)
dexterity_list.remove(min(dexterity_list))
dexterity = sum(dexterity_list)

constitution1 = random.randint(1, 6); constitution2 = random.randint(1, 6)
constitution3 = random.randint(1, 6); constitution4 = random.randint(1, 6)
constitution_list = [constitution1, constitution2, constitution3, constitution4]
constitution_removed = min(constitution_list)
constitution_list.remove(min(constitution_list))
constitution = sum(constitution_list)

intelligence1 = random.randint(1, 6); intelligence2 = random.randint(1, 6)
intelligence3 = random.randint(1, 6); intelligence4 = random.randint(1, 6)
intelligence_list = [intelligence1, intelligence2, intelligence3, intelligence4]
intelligence_removed = min(intelligence_list)
intelligence_list.remove(min(intelligence_list))
intelligence = sum(intelligence_list)

wisdom1 = random.randint(1, 6); wisdom2 = random.randint(1, 6)
wisdom3 = random.randint(1, 6); wisdom4 = random.randint(1, 6)
wisdom_list = [wisdom1, wisdom2, wisdom3, wisdom4]
wisdom_removed = min(wisdom_list)
wisdom_list.remove(min(wisdom_list))
wisdom = sum(wisdom_list)

charisma1 = random.randint(1, 6); charisma2 = random.randint(1, 6)
charisma3 = random.randint(1, 6); charisma4 = random.randint(1, 6)
charisma_list = [charisma1, charisma2, charisma3, charisma4]
charisma_removed = min(charisma_list)
charisma_list.remove(min(charisma_list))
charisma = sum(charisma_list)

print('''\
##############################################
################# STATISTICS #################
########### 4d6, drop the lowest: ############
##############################################''')
print(f'## STR: {strength:<4} ({strength_list[0]} + {strength_list[1]}\
 + {strength_list[2]} (a {strength_removed} was rerolled)) ##')
print(f'## DEX: {dexterity:<4} ({dexterity_list[0]} + {dexterity_list[1]}\
 + {dexterity_list[2]} (a {dexterity_removed} was rerolled)) ##')
print(f'## CON: {constitution:<4} ({constitution_list[0]} + {constitution_list[1]}\
 + {constitution_list[2]} (a {constitution_removed} was rerolled)) ##')
print(f'## INT: {intelligence:<4} ({intelligence_list[0]} + {intelligence_list[1]}\
 + {intelligence_list[2]} (a {intelligence_removed} was rerolled)) ##')
print(f'## WIS: {wisdom:<4} ({wisdom_list[0]} + {wisdom_list[1]}\
 + {wisdom_list[2]} (a {wisdom_removed} was rerolled)) ##')
print(f'## CHA: {charisma:<4} ({charisma_list[0]} + {charisma_list[1]}\
 + {charisma_list[2]} (a {charisma_removed} was rerolled)) ##')
print('''\
##############################################
##############################################''')
