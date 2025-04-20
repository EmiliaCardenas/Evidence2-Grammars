import nltk
from nltk import CFG

# Define the grammar on the established structure
korean_grammar = CFG.fromstring("""
    S -> NSC VS | NSC VS NSC | S Conj S | NSC VS Conj VS | NSC VS Conj NSC VS
    S -> NSC NSC VS
    NSC -> NP | NP Conj NP
    NP -> CR SubjParticle | CR ObjParticle | CR | CR NP
    VS -> VoR TenseMarker PolitenessEnding | VoR PolitenessEnding | VoR
    VS -> VoR TenseEnding
    VoR -> 'gada' | 'meokda' | 'masida' | 'boda' | 'malhada' | 'saranghada'
    TenseMarker -> 'at' | 'eot'
    PolitenessEnding -> 'eoyo' | 'seumnida'
    SubjParticle -> 'eun' | 'neun' | 'i' | 'ga'
    ObjParticle -> 'eul' | 'reul'
    CR -> 'haksaeng' | 'seonsaengnim' | 'chingu' | 'mul' | 'jib' | 'haksang' | 'kpop' | 'aideol' | 'eumak' | 'norae' | 'albom'
    Conj -> 'geurigo' | 'ttoneun' | 'hajiman' | 'waenyaheumyeon'
""")
# Create the parser
korean_parser = nltk.ChartParser(korean_grammar)

# Function to parse a sentence and print its syntax tree
def parse_sentence(sentence):
    sentence_tokens = sentence.split()
    try:
        for tree in korean_parser.parse(sentence_tokens):
            tree.pretty_print() 
            return True
    except ValueError:
        print(f"Invalid sentence: {sentence}")
        return False

# List of correct and incorrect sentences
correct_sentences = [
    'haksaeng eul meokda',
    'chingu eul meokda geurigo saranghada',
    'seonsaengnim i masida',
    'haksaeng eun norae reul masida',
    'jib eul meokda eoyo',
    'haksaeng i saranghada eoyo',
    'mul eul malhada',
    'haksaeng eul meokda hajiman chingu eul malhada',
    'seonsaengnim eun haksaeng eul saranghada',
    'haksaeng i meokda geurigo seonsaengnim i malhada',
    'haksaeng eul malhada',
    'haksaeng i saranghada',  
    'seonsaengnim eul masida'
]

incorrect_sentences = [
    'jib masida wa chingu eul meokda',
    'seonsaengnim i meokda wa haksaeng eul saranghada',
    'chingu eul masida wa jib eul meokda',
    'albom eul meokda eoyoseo norae masida',
    'kpop eul meokda wa eumak eul masida',
    'haksaeng eun haksang eul meokda wa seonsaengnim eul masida'
]

# Function to run the tests
def run_tests():
    print("Testing valid sentences:")
    for sentence in correct_sentences:
        print(f"Testing: {sentence}")
        parse_sentence(sentence)

    print("\nTesting invalid sentences:")
    for sentence in incorrect_sentences:
        print(f"Testing: {sentence}")
        parse_sentence(sentence)

# Main program to run the tests
if __name__ == "__main__":
    run_tests()

    # Allow the user to input a sentence to test
    user_sentence = input("\nEnter a sentence to test (in Korean): ")
    parse_sentence(user_sentence)
