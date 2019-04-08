"""
A2C scores from PPO paper.

   12 entries
------------------------------------------------------------------------
   12 unique entries

"""
from .entries import entries


# Specify ALGORITHM
algo = {
    # ALGORITHM
    "algo-title": "Proximal Policy Optimization (from OpenAI Baselines cbd21ef)",
    "algo-nickname": "PPO (from OpenAI Baselines cbd21ef)",
    "algo-source-title": "Proximal Policy Optimization Algorithms",
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]

assert len(entries) == 12
