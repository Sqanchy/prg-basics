# Program, który oblicza cenę po rabacie i kwotę obniżki

# Wczytanie danych od użytkownika
price = float(input("Enter price: "))
discount = float(input("Enter discount %: "))

# Obliczenia
price_after = price * (1 - discount / 100)  # cena po rabacie
reduction = price - price_after              # różnica (obniżka)

# Wyświetlenie wyników z dokładnością do dwóch miejsc po przecinku
print(f"Price with discount: {price_after:.2f}")
print(f"Reduction: {reduction:.2f}")