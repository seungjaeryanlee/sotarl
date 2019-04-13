"""
Random scores from Gorila DQN paper.

   98 entries
 - 49 no-op entries from DQN paper
------------------------------------------------------------------------
   98 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Random",
    "algo-nickname": "Random",
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 49
