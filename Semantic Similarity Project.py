# Synonyms - Nivetha Sathish
#Semantic Similarity: starter code

import math


def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 3.
    '''

    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    # take two dictionaries and see how similar they are
    # 15 + 8 = 23    add up the multiplication of stuff they both show up in
    # bottom = root(1078)   always the same

    first_length = len(vec1)
    second_length = len(vec2)
    numerator = 0
    denom_one = 0
    denom_two = 0
    cos_similarity = 0

    if first_length >= second_length:
        # loop through second vector
        for i in vec2:
            if i in vec1: # they both contain the same key
                #print(vec1)
                #print(i)
                numerator = numerator + (vec1[i] * vec2[i])

    elif second_length > first_length:
        # loop through first vector
        for i in vec1:
            if i in vec2: # they both contain the same key
                numerator = numerator + (vec1[i] * vec2[i])

    for i in vec1:
        denom_one = denom_one + (vec1[i]**2)

    for i in vec2:
        denom_two = denom_two + (vec2[i]**2)

    cos_similarity = numerator / (math.sqrt(denom_one * denom_two))

    return cos_similarity

    pass


#print(cosine_similarity({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}))

def build_semantic_descriptors(sentences):

# example of sentences, each sentence will be a list inside of the list of text
    ''''[["i", "am", "a", "sick", "man"],
