import sympy as sp

# ============================================================
# Úloha 1 – Vytváření symbolických výrazů
# ============================================================
print("=" * 50)
print("Úloha 1 – Kinetická energie")
print("=" * 50)

m, v = sp.symbols('m v')
E = sp.Rational(1, 2) * m * v**2
print("Vzorec kinetické energie:", E)

# ============================================================
# Úloha 2 – Dosazování hodnot
# ============================================================
print("\n" + "=" * 50)
print("Úloha 2 – Dosazování hodnot")
print("=" * 50)

E_hodnota = E.subs([(m, 1200), (v, 25)])
print("Kinetická energie (m=1200 kg, v=25 m/s):", E_hodnota, "J")
print("Numerická hodnota (.evalf()):", E_hodnota.evalf(), "J")

# ============================================================
# Úloha 3 – Zjednodušování výrazů
# ============================================================
print("\n" + "=" * 50)
print("Úloha 3 – Zjednodušování výrazů")
print("=" * 50)

A, B = sp.symbols('A B')
vyraz3 = (A + B)**2 - (A**2 + 2*A*B)
print("Výraz:", vyraz3)
print("Po expand():", sp.expand(vyraz3))
print("Po simplify():", sp.simplify(vyraz3))
# Zůstane B**2

# ============================================================
# Úloha 4 – Rozklad výrazu
# ============================================================
print("\n" + "=" * 50)
print("Úloha 4 – Rozklad výrazu")
print("=" * 50)

x = sp.Symbol('x')
vyraz4 = x**2 - 25
print("Výraz:", vyraz4)
print("Po factor():", sp.factor(vyraz4))
# Připomíná vzorec rozdílu čtverců: a² - b² = (a+b)(a-b)

# ============================================================
# Úloha 5 – Řešení rovnice (dráha pohybu)
# ============================================================
print("\n" + "=" * 50)
print("Úloha 5 – Řešení rovnice s = v*t")
print("=" * 50)

s, t = sp.symbols('s t')
rovnice5 = sp.Eq(s, v * t)
print("Rovnice:", rovnice5)

t_reseni = sp.solve(rovnice5, t)
print("Čas t =", t_reseni[0])

# Dosazení: s=150, v=75
t_hodnota = t_reseni[0].subs([(s, 150), (v, 75)])
print("Pro s=150 km, v=75 km/h: t =", t_hodnota, "h")

# ============================================================
# Úloha 6 – Kvadratická rovnice (trajektorie míče)
# ============================================================
print("\n" + "=" * 50)
print("Úloha 6 – Kvadratická rovnice h = -5t² + 20t")
print("=" * 50)

t = sp.Symbol('t')
h = -5*t**2 + 20*t
rovnice6 = sp.Eq(h, 0)
print("Rovnice:", rovnice6)

casy = sp.solve(rovnice6, t)
print("Časy kdy h=0:", casy)
# t=0 znamená okamžik výstřelu/hodu, t=4 znamená dopad zpět na zem

# ============================================================
# Úloha 7 – Soustava rovnic (sešity a tužky)
# ============================================================
print("\n" + "=" * 50)
print("Úloha 7 – Soustava rovnic")
print("=" * 50)

sesit, tuzka = sp.symbols('sesit tuzka')
rov1 = sp.Eq(3*sesit + 2*tuzka, 44)
rov2 = sp.Eq(2*sesit + 5*tuzka, 46)
print("Rovnice 1:", rov1)
print("Rovnice 2:", rov2)

reseni7 = sp.solve([rov1, rov2], [sesit, tuzka])
print("Cena sešitu:", reseni7[sesit], "Kč")
print("Cena tužky:", reseni7[tuzka], "Kč")

# ============================================================
# Úloha 8 – Ohmův zákon U = R*I
# ============================================================
print("\n" + "=" * 50)
print("Úloha 8 – Ohmův zákon U = R*I")
print("=" * 50)

U, R, I = sp.symbols('U R I')
ohmova = sp.Eq(U, R * I)
print("Rovnice:", ohmova)

R_vyraz = sp.solve(ohmova, R)
I_vyraz = sp.solve(ohmova, I)
print("Odpor R =", R_vyraz[0])
print("Proud I =", I_vyraz[0])

# ============================================================
# Úloha 9 – Hustota (vícenásobné dosazování)
# ============================================================
print("\n" + "=" * 50)
print("Úloha 9 – Hustota ρ = m/V")
print("=" * 50)

rho, m_sym, V = sp.symbols('rho m V')
hustota_eq = sp.Eq(rho, m_sym / V)
print("Rovnice:", hustota_eq)

m_reseni = sp.solve(hustota_eq, m_sym)
print("Hmotnost m =", m_reseni[0])

