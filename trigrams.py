import io


def make_trigram(text):
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
    print tri_dict


def main(path):
    file = io.open(path, encoding='utf-8')
    read_file = file.read()
    return make_trigram(read_file)
    # print split_text(read_file)

main('test.txt')
