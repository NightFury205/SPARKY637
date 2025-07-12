# ⚡ Sparky - Discord Bot

**Sparky** is a powerful, multipurpose Discord bot written in Python using `discord.py`.  
It includes moderation tools, a fully functional custom economy system, a virtual shop, per-server custom prefixes, anti-link filters, and more- all designed to enhance any Discord community.

---

## 📦 Features

### 🔧 Admin Tools
- `*changeprefix` Customize the bot prefix per server
- `*clear` Bulk delete messages
- `*kick`, `*ban`, `*unban` Basic moderation commands
- `*whois` User info lookup with embedded stats

### 💰 Economy System
- `*balance` Check wallet and bank balances
- `*beg` Random coin generator
- `*deposit`, `*withdraw` Transfer between wallet and bank
- `*give` Transfer coins to another user
- `*rob` Rob coins from another member
- `*slots` Fun slot machine minigame
- `*shop`, `*buy`, `*sell` Virtual shop with item trading
- `*bag` View inventory
- `*leaderboard` Global server ranking based on total wealth

### 🛠️ Utility & Fun
- `*poll` Quick polls with reaction-based voting
- Emoji preview: Use `:emoji_name:` to trigger emoji previews
- Automatic **anti-link protection** (blocks messages containing invite links)

---

## 📁 Project Structure

```
Sparky/
├── Sparky.py           # Main bot code
├── mainbank.json       # Economy database
├── prefixes.json       # Server-specific prefix settings
├── requirements.txt    # Python dependencies
├── Procfile            # Deployment config (e.g. for Heroku)
└── README.md           # This file
```

---

## 🚀 Setup & Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/NightFury205/Sparky.git
   cd Sparky
   ```

2. **Install required packages:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set your bot token:**

   Open `Sparky.py` and replace the last line with your actual bot token:

   ```python
   client.run("YOUR_BOT_TOKEN")
   ```

4. **Run the bot:**

   ```bash
   python Sparky.py
   ```

---

> [!NOTE]
> - User data is saved in `mainbank.json` (wallet, bank, inventory). <br>
> - Server-specific prefixes are stored in `prefixes.json`.<br>
> - `discord.py` is used as the core library — install via pip if not already present.<br>
> - Written as a single file for simplicity; can be modularized for large-scale use.<br>

---

## 📜 License

This bot is built for personal and educational use.  
If you plan to host it publicly or contribute, please give credit to the original author.