["i", "am", "a", "spiteful", "man"],
["i", "am", "an", "unattractive", "man"],
["i", "believe", "my", "liver", "is", "diseased"],
["however", "i", "know", "nothing", "at", "all", "about", "my",
"disease", "and", "do", "not", "know", "for", "certain", "what", "ails", "me"]],
'''
    # make a list of all unique words
    # go through each word and if it's in a sentence, check to see if any other words are also in that sentence
    # if a word is also in that sentence,

    list_words = [] # list of words in the whole text
    new = []

    # make a list of all words
    for i in sentences: # loop through sentences
        for k in i: # loop through the words in the sentence
            if k not in list_words:
                #print(k)
                list_words.append(k)
            else:
                pass


    words = {} # make a dictionary that contains words, and also contains the words that appear with it in the same sentence
    list_words = [x.lower() for x in list_words]

    for i in list_words:
        words[i] = {}

    #print(words)


    # add each word to the words dictionary

    for i in list_words:
        #print("list words: " + i)
        for k in sentences: # loop through sentences
            if i in k: # if the word we're looking at is in the current sentence
                for other in list_words: # loop through all words

                    if other == i: # if it's the same word, don't add it
                        pass

                    else: # if it's not the same work

                        if other in k: # if another word's in the same sent, add it

                            try:
                                words[i][other]
                            except KeyError:
                                present = False
                            else:
                                present = True
                            if present:
                                words[i][other] = words[i][other] + 1
                            else:
                                words[i][other] = 1

                            '''if words[i][other] not in words:
                                words[i][other] = 1
                            else:
                                words[i][other] = words[i][other] + 1'''


    return words
    pass

sentences = [["i", "am", "a", "sick", "man"],
["i", "am", "a", "spiteful", "man"],
["i", "am", "an", "unattractive", "man"],
["i", "believe", "my", "liver", "is", "diseased"],
["however", "i", "know", "nothing", "at", "all", "about", "my",
"disease", "and", "do", "not", "know", "for", "certain", "what", "ails", "me"]]
#print(build_semantic_descriptors(sentences))

def build_semantic_descriptors_from_files(filenames):

    # each sentence array of words needs to go into a bigger array

    file = open(filenames[0], "r", encoding="latin1")
    text = file.read()

    # open all files and put them all into one string of text
    for i in range(1, len(filenames)):
        addition = open(filenames[i], "r", encoding="latin1")
        addition_text = addition.read()
        text = text + addition_text

    #file = open("extest.txt.py")

    text = text.replace(",", "") # delete commas
    text = text.replace("!", ".") # replace exclamations with periods
    text = text.replace("?", ".") # replace questions with periods
    text = text.replace(":", "")
    text = text.replace(";", "")
    text = text.replace("-", " ")
    text = text.replace("--", " ")

    text = text.replace("\n", " ") # replace new lines with spaces

    words = text.split(".") # actually sentences

    #print(words)

    words = [x.lower() for x in words]


    # now, split each item in word into its own array of words and put it back in
    for i in range (0, len(words)):

        words[i] = words[i].split(" ")


    for i in range(0, len(words)):
        #words[i] = filter(None, words[i])
        words[i] = list(filter(None, words[i]))

    #print(words)

    semantic = build_semantic_descriptors(words)
    return semantic

    pass

filenames = ["extest.txt.py", "secondexample.py", "thirdexample.py"]

#print(build_semantic_descriptors_from_files(filenames))

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):

    word_one = word
    highest_similarity = 0
    element = 0

    for i in range(0, len(choices)):
        one = semantic_descriptors[word_one]
        word_choice = choices[i]

        if word_choice in semantic_descriptors:
            semantic_choice = semantic_descriptors[word_choice]
            current_similarity = similarity_fn(one, semantic_choice)

        else:
            current_similarity = 0

        if current_similarity > highest_similarity:
            highest_similarity = current_similarity
            element = i

    return choices[element] # returns the element
    pass

def run_similarity_test(filename, semantic_descriptors, similarity_fn):

    # split into array of different lines, for the different questions
    # split each item into an array of words based on the spaces
    # the first word is what we're comparing the words after the second word to

    questions_file = open(filename)
    questions_everything = questions_file.read()

    questions = questions_everything.split("\n")
    out_of = len(questions)
    current_choice = ""
    highest_similarity = 0
    num_correct = 0

    #questions.pop(len(questions) - 1) # remove empty line

    for i in range (0, len(questions)):
        questions[i] = questions[i].split(" ")  # split the questions into words



    for i in range(0, len(questions)): # now start answering questions
        #for k in questions[i]: # go through the words in a question
        #print(questions[i])
        #print(questions)
        q = questions[i][0]
        a = questions[i][1]
        q_dict = semantic_descriptors[q]

        # when answering question:
        # loop through choices and see which choice has a higher sim
        # if all have same, return first, otherwise return highest
        # keep a running total of the highest similarity

        highest_similarity = 0 # reset highest similarity

        for e in range (2, len(questions[i])):
            choice = questions[i][e]
            #print("OPTIONS")
            #print(choice)
            #print(q)

            if choice in semantic_descriptors:
                choice_dict = semantic_descriptors[choice]
                current_similarity = similarity_fn(q_dict, choice_dict)
            else:
                current_similarity = 0

            if current_similarity > highest_similarity:
                current_choice = choice
                highest_similarity = current_similarity

        #print("Current choice is: " + current_choice)
        if current_choice == a:
            num_correct = num_correct + 1

    percent = (num_correct/out_of) * 100

    return percent

    pass

#sem_descriptors = build_semantic_descriptors_from_files(["mydescriptors.py"])
#print(sem_descriptors)
#res = run_similarity_test("trialtest.txt", sem_descriptors, cosine_similarity)
#print(res, "of the guesses were correct")

#sem_descriptors = build_semantic_descriptors_from_files(["sample_case.txt"])
#print(sem_descriptors)
#res = run_similarity_test("sample_test.txt", sem_descriptors, #cosine_similarity)
#print(res, "of the guesses were correct")

#sem_descriptors = build_semantic_descriptors_from_files(["swann'sway.txt", "warandpeace.txt"])
#sem_descriptors = build_semantic_descriptors_from_files(["mydescriptors.py"])
#print(sem_descriptors)

#res = run_similarity_test("test.txt", sem_descriptors, cosine_similarity)
#print(res, "of the guesses were correct")
#run_similarity_test("swann'sway.txt", )

#sem_desc = {"dog": {"cat": 1, "food": 1},"cat": {"dog": 1}}
#most_similar_word("dog", ["cat", "rat"], sem_desc,cosine_similarity)
#print(most_similar_word("dog", ["cat", "rat"], sem_desc,cosine_similarity))


