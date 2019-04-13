"""
A3C FF scores from A3C paper.

 57 entries
------------------------------------------------------------------------
 57 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Asynchronous Advantage Actor Critic Feed Forward",
    "algo-nickname": "A3C FF",
    "algo-source-title": "Asynchronous Methods for Deep Reinforcement Learning",

    # HYPERPARAMETERS
    # NOTE 4M frames per epoch, 50 epochs
    "algo-frames": 200 * 1000 * 1000,  # Number of frames
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 57
