from elgamal_util import mod_inverse
import random

from params import p
from params import g

def keygen():
    sk = random.randint(1, p)
    pk = pow(g, sk, p)
    return pk,sk

def encrypt(pk,m):
    q = (p-1)/2
    r = random.randint(1, q)
    c1 = pow(g, r, p)
    hrm= (pow(pk, r)) * m
    c2 = pow(hrm, 1, p)
    return [c1,c2]

def decrypt(sk,c):
    denominator = pow(c[0], sk)
    m = pow((c[1]/denominator),1,p)
    return m