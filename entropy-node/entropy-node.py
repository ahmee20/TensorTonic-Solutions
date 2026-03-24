import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    y=np.asarray(y, dtype=float)
    val,count=np.unique(y,return_counts=True)
    if len(val)==1:
        return -0.0
        
    p=count/count.sum()

    return -np.sum(p*np.log2(p))
    pass