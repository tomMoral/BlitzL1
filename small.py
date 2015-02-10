import python as blitzl1

import numpy as np
from scipy import sparse

n = 10
d = 10
A = np.random.randn(n, d)
b = np.random.randn(n)
A_csc = sparse.csc_matrix(A)

blitzl1.set_tolerance(0.2)
print "tolerance is", blitzl1.get_tolerance()

prob = blitzl1.LassoProblem(A_csc, b)

sol = prob.solve(0.01)

from IPython import embed
embed()

