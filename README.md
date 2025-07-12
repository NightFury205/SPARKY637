# ⚡ Sparky - Discord Bot

Sparky is a feature-rich, multipurpose Discord bot written in Python using `discord.py`. It includes moderation tools, a custom economy system, a dynamic shop, server-specific prefixes, anti-link filters, and more—all designed to enhance your Discord server.

---

## 📦 Features

### ⚙️ Admin Tools
- `*changeprefix` – Set a custom prefix for your server
- `*clear` – Bulk delete messages
- `*kick` / `*ban` / `*unban` – Member moderation
- `*whois` – Get detailed info about a member

### 💰 Economy System
- `*balance` – Check your wallet and bank
- `*beg` – Earn free coins randomly
- `*deposit` / `*withdraw` – Manage funds
- `*give` – Transfer coins to others
- `*slots` – Try your luck with a slot machine
- `*rob` – Steal coins from others
- `*shop` / `*buy` / `*sell` – Custom items marketplace
- `*bag` – Check your inventory
- `*leaderboard` – View top richest users

### 📊 Utility
- `*poll` – Create simple 2-option polls
- Anti-link protection (deletes messages with links)
- Emoji preview using `:emoji:` formatting

---

## 📁 Project Structure
Sparky/ <br>
│ <br>
├── Sparky.py # Main bot code <br>
├── mainbank.json # Stores user economy data <br>
├── prefixes.json # Stores custom prefixes per guild <br>
├── requirements.txt # Python dependencies <br>
├── Procfile # For Heroku or similar deployment <br>
└── README.md # This file! <br>


---

## 🚀 Setup

1. **Clone the repo:**
  ```bash
  git clone https://github.com/NightFury205/Sparky.git
  cd Sparky
  ```
3. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
3. Add your bot token: <br>
Replace "TOKEN" in the last line of Sparky.py with your actual bot token:
  ```bash
  client.run("YOUR_BOT_TOKEN")
  ```
4. Run the bot:
  ```bash
  python Sparky.py
  ```

---

## 🧠 Notes
1. All user-related data is stored in mainbank.json.
2. Server prefixes are stored in prefixes.json.
3. Supports dynamic reactions and anti-spam/anti-link measures.
4. Code is structured in a single Python file for easy understanding.

---

## 📜 License

This bot is made for personal and educational use. If you plan to redistribute or host it publicly, please give proper credit.
