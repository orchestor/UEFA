以下是 README 文件的内容，适用于你的 **Champions League Knockout Simulator** 项目，包括描述、安装步骤、使用方法等。

---

### **🏆 Champions League Knockout Simulator**
A graphical simulation of the UEFA Champions League knockout stage, where teams compete in elimination rounds until the final champion is determined.

## **📌 Features**
- 16 top European football teams with **realistic strengths** (attack & defense ratings).
- **Automatic match simulation**, including:
  - Regular time scoring
  - **Extra time** if needed
  - **Penalty shootout** to determine the winner
- **Team logos** displayed on the canvas.
- Randomized match results based on team strengths.

---

## **📂 Project Structure**
```
ChampionsLeagueSimulator/
│── team_logos/          # Directory for storing team logo images
│── main.py              # Main application file (Tkinter-based UI)
│── download_logos.py    # Script to download team logos automatically
│── README.md            # Project documentation
```

---

## **⚙️ Installation**
### **1️⃣ Install Dependencies**
Make sure you have Python installed (>=3.7). Then, install required libraries:
```bash
pip install pillow requests
```

### **2️⃣ Run the Application**
Simply execute:
```bash
python main.py
```
This will launch the Champions League simulator with a **graphical user interface (GUI).**

---

## **🎮 How to Use**
### **1️⃣ Start Simulation**
- Click the **"Start Simulation"** button.
- The tournament starts from the **Round of 16**.
- The application simulates all matches **until the final champion is determined**.

### **2️⃣ Match Simulation**
Each match follows:
1. **Regular time**: Goals are calculated based on team strength.
2. **Extra time**: If tied, teams have a chance to score in extra time.
3. **Penalty shootout**: If still tied, penalties decide the winner.

### **3️⃣ Winning Team**
- The final **champion** is displayed with a **golden text** and its **team logo**.

---

## **⚽ Team Strengths**
Each team has predefined **attack & defense** ratings:
```python
team_strength = {
    "real_madrid": (90, 85), "barcelona": (85, 80), "bayern": (88, 86), "man_city": (92, 88),
    "liverpool": (87, 83), "chelsea": (82, 80), "juventus": (80, 78), "psg": (89, 85),
    "dortmund": (78, 76), "inter_milan": (83, 80), "ac_milan": (82, 79), "atletico": (84, 82),
    "arsenal": (81, 78), "tottenham": (79, 76), "napoli": (80, 77), "leipzig": (76, 72)
}
```
- **Higher attack** = more goals scored.
- **Higher defense** = harder to concede goals.

---

## **🖼️ Team Logos**
- Logos are stored in the `team_logos/` directory.
- If a logo is missing, a **default black & white image** (`default_bw.png`) is used.

### **Automatically Download Logos**
You can run `download_logos.py` to **download team logos automatically**:
```bash
python download_logos.py
```

---

## **📜 License**
This project is for **educational and entertainment purposes only.**  
It is **not affiliated with UEFA, FIFA, or any football clubs.**  

---

🚀 **Enjoy the Champions League Knockout Simulator!** 🏆⚽🎮