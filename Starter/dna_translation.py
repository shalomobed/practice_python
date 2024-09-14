import helper
from helper import chunk
from helper import amino_acids


def transcription(dna_sequence):
    mrna = dna_sequence.replace("T", "U")
    complement = ""
    for x in mrna:
        if x == "A":
            complement += "U"
        elif x == "U":
            complement += "A"
        elif x == "C":
            complement += "G"
        elif x == "G":
            complement += "C"
    return complement


def translation(mrna):
    protein = ""
    triplets = chunk(mrna, 3)
    for triplet in triplets:
        if triplet in ["AAC", "UGA", "UGG"]:
            break
        else:
            protein += amino_acids.get(triplet, "X") + " "
    return protein


dna = "TACGCAGAAAAAAATCAGCGGGGTTGTTGGTCATTAGTCTGAATT"
print("DNA Sequence")
print(dna, "\n")
print("mRNA Sequence")
mrna = transcription(dna)
print(mrna, "\n")
print("Protein Sequence")
protein = translation(mrna)
print(protein, "\n")
