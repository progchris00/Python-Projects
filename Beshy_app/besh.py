import emoji

def besh_it():
    phrase = "bakit malungkot"
    cartwheel = emoji.emojize(":man_cartwheeling:")
    new_phrase = phrase.strip().split()
    return " ". join(f"{word} {cartwheel}" for word in new_phrase)