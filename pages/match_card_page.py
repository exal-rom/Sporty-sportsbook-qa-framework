from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class MatchCardPage:
    """
    Representa una tarjeta de partido en la lista de eventos.
    Permite seleccionar HOME (1), DRAW (X) o AWAY (2).
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_match_cards(self):
        """
        Devuelve todas las tarjetas de partido visibles.
        """
        return self.driver.find_elements(By.CSS_SELECTOR, "[data-testid='match-card']")

    def select_home(self, card):
        """
        Selecciona la cuota HOME (1) en una tarjeta específica.
        """
        card.find_element(By.CSS_SELECTOR, "[data-testid='odd-home']").click()

    def select_draw(self, card):
        """
        Selecciona la cuota DRAW (X).
        """
        card.find_element(By.CSS_SELECTOR, "[data-testid='odd-draw']").click()

    def select_away(self, card):
        """
        Selecciona la cuota AWAY (2).
        """
        card.find_element(By.CSS_SELECTOR, "[data-testid='odd-away']").click()

    def get_match_info(self, card):
        """
        Devuelve un diccionario con la información del partido:
        homeTeam, awayTeam, kickoffDate.
        """
        home = card.find_element(By.CSS_SELECTOR, "[data-testid='home-team']").text
        away = card.find_element(By.CSS_SELECTOR, "[data-testid='away-team']").text
        kickoff = card.find_element(By.CSS_SELECTOR, "[data-testid='kickoff']").text

        return {
            "home": home,
            "away": away,
            "kickoff": kickoff
        }
