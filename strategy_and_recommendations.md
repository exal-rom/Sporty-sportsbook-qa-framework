# Strategy & Recommendations — Single Bet Placement

## 1. Why these 2 tests were selected for automation

### ✔️ UI Test: Single Bet Happy Path  
Este es el flujo más crítico del negocio.  
Automatizarlo garantiza que la funcionalidad principal (seleccionar cuota → introducir stake → colocar apuesta → receipt) se valida en cada ejecución.  
Es un candidato ideal para automatización porque:
- Es estable  
- Tiene alto impacto  
- Es repetitivo  
- Es esencial para el negocio  

### ✔️ API Test: Stake Validation (Minimum Stake Rule)  
La validación de stake es una regla financiera clave.  
Automatizarla permite detectar rápidamente regresiones en:
- límites regulatorios  
- validaciones numéricas  
- integridad del payload  

Además, la API es más estable que la UI, lo que lo convierte en un test de alto valor y bajo mantenimiento.

---

## 2. What was intentionally left as manual only

### ❌ Suspensión por kickoff pasado (UI)  
La UI no implementa correctamente la suspensión.  
Es un área volátil y dependiente del tiempo, por lo que se deja manual para evitar flakiness.

### ❌ Validaciones de receipt  
Aunque importantes, requieren validación visual y consistencia de datos.  
Son mejores para exploración manual.

### ❌ Filtros (date range, odds range)  
Son funcionalidad secundaria y no crítica para el flujo principal.  
Se validan manualmente para evitar sobrecargar la suite.

---

## 3. Recommendations if the project were to scale

### 🔧 1. CI/CD Integration  
Integrar la suite en un pipeline (GitHub Actions, Jenkins, GitLab CI) para:
- ejecutar tests en cada PR  
- generar reportes automáticos  
- bloquear merges con fallos críticos  

### 🧱 2. Add Test Layers  
Agregar capas adicionales:
- **Contract tests** para validar OpenAPI  
- **Component tests** para bet slip y match card  
- **Mocked API tests** para aislar UI  

Esto reduce dependencia del backend y mejora estabilidad.

### 📊 3. Reporting & Observability  
Integrar herramientas como:
- Allure  
- Playwright Trace Viewer (si se migrara)  
- Logging estructurado  

Permite diagnósticos más rápidos y mejor visibilidad.

### 🧪 4. Data Strategy  
- Reset de balance antes de cada test  
- Fixtures deterministas  
- Datos de partidos controlados o mockeados  

Evita flakiness y dependencias del estado del sistema.

---

# Conclusion
La estrategia se centra en **alto valor, bajo mantenimiento y foco en riesgo**, priorizando lo que realmente importa para un sportsbook:  
**validaciones financieras, reglas de negocio y el flujo principal de apuesta.**
