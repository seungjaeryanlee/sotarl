"""
PPO2 scores from OpenAI Baselines.

 7 entries
------------------------------------------------------------------------
 7 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Trust Region Policy Optimization (MPI) (from OpenAI Baselines cbd21ef)",
    "algo-nickname": "TRPO (MPI) (from OpenAI Baselines cbd21ef)",
    "algo-source-title": "Trust Region Policy Optimization",
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 7
