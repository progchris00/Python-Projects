def besh_it(phrase):
    new_phrase = phrase.strip().split()
    return " ". join(f"{word} 🤸" for word in new_phrase)