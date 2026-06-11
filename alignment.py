
import numpy as np
from shapely.affinity import translate

def search_best_shift(geom, shifts, scorer):
    best_geom = geom
    best_score = -1
    for dx in shifts:
        for dy in shifts:
            g = translate(geom, dx, dy)
            s = scorer(g)
            if s > best_score:
                best_score = s
                best_geom = g
    return best_geom, float(best_score)
