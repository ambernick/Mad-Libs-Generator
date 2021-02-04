#Mad Libs Random Story Generator

class MadLibs:
    def _init_(self, word_descriptions, template):
        self.template = templateself.word_descriptions = word_descriptions 


def get_words_from_user(word_descriptions):
    words = []
    print("Please provide the following words: ")
    for desc in word_descriptions:
        user_input = input(desc + " ")
        words.append(user_input)
    return words

#Story Building
def build_story(template, words):
    story = template.format(*words)
    return story

template = "I own a big {}. I like to {}."
words = get_words_from_user(["noun", "verb"])
story = build_story(template, words)

print(story)

