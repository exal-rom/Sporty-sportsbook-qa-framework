# Bug Reports — Single Bet Placement

---

## 🐞 BUG-01 — Place Bet button stuck in “Placing…” (no receipt shown)

**Severity:** Critical  
**Area:** Bet Placement / UI → API integration  

### Steps to Reproduce
1. Seleccionar un partido pre‑match  
2. Seleccionar cuota HOME  
3. Introducir stake válido (ej. €10.00)  
4. Pulsar *Place Bet*  

### Expected Result
- Apuesta procesada  
- Receipt mostrado  
- Balance actualizado  

### Actual Result
- Botón queda en estado “Placing…” indefinidamente  
- No aparece receipt  
- No se actualiza balance  

### Business Impact
El usuario no puede completar apuestas.  
Bloqueo total del flujo principal del negocio.

### Evidence
- Loading spinner infinito

---

## 🐞 BUG-02 — UI allows betting on events that already started

**Severity:** High  
**Area:** Odds / Match Card UI  

### Steps to Reproduce
1. Identificar partido con kickoff pasado  
2. Intentar seleccionar cuota  

### Expected Result
- Cuotas deshabilitadas (suspended)  
- No se permite selección  

### Actual Result
- Cuotas siguen clicables  
- Se puede abrir bet slip  

### Business Impact
Permite apuestas fuera de ventana pre‑match, violando reglas sportsbook.

---

## 🐞 BUG-03 — Stake precision validation missing in UI

**Severity:** Medium  
**Area:** Stake Input / Validation  

### Steps to Reproduce
1. Seleccionar cuota  
2. Introducir stake con más de 2 decimales (ej. 10.999)  

### Expected Result
- UI muestra error: “Max 2 decimal places”  
- API rechaza con 422  

### Actual Result
- UI no muestra error  
- API sí rechaza  

### Business Impact
Inconsistencia entre UI y API.  
El usuario cree que el valor es válido, pero la apuesta falla.

