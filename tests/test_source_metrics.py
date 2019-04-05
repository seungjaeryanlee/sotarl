"""Test metrics for each source."""
import rldb


def test_openai_baselines_count():
    """Verify number of entries in OpenAI Baselines."""
    a3c_entries = rldb.find_all({
        'source-title': 'OpenAI Baselines',
    })

    assert len(a3c_entries) == (
        0
        + 7  # A2C
        + 7  # ACER
        + 7  # ACKTR
        + 7  # DQN
        + 7  # PPO2
        + 7  # PPO2 (MPI)
        + 7  # TRPO (MPI)
    )
