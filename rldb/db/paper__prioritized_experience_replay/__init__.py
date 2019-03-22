from .algo__ddqn import entries as ddqn_entries
from .algo__dqn2015 import entries as dqn2015_entries
from .algo__gorila import entries as gorila_entries
from .algo__human import entries as human_entries
from .algo__prop_prioritized_ddqn import entries as prop_pddqn_entries
from .algo__random import entries as random_entries
from .algo__rank_prioritized import entries as rank_prioritized_entries
from .algo__rank_prioritized_ddqn import entries as rank_pddqn_entries


# Specify SOURCE
source = {
    #  BASICS
    "source-title": "Prioritized Experience Replay",
    "source-nickname": "PER",
    "source-authors": [
        "Tom Schaul",
        "John Quan",
        "Ioannis Antonoglou",
        "David Silver",
    ],

    #  ARXIV
    "source-arxiv-id": "1511.05952",
    "source-arxiv-version": 4,

    #  MISC.
    "source-bibtex": """\
@article{DBLP:journals/corr/SchaulQAS15,
  author    = {Tom Schaul and
               John Quan and
               Ioannis Antonoglou and
               David Silver},
  title     = {Prioritized Experience Replay},
  journal   = {CoRR},
  volume    = {abs/1511.05952},
  year      = {2015},
  url       = {http://arxiv.org/abs/1511.05952},
  archivePrefix = {arXiv},
  eprint    = {1511.05952},
  timestamp = {Mon, 13 Aug 2018 16:46:28 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/SchaulQAS15},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}""",
}

# Populate entries
entries = (
    []
    + ddqn_entries
    + dqn2015_entries
    + gorila_entries
    + human_entries
    + prop_pddqn_entries
    + random_entries
    + rank_prioritized_entries
    + rank_pddqn_entries
)
entries = [{**entry, **source} for entry in entries]

assert len(entries) == 57 * 8  # 57 games, 8 algorithms