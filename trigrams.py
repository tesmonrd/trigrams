import io
import random
import sys


def make_trigram(text):
    """Make a dictionary of trigrams."""
    tri_dict = {}
    while len(text.split(" ")) > 2:
        split_words = text.split(" ", 3)
        our_keys = (split_words[0], split_words[1])
        our_value = split_words[2]
        tri_dict.setdefault(our_keys, []).append(our_value)
        length = len(split_words[0]) + 1
        text = text[length:]
    return tri_dict


def rand_words(dictionary, story):
    """Get a random key from dictionary and add key/value to story."""
    rand_key = random.choice(dictionary.keys())
    first = str(rand_key[0])
    second = str(rand_key[1])
    third = random.choice(dictionary[rand_key])
    story.extend([first, second, third])
    return story


def make_story(dictionary, num_words):
    """Use dictionary to create story that is num_words long."""
    story = []
    rand_words(dictionary, story)
    while len(story) < num_words:
        last_words = (story[-2], story[-1])
        if last_words in dictionary:
            get_lastword = random.choice(dictionary[last_words])

            story.append(get_lastword)
        else:
            rand_words(dictionary, story)
    return " ".join(story)


def read_file(fh):
    """Read a file and return the text."""
    file = io.open(fh, encoding='utf-8')
    file_text = file.read()
    file.close()
    return file_text


def main(path, num_words):
    """Process make_trigram and make_story to create new story."""
    text = read_file(path)
    trigrams = make_trigram(text)
    random_story = make_story(trigrams, num_words)
    print random_story


def clean_cli(argv):
    if len(argv) != 3:
        print "You didn't give us a file and a number"
        sys.exit(1)
    filename = argv[1]
    num_words = int(argv[2])
    return filename, num_words


if __name__ == "__main__":
    filename, num_words = clean_cli(sys.argv)
    main(filename, num_words)
