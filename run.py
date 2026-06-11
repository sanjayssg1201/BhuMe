
import argparse
from predictor import build_predictions

parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True)
parser.add_argument("--output", required=True)

args = parser.parse_args()

preds = build_predictions(args.input)
preds.to_file(args.output, driver="GeoJSON")
print("saved", args.output)
