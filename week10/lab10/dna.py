def read_dna(dna_file):
    """
    Read a DNA string from a file.
    the file contains data in the following format:
    A <-> T
    G <-> C
    G <-> C
    C <-> G
    G <-> C
    T <-> A
    Output a list of touples:
    [
        ('A', 'T'),
        ('G', 'C'),
        ('G', 'C'),
        ('C', 'G'),
        ('G', 'C'),
        ('T', 'A'),
    ]
    Where either (or both) elements in the string might be missing:
    <-> T
    G <->
    G <-> C
    <->
    <-> C
    T <-> A
    Output:
    [
        ('', 'T'),
        ('G', ''),
        ('G', 'C'),
        ('', ''),
        ('', 'C'),
        ('T', 'A'),
    ]
    """
    fp = open(dna_file, 'r')
    lines = fp.readlines()
    output = []
    for line in lines:
        line = line.replace('\n', '')
        tmp = line.split(' ')
        ################# ignore base 1 and 2 are all ''######################
        if tmp[0] =='' and tmp[2] == '':
            continue
        output.append((tmp[0], tmp[2]))
    return output

def is_rna(dna):
    """
    Given DNA in the aforementioned format,
    return the string "DNA" if the data is DNA,
    return the string "RNA" if the data is RNA,
    return the string "Invalid" if the data is neither DNA nor RNA.
    DNA consists of the following bases:
    Adenine  ('A'),
    Thymine  ('T'),
    Guanine  ('G'),
    Cytosine ('C'),
    RNA consists of the following bases:
    Adenine  ('A'),
    Uracil   ('U'),
    Guanine  ('G'),
    Cytosine ('C'),
    The data is DNA if at least 90% of the bases are one of the DNA bases.
    The data is RNA if at least 90% of the bases are one of the RNA bases.
    The data is invalid if more than 10% of the bases are not one of the DNA or RNA bases.
    Empty bases should be ignored.
    """
    total_num = 0
    dna_ = 0
    rna_ = 0
    for t1, t2 in dna:
        if t1 != '':
            total_num+=1
        if t2 != '':
            total_num+=1

        ################### count dna base#################
        if t1 == 'A' or t1 == 'G' or t1 == 'T' or t1 == 'C':
            dna_+=1
        if t2 == 'A' or t2 == 'G' or t2 == 'T' or t2 == 'C':
            dna_+=1
        #####################count rna base#################
        if t1 == 'A' or t1 == 'G' or t1 == 'U' or t1 == 'C':
            rna_+=1
        if t2 == 'A' or t2 == 'G' or t2 == 'U' or t2 == 'C':
            rna_+=1

    if dna_ / total_num >= 0.9:
        return "DNA"
    if rna_ / total_num >= 0.9:
        return "RNA"
    return 'Invalid'

def check_invalid_dna(term):
    if term != 'A' and term != 'T' and term != 'C' and term != 'G'and term != '':
        return False
    return True

def check_invalid_rna(term):
    if term != 'A' and term != 'U' and term != 'C' and term != 'G' and term != '':
        return False
    return True

def clean_dna(dna):
    """
    Given DNA in the aforementioned format,
    If the pair is incomplete, ('A', '') or ('', 'G'), ect
    Fill in the missing base with the match base.
    In DNA 'A' matches with 'T', 'G' matches with 'C'
    In RNA 'A' matches with 'U', 'G' matches with 'C'
    If a pair contains an invalid base the pair should be removed.
    Pairs of empty bases should be ignored.
    """
    result = []
    if is_rna(dna) == "DNA":
        for t1, t2 in dna:
            # remove invalid
            if not check_invalid_dna(t1) or not check_invalid_dna(t2):
                continue
            if (t1 == "A" and t2 == ''):
                t2 = 'T'
            elif (t2 == "A" and t1 == ''):
                t1 = 'T'
            elif (t2 == "T" and t1 == ''):
                t1 = 'A'
            elif (t1 == "T" and t2 == ''):
                t2 = 'A'
            elif (t1 == "G" and t2 == ''):
                t2 = 'C'
            elif (t2 == "G" and t1 == ''):
                t1 = 'C'
            elif (t2 == "C" and t1 == ''):
                t1 = 'G'
            elif (t1 == "C" and t2 == ''):
                t2 = 'G'
            result.append((t1, t2))

    if is_rna(dna) == "RNA":
        for t1, t2 in dna:
            if not check_invalid_rna(t1) or not check_invalid_rna(t2):
                continue
            if (t1 == "A" and t2 == ''):
                t2 = 'U'
            elif (t2 == "A" and t1 == ''):
                t1 = 'U'
            elif (t2 == "U" and t1 == ''):
                t1 = 'A'
            elif (t1 == "U" and t2 == ''):
                t2 = 'A'
            elif (t1 == "G" and t2 == ''):
                t2 = 'C'
            elif (t2 == "G" and t1 == ''):
                t1 = 'C'
            elif (t2 == "C" and t1 == ''):
                t1 = 'G'
            elif (t1 == "C" and t2 == ''):
                t2 = 'G'
            result.append((t1, t2))
    return result

    
    
def mast_common_base(dna):
    """
    Given DNA in the aforementioned format,
    return the most common first base:
    eg. given:
    A <-> T
    G <-> C
    G <-> C
    C <-> G
    G <-> C
    T <-> A
    The most common first base is 'G'.
    Empty bases should be ignored.
    """


    count = {'A': 0, 'U': 0, 'G': 0, 'T': 0, 'C': 0, '': 0}

    for pair in dna:
        t1 = pair[0]
        count[t1] +=1
    max_c = 0
    max_b = ''
    for key, value in count.items():
        if value > max_c:
            max_b = key
            max_c = value
    return max_b

def base_to_name(base):
    """
    Given a base, return the name of the base.
    The base names are:
    Adenine  ('A'),
    Thymine  ('T'),
    Guanine  ('G'),
    Cytosine ('C'),
    Uracil   ('U'),
    return the string "Unknown" if the base isn't one of the above.
    """
    if base == 'A': return 'Adenine'
    elif base == 'T': return 'Thymine'
    elif base == 'G': return 'Guanine'
    elif base == 'C': return 'Cytosine'
    elif base == 'U': return 'Uracil'
    return 'unknown'
