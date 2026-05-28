from selenium.webdriver.common.by import By
import time


def test_stake_minimum_validation(driver):
    """
    UI Test:
    Verifica que el stake inferior al mínimo (€1.00) muestra mensaje de error.
    """

    # Seleccionar primer partido y cuota HOME
    driver.find_element(By.CSS_SELECTOR, "[data-testid='odd-home']").click()

    stake_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='stake-input']")
    stake_input.clear()
    stake_input.send_keys("0.50")

    error = driver.find_element(By.CSS_SELECTOR, "[data-testid='stake-error']").text
    assert "Minimum stake is €1.00" in error


def test_stake_maximum_validation(driver):
    """
    UI Test:
    Verifica que stake superior al máximo (€100.00) muestra error.
    """

    driver.find_element(By.CSS_SELECTOR, "[data-testid='odd-home']").click()

    stake_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='stake-input']")
    stake_input.clear()
    stake_input.send_keys("150")

    error = driver.find_element(By.CSS_SELECTOR, "[data-testid='stake-error']").text
    assert "Maximum stake is €100.00" in error


def test_stake_precision_validation(driver):
    """
    UI Test:
    Verifica que más de 2 decimales no es aceptado.
    """

    driver.find_element(By.CSS_SELECTOR, "[data-testid='odd-home']").click()

    stake_input = driver.find_element(By.CSS_SELECTOR, "[data-testid='stake-input']")
    stake_input.clear()
    stake_input.send_keys("10.999")

    error = driver.find_element(By.CSS_SELECTOR, "[data-testid='stake-error']").text
    assert "2 decimal places" in error.lower()
