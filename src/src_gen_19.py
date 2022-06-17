from typing import List

def sat195(lst: List[int], tot=1125181293221):
    return sum(n ** 2 if n % 3 == 0 else n ** 3 if n % 4 == 0 else n for n in lst) == tot
def sol195(tot=1125181293221):
    """Find a list of integers such that tot is the sum of (n^2 if 3 | n, else n^3 if 4 | n, else n)"""
    residue = (tot - 1) % 12
    return [1] * residue + [tot - residue]
# assert sat195(sol195())
