import constants
import copy

#print(constants.PLAYERS)

# Write the logic to:
# 1) Read the existing player data from the PLAYERS constants provided
# in constants.py

# 2) Clean the player data without changing the original data!
# Data to be cleaned:
# * Height: This should be saved as an integer
# * Experience: This should be saved as a boolean value(True or False)

# 3) Save it to a new collection - build a new collection with what you
# have learned up to this point.

# HINT: Think Lists with nested Dictionaries might be one way
# NOTe: Ensure you **do not directly modify the data in PLAYERS or TEAMS
# constants. This data you should iterate and read from to build your own
# collection and would be ideal to clean the data as you loop over it
# building your new collection. If you are unsure of what this means,
# checkout this instruction step.

# 1) check!

# 2) - 
unchanged_PLAYERS = copy.deepcopy(constants.PLAYERS)
#print(unchanged_PLAYERS)

"""
def getList(dict):
    list = []
    for key in dict.keys():
        list.append(key)
    
    return list

print(getList(unchanged_PLAYERS[0]))
"""