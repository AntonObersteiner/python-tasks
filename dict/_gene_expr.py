from gene_data import *

codon_to_amino = {}
for amino, codons in amino_to_dna.items():
    for codon in codons:
        codon_to_amino[codon] = amino

HEXA_file_name = "HEXA.dna"
HEXA_file = open(HEXA_file_name)
HEXA = HEXA_file.read().upper()
HEXA_file.close()
HEXA_len = len(HEXA) // 3
print(f"HEXA is {HEXA_len} triplets long.")

distribution = {}
for i in range(HEXA_len):
    amino = codon_to_amino[HEXA[i : i + 3]]
    if amino in distribution:
        distribution[amino] += 1
    else:
        distribution[amino] = 1

from random import random
add_to_distr = {
    amino: (random() - .5) * .05
    for amino in distribution
}
shift_add = sum(add_to_distr.values())/len(distribution)
add_to_distr = {
    amino: add_to_distr[amino] - shift_add
    for amino in add_to_distr
}

max_prob = 0
for amino in distribution:
    distribution[amino] /= HEXA_len
    distribution[amino] += add_to_distr[amino]
    if distribution[amino] > max_prob:
        max_prob = distribution[amino]

print("The distribution is:")
for amino in distribution:
    rel = distribution[amino] / max_prob
    print(f"{abbrev[amino]}: {distribution[amino]: 5.1}%", "#" * int(100 * rel))

print(f"Ʃ(distr) = {sum(distribution.values())}")
