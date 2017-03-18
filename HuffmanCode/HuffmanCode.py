class DNAHuffmanCode:

    def __init__(self, DNA):
        self.DNA = DNA
        self.bin_DNA = ''
        self.DNA_weight = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
        self.bin_code = {'A': '00', 'T': '01', 'G': '10', 'C': '11'}

    def __str__(self):
        char_weight = "DNA character weights: "
        char_code = "DNA character codes: "
        print_str = char_weight + str(self.DNA_weight) + '\n' + char_code + str(self.bin_code)
        return print_str

    def create_weight(self):
        """
        Examine the genome of dna_sample and create dictionary
        with weights for A, T, G, C.
        """
        for c in self.DNA:
            if c == 'A':
                self.DNA_weight['A'] += 1
            elif c == 'T':
                self.DNA_weight['T'] += 1
            elif c == 'G':
                self.DNA_weight['G'] += 1
            elif c == 'C':
                self.DNA_weight['C'] += 1

    def create_bin_code(self):
        """
        Create the binary translation based on frequency of occurance
        of each character 'A', 'T', 'G', 'C'
        """
        # Create list to hold DNA chars and associated weights
        DNA_weight_map = [[key, val] for key, val in self.DNA_weight.items()]
        # Sort this list by: most common character -> least common character
        DNA_weight_map.sort(key=lambda x: x[1], reverse=True)
        size = len(DNA_weight_map)
        # go through the weight map and assign ('1' * i) + '0' to each char
        # except the least frequent, which will be '1' * (size - 1)
        bin_string = ''
        for i in range(size):
            # If most common
            if(i < 1):
                bin_string = '0'
            # If not most or least common
            elif i < size - 1:
                bin_string = '1' + bin_string
            # If least common
            else:
                bin_string = '1' * (size - 1)
            self.bin_code[DNA_weight_map[i][0]] = bin_string

    def convert_dna_to_bin_dna(self):
        size = len(self.DNA)
        for i in range(size):
            if self.DNA[i] == 'A':
                self.bin_DNA += self.bin_code['A']
            elif self.DNA[i] == 'T':
                self.bin_DNA += self.bin_code['T']
            elif self.DNA[i] == 'G':
                self.bin_DNA += self.bin_code['G']
            elif self.DNA[i] == 'C':
                self.bin_DNA += self.bin_code['C']











#
