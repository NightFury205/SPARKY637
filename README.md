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
Sparky/
> │

> ├── Sparky.py # Main bot code

> ├── mainbank.json # Stores user economy data

> ├── prefixes.json # Stores custom prefixes per guild

> ├── requirements.txt # Python dependencies

> ├── Procfile # For Heroku or similar deployment

> └── README.md # This file!
