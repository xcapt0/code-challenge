import re

def same_structure_as(original,other):
    original, other = str(original), str(other)  
    return re.sub(r'\d|(\'.\')', '', original) == re.sub(r'\d|(\'.\')', '', other)