import io
import random
import sys


def make_trigram(text):
    """Make a dictionary of trigrams."""
    tri = {}
    text = text.split()
    {tri.setdefault(tuple(text[i:i + 2]), []).append(text[i + 2]) for i in range(0, len(text) - 2, 3)}
    return tri


def rand_words(dictionary):
    """Get a random key from dictionary and add key/value to story."""
    rand_key = random.choice(dictionary.keys())
    return [rand_key[0], rand_key[1], random.choice(dictionary[rand_key])]


def make_story(d, num_words):
    """Use dictionary to create story that is num_words long."""
    story = rand_words(d)
    while len(story) < num_words:
        last_words = (story[-2], story[-1])
        if last_words in d:
            story.append(random.choice(d[last_words]))
        else:
            story.extend(rand_words(d))
    return " ".join(story)


def read_file(fh):
    """Read a file and return the text."""
    with open(fh, "r") as f:
        file_text = f.read()
    return file_text


def clean_cli(argv):
    if len(argv) != 3:
        print("You didn't give us a file and a number")
        sys.exit(1)
    filename = argv[1]
    num_words = int(argv[2])
    return filename, num_words


if __name__ == "__main__":
    filename, num_words = clean_cli(sys.argv)
    print(make_story(make_trigram(read_file(filename)), num_words))
