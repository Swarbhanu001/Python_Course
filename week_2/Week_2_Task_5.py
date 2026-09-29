from datetime import date

events = {
    "DEW21 Museumsnacht": (date(2026, 9, 19), date(2026, 9, 19)),
    "Kunstverein guided tours + DDDR synth workshop": (date(2026, 9, 19), date(2026, 9, 19)),
    "Kindermuseum Adlerturm medieval day + fire show": (date(2026, 9, 19), date(2026, 9, 19)),
    "Naturmuseum night tour + microscopy stations": (date(2026, 9, 19), date(2026, 9, 19)),
    "Institut français Bibliobus": (date(2026, 9, 19), date(2026, 9, 19)),
    "Senior bus tours through the city districts": (date(2026, 9, 18), date(2026, 9, 18)),
    "Eving movement programme": (date(2026, 9, 23), date(2026, 9, 23)),
    "Democracy Day Scharnhorst": (date(2026, 9, 25), date(2026, 9, 25)),
}

museum_night = date(2026, 9, 19)

running = [name for name, (start, end) in events.items()
           if start <= museum_night <= end]

print("Events running during the Night of Museums:")
for name in running:
    print("-", name)