# Symbolická matematika v Pythonu – SymPy

Samostatná práce zaměřená na práci s knihovnou **SymPy** pro symbolickou matematiku v Pythonu.

## Co program dělá

Soubor `main.py` řeší 15 úloh zaměřených na základní operace knihovny SymPy:

| Úloha | Téma |
|-------|------|
| 1 | Vytváření symbolických výrazů (kinetická energie) |
| 2 | Dosazování hodnot a `.evalf()` |
| 3 | Zjednodušování výrazů – `expand()`, `simplify()` |
| 4 | Rozklad výrazu – `factor()` |
| 5 | Řešení rovnice – `solve()` |
| 6 | Kvadratická rovnice (trajektorie míče) |
| 7 | Soustava rovnic (ceny zboží) |
| 8 | Ohmův zákon – vyjádření proměnné |
| 9 | Hustota – vícenásobné dosazování |
| 10 | Rozvoj výrazu `(p+q)³` |
| 11 | Ověření rovnosti dvou výrazů |
| 12 | Průměrná rychlost – vyjádření proměnné |
| 13 | Kontrola řešení rovnice zpětným dosazením |
| 14 | Symbolický model ceny |
| 15 | Vlastní příklad – brzdná dráha auta |

## Jak spustit

### 1. Instalace závislostí

```bash
pip install sympy  --break-system-packages
```

### 2. Spuštění programu

```bash
python3 main.py
```

Program postupně vypíše výsledky všech 15 úloh do terminálu.

## Požadavky

- Python 3.8+
- sympy

## Použité funkce SymPy

- `sp.symbols()` – definice symbolů
- `sp.Eq()` – zápis rovnic
- `sp.solve()` – řešení rovnic a soustav
- `sp.expand()` – rozvinutí výrazů
- `sp.simplify()` – zjednodušení výrazů
- `sp.factor()` – rozklad na součin
- `.subs()` – dosazování hodnot
- `.evalf()` – numerické vyhodnocení
