"""
Trust-PCL scores from Trust-PCL paper.

 5 entries
------------------------------------------------------------------------
 5 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Trust Region Path Consistency Learning",
    "algo-nickname": "Trust-PCL",
    "algo-source-title": "Trust-PCL: An Off-Policy Trust Region Method for Continuous Control",

    # HYPERPARAMETERS
    "algo-frames": 10 * 1000 * 1000,  # Number of frames
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 5
