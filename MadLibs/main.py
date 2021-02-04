#Mad Libs Random Story Generator

class MadLibs:
    def _init_(self, word_descriptions, template):
        self.template = templateself.word_descriptions = word_descriptions 
#Template

#User Input
word_descriptions = ["noun", "verb"]
words = []
print("Please provide the following words: ")
for desc in word_descriptions:
    user_input = input(desc + " ")
    words.append(user_input)
print(words)
#Story Building