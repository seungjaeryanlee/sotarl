"""Test filter find functions of rldb."""
import rldb


def test_find_one_rtype_dict():
    """Verify that find_one() returns an entry (dict), not a list of entries."""
    entry = rldb.find_one({})

    assert type(entry) == dict


def test_find_all_rtype_list():
    """Verify that find_one() returns an entry (dict), not a list of entries."""
    all_entries = rldb.find_all({})

    assert type(all_entries) == list


def test_find_one_return_none():
    """Verify that find_one() returns None if nothing is found."""
    entry = rldb.find_one({ 'env-title': 'There is no env with this title.' })

    assert entry is None


def test_find_all_return_empty_list():
    """Verify that find_all() returns an empty list if nothing is found."""
    all_entries = rldb.find_all({ 'env-title': 'There is no env with this title.' })

    assert all_entries == []
