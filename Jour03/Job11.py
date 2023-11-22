def time_to_text(minutes):
    heures = minutes // 60
    minutes_restantes = minutes % 60
    print(f"{heures} heures et {minutes_restantes} minutes")
    
time_to_text(70)