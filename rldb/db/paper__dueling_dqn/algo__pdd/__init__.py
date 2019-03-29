"""
PDD DQN scores from DuDQN paper.

 114 entries
------------------------------------------------------------------------
 114 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Prioritized Dueling Double Deep Q-Network",
    "algo-nickname": "PDD DQN",
    "algo-source-title": "Dueling Network Architectures for Deep Reinforcement Learning",

    # HYPERPARAMETERS
    # Not specified
    "algo-frames": 0,
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 57 * 2  # 57 environments, 2 variants
