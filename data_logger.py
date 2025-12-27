import csv

def log_move(player, position):
    with open("game_data.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([player, position])
