"""
ACER scores from PPO paper.

   12 entries
------------------------------------------------------------------------
   12 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Actor-Critic with Experience Replay",
    "algo-nickname": "ACER",
    "algo-source-title": "Sample Efficient Actor-Critic with Experience Replay",
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 12
