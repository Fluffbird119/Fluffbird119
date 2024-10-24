string_to_split = 'Beautiful, is; better*than\nugly ><><><><>>><><'
splitString = []
import re
splitString = re.split('|\>|<', string_to_split)

print(splitString)