
events = {
    "DEW21 Museumsnacht at Dortmunder U": "2026-09-19",
    "INDUSTRIAL: Seidenstrassen 3000 short tours": "2026-09-19",
    "Print Your Own - Screen Printing": "2026-09-19",
   
}

target_date = "2026-09-19"

print("Dortmund Night of Museums")
print("Date:", target_date)
print()

print("Events taking place on this date:")

for event, date in events.items():
    if date == target_date:
        print("-", event)