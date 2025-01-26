import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random
import time
import os

# Mapping of teams and their logos (image file names should match team names)
teams = {
    "real_madrid": "real_madrid.png", "barcelona": "barcelona.png", "bayern": "bayern.png", "man_city": "man_city.png",
    "liverpool": "liverpool.png", "chelsea": "chelsea.png", "juventus": "juventus.png", "psg": "psg.png",
    "dortmund": "dortmund.png", "inter_milan": "inter_milan.png", "ac_milan": "ac_milan.png", "atletico": "atletico.png",
    "arsenal": "arsenal.png", "tottenham": "tottenham.png", "napoli": "napoli.png", "leipzig": "leipzig.png"
}

# Team Strengths (Attack, Defense)
team_strength = {
    "real_madrid": (90, 85), "barcelona": (85, 80), "bayern": (88, 86), "man_city": (92, 88),
    "liverpool": (87, 83), "chelsea": (82, 80), "juventus": (80, 78), "psg": (89, 85),
    "dortmund": (78, 76), "inter_milan": (83, 80), "ac_milan": (82, 79), "atletico": (84, 82),
    "arsenal": (81, 78), "tottenham": (79, 76), "napoli": (80, 77), "leipzig": (76, 72)
}


class ChampionsLeagueApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🏆 Champions League Knockout Simulator")

        # Canvas
        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()

        # Button
        self.start_button = ttk.Button(root, text="Start Simulation", command=self.start_simulation)
        self.start_button.pack(pady=10)

        self.teams_list = list(teams.keys())

    def load_team_logo(self, team_name):
        """Load team logo; if the file does not exist, use the default black-and-white image"""
        img_path = os.path.join("team_logos", f"{team_name}.png")  # Use os.path.join() for cross-platform compatibility

        # Check if the file exists; otherwise, use the default black-and-white image
        if not os.path.exists(img_path):
            print(f"⚠️ Team logo for {team_name} not found. Using default image.")
            img_path = os.path.join("team_logos", "default_bw.png")  # Ensure the default image is in the team_logos directory

        try:
            img = Image.open(img_path)
            img = img.resize((80, 80))  # Standardized size
            return ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"❌ Failed to load logo for {team_name}: {e}")
            return None  # Prevent program crash

    def simulate_match(self, team1, team2):
        """Simulate a match"""
        attack1, defense1 = team_strength[team1]
        attack2, defense2 = team_strength[team2]

        # Calculate goals
        score1 = random.randint(0, (attack1 + 100 - defense2) // 10)
        score2 = random.randint(0, (attack2 + 100 - defense1) // 10)

        # Extra time
        if score1 == score2:
            extra1, extra2 = random.randint(0, 2), random.randint(0, 2)
            score1 += extra1
            score2 += extra2

        # Penalty shootout
        if score1 == score2:
            penalties1, penalties2 = 0, 0
            for _ in range(5):
                if random.random() < attack1 / (attack1 + attack2):
                    penalties1 += 1
                if random.random() < attack2 / (attack1 + attack2):
                    penalties2 += 1

            while penalties1 == penalties2:
                if random.random() < attack1 / (attack1 + attack2):
                    penalties1 += 1
                if random.random() < attack2 / (attack1 + attack2):
                    penalties2 += 1

            winner = team1 if penalties1 > penalties2 else team2
        else:
            winner = team1 if score1 > score2 else team2

        return winner, f"{score1} - {score2}"

    def start_simulation(self):
        """Start knockout stage simulation"""
        current_teams = self.teams_list[:]
        round_names = ["Round of 16", "Quarter-finals", "Semi-finals", "Final"]

        for round_num, round_name in enumerate(round_names):
            self.canvas.delete("all")
            self.canvas.create_text(400, 50, text=f"🏆 {round_name}", font=("Arial", 20, "bold"))

            next_round_teams = []
            for i in range(0, len(current_teams), 2):
                team1, team2 = current_teams[i], current_teams[i + 1]

                # Simulate match
                winner, score = self.simulate_match(team1, team2)

                # Display team logos & scores
                img1 = self.load_team_logo(team1)
                img2 = self.load_team_logo(team2)

                x = 200
                y = 150 + i * 40
                self.canvas.create_image(x, y, image=img1, anchor=tk.W)
                self.canvas.create_text(x + 90, y, text=f"{team1} vs {team2} ({score})", font=("Arial", 12))
                self.canvas.create_image(x + 400, y, image=img2, anchor=tk.W)

                next_round_teams.append(winner)

            current_teams = next_round_teams
            self.root.update()
            time.sleep(2)  # Allow users to see match progress

        # Champion display
        self.canvas.delete("all")
        champion = current_teams[0]
        img = self.load_team_logo(champion)
        self.canvas.create_text(400, 100, text="🏆 Champion:", font=("Arial", 20, "bold"))
        self.canvas.create_image(400, 250, image=img, anchor=tk.CENTER)
        self.canvas.create_text(400, 350, text=champion, font=("Arial", 24, "bold"), fill="gold")


if __name__ == "__main__":
    root = tk.Tk()
    app = ChampionsLeagueApp(root)
    root.mainloop()
