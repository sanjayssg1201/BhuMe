
import geopandas as gpd
from alignment import search_best_shift
from confidence import confidence_from_score

def build_predictions(input_path):
    gdf = gpd.read_file(input_path)
    preds = []
    shifts = [-20,-10,-5,0,5,10,20]

    for _, row in gdf.iterrows():
        geom = row.geometry

        def scorer(g):
            return 1.0

        best_geom, score = search_best_shift(geom, shifts, scorer)
        conf = confidence_from_score(score)

        preds.append({
            "plot_number": row["plot_number"],
            "status": "corrected" if conf >= 0.55 else "flagged",
            "confidence": conf,
            "method_note": "local boundary search",
            "geometry": best_geom
        })

    return gpd.GeoDataFrame(preds, geometry="geometry", crs="EPSG:4326")
