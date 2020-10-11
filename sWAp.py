text = "ThiS iS 'viCTop' ColLegE"

def swap_case():
    newstring = ""
    for t in text:
        if t.isupper() == True:
            newstring += (t.lower())
            
        elif t.islower() == True:
            newstring += (t.upper())
        elif t.isspace() == True:
            newstring += t
    return newstring
print(swap_case())