# BhuMe Boundary Solution

Pipeline:
1. Load input.geojson
2. Estimate global village shift from example truths (if available)
3. Refine locally using boundaries.tif overlap
4. Compute confidence from boundary alignment score
5. Output predictions.geojson

Run:

```bash
python src/run.py --input input.geojson --boundaries boundaries.tif --output predictions.geojson
