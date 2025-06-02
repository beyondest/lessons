

# 🧪 **Game Test Report – *Rift v1.3***

**Date:** 2025-05-24
**Tester:** Beyondest
**Build:** v1.3
**Platform:** Unity Editor (PC, NVIDIA GPU)
**Test Duration:** \~8 minutes
**Test Mode:** Manual Playtest
**Map/Scenario:** Lihgt faction/Dark faction

---

## Test Objectives : Exploration

* Validate basic gameplay loop for **Light faction** (player-controlled)
* Observe **Dark faction AI** behavior (Light faction controlled by AI)
* Test core features: **unit command, construction system, conjure function**, healing and damage mechanics
* Test whether crash will happen again after 30 seconds gameplay.

---

## Performance Metrics

* **Observed FPS:** 25–40
  *(measured via NVIDIA Game Monitor in Unity Editor)*
* **Performance Note:** FPS is significantly low for a scene with \~100 active units and hybrid physics; further optimization needed especially in physics-heavy frames.

---

## Key Bugs / Issues

### 1. **Unit Attack Animation/Behavior Bug**

* **Description:**
  When some melee units start an attack animation, they become stuck in a swinging animation loop and cease all movement. Only ranged units (e.g., archers) apply damage correctly.
* **Severity:** High
* **Reproducible:** Yes (frequent)

---

### 2. **Cleric Healing Malfunction**

* **Dark Faction:**
  When the player controls the **Light faction**, **Dark clerics aoe circle fail to heal allies**.
* **Light Faction (suspected):**
  Suspected similar issue where **Light clerics occasionally fail to heal** their allies.
* **Severity:** Medium
* **Reproducible:** Occasionally (Dark); Needs further confirmation (Light)

---

### 3. **Mage AOE Damage Bug**

* **Description:**
  Mage AOE spell **sometimes does not trigger any damage** on targets within range.
* **Severity:** Medium
* **Reproducible:** Intermittent

---

### 4. **AI Worker Navigation Bug**

* **Description:**
  While playing as the **Dark faction**, observed that **Light faction AI** sometimes leaves one or more workers stuck in place during a team gather/move command.
* **Severity:** Low
* **Reproducible:** Occasionally
* **Suggestion:** 
  Need to investigate whether team target assignment bugs are causing worker idling behavior, Or the animation swinging bug cause it.

---

## Open Questions / Concerns

* **Performance Bottleneck:**
  Even in-editor, FPS can stay with 40 fps, why in build it cannot stay in 40?
* **Mage AOE Attack Remake:**
  Aoe magic sword swing should not deal thoroughly damage to many walls. Wall should be able to stop sword swing. Also, the mage aoe damage trigger sometimes works bad.

---

## Fixed

### Crash problem in v1.2 fixed.
It is caused by not able to handled error in stat system. OocTag component manuaplation in UpdateOoc function cause the error **AppendRemovedComponentRecordError**. Use Ooc lookup to check first will solve it. 




## 📎 Attachments

* \[Optional: GIFs, logs, profile captures, crash dumps]


