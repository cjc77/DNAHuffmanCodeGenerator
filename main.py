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
    comparison = my_code.huffman_vs_naive()
    percent_diff = ((comparison['Huffman'] - comparison['Naive']) /
                    (comparison['Huffman'] + comparison['Naive'])) * 100
    print("Huffman vs. Naive ('-' means Huffman more efficient)")
    print("Difference: ", str(comparison["Difference"]) + " bits")
    print("Percent Difference", percent_diff)
    if percent_diff > 0:
        print("Huffman Less Efficient")
    else:
        print("Huffman More Efficient")



if __name__ == '__main__':
    main()
