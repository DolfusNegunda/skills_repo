# Weighted Decision Matrix Template

## Step 1 — Must-have gate (pass/fail; fail = eliminated)

| Must-have | Option A | Option B | Option C |
|-----------|----------|----------|----------|
| [hard requirement] | Pass | Pass | Fail (eliminated) |

## Step 2 — Weighted scoring (survivors only)

Weights sum to 100%. Score each 1–5 (anchor: 1 = poor, 3 = adequate, 5 = excellent).
Weighted = weight × score. Total = sum of weighted scores.

| Criterion | Weight | A score | A wtd | B score | B wtd |
|-----------|--------|---------|-------|---------|-------|
| [criterion 1] | 30% | 4 | 1.20 | 5 | 1.50 |
| [criterion 2] | 25% | 3 | 0.75 | 4 | 1.00 |
| [criterion 3] | 20% | 5 | 1.00 | 3 | 0.60 |
| [criterion 4] | 15% | 4 | 0.60 | 4 | 0.60 |
| [criterion 5] | 10% | 3 | 0.30 | 4 | 0.40 |
| **Total** | **100%** | | **3.85** | | **4.10** |

## Step 3 — Sensitivity
- Which weight, if changed, flips the ranking? At what value?
- If the winner flips easily → report as a close call.

## Recommendation
[Winner], because [deciding criteria]. Robustness: [robust / close — flips if …].
Set weights with the decision-owner BEFORE scoring.