m_hodnota = m_reseni[0].subs([(rho, 7800), (V, 0.002)])
print("Pro ρ=7800 kg/m³, V=0.002 m³: m =", m_hodnota.evalf(), "kg")
# Přibližně ocel/železo (hustota ~7800 kg/m³)

# ============================================================
# Úloha 10 – Rozvoj výrazu (p+q)³
# ============================================================
print("\n" + "=" * 50)
print("Úloha 10 – Rozvoj výrazu (p+q)³")
print("=" * 50)

p, q = sp.symbols('p q')
vyraz10 = (p + q)**3
print("Výraz:", vyraz10)
rozvinuto = sp.expand(vyraz10)
print("Po expand():", rozvinuto)
print("Počet členů:", len(rozvinuto.as_ordered_terms()))

# ============================================================
# Úloha 11 – Ověření rovnosti výrazů
# ============================================================
print("\n" + "=" * 50)
print("Úloha 11 – Ověření rovnosti (a+b)² = a²+2ab+b²")
print("=" * 50)

a, b = sp.symbols('a b')
vyraz_a = (a + b)**2
vyraz_b = a**2 + 2*a*b + b**2
rozdil = sp.simplify(vyraz_a - vyraz_b)
print("Výraz 1:", vyraz_a)
print("Výraz 2:", vyraz_b)
print("Rozdíl po simplify():", rozdil)
print("Jsou stejné:", rozdil == 0)

# ============================================================
# Úloha 12 – Průměrná rychlost v = s/t
# ============================================================
print("\n" + "=" * 50)
print("Úloha 12 – Průměrná rychlost v = s/t")
print("=" * 50)

v_sym, s_sym, t_sym = sp.symbols('v s t')
rychlost_eq = sp.Eq(v_sym, s_sym / t_sym)
print("Rovnice:", rychlost_eq)

s_vyraz = sp.solve(rychlost_eq, s_sym)
t_vyraz_sym = sp.solve(rychlost_eq, t_sym)
print("Dráha s =", s_vyraz[0])
print("Čas t =", t_vyraz_sym[0])
# Závislá proměnná závisí na kontextu – v je závislá na s a t

# ============================================================
# Úloha 13 – Kontrola řešení rovnice 3x + 7 = 25
# ============================================================
print("\n" + "=" * 50)
print("Úloha 13 – Kontrola řešení 3x + 7 = 25")
print("=" * 50)

x = sp.Symbol('x')
rovnice13 = sp.Eq(3*x + 7, 25)
print("Rovnice:", rovnice13)

x_reseni = sp.solve(rovnice13, x)
print("Řešení x =", x_reseni[0])

overeni = rovnice13.subs(x, x_reseni[0])
print("Ověření dosazením:", overeni)
# Dosazení zpět potvrdí správnost – zabrání chybám ve výpočtu

# ============================================================
# Úloha 14 – Symbolický model ceny C = p*q + d
# ============================================================
print("\n" + "=" * 50)
print("Úloha 14 – Model ceny C = p*q + d")
print("=" * 50)

p_sym, q_sym, d_sym, C_sym = sp.symbols('p q d C')
cena_eq = sp.Eq(C_sym, p_sym * q_sym + d_sym)
print("Rovnice:", cena_eq)

q_reseni = sp.solve(cena_eq, q_sym)
print("Počet kusů q =", q_reseni[0])

q_hodnota = q_reseni[0].subs([(C_sym, 550), (p_sym, 45), (d_sym, 100)])
print("Pro C=550, p=45, d=100: q =", q_hodnota.evalf())

# ============================================================
# Úloha 15 – Vlastní příklad: Výpočet brzdné dráhy
# ============================================================
print("\n" + "=" * 50)
print("Úloha 15 – Vlastní příklad: Brzdná dráha")
print("=" * 50)

# Problém: Brzdná dráha auta se vypočítá jako d = v² / (2*a)
# kde v je rychlost a a je zpomalení při brzdění.
# Chceme zjistit, při jaké rychlosti auto urazí nejvýše 50 m brzdnou dráhu.

v_br, a_br, d_br = sp.symbols('v a d', positive=True)
brzdna_eq = sp.Eq(d_br, v_br**2 / (2 * a_br))
print("Vzorec brzdné dráhy:", brzdna_eq)

# Vyjádření rychlosti v
v_max = sp.solve(brzdna_eq, v_br)
print("Maximální rychlost v =", v_max[0])

# Dosazení: d=50 m, a=6 m/s² (běžné brzdění)
v_hodnota = v_max[0].subs([(d_br, 50), (a_br, 6)])
print("Pro d=50 m, a=6 m/s²: v =", sp.simplify(v_hodnota).evalf(4), "m/s")
print("Tedy přibližně:", (sp.simplify(v_hodnota).evalf() * 3.6).evalf(4), "km/h")
print("\nVýsledek: Auto brzdí z max. ~88.2 km/h, aby zastavilo do 50 m při zpomalení 6 m/s².")