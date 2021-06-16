# 0. Hello World!

print("Hello World!")


# 1. Variabili

x = "Ciao di nuovo!"  # Stringa

print(x)

# 2. Calcoli semplici

a = 12345
b = 7

c = a + b

print("Il risultato è", c)

print("Il risultato è " + str(c))


# 3. Librerie

# Math

number = 100

import math

print("La radice quadrata di " + str(number) + " è " + str(math.sqrt(number)))


# Datetime

import datetime
today = datetime.date.today()
print("Oggi:\t", today)


# Domani

print("Domani:\t", datetime.date.today() + datetime.timedelta(days=1))

