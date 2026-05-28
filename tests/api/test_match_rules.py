import requests
import json


def test_reject_missing_match_id(api_base, api_headers):
    payload = {
        "selection": "HOME",
        "stake": 10
    }

    response = requests.post(
        f"{api_base}/place-bet",
        headers=api_headers,
        data=json.dumps(payload)
    )

    assert response.status_code == 422
    assert "match" in response.json()["message"].lower()


def test_reject_unknown_match(api_base, api_headers):
    payload = {
        "matchId": "unknown-123",
        "selection": "HOME",
        "stake": 10
    }

    response = requests.post(
        f"{api_base}/place-bet",
        headers=api_headers,
        data=json.dumps(payload)
    )

    assert response.status_code == 422
    assert "unknown" in response.json()["message"].lower()
