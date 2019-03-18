# All entries
entries = [
    {
        "score": 1850.3,
    },
]

# Add ENV keys
env = {
    "env-title": "Alien",
}
entries = [{**entry, **env} for entry in entries]
