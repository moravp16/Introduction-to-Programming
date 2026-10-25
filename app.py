name = input("Jak se jmenujete? ")
style = input("Zvolte styl pozdravu (neformalni/formalni): ").strip().lower()

if style == "formalni":
    greeting = f"Dobrý den, {name}. Vítejte."
else:
    greeting = f"Čau, {name}! Rád tě vidím."

print(greeting)