# Somnia-Auto
Somnia Auto — Automation bot for Somnia Network EVM-compatible blockchain testnet with faucet claiming, token transfers, smart contract deployment, transaction batching, multi-account management, proxy support, and Rich CLI for high-throughput metaverse blockchain interaction
<div align="center">

```
                                            ##              
  :####:                                    ##              
 :######                                    ##              
 ##:  :#                                                    
 ##         .####.   ## #:##:  ##.####    ####      :####   
 ###:      .######.  ########  #######    ####      ######  
 :#####:   ###  ###  ##.##.##  ###  :##     ##      #:  :## 
  .#####:  ##.  .##  ## ## ##  ##    ##     ##       :##### 
     :###  ##    ##  ## ## ##  ##    ##     ##     .####### 
       ##  ##.  .##  ## ## ##  ##    ##     ##     ## .  ## 
 #:.  :##  ###  ###  ## ## ##  ##    ##     ##     ##:  ### 
 #######:  .######.  ## ## ##  ##    ##  ########  ######## 
 .#####:    .####.   ## ## ##  ##    ##  ########    ###.## 
```

# Somnia-Auto

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![Somnia](https://img.shields.io/badge/Somnia-Network-00D4AA?style=for-the-badge)](https://somnia.network/)
[![EVM](https://img.shields.io/badge/EVM-Compatible-3C3C3D?style=for-the-badge&logo=ethereum&logoColor=white)](https://docs.somnia.network/)

**Retrodrop automation bot for Somnia Network — multi-threaded campaigns, faucet, swaps, Quills messaging, NFT minting, social linking.**

[Features](#features) • [Getting Started](#getting-started) • [Configuration](#configuration) • [Usage](#usage) • [FAQ](#faq)

</div>

---

## Official Links

| Resource | URL |
|----------|-----|
| **Somnia Network** | https://somnia.network/ |
| **Documentation** | https://docs.somnia.network/ |
| **Testnet / Faucet** | https://testnet.somnia.network/ |
| **Block Explorer** | https://browser.somnia.network/ |
| **Data Streams** | https://datastreams.somnia.network/ |
| **Blog** | https://blog.somnia.network/ |
| **Discord** | https://discord.com/invite/somnia |

---

## Features

<table>
<tr>
<td width="50%">

| Feature | Status |
|---------|:------:|
| Multi-threaded wallet processing | ✓ |
| Proxy support (IP rotation) | ✓ |
| Faucet claiming | ✓ |
| Token transfers | ✓ |
| Campaign automation | ✓ |
| Twitter / Discord linking | ✓ |
| Quills blockchain messaging | ✓ |

</td>
<td width="50%">

| Feature | Status |
|---------|:------:|
| Ping Pong token minting | ✓ |
| Ping Pong swaps | ✓ |
| NFT minting (SHANNON, NEE, YAPPERS, SOMNI) | ✓ |
| Discord inviter | ✓ |
| Username setup | ✓ |
| Rich CLI interface | ✓ |
| Configurable task presets | ✓ |

</td>
</tr>
</table>

---

## Getting Started

### Prerequisites

- **Python** 3.11.1 to 3.11.6
- **pip** (latest recommended)
- **Somnia-compatible private keys** (EVM format)
- **Optional:** Proxies, Twitter API tokens, Discord tokens

### Installation

```bash
# Clone the repository
git clone https://github.com/Dcurig/Somnia-Auto
cd Somnia-Auto

# Install dependencies
pip install -r requirements.txt
```

### Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| rich | ≥13.7.0 | Rich CLI, panels, tables |
| PyYAML | ≥6.0 | Config parsing |
| requests | ≥2.28.0 | HTTP requests |

---

## Configuration

Edit `config.yaml` in the project root. Example with realistic values:

```yaml
# Somnia-Auto Configuration

SETTINGS:
  THREADS: 4
  ATTEMPTS: 5
  ACCOUNTS_RANGE: [0, 0]      # [0, 0] = all wallets
  EXACT_ACCOUNTS_TO_USE: []
  SHUFFLE_WALLETS: true
  PAUSE_BETWEEN_ATTEMPTS: [3, 10]
  PAUSE_BETWEEN_SWAPS: [3, 10]

SOMNIA_NETWORK:
  SOMNIA_SWAPS:
    BALANCE_PERCENT_TO_SWAP: [5, 10]
    NUMBER_OF_SWAPS: [1, 2]

  SOMNIA_TOKEN_SENDER:
    BALANCE_PERCENT_TO_SEND: [1.5, 3]
    NUMBER_OF_SENDS: [1, 1]
    SEND_ALL_TO_DEVS_CHANCE: 50

  SOMNIA_CAMPAIGNS:
    REPLACE_FAILED_TWITTER_ACCOUNT: false

  DISCORD_INVITER:
    INVITE_LINK: "https://discord.gg/your-invite"
```

Place private keys in `data/private_keys.txt`, proxies in `data/proxies.txt` (format: `http://user:pass@ip:port`), and optional tokens in `data/twitter_tokens.txt` and `data/discord_tokens.txt`.

---

## Usage

**Windows:** Double-click `run.bat` or run:

```bash
python main.py
```

**CLI menu mockup:**

```
┌─────────────────────────────────────────────────────────────────┐
│                    Main Menu                                     │
├───┬─────────────────────────────┬───────────────────────────────┤
│ # │ Action                       │ Description                   │
├───┼─────────────────────────────┼───────────────────────────────┤
│ 1 │ Install Dependencies         │ pip install -r requirements   │
│ 2 │ Settings                     │ Edit config.yaml              │
│ 3 │ Configure Tasks              │ Edit tasks.py presets         │
│ 4 │ Data Management              │ Manage keys, proxies, tokens  │
│ 5 │ Run Bot                      │ Launch Somnia-Auto automation │
│ 6 │ About                        │ Project info & hashtags       │
│ 0 │ Exit                         │ Exit the application          │
└───┴─────────────────────────────┴───────────────────────────────┘

Select option [0]: 5
```

---

## Project Structure

```
Somnia-Auto/
├── main.py              # Entry point, Rich CLI menu
├── tasks.py             # Task presets (CAMPAIGNS, FAUCET, etc.)
├── config.yaml          # Threads, attempts, Somnia settings
├── requirements.txt     # Python dependencies
├── run.bat              # Windows launcher
├── about/
│   ├── hashtags.txt     # Project hashtags
│   └── somnia_about.txt # Project description
├── data/
│   ├── private_keys.txt
│   ├── proxies.txt
│   ├── twitter_tokens.txt
│   ├── discord_tokens.txt
│   └── random_message_quills.txt
└── src/
    ├── modules/
    └── utils/
```

---

## FAQ

<details>
<summary><b>What is Somnia Network?</b></summary>

Somnia is a high-performance EVM-compatible Layer 1 blockchain for gaming, metaverses, and real-time applications. It targets 1M+ TPS, sub-second finality, and sub-cent fees. Mainnet launched September 2025.
</details>

<details>
<summary><b>Which Python version is required?</b></summary>

Python 3.11.1 through 3.11.6 is recommended. The bot uses Rich for the CLI and PyYAML for config parsing.
</details>

<details>
<summary><b>How do I add wallets?</b></summary>

Add Somnia-compatible private keys (0x-prefixed or raw hex) to `data/private_keys.txt`, one per line. Use the main menu → Data Management to edit.
</details>

<details>
<summary><b>What task presets are available?</b></summary>

CAMPAIGNS, FAUCET, SEND_TOKENS, CONNECT_SOCIALS, MINT_PING_PONG, SWAPS_PING_PONG, QUILLS_CHAT, SOMNIA_NETWORK_SET_USERNAME, SOMNIA_NETWORK_INFO, DISCORD_INVITER. Configure via menu option 3 or by editing `tasks.py`.
</details>

<details>
<summary><b>Do I need proxies?</b></summary>

Proxies are optional but recommended for multi-account farming. Use format `http://user:pass@ip:port` in `data/proxies.txt`.
</details>

<details>
<summary><b>Where can I get testnet tokens?</b></summary>

Use the Somnia faucet at https://testnet.somnia.network/ or request tokens in Discord (#dev-chat, tag @emma_odia).
</details>

<details>
<summary><b>Is this safe for mainnet?</b></summary>

This bot is intended for **educational and testnet use only**. Use at your own risk. Never expose private keys. Respect platform ToS and applicable laws.
</details>

---

## Disclaimer

This software is provided **for educational and testnet purposes only**. Use responsibly and at your own risk. The authors are not responsible for any loss of funds, account bans, or violations of platform terms of service. Always comply with applicable laws and Somnia Network policies.

---

<div align="center">

**Support:** [@jackthedevv](https://t.me/jackthedevv)

**Donations (ETH):** `0x7F3a8E4c1D6f9A5e0B3d7C8a2F4e6D1b9C5a0312`

*If this project helped you, consider giving it a ⭐*

</div>
