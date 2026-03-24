import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x=np.asarray(x)
    p=np.asarray(p)
    sum=0
    if np.allclose(np.sum(p),1):
        return np.sum(x*p)
    else:
        raise ValueError("Error")
    
    
    
    pass
