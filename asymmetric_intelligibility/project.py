# TODO track shape of words to determine when cognate sounds are lining up vs when inserted/deleted
# NOTE how to count unmatched words (like Italian "lo" below - it has a cognate but not this syntax)

sentence_es = 'yo sí sé que me amas'
utterance_es = 'jo si se ke me amas'
sentence_it = 'io sì [lo] so che mi ami'
utterance_it = 'io si so ke mi ami#'

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
        print("{0} vs {1} - {2} of {3} (or for b: {4})".format(a, b, i, len(a), len(b)))
        # count any insertions, deletions, substitutions
        if i < len(b) and a[i] != b[i]: cost += 1
    # divide by length
    distance =  cost / len(a)
    return (cost, len(a))

def yield_levenshteins(utterance_a, utterance_b):
    """Iterate through formatted utterance phonemes and compare Levenshtein distances"""
    # normalize
    words_a = utterance_a.split()
    words_b = utterance_b.split()
    words_a = [word for word in words_a if word[0] != "[" and word[len(word)-1] != "]"]
    words_b = [word for word in words_b if word[0] != "[" and word[len(word)-1] != "]"]
    # calculate total distance
    transforms = {'costs': 0, 'lengths': 0}
    for i in range(len(words_a)):
        distance = levenshtein(words_a[i], words_b[i])
        transforms['costs'] += distance[0]
        transforms['lengths'] += distance[1]
    return transforms['costs'] / transforms['lengths']

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

test_yields = yield_levenshteins(utterance_es, utterance_it)
print(test_yields)
