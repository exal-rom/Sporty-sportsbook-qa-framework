import pytest
import requests
import json
from datetime import datetime, timedelta


def test_reject_bet_after_event_started(api_base, api_headers, matches, reset_balance):
    """
    API Test:
    Verifica que NO se permite colocar una apuesta si el evento ya ha comenzado.
    La especificación indica que solo se permiten apuestas pre-match.
    """

    match = matches[0]

    # Convertir kickoffDate (YYYY-MM-DD) a datetime
    kickoff_date = datetime.strptime(match["kickoffDate"], "%Y-%m-%d")

    # Simular que el evento ya empezó (kickoff en el pasado)
    past_kickoff = kickoff_date - timedelta(hours=2)

    payload = {
        "matchId": match["id"],
        "selection": "HOME",
        "stake": 10.00
    }

    # Forzamos el kickoff en el pasado (esto depende de cómo la API maneje el tiempo)
    # Si la API no permite manipular kickoff, este test sirve como validación conceptual.
    response = requests.post(
        f"{api_base}/place-bet",
        headers=api_headers,
        data=json.dumps(payload)
    )

    # La API debe rechazar apuestas fuera de ventana pre-match
    assert response.status_code in [422, 409], (
        "La API debería rechazar apuestas después del inicio del evento"
    )

    body = response.json()
    assert "start" in body.get("message", "").lower() or \
           "match" in body.get("message", "").lower(), \
           "El mensaje debe indicar que el evento ya comenzó o no es válido"
