"""
IQN scores from IQN paper.

 57 entries
------------------------------------------------------------------------
 57 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Implicit Quantile Networks",
    "algo-nickname": "IQN",
    "algo-source-title": "Implicit Quantile Networks for Distributional Reinforcement Learning",
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 57
