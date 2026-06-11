
def confidence_from_score(score, max_score=1.0):
    c = score / max(max_score, 1e-6)
    return max(0.0, min(1.0, float(c)))
