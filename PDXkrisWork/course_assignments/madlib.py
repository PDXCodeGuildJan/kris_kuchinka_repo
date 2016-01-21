# Make a madlib that prompts a user for five words/phrases
# and then adds those to a silly story

plural_noun = input("Please choose a plural noun. ")
action_verb_1 = input("Please choose an action verb. ")
proper_noun = input("Please choose a Proper Noun. ")
bad_word = input("Please choose a 'bad' word. ")
action_verb_2 = input("Please choose another action verb. ")
final_sentence = " And that's where echoli comes from."

madlib = "When all the " + plural_noun + " had gathered at the coconut tree, they looked around and then suddenly " + action_verb_1 + ". Everybody was so afraid that they had insulted " + proper_noun + ", but that person just said '" + bad_word + "'-- I'm going to " + action_verb_2 + "."

madlib += final_sentence

print(madlib)