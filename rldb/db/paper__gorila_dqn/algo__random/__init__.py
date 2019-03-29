"""
Random scores from Gorila DQN paper.

 49 human entries
 49 no-op entries
------------------------------------------------------------------------
 98 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Random (from Gorila DQN)",
    "algo-nickname": "Random (from Gorila DQN)",

    # HYPERPARAMETERS
    # Not specified
    "algo-frames": 0,
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 49 + 49  # 49 human, 49 noop
