# https://github.com/yuce/pyswip
from pyswip import Prolog

# path to https://github.com/jan-Lope/Toki_Pona-Parser
prolog_path = "../prolog/"

# NOTE: ENSURE YOUR LIBRARY IS UPDATED
# https://github.com/yuce/pyswip/issues/143
Prolog.consult('toki-pona-grammar-rules.pro', relative_to=prolog_path)
Prolog.consult('toki-pona-official-words.pro', relative_to=prolog_path)
Prolog.consult('toki-pona-io-rules.pro', relative_to=prolog_path)

# Ideally, we should not use these, and instead support arbitrary names...
# TODO change in a rewrite
Prolog.consult('toki-pona-unofficial-words-continents.pro', relative_to=prolog_path)
Prolog.consult('toki-pona-unofficial-words-countries.pro', relative_to=prolog_path)
Prolog.consult('toki-pona-unofficial-words-cities.pro', relative_to=prolog_path)
Prolog.consult('toki-pona-unofficial-words-languages.pro', relative_to=prolog_path)
Prolog.consult('toki-pona-unofficial-words-ideologies.pro', relative_to=prolog_path)
Prolog.consult('toki-pona-unofficial-words-communities.pro', relative_to=prolog_path)
Prolog.consult('toki-pona-unofficial-words-female-prominent-personages.pro', relative_to=prolog_path)
Prolog.consult('toki-pona-unofficial-words-male-prominent-personages.pro', relative_to=prolog_path)
Prolog.consult('toki-pona-unofficial-words-female-names.pro', relative_to=prolog_path)
Prolog.consult('toki-pona-unofficial-words-male-names.pro', relative_to=prolog_path)
Prolog.consult('toki-pona-unofficial-words-persons.pro', relative_to=prolog_path)
Prolog.consult('toki-pona-unofficial-words-movies.pro', relative_to=prolog_path)
Prolog.consult('toki-pona-unofficial-words-miscellaneous.pro', relative_to=prolog_path)

## Parses a string in Prolog's notation into a more structured data type.
def internal_parse_prolog(prolog: str):
    return # TODO implement

## A reimplementation of the provided codelist query.
## Theirs reads from stdin, which we don't want to deal with...
def codelist(sentence: str) -> list[chr]:
    sentence = sentence \
        .replace("!", " ! ") \
        .replace(",", " , ") \
        .replace(".", " . ") \
        .replace(":", " : ") \
        .replace(";", " ; ") \
        .replace("?", " ? ")
    return [ord(char) for char in sentence]

## Queries whether a string is valid Toki Pona, returning the parses.
def query(sentence: str) -> list[str]:
    chars = codelist(sentence)
    query = 'wordlist(WL,{},[]), paragraph(P,WL,[]).'.format(chars)
    # Note: here is the logic of the prolog query in a more Pythonic format:
    #   WL = wordlist({})
    #   P = paragraph(WL)
    #   return {'WL': WL, 'P': P}
    # print("debug: query is {}".format(query))

    result = list(Prolog.query(query))
    # print("debug: result is {}".format(result))

    return [res['P'] for res in result]

## Queries whether a string is valid Toki Pona, throwing away the parses.
def valid(sentence: str):
    if len(query(sentence)) != 0:
        print("valid!")
    else:
        print("invalid...")

if __name__ == "__main__":
    print("toki!! o pana e toki ona:")
    while True:
        sentence = input()
        print(query(sentence))
        valid(sentence)
