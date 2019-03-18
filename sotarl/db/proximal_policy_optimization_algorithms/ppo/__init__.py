from .alien import entries as alien_entries


# Unite all entries
entries = alien_entries

# Add ALGO keys
algo = {
    "algo-title": "Proximal Policy Optimization",
    "algo-nickname": "PPO",
}
entries = [{**entry, **algo} for entry in entries]
