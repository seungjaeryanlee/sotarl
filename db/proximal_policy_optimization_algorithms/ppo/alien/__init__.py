from .variants import entries

# Add ENV keys
env = {
    "env-title": "Alien",
}
entries = [{**entry, **env} for entry in entries]
