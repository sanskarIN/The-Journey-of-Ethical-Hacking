from tools.evidence_freshness import freshness_bucket


def test_fresh_bucket():
    assert freshness_bucket(0) == "fresh"
    assert freshness_bucket(30) == "fresh"


def test_aging_bucket():
    assert freshness_bucket(31) == "aging"
    assert freshness_bucket(60) == "aging"


def test_stale_bucket():
    assert freshness_bucket(61) == "stale"
    assert freshness_bucket(120) == "stale"
