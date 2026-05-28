from selenium.webdriver.common.by import By
from datetime import datetime


def test_odds_not_clickable_if_event_started(driver):
    """
    UI Test:
    Verifica que si el kickoff ya pasó, las cuotas no son clicables.
    """

    cards = driver.find_elements(By.CSS_SELECTOR, "[data-testid='match-card']")
    assert cards, "No se encontraron partidos"

    for card in cards:
        kickoff = card.find_element(By.CSS_SELECTOR, "[data-testid='kickoff']").text
        kickoff_date = datetime.strptime(kickoff, "%Y-%m-%d")

        if kickoff_date < datetime.now():
            # Odds deben estar deshabilitadas
            odds = card.find_elements(By.CSS_SELECTOR, "[data-testid^='odd-']")
            for odd in odds:
                assert "disabled" in odd.get_attribute("class").lower(), \
                    "La cuota debería estar suspendida"
