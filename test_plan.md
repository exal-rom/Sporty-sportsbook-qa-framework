# Test Plan — Single Bet Placement

## 1. Scope
Este plan cubre la funcionalidad de **Single Bet Placement** para eventos **pre‑match** de fútbol en la aplicación web.  
Incluye validaciones de selección, stake, bet slip, reglas de negocio y comportamiento esperado del flujo de apuesta.

**Fuera de alcance:**  
- Live betting  
- Multi‑bets  
- Mobile  
- Otros deportes  
- Cambios dinámicos de odds  

---

## 2. Prioritized Test Scenarios (5–6)

Escenarios diseñados según riesgo, impacto y criticidad del negocio.

---

## 🟥 TC01 — Place a valid single bet (Happy Path)
**Priority:** Critical  
**Risk Rationale:** Es el flujo principal del negocio. Si falla, el usuario no puede apostar.  

**Steps:**  
1. Seleccionar un partido pre‑match.  
2. Elegir una cuota válida (HOME, DRAW o AWAY).  
3. Introducir un stake válido (entre €1.00 y €100.00).  
4. Pulsar *Place Bet*.  
5. Verificar receipt.  

**Expected Result:**  
La apuesta se procesa correctamente, el balance se actualiza y el receipt muestra datos consistentes.

---

## 🟥 TC02 — Stake below minimum (€1.00)
**Priority:** Critical  
**Risk Rationale:** Validación financiera crítica. Evita pérdidas y errores de negocio.  

**Steps:**  
1. Seleccionar una cuota.  
2. Introducir stake inferior a €1.00 (ej. 0.50).  
3. Intentar colocar la apuesta.  

**Expected Result:**  
La UI muestra “Minimum stake is €1.00” y la API devuelve 422.

---

## 🟥 TC03 — Stake above maximum (€100.00)
**Priority
