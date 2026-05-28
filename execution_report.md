# Execution Report — Single Bet Placement

Este documento resume la ejecución de los 3 escenarios de mayor prioridad definidos en el Test Plan.

---

## 🟥 TC01 — Place a valid single bet (Happy Path)

**Status:** ❌ Failed  
**Environment:** Chrome latest, Desktop  
**User-ID:** test-user-123  

### Steps Executed
1. Seleccionar partido pre‑match  
2. Seleccionar cuota HOME  
3. Introducir stake válido (€10.00)  
4. Pulsar *Place Bet*  

### Expected Result
- Apuesta procesada  
- Balance actualizado  
- Receipt consistente  

### Actual Result
- El botón *Place Bet* queda en estado “Placing…” indefinidamente  
- No aparece receipt  
- No se actualiza balance  

### Evidence
- Pantallazo adjunto (loading infinito)

### Notes
Este fallo bloquea el flujo principal del negocio.

---

## 🟥 TC02 — Stake below minimum (€1.00)

**Status:** ✔️ Passed  
**Steps Executed**
1. Seleccionar cuota  
2. Introducir stake = 0.50  
3. Intentar colocar apuesta  

**Expected Result**
- UI muestra “Minimum stake is €1.00”  
- API devuelve 422  

**Actual Result**
- UI muestra mensaje correctamente  
- API devuelve 422  

---

## 🟥 TC04 — Attempt to bet after event has started (Suspension Rule)

**Status:** ⚠️ Partial Pass  
**Steps Executed**
1. Identificar partido con kickoff pasado  
2. Intentar seleccionar cuota  
3. Intentar enviar apuesta vía API  

**Expected Result**
- Cuotas deshabilitadas  
- API rechaza con 422 o 409  

**Actual Result**
- UI: cuotas siguen clicables (❌ incorrecto)  
- API: rechaza con 422 (✔️ correcto)  

### Notes
La UI no respeta la regla de suspensión pre‑match.

---

# Summary

| Test Case | Status |
|----------|--------|
| TC01 — Happy Path | ❌ Failed |
| TC02 — Stake Min | ✔️ Passed |
| TC04 — Suspension Rule | ⚠️ Partial |

**Conclusion:**  
El flujo principal está roto y la UI no respeta reglas de suspensión.  
La API sí valida correctamente la ventana pre‑match.
