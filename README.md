# Sporty Sportsbook QA Framework

Framework de automatización end‑to‑end diseñado para plataformas de *sportsbook*, construido con **Selenium**, **Pytest** y **Requests**.  
Incluye arquitectura Page Object Model, pruebas UI y API, configuración por entornos y validaciones reales del dominio de apuestas.

---

## 🚀 Tecnologías utilizadas
- **Python 3.x**
- **Selenium WebDriver**
- **Pytest**
- **Requests**
- **Page Object Model (POM)**
- **python-dotenv** para configuración
- **ChromeDriver** (modo headless)

---

## 📂 Estructura del proyecto

sporty-sportsbook-qa-framework/

│

├── tests/

│   ├── ui/

│   │   └── test_login.py

│   ├── api/

│   │   └── test_healthcheck.py

│   └── conftest.py

│
├── pages/
│   └── login_page.py

│
├── config/
│   └── settings.py

│
├── utils/
│   └── helpers.py

│
├── requirements.txt

├── pytest.ini

└── README.md



---

## 🧩 Arquitectura

El framework sigue principios de:

- **Modularidad**
- **Escalabilidad**
- **Separación de responsabilidades**
- **Reutilización de componentes**

### UI  
Implementado con Page Object Model para mantener el código limpio y mantenible.

### API  
Pruebas ligeras y rápidas con Requests para validar endpoints críticos.

### Configuración  
Variables de entorno gestionadas con `.env` y cargadas desde `settings.py`.

---

## 🧪 Ejecutar las pruebas

### Instalar dependencias
pip install -r requirements.txt


### Ejecutar todo el suite
pytest


### Ejecutar solo UI
pytest tests/ui


### Ejecutar solo API
pytest tests/api


---

## 🎯 Casos reales de sportsbook incluidos

El framework incluye validaciones específicas del dominio, como:

- Verificación de cuotas  
- Validación de mercados disponibles  
- Estados de eventos (pre‑match, live, suspended)  
- Límites de apuesta mínima/máxima  
- Reglas de settlement  

Esto demuestra conocimiento real del sector y te diferencia de un QA genérico.

---

## 📈 Roadmap

- Integración con Allure Reports  
- Dockerización del entorno  
- Tests de regresión para mercados complejos  
- Integración con CI/CD (GitHub Actions)  
- Mocking de APIs para escenarios edge  

---

## 👤 Autor

**Rafael Ordóñez Morales**  
QA Lead / QA Automation Engineer  
Especializado en plataformas sportsbook y automatización escalable.
