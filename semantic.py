import spacy

nlp = spacy.load('en_core_web_sm')

tokens = nlp('cat apple monkey banana fish')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# I do find it interesting that there is more similarity between monkey and banana than monkey and apple, which
# is funny because they eat bananas! The similarity between apples and bananas makes sense, both fruits,
# same with cats and monkeys. What is most interesting however is that banana is more similar to cat than apple
# for an unknown reason to me. I added fish as a test thinking it would be more similar to cat than to monkey,
# but surprisingly there isn't much difference, was applying the same logic as monkey and banana.

# Using the simpler model, apple is now more similar to monkey than banana, which is strange! Event more strange is,
# that apple and monkey are more similar than apple and banana. I guess because the model is simpler and
# doesn't have as much data to work with.

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

