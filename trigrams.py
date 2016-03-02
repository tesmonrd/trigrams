import io


def main(path):
    file = io.open(path)
    read_file = file.read()
    print read_file
    
main('test.txt')
