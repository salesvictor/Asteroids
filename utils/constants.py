# Actions
FORWARD = 0
TURN_LEFT = 1
TURN_RIGHT = 2
SHOOT = 3

# Information for bot to predict which actions it should take
# Inputs (normalized):
#   x and y of player
#   x and y of player's speed
#   direction of player
#   x and y of closest enemy in each of 4 circular sections
#   x and y of closest enemy's speed
#
# Outputs:
#   forward
#   turn right
#   turn left
#   shoot
N_INPUTS = 16
N_OUTPUTS = 4
