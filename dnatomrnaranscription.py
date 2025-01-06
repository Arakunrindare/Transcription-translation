# DNA to mRNA Transcription

def transcribe_dna_to_mrna(dna_sequence):
    """
    Converts a DNA sequence to an mRNA sequence by replacing T with U.
    
    :param dna_sequence: String representing the DNA sequence
    :return: String representing the transcribed mRNA sequence
    """
    # Replace 'T' with 'U' to transcribe DNA to mRNA
    mrna_sequence = dna_sequence.upper().replace('T', 'U')
    return mrna_sequence

if __name__ == "__main__":
    print("Welcome to the DNA to mRNA Transcription Program!")
    dna_input = input("Enter a DNA sequence: ").strip()
    mrna_output = transcribe_dna_to_mrna(dna_input)
    print(f"Transcribed mRNA sequence: {mrna_output}")
