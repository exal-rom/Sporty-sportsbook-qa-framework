import pytest
import requests
import json


def test_reject_stake_below_minimum(api_base, api_headers, matches, reset_balance):
    """
    API Test:
    Verifica que la API rechaza un stake inferior al mínimo permitido (€1.00).
    Regla tomada de la Feature Specification (Stake Validation).
    """

    match = matches[0]

    payload = {
        "matchId": match["id"],
        "selection": "HOME",
        "stake": 0.50  # menor al mínimo
    }

    response = requests.post(
        f"{api_base}/place-bet",
        headers=api_headers,
        data=json.dumps(payload)
    )

    # La API debe rechazar stake inválido con 422 (semantic validation failure)
    assert response.status_code == 422, "La API debería rechazar stake inferior al mínimo"

    body = response.json()
    assert "stake" in body.get("message", "").lower(), "El mensaje debe mencionar el error de stake"
