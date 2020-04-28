"""
Implement the mathematical function 
f(x) = -5 x5 + 69 x2 - 47 as a Python function. 
Then use Python to compute the 
function values f(0), f(1), f(2), and f(3).
Enter the maximum of these four numbers.
"""


def quadratica(x):
    
    formula= -5*(x**5) + 69*(x**2) - 47
    
    return formula


print quadratica(0)
print quadratica(1)
print quadratica(2)
print quadratica(3)