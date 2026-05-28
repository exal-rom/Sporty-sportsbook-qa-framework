import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.settings import (
    get_base_url,
    get_user_id,
    get_api_headers
)


@pytest.fixture(scope="session")
def base_url():
    """
    URL base de la aplicación web.
    """
    return get_base_url()


@pytest.fixture(scope="session")
def user_id():
    """
    user-id requerido por UI y API.
    """
    return get_user_id()


@pytest.fixture(scope="session")
def api_headers():
    """
    Headers comunes para todas las llamadas API.
    """
    return get_api_headers()


@pytest.fixture(scope="session")
def api_base():
    """
    URL base de la API.
    """
    return f"{get_base_url()}api"


@pytest.fixture
def driver(user_id, base_url):
    """
    Inicializa Chrome en modo headless y navega a la URL con user-id.
    """
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    # Navegar con user-id obligatorio
    driver.get(f"{base_url}?user-id={user_id}")

    yield driver
    driver.quit()


@pytest.fixture
def reset_balance(api_base, api_headers):
    """
    Resetea el balance antes de cada test que lo requiera.
    """
    requests.post(f"{api_base}/reset-balance", headers=api_headers)
    yield


@pytest.fixture
def matches(api_base, api_headers):
    """
    Devuelve la lista de partidos desde la API.
    """
    response = requests.get(f"{api_base}/matches", headers=api_headers)
    response.raise_for_status()
    return response.json()
