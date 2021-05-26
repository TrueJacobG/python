# Walidacja adresu email

import re

email = input("Podaj swój email, a ja sprawdzę czy jest prawidłowy\n")

if re.match(r"^([A-Za-z0-9\.-]){3,20}@([A-Za-z0-9-\.])+\.([A-Za-z]){2,4}$",email):
    print("jest poprawny")
else:
    print("nie jest poprawny")
