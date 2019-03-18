from .variants import entries

# Add ENV keys
env = {
    "env-title": "Amidar",
}
entries = [{**entry, **env} for entry in entries]
