from .entries import entries


# Specify ALGORITHM
algo = {
    "algo-title": "Proximal Policy Optimization",
    "algo-nickname": "PPO",
}

# Populate entries
entries = [{**entry, **algo} for entry in entries]
