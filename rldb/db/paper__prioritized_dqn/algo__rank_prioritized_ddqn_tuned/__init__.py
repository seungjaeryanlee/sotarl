"""
Prioritized DDQN (rank, tuned) scores from Prioritized DQN paper.

   57 entries
------------------------------------------------------------------------
   57 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Prioritized Double Deep Q-Network (rank, tuned)",
    "algo-nickname": "Prioritized DDQN (rank, tuned)",
    "algo-source-title": "Prioritized Experience Replay",

    # HYPERPARAMETERS
    # Not specified
    "algo-frames": 0,
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 57
