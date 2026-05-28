import time
from pages.match_card_page import MatchCardPage
from selenium.webdriver.common.by import By


def test_select_home_shows_in_betslip(driver):
    """
    E2E UI Test:
    Verifica que al seleccionar HOME (1) en un partido,
    la selección aparece correctamente en el bet slip.
    """

    match_page = MatchCardPage(driver)

    # Obtener tarjetas de partido
    cards = match_page.get_match_cards()
    assert len(cards) > 0, "No se encontraron partidos en la lista"

    first_card = cards[0]

    # Obtener info del partido para validación
    match_info = match_page.get_match_info(first_card)

    # Seleccionar HOME (1)
    match_page.select_home(first_card)

    # Validar que el bet slip muestra la selección
    selection_text = driver.find_element(By.CSS_SELECTOR, "[data-testid='betslip-selection']").text
    assert match_info["home"] in selection_text, "El equipo HOME no aparece en el bet slip"
    assert "1" in selection_text or "HOME" in selection_text, "La selección HOME no se reflejó correctamente"

    # Validar que el input de stake aparece
    stake_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='stake-input']")
    assert stake_input.is_displayed(), "El campo de stake no está visible"

    # Validar que el botón Place Bet aparece
    place_bet_btn = driver.find_element(By.CSS_SELECTOR, "[data-testid='place-bet-btn']")
    assert place_bet_btn.is_displayed(), "El botón Place Bet no está visible"
