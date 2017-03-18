from Utilities import DNAString as DS
from HuffmanCode import HuffmanCode as HC

def write_out(encoded_dna):
    with open("bin_DNASample.txt", "w") as text_file:
        text_file.write(encoded_dna)
    text_file.close()


def main():
    dna_sample = DS.make_dna_string()
    my_code = HC.DNAHuffmanCode(dna_sample)
    my_code.create_weight()
    print("BEFORE Huffman Coding: ", my_code, '\n', sep='\n')
    my_code.create_bin_code()
    print("AFTER Huffman Coding: ", my_code, '\n', sep='\n')
    my_code.convert_dna_to_bin_dna()
    write_out(my_code.bin_DNA)
    lengths_match = my_code.verify_encoding_len()
    saved = my_code.bits_saved()
    print("Encoded accurately: ", lengths_match, '\n', "Bits saved: ", saved, sep='')

    naive_case = len(my_code.DNA) * 2
    # If you are using more bits with the huffman encoding than the naive encoding
    if saved < naive_case:
        print("Less efficient than naive encoding.")
    # If you are saving less than 5%
    elif saved < (naive_case * .05):
        print("Naive encoding is sufficient.")
    # If you are saving at least 5%
    elif saved <= (naive_case * .05):
        print("Huffman encoding is recommended.")


if __name__ == '__main__':
    main()
