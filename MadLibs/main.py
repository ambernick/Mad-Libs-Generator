#Mad Libs Random Story Generator

class MadLibs:
    def _init_(self, word_descriptions, template):
        self.template = templateself.word_descriptions = word_descriptions 
#Template

#User Input
def get_words_from_user(word_descriptions):
    words = []
    print("Please provide the following words: ")
    for desc in word_descriptions:
        user_input = input(desc + " ")
        words.append(user_input)
    return words
words = get_words_from_user(["noun", "verb"])
print(words)

#Story Building