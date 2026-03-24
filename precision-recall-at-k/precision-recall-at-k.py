def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    top=list(recommended[:k])
    precesion=len( (set(top) & set(relevant)) )/k
    recall= len( (set(top) & set(relevant)) )/len(relevant)

    return [precesion,recall]