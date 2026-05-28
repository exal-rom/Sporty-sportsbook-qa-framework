import requests
import json


def test_reject_non_numeric_stake(api_base, api_headers, matches):
    match = matches[0]

    payload = {
        "matchId": match["id"],
        "selection": "HOME",
        "stake": "abc"
    }

    response = requests.post(
        f"{api_base}/place-bet",
        headers=api_headers,
        data=json.dumps(payload)
    )

    assert response.status_code == 422
    assert "numeric" in response.json()["message"].lower()


def test_reject_stake_above_max(api_base, api_headers, matches):
    match = matches[0]

    payload = {
        "matchId": match["id"],
        "selection": "HOME",
        "stake": 150
    }

    response = requests.post(
        f"{api_base}/place-bet",
        headers=api_headers,
        data=json.dumps(payload)
    )

    assert response.status_code == 422
    assert "maximum" in response.json()["message"].lower()


def test_reject_stake_precision(api_base, api_headers, matches):
    match = matches[0]

    payload = {
        "matchId": match["id"],
        "selection": "HOME",
        "stake": 10.999
    }

    response = requests.post(
        f"{api_base}/place-bet",
        headers=api_headers,
        data=json.dumps(payload)
    )

    assert response.status_code == 422
    assert "decimal" in response.json()["message"].lower()
