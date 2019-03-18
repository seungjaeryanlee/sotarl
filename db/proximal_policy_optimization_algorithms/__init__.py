from .source import source

from .ppo import entries as ppo_entries

entries = ppo_entries
entries = [{**entry, **source} for entry in entries]
