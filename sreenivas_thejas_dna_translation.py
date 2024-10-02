amino_acids = {
    'UUU': 'Phe',
    'UUC': 'Phe',

    'UUA': 'Leu',
    'UUG': 'Leu',
    'CUU': 'Leu',
    'CUC': 'Leu',
    'CUA': 'Leu',
    'CUG': 'Leu',

    'AUU': 'Ile',
    'AUC': 'Ile',
    'AUA': 'Ile',

    'AUG': 'Met',

    'GUU': 'Val',
    'GUC': 'Val',
    'GUA': 'Val',
    'GUG': 'Val',

    'UCU': 'Ser',
    'UCC': 'Ser',
    'UCA': 'Ser',
    'UCG': 'Ser',
    'AGU': 'Ser',
    'AGC': 'Ser',

    'CCU': 'Pro',
    'CCC': 'Pro',
    'CCA': 'Pro',
    'CCG': 'Pro',

    'ACU': 'Thr',
    'ACC': 'Thr',
    'ACA': 'Thr',
    'ACG': 'Thr',

    'GCU': 'Ala',
    'GCC': 'Ala',
    'GCA': 'Ala',
    'GCG': 'Ala',

    'UAU': 'Tyr',
    'UAC': 'Tyr',

    'UAA': 'STOP',
    'UAG': 'STOP',

    'CAU': 'His',
    'CAC': 'His',

    'CAA': 'Gln',
    'CAG': 'Gln',

    'AAU': 'Asn',
    'AAC': 'Asn',

    'AAA': 'Lys',
    'AAG': 'Lys',

    'GAU': 'Asp',
    'GAC': 'Asp',

    'GAA': 'Glu',
    'GAG': 'Glu',

    'UGU': 'Cys',
    'UGC': 'Cys',

    'UGA': 'STOP',

    'UGG': 'Trp',

    'CGU': 'Arg',
    'CGC': 'Arg',
    'CGA': 'Arg',
    'CGG': 'Arg',
    'AGA': 'Arg',
    'AGG': 'Arg',

    'GGU': 'Gly',
    'GGC': 'Gly',
    'GGA': 'Gly',
    'GGG': 'Gly',
}
def transcription(DNA):
    complement = ''
    for each in DNA:
        if each == 'T':
            complement+= 'A'
        elif each == 'A':
            complement+= 'U'
        elif each == 'U':
            complement+= 'A'
        elif each == 'C':
            complement+= 'G'
        elif each == 'G':
            complement+= 'C'
    return complement 

def translate(mrna):
    protein = ''
    for i in range(0, len(mrna), 3):
        chunk = mrna[i:i+3]
        protein+= '' + amino_acids[chunk]
    return protein

dna = 'TACGCAGAAAAAAATCAGCGGGGTTGTTGGTCATTAGTCTGAATT'
dna = transcription(dna)
print('Dna sequence: ',dna)
dna = translate(dna)
print('mrna sequence: ',dna)
