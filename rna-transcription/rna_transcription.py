def to_rna(dna_strand):
    """ Given a DNA strand, return its RNA complement (per RNA transcription).
        Both DNA and RNA strands are a sequence of nucleotides.  The four 
        nucleotides found in DNA are adenine (**A**), cytosine (**C**), guanine
        (**G**) and thymine (**T**).  The four nucleotides found in RNA are 
        adenine (**A**), cytosine (**C**), guanine (**G**) and uracil (**U**).  
        Given a DNA strand, its transcribed RNA strand is formed by replacing 
        each nucleotide with its complement:
        * `G` -> `C`
        * `C` -> `G`
        * `T` -> `A`
        * `A` -> `U` 
    """
    trans = { 'G': 'C',
              'C': 'G',
              'T': 'A',
              'A': 'U'
            }
    new_strand = []
    
    for nucleotide in dna_strand:
        try:
            new_strand.append(trans[nucleotide])
        except KeyError:
            return ""

    return ''.join(new_strand)