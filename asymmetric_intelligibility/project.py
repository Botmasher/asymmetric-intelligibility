entries_es = {
    'yo': ['j', 'o'],
    'tú': ['t', 'u'],
    'sé': ['s', 'e'],
    'que': ['k', 'e'],
    'sí': ['s', 'i'],
    'lo': ['l', 'o'],
    'es': ['e', 's'],
    'son': ['s', 'o', 'n'],
    'mi': ['m', 'i'],
    'mis': ['m', 'i', 's'],
    'tu': ['t', 'u'],
    'tus': ['t', 'u', 's'],
    'mí': ['m', 'i'],
    'me': ['m', 'e'],
    'a': ['a'],
    'amo': ['a', 'm', 'o'],
    'amas': ['a', 'm', 'a', 's'],
    'un': ['u', 'n'],
    'una': ['u', 'n', 'a'],
    'persona': ['p', 'e', 'ɾ', 's', 'o', 'n', 'a'],
    'feliz': ['f', 'e', 'l', 'i', 's']
}

entries_it = {
    'io': ['i', 'o'],
    'tu': ['t', 'u'],
    'so': ['s', 'ɔ'],
    'che': ['k', 'e'],
    'sì': ['s', 'i'],
    'lo': ['l', 'o'],
    'è': ['ɛ'],
    'sono': ['s', 'o', 'n', 'o'],
    'mio': ['m', 'i', 'o'],
    'mia': ['m', 'i', 'a'],
    'miei': ['m', 'j', 'ɛ', 'i'],
    'mie': ['m', 'i', 'e'],
    'tuo': ['t', 'u', 'o'],
    'tua': ['t', 'u', 'a'],
    'tui': ['t', 'u', 'i'],
    'tue': ['t', 'u', 'e'],
    'me': ['m', 'e'],
    'a': ['a'],
    'amo': ['a', 'm', 'o'],
    'ami': ['a', 'm', 'i'],
    'un': ['u', 'n'],
    'una': ['u', 'n', 'a'],
    'persona': ['p', 'e', 'r', 's', 'o', 'n', 'a'],
    'felice': ['f', 'e', 'l', 'i', 'tʃ', 'e']
}

utterance_es_0 = 'yo sí sé que me amas'
utterance_it_0 = 'io sì lo so che mi ami'

# already spotted issues with calculation based naïvely on phonology:
# - when there's tolerance for variation:
#    - It sono varies with son#
#    - mio or mia would be transparent though quirky bc Spanish has OTHER words matching those
# - when variation is less clear than it should be:
#    - mi ami vs me amas (when hear -i not thinking 2.s. form in Spanish, also sounds like "Miami")
# - word length, word order, little differences
# - things that could be understood even though not said ("io sì lo so che..." )
# - presence or absence of pronouns major signal and could clarify It 2.s. -i

def levenshtein(a, b):
    """Measure the Levenshtein distance for transforming source to targets"""
    # Basis: http://www.let.rug.nl/gooskens/pdf/publ_langvarch_2004.pdf
    # NOTE using crosshatch to signal void segment in position where alter has a sound
    cost = 0
    for i in range(len(a)):
        if a[i] != b[i]: cost += 1
        # check that it counts the following:
        # - insert sound
        # - delete sound
        # - substitute sound
    # divide by length
    distance =  cost / len(a)
    return distance

def phonetic_distance(word_a, word_b):
    """Measure the difficulty of transforming a cognate's sounds from one language into another language"""
    # TODO this calculation is a standin - start from process overviewed in Moberg et al
    return abs(len(word_a) - len(word_b))

def conditional_entropy(words_a=[], words_b=[]):
    """Sum the entropies of sounds in one language's word list given cognates of those words in another language"""
    if len(a) != len(b): return
    sum_entropy = 0
    for i in range(words_a):
        entropy = 0
        sum_entropy += 0
    return sum_entropy
