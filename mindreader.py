# NAME Guesser
# CODER : Convexly
print("THINK A NAME/WORD IN MIND WHICH HAS 4 LETTERS")
print("1   2   3   4   5")
print("_________________")
print("a   b   c   d   e")
print("f   g   h   i   j")
print("k   l   m   n   o")
print("p   q   r   s   t")
print("u   v   w   x   y")
print("z")
A = input("WHICH COLUMN CONTAINS FIRST LETTER :  ")
B = input("WHICH COLUMN CONTAINS SECOND LETTER :  ")
C = input("WHICH COLUMN CONTAINS THIRD LETTER :  ")
D = input("WHICH COLUMN CONTAINS FOURTH LETTER :  ")
print("===============================")
print("KEEP THAT NAME/WORD IN MIND AND RE-ANSWER FOLLOWING QUESTIONS")
print("===============================")
print("1   2   3   4   5   6")
print("_____________________")
print("a   f   k   p   u   z")
print("b   g   l   q   v")
print("c   h   m   r   w")
print("d   i   n   s   x")
print("e   j   o   t   y")
AA = input("WHICH COLUMN CONTAINS FIRST LETTER :  ")
BB = input("WHICH COLUMN CONTAINS SECOND LETTER :  ")
CC = input("WHICH COLUMN CONTAINS THIRD LETTER :  ")
DD = input("WHICH COLUMN CONTAINS FOURTH LETTER :  ")
AREF = AA, A
BREF = BB, B
CREF = CC, C
DREF = DD, D
#==============================================================================
#=======================ONE===============================
#==============================================================================
if AREF == ('1', '1'):
    first = 'a'
elif AREF == ('1', '2'):
    first = 'b'
elif AREF == ('1', '3'):
    first = 'c'
elif AREF == ('1', '4'):
    first = 'd'
elif AREF == ('1', '5'):
    first = 'e'
elif AREF == ('2', '1'):
    first = 'f'
elif AREF == ('2', '2'):
    first = 'g'
elif AREF == ('2', '3'):
    first = 'h'
elif AREF == ('2', '4'):
    first = 'i'
elif AREF == ('2', '5'):
    first = 'j'
elif AREF == ('3', '1'):
    first = 'k'
elif AREF == ('3', '2'):
    first = 'l'
elif AREF == ('3', '3'):
    first = 'm'
elif AREF == ('3', '4'):
    first = 'n'
elif AREF == ('3', '5'):
    first = 'o'
elif AREF == ('4', '1'):
    first = 'p'
elif AREF == ('4', '2'):
    first = 'q'
elif AREF == ('4', '3'):
    first = 'r'
elif AREF == ('4', '4'):
    first = 's'
elif AREF == ('4', '5'):
    first = 't'
elif AREF == ('5', '1'):
    first = 'u'
elif AREF == ('5', '2'):
    first = 'v'
elif AREF == ('5', '3'):
    first = 'w'
elif AREF == ('5', '4'):
    first = 'x'
elif AREF == ('5', '5'):
    first = 'y'
elif AREF == ('6', '1'):
    first = 'z'
else:
    print("ERROR")
#==============================================================================
#=======================TWO===============================
#==============================================================================
if BREF == ('1', '1'):
    sec = 'a'
elif BREF == ('1', '2'):
    sec = 'b'
elif BREF == ('1', '3'):
    sec = 'c'
elif BREF == ('1', '4'):
    sec = 'd'
elif BREF == ('1', '5'):
    sec = 'e'
elif BREF == ('2', '1'):
    sec = 'f'
elif BREF == ('2', '2'):
    sec = 'g'
elif BREF == ('2', '3'):
    sec = 'h'
elif BREF == ('2', '4'):
    sec = 'i'
elif BREF == ('2', '5'):
    sec = 'j'
elif BREF == ('3', '1'):
    sec = 'k'
elif BREF == ('3', '2'):
    sec = 'l'
elif BREF == ('3', '3'):
    sec = 'm'
elif BREF == ('3', '4'):
    sec = 'n'
elif BREF == ('3', '5'):
    sec = 'o'
