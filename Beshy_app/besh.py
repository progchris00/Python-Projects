import emoji

def besh_it(phrase):
    cartwheel = emoji.emojize(":man_cartwheeling:")
    new_phrase = phrase.strip().split()
    return " ". join(f"{word} {cartwheel}" for word in new_phrase)