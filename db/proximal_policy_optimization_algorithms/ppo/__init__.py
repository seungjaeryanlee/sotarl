from .algo import algo


from .alien import entries as alien_entries

entries = alien_entries
entries = [{**entry, **algo} for entry in entries]