elif BREF == ('4', '1'):
    sec = 'p'
elif BREF == ('4', '2'):
    sec = 'q'
elif BREF == ('4', '3'):
    sec = 'r'
elif BREF == ('4', '4'):
    sec = 's'
elif BREF == ('4', '5'):
    sec = 't'
elif BREF == ('5', '1'):
    sec = 'u'
elif BREF == ('5', '2'):
    sec = 'v'
elif BREF == ('5', '3'):
    sec = 'w'
elif BREF == ('5', '4'):
    sec = 'x'
elif BREF == ('5', '5'):
    sec = 'y'
elif BREF == ('6', '1'):
    sec = 'z'
else:
    print("ERROR")

#==============================================================================
#=======================THREE===============================
#==============================================================================
if CREF == ('1', '1'):
    third = 'a'
elif CREF == ('1', '2'):
    third = 'b'
elif CREF == ('1', '3'):
    third = 'c'
elif CREF == ('1', '4'):
    third = 'd'
elif CREF == ('1', '5'):
    third = 'e'
elif CREF == ('2', '1'):
    third = 'f'
elif CREF == ('2', '2'):
    third = 'g'
elif CREF == ('2', '3'):
    third = 'h'
elif CREF == ('2', '4'):
    third = 'i'
elif CREF == ('2', '5'):
    third = 'j'
elif CREF == ('3', '1'):
    third = 'k'
elif CREF == ('3', '2'):
    third = 'l'
elif CREF == ('3', '3'):
    third = 'm'
elif CREF == ('3', '4'):
    third = 'n'
elif CREF == ('3', '5'):
    third = 'o'
elif CREF == ('4', '1'):
    third = 'p'
elif CREF == ('4', '2'):
    third = 'q'
elif CREF == ('4', '3'):
    third = 'r'
elif CREF == ('4', '4'):
    third = 's'
elif CREF == ('4', '5'):
    third = 't'
elif CREF == ('5', '1'):
    third = 'u'
elif CREF == ('5', '2'):
    third = 'v'
elif CREF == ('5', '3'):
    third = 'w'
elif CREF == ('5', '4'):
    third = 'x'
elif CREF == ('5', '5'):
    third = 'y'
elif CREF == ('6', '1'):
    third = 'z'
else:
    print("ERROR")

#==============================================================================
#=======================FOUR===============================
#==============================================================================
if DREF == ('1', '1'):
    fourth = 'a'
elif DREF == ('1', '2'):
    fourth = 'b'
elif DREF == ('1', '3'):
    fourth = 'c'
elif DREF == ('1', '4'):
    fourth = 'd'
elif DREF == ('1', '5'):
    fourth = 'e'
elif DREF == ('2', '1'):
    fourth = 'f'
elif DREF == ('2', '2'):
    fourth = 'g'
elif DREF == ('2', '3'):
    fourth = 'h'
elif DREF == ('2', '4'):
    fourth = 'i'
elif DREF == ('2', '5'):
    fourth = 'j'
elif DREF == ('3', '1'):
    fourth = 'k'
elif DREF == ('3', '2'):
    fourth = 'l'
elif DREF == ('3', '3'):
    fourth = 'm'
elif DREF == ('3', '4'):
    fourth = 'n'
elif DREF == ('3', '5'):
    fourth = 'o'
elif DREF == ('4', '1'):
    fourth = 'p'
elif DREF == ('4', '2'):
    fourth = 'q'
elif DREF == ('4', '3'):
    fourth = 'r'
elif DREF == ('4', '4'):
    fourth = 's'
elif DREF == ('4', '5'):
    fourth = 't'
elif DREF == ('5', '1'):
    fourth = 'u'
elif DREF == ('5', '2'):
    fourth = 'v'
elif DREF == ('5', '3'):
    fourth = 'w'
elif DREF == ('5', '4'):
    fourth = 'x'
elif DREF == ('5', '5'):
    fourth = 'y'
elif DREF == ('6', '1'):
    fourth = 'z'
else:
    print("ERROR")
print(f"IS IT YOUR WORD ==> {first}{sec}{third}{fourth}")
AAAA = input("")
