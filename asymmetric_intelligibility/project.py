# TODO track shape of words to determine when cognate sounds are lining up vs when inserted/deleted
# NOTE how to count unmatched words (like Italian "lo" below - it has a cognate but not this syntax)

# already spotted issues with calculation based naïvely on phonology:
# - when there's tolerance for variation:
#    - It sono varies with son#
#    - mio or mia would be transparent though quirky bc Spanish has OTHER words matching those
# - when variation is less clear than it should be:
#    - mi ami vs me amas (when hear -i not thinking 2.s. form in Spanish, also sounds like "Miami")
# - word length, word order, little differences
# - things that could be understood even though not said ("io sì lo so che..." )
# - presence or absence of pronouns major signal and could clarify It 2.s. -i

def recursive_levenshtein(a, len_a, b, len_b):
    """Basic implementation of Levenshtein distance algorithm"""
    cost = 0

    # empty string
    if len_a == 0: return len_b
    if len_b == 0: return len_a

    # last character match
    if a[len_a-1] == b[len_b-1]:
        cost = 0
    else:
        cost = 1

    return min( \
        recursive_levenshtein(a, len_a-1, b, len_b) + 1, \
        recursive_levenshtein(a, len_a, b, len_b-1) + 1, \
        recursive_levenshtein(a, len_a-1, b, len_b-1) + cost \
    )


def track_distances():
    distances = {}      # 'language_pair': [costs, lengths]
    def update_distances(language_pair='', cost=0, length=0):
        if not language_pair or language_pair not in distances: return None
        distances[language_pair][0] += cost
        distances[language_pair][1] += length
        return distances[language_pair][0] / distances[language_pair][1]
    return update_distances

def levenshtein(a, b):
    """Measure the Levenshtein distance for transforming source to targets"""
    # Basis: http://www.let.rug.nl/gooskens/pdf/publ_langvarch_2004.pdf
    # NOTE using crosshatch to signal void segment in position where alter has a sound
    cost = 0
    for i in range(len(a)):
        print("{0} vs {1} - {2} of {3} (or for b: {4})".format(a, b, i, len(a), len(b)))
        # count any insertions, deletions, substitutions
        if i < len(b) and a[i] != b[i]: cost += 1
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
    return (transforms['costs'], transforms['lengths'])

def manage_levenshteins(lang_a, lang_b, utterance_a, utterance_b):
    update_distances = track_distances()
    lang_pair = '{0}_{1}'.format(lang_a, lang_b)
    levenshtein = yield_levenshteins(utterance_a, utterance_b)
    update_distances and update_distances(language_pair=lang_pair, cost=levenshtein[0], length=levenshtein[1])
    return update_distances(language_pair=lang_pair)

def test_levenshteins():
    sentences = {
        '1': {
            'es': {
                'yo sí sé que me amas': 'jo si se ke me amas'
            },
            'it': {
                'io sì lo so che mi ami': 'io si [lo] so ke mi ami#'
            }
        },
        '2': {
            'es': {
                'dice que no habla latín': 'di#se ke no aβla latin#'
            },
            'it': {
                'dice che non parla latino': 'ditʃe ke non [parla] latino'
            }
        },
        '3': {
            'es': {
                'pero también dijo que sí': 'pero tambjen di#ho ke si'
            },
            'it': {
                'però anche disse di sì': 'perɔ [anke] disse [di] si'
            }
        },
        '4': {
            'es': {
                'fue un placer': 'fwe un pla#seɾ#'
            },
            'it': {
                'fu un piacere': 'fu# un pjatʃere'
            }
        },
        '5': {
            'es': {
                'sabes cuántos países hay en el mundo': 'saβes kwantos paises aj en el mundo'
            },
            'it': {
                'sai quanti paesi ci sono nel mondo': 'sa#i# kwanti# paesi# [ci] [sono] #n el mondo'
            }
        }
        
    }
    for s in sentences.keys():
        test_yields = yield_levenshteins(sentences[s][es], sentences[s][it])
        print(test_yields)
    return

test_levenshteins()
