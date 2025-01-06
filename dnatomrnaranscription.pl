#!/usr/bin/perl -w
# This script performs the transcription of a DNA sequence into an RNA sequence.

# Define the DNA sequence to be transcribed.
# For simplicity, the sequence is hard-coded here, but it can be modified or input dynamically if needed.
$DNA = 'ATATAGATAGATCGCTCGTAGAGATAGCTTCGGCCTCGATAGCTTCTAGGATAATATAGAGATATAGGTTGCGCTAGATAGCTGATAGCTGAGGATCGGCGCGTGATCGGCTCTCTCTCTGGAAAAATAGT';

# Print the original DNA sequence.
print "Here is the DNA to be transcribed:\n\n";
print "$DNA\n";

# Transcription: Convert the DNA sequence to RNA by replacing all occurrences of 'T' with 'U'.
# Explanation:
# - The `=~` operator binds the variable `$RNA` to the substitution operation.
# - The `s/T/U/g` command substitutes 'T' with 'U' globally (i.e., throughout the entire string).
$RNA = $DNA;
$RNA =~ s/T/U/g;

# Print the transcribed RNA sequence.
print "Here is the transcribed RNA:\n\n";
print "$RNA\n";

# Exit the program.
exit;
