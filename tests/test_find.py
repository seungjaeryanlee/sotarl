"""Test filter find functions of rldb."""
import rldb


def test_find_one_rtype_dict():
    """Verify that find_one() returns an entry (dict), not a list of entries."""
    all_entries = rldb.find_one({})

    assert type(all_entries) == dict


def test_find_all_rtype_list():
    """Verify that find_one() returns an entry (dict), not a list of entries."""
    all_entries = rldb.find_all({})

    assert type(all_entries) == list


