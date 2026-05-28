# Sporty Sportsbook QA Framework

Framework de automatización para el flujo **Single Bet Placement** del assignment de Sportsbook.  
Diseñado con foco en **claridad, mantenibilidad y validación de reglas de negocio reales** del dominio de apuestas.

Incluye:
- Pruebas **UI** con Selenium  
- Pruebas **API** con Requests  
- Arquitectura **Page Object Model**  
- Configuración por entornos  
- Validaciones de negocio: stake, selección, suspensión, match integrity  

---

## 🚀 Tecnologías utilizadas

- Python 3.x  
- Selenium WebDriver  
- Pytest  
- Requests  
- Page Object Model (POM)  
- python-dotenv para configuración  
- ChromeDriver (headless)  

---

## 📂 Estructura del proyecto

```
sporty-sportsbook-qa-framework/
│
├── config/
│   └── settings.py
│
├── pages/
│   └── match_card_page.py
│
├── tests/
│   ├── ui/
│   │   ├── test_select_odds.py
│   │   ├── test_stake_validation_ui.py
│   │   └── test_suspension_ui.py
│   └── api/
│       ├── test_place_bet_validation.py
│       ├── test_stake_rules.py
│       ├── test_selection_rules.py
│       ├── test_match_rules.py
│       └── test_event_suspension_rules.py
│
├── test_plan.md
├── execution_report.md
├── bug_reports.md
├── strategy_and_recommendations.md
│
├── pytest.ini
├── requirements.txt
└── README.md


```
---

## 🧩 Arquitectura

### **UI — Page Object Model**
- Componentes desacoplados  
- Selectores estables usando `data-testid`  
- Métodos reutilizables para interacción con cuotas y tarjetas de partido  

### **API — Requests**
- Validaciones de negocio críticas  
- Fixtures para headers, base URL y matches  
- Tests rápidos, deterministas y de bajo mantenimiento  

### **Configuración**
- Variables gestionadas con `.env`  
- Cargadas desde `settings.py`  
- Permite cambiar entorno sin modificar código  

---

## 🧪 Ejecutar las pruebas

### Instalar dependencias
pip install -r requirements.txt


### Ejecutar todo el suite
pytest


### Ejecutar solo UI
pytest tests/ui


---

## 🎯 Validaciones de sportsbook incluidas

- Selección de cuotas (HOME / DRAW / AWAY)  
- Stake mínimo (€1.00)  
- Stake máximo (€100.00)  
- Precisión de stake (máx. 2 decimales)  
- Suspensión por kickoff pasado  
- Selección inválida  
- matchId inválido o inexistente  
- Receipt consistency (manual)  

Estas pruebas cubren las reglas fundamentales del dominio sportsbook.

---

## 📈 Roadmap

- Integración con Allure Reports  
- Dockerización del entorno  
- Mocking de API para escenarios edge  
- Tests de regresión para mercados complejos  
- Integración con CI/CD (GitHub Actions)  

---

## 👤 Autor

**Rafael Ordóñez Morales**  
QA Lead / QA Automation Engineer  
Especializado en plataformas sportsbook y automatización escalable.  


