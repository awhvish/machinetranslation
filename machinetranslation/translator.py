from deep_translator import MyMemoryTranslator 


def englishtofrench(word):
    translated_word = MyMemoryTranslator(source='english', target='french').translate(word)
    return translated_word

def frenchtoenglish(word):
    translated_word = MyMemoryTranslator(source='french', target='english').translate(word)
    return translated_word
