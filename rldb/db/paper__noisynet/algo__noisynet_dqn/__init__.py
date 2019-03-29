"""
NoisyNet DQN scores from NoisyNet paper.

 57 entries
------------------------------------------------------------------------
 57 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "NoisyNet Deep Q-Networks",
    "algo-nickname": "NoisyNet DQN",
    "algo-source-title": "Noisy Networks for Exploration",
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 57
