# mRNA Codon to Amino Acid Translation

# Codon to amino acid mapping
codon_table = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': 'Stop', 'UAG': 'Stop',
    'UGU': 'C', 'UGC': 'C', 'UGA': 'Stop', 'UGG': 'W',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}

def translate_mrna_to_protein(mrna_sequence):
    """
    Translates an mRNA sequence into a protein sequence.
    :param mrna_sequence: String representing the mRNA sequence
    :return: Protein sequence as a string
    """
    protein_sequence = []
    # Ensure sequence length is a multiple of 3
    for i in range(0, len(mrna_sequence), 3):
        codon = mrna_sequence[i:i+3]
        if len(codon) == 3:  # Skip incomplete codons
            amino_acid = codon_table.get(codon, '?')  # '?' for unknown codons
            if amino_acid == 'Stop':
                break
            protein_sequence.append(amino_acid)
    return ''.join(protein_sequence)

# Example usage
if __name__ == "__main__":
    print("Welcome to the mRNA to Protein Translator!")
    mrna_input = input("Enter an mRNA sequence: ").upper()
    protein = translate_mrna_to_protein(mrna_input)
    print(f"Protein sequence: {protein}")
