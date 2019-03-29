"""
Gorila DQN scores from Gorila DQN paper.

 49 no-op entries
 49 human entries
------------------------------------------------------------------------
 98 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "General Reinforcement Learning Architecture Deep Q-Network",
    "algo-nickname": "Gorila DQN",
    "algo-source-title": "Massively Parallel Methods for Deep Reinforcement Learning",

    # HYPERPARAMETERS
    "algo-frames": 0,  # TODO Unsure
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 49 + 49
