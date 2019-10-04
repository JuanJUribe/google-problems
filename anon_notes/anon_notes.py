def anon_note_checker(magazine, note):
    magazine_words = magazine.lower().split()
    words_needed = note.lower().split()
    for word in words_needed:
        if word in magazine_words:
            magazine_words.remove(word)
        else:
            return False
    return True