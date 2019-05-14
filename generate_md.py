#!/usr/bin/env python3
"""
Generate Markdown files for endtoend.ai
"""
from string import Template

import rldb


def get_template(filename):
    """Load template file."""
    with open(filename, 'r') as f:
        template = Template(f.read())

    return template

def split_entries_by_variants(entries):
    """Split entries by their variants."""
    human_entries = []
    noop_entries = []
    unspecified_entries = []
    for entry in entries:
        if 'env-variant' not in entry:
            unspecified_entries.append(entry)
        elif entry['env-variant'] == 'Human start':
            human_entries.append(entry)
        elif entry['env-variant'] == 'No-op start':
            noop_entries.append(entry)
        else:
            unspecified_entries.append(entry)

    return human_entries, noop_entries, unspecified_entries

def entries_to_table(entries):
    """Generate Markdown table from rldb entries."""
    table = ''
    table += '| Result | Algorithm | Source |\n'
    table += '|--------|-----------|--------|\n'
    for entry in entries:
        # Boldface if Human or Random
        if entry['algo-nickname'] in ['Human', 'Random']:
            table += '| {} | **{}** | {} |\n'.format(
                entry['score'], entry['algo-nickname'], entry['source-title'],
            )
        else:
            table += '| {} | {} | {} |\n'.format(
                entry['score'], entry['algo-nickname'], entry['source-title'],
            )

    return table

def populate_template(template, feed_dict):
    """Populate template."""
    result = template.substitute(feed_dict)

    return result

def save_file(filename, result):
    """Save text into file."""
    with open(filename, 'w') as f:
        f.write(result)

def generate_md(filepath, env_title):
    # Get template
    template = get_template('markdown/source/{}'.format(filepath))

    # Parse rldb
    entries = rldb.find_all({
        'env-title': env_title,
    })
    entries.sort(key=lambda entry: entry['score'], reverse=True)
    human_entries, noop_entries, unspecified_entries = split_entries_by_variants(entries)
    feed_dict = {
        'human_table': entries_to_table(human_entries),
        'noop_table': entries_to_table(noop_entries),
        'unspecified_table': entries_to_table(unspecified_entries),
    }

    result = populate_template(template, feed_dict)
    save_file('markdown/docs/{}'.format(filepath), result)

def generate_md_atari(atari_subnames):
    for name in atari_subnames:
        generate_md(filepath='envs/gym/atari/{}.md'.format(name), env_title='atari-{}'.format(name))



if __name__ == "__main__":
    entries = rldb.find_all({})
    envs = set([entry['env-title'] for entry in entries])
    atari_envs = [env for env in envs if 'atari-' in env]

    generate_md(filepath='envs/gym/atari/alien.md', env_title='atari-alien')
