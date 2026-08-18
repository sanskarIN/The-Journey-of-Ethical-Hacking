from tools.json_metadata import validate_contracts, validate_release


def valid_release():
    return {
        "project": "The Journey of Ethical Hacking — Companion Resources",
        "edition": "2026 Edition",
        "companion_release": "2026.08.18.3",
        "author": "Ram Sandesh",
        "repository": "https://github.com/sanskarIN/The-Journey-of-Ethical-Hacking",
        "official_gumroad": "https://ramsandesh.gumroad.com",
        "series_parts": 200,
        "public_scope": ["synthetic datasets"],
        "code_license": "Apache-2.0",
        "commercial_book_rights": "Copyright © 2026 Ram Sandesh. All rights reserved.",
        "commercial_manuscript_in_public_repo": False,
        "author_avatar_or_photo_used": False,
        "x_or_twitter_link_included": False,
        "safety_scope": "lawful, authorized, defensive learning only",
    }


def test_release_metadata_accepts_expected_structure():
    assert validate_release(valid_release()) == []


def test_release_metadata_rejects_wrong_storefront():
    data = valid_release()
    data["official_gumroad"] = "https://example.invalid"
    assert any("official_gumroad" in item for item in validate_release(data))


def test_release_metadata_enforces_publication_boundaries():
    data = valid_release()
    data["commercial_manuscript_in_public_repo"] = True
    data["author_avatar_or_photo_used"] = True
    data["x_or_twitter_link_included"] = True
    errors = validate_release(data)
    assert len(errors) >= 3


def test_contracts_accept_expected_structure():
    data = {
        "version": 1,
        "datasets": {
            "sample.csv": {
                "primary_id": "record_id",
                "required_columns": ["record_id", "status"],
                "allow_extra_columns": False,
            }
        },
    }
    assert validate_contracts(data) == []


def test_contracts_require_primary_id_in_columns():
    data = {
        "version": 1,
        "datasets": {
            "sample.csv": {
                "primary_id": "record_id",
                "required_columns": ["status"],
                "allow_extra_columns": False,
            }
        },
    }
    assert any("primary_id" in item for item in validate_contracts(data))
