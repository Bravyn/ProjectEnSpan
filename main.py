def translate_to_spanish(word):
    english_suffix = "tion"
    spanish_suffix = "ción"
    plural_suffix = "es"
    if word.endswith(english_suffix):
        spanish_word = word[:-len(english_suffix)] + spanish_suffix
        if word.endswith("s" + english_suffix):
            # Handle pluralization
            spanish_word += plural_suffix
        return spanish_word
    else:
        return None

# Example usage:
english_words = ['education', 'creation', 'inspiration', 'perception', 'communication',
              'motivation', 'revolution', 'association', 'evaluation', 'generation', 'suggestion']

spanish_translations = [translate_to_spanish(word) for word in english_words]
print(spanish_translations)
