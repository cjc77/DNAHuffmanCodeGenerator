def make_dna_string():
    with open("DNASample.txt", "r") as text_file:
        dna_string = text_file.read().replace('\n', '')
        return dna_string


if __name__ == '__main__':
    make_dna_string()
