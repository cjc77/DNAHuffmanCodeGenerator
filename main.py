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



if __name__ == '__main__':
    main()
