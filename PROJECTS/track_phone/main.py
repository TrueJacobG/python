import phonenumbers as pn
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

# with +country_number

number = input()

modNumber1 = pn.parse(number, "CH")
modNumber2 = pn.parse(number, "RO")
modNumber3 = pn.parse(number, "GB")

print(geocoder.description_for_number(modNumber1, "en"))
print(carrier.name_for_number(modNumber2, "en"))
print(timezone.time_zones_for_number(modNumber3))


# find number in text
text = "Hello sad asdasiujh oasudouiaspuidfb uipahbspiudbasubdpiu abpsda ipuhaspdh piaushdpuh a 690873928 ksjdnf;jsdnf;io"

# random number

for number in pn.PhoneNumberMatcher(text, "PL"):
    print(pn.format_number(number.number, pn.PhoneNumberFormat.E164))
