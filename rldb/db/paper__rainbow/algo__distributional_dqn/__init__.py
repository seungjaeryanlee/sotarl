"""
Distributional DQN scores from Rainbow paper.

 57 entries
------------------------------------------------------------------------
 57 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Distributional Deep Q-Network",
    "algo-nickname": "Distributional DQN",
    "algo-source-title": "Rainbow: Combining Improvements in Deep Reinforcement Learning",
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 57
