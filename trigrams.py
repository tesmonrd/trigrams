import io
import random


def make_trigram(text):
    """Make a dictionary of trigrams."""
    tri_dict = {}
    while len(text.split(" ")) > 2:
        split_words = text.split(" ", 3)
        our_keys = (split_words[0], split_words[1])
        our_value = split_words[2]
        if our_keys not in tri_dict:
            tri_dict[our_keys] = [our_value]
        else:
            new_value = tri_dict.get(our_keys)
            new_value.append(our_value)
            tri_dict[our_keys] = new_value
        length = len(split_words[0]) + 1
        text = text[length:]
    return tri_dict


def make_story(dictionary, num_words):
    story = []
    rand_key = random.choice(dictionary.keys())
    rand_value = random.choice(dictionary[rand_key])
    first_stringify = str(rand_key[0])
    second_stringify = str(rand_key[1])
    story.extend([first_stringify, second_stringify, rand_value])
    while len(story) < num_words:
        last_words = (story[-2], story[-1])
        if last_words in dictionary:
            get_lastword = random.choice(dictionary[last_words])

            story.append(get_lastword)
        else:
            rand_key = random.choice(dictionary.keys())
            rand_value = random.choice(dictionary[rand_key])
            first_stringify = str(rand_key[0])
            second_stringify = str(rand_key[1])
            story.extend([first_stringify, second_stringify, rand_value])
    return " ".join(story)


def main(path, num_words):
    file = io.open(path, encoding='utf-8')
    read_file = file.read()
    trigrams = make_trigram(read_file)
    random_story = make_story(trigrams, num_words)
    print random_story


main('test.txt', 100)
