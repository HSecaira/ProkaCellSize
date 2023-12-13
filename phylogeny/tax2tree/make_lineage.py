# Convert ranks to lineage strings

import fileinput

codes = 'kpcofgs'

for line in fileinput.input():
    g, ranks = line.rstrip('\r\n').split('\t', 1)
    ranks = ranks.split('\t')
    for i in range(len(ranks)):
        ranks[i] = codes[i] + '__' + ranks[i]
    print(g, '; '.join(ranks), sep='\t')
