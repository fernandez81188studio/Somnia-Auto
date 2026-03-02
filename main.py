#!/usr/bin/env python3
"""
Somnia-Auto — Retrodrop Automation Bot
Rich Interactive Interface for Somnia Network automation
SUPPORT: @jackthedevv
"""

import os
import sys

from utils import ensure_env

import json
import subprocess
from pathlib import Path
from typing import Any, Dict, List

import yaml
from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm, IntPrompt, Prompt
from rich.table import Table
from rich.text import Text

BASE_DIR = Path(__file__).resolve().parent
REQUIREMENTS_PATH = BASE_DIR / "requirements.txt"
CONFIG_PATH = BASE_DIR / "config.yaml"
TASKS_PATH = BASE_DIR / "tasks.py"
README_PATH = BASE_DIR / "README.md"
ABOUT_HASHTAGS = BASE_DIR / "about" / "hashtags.txt"
ABOUT_SOMNIA = BASE_DIR / "about" / "somnia_about.txt"
DATA_DIR = BASE_DIR / "data"

DATA_FILES = {
    "1": ("private_keys.txt", "Somnia-compatible private keys"),
    "2": ("proxies.txt", "Proxies (http://user:pass@ip:port)"),
    "3": ("twitter_tokens.txt", "Twitter API tokens"),
    "4": ("discord_tokens.txt", "Discord tokens"),
    "5": ("random_message_quills.txt", "Quills messages"),
}

LOGO = r"""
                                                            
                                                            
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
                                                            
                                                            
                                                            
                                                            
"""

TASK_PRESETS = [
    "CAMPAIGNS",
    "FAUCET",
    "SEND_TOKENS",
    "CONNECT_SOCIALS",
    "MINT_PING_PONG",
    "SWAPS_PING_PONG",
    "QUILLS_CHAT",
    "SOMNIA_NETWORK_SET_USERNAME",
    "SOMNIA_NETWORK_INFO",
    "DISCORD_INVITER",
]

console = Console()


def load_config() -> Dict[str, Any]:
    """Load config.yaml"""
    if not CONFIG_PATH.exists():
        return {}
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    except Exception as e:
        console.print(f"[red]Error loading config: {e}[/red]")
        return {}


def save_config(config: Dict[str, Any]) -> bool:
    """Save config.yaml"""
    try:
        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            yaml.dump(config, f, default_flow_style=False, allow_unicode=True)
        return True
    except Exception as e:
        console.print(f"[red]Error saving config: {e}[/red]")
        return False


def show_logo() -> None:
    """Display logo and header"""
    console.clear()
    text = Text(LOGO, style="bold cyan")
    panel = Panel.fit(
        text,
        title="[bold yellow]SOMNIA-AUTO — Retrodrop Automation Bot[/bold yellow]",
        subtitle="[dim]SUPPORT @jackthedevv[/dim]",
        border_style="cyan",
        box=box.DOUBLE,
    )
    console.print(panel)


def show_main_menu() -> str:
    """Display main menu and return user choice"""
    table = Table(
        title="[bold]Main Menu[/bold]",
        title_style="bold cyan",
        box=box.DOUBLE_EDGE,
        show_header=True,
        header_style="bold magenta",
        border_style="cyan",
        padding=(0, 2),
    )
    table.add_column("#", style="bold yellow", justify="center", width=4)
    table.add_column("Action", style="bold white")
    table.add_column("Description", style="dim")

    table.add_row("1", "[green]Install Dependencies[/green]", "pip install -r requirements.txt")
    table.add_row("2", "[cyan]Settings[/cyan]", "Edit config.yaml (THREADS, ATTEMPTS, etc.)")
    table.add_row("3", "[magenta]Configure Tasks[/magenta]", "Edit tasks.py presets")
    table.add_row("4", "[blue]Data Management[/blue]", "Manage private_keys, proxies, tokens")
    table.add_row("5", "[bright_green]Run Bot[/bright_green]", "Launch Somnia-Auto automation")
    table.add_row("6", "[yellow]About[/yellow]", "Project info & hashtags")
    table.add_row("0", "[red]Exit[/red]", "Exit the application")

    console.print(table)
    choice = Prompt.ask("[bold cyan]Select option[/bold cyan]", default="0")
    return choice.strip()


def action_install_dependencies() -> None:
    """Install dependencies via pip"""
    show_logo()
    console.rule("[bold green]Install Dependencies[/bold green]", style="green")

    if not REQUIREMENTS_PATH.exists():
        console.print(f"[red]File {REQUIREMENTS_PATH.name} not found.[/red]")
        Prompt.ask("[yellow]Press Enter to return[/yellow]", default="")
        return

    cmd = [sys.executable, "-m", "pip", "install", "-r", str(REQUIREMENTS_PATH)]
    console.print(f"[cyan]Running:[/cyan] [bold]{' '.join(cmd)}[/bold]\n")

    with console.status("[bold green]Installing...[/bold green]", spinner="dots"):
        result = subprocess.run(cmd, capture_output=True, text=True)

    output = (result.stdout or "") + ("\n" + (result.stderr or "") if result.stderr else "")
    panel = Panel(
        output or "(no output)",
        title="pip output",
        border_style="green" if result.returncode == 0 else "red",
    )
    console.print(panel)

    if result.returncode == 0:
        console.print("[bold green]Dependencies installed successfully.[/bold green]")
    else:
        console.print(f"[bold red]Installation failed (code {result.returncode}).[/bold red]")

    Prompt.ask("[yellow]Press Enter to return[/yellow]", default="")


def action_settings() -> None:
    """Settings menu - edit config.yaml"""
    show_logo()
    console.rule("[bold cyan]Settings[/bold cyan]", style="cyan")

    config = load_config()
    settings = config.get("SETTINGS", {})

    defaults = {
        "THREADS": 1,
        "ATTEMPTS": 5,
        "ACCOUNTS_RANGE": [0, 0],
        "SHUFFLE_WALLETS": True,
        "PAUSE_BETWEEN_ATTEMPTS": [3, 10],
        "PAUSE_BETWEEN_SWAPS": [3, 10],
    }

    for k, v in defaults.items():
        if k not in settings:
            settings[k] = v

    if "SETTINGS" not in config:
        config["SETTINGS"] = settings

    table = Table(title="Current Settings", box=box.ROUNDED, border_style="yellow")
    table.add_column("Key", style="bold cyan")
    table.add_column("Value", style="white")

    for key, value in settings.items():
        table.add_row(key, str(value))
    console.print(table)
    console.print()

    console.print("[bold]Edit settings:[/bold]")
    threads = IntPrompt.ask("THREADS (1-32)", default=settings.get("THREADS", 1))
    if 1 <= threads <= 32:
        settings["THREADS"] = threads

    attempts = IntPrompt.ask("ATTEMPTS (retries)", default=settings.get("ATTEMPTS", 5))
    if attempts > 0:
        settings["ATTEMPTS"] = attempts

    shuffle = Confirm.ask("SHUFFLE_WALLETS", default=settings.get("SHUFFLE_WALLETS", True))
    settings["SHUFFLE_WALLETS"] = shuffle

    pause_min = IntPrompt.ask("PAUSE_BETWEEN_ATTEMPTS min (sec)", default=settings.get("PAUSE_BETWEEN_ATTEMPTS", [3, 10])[0])
    pause_max = IntPrompt.ask("PAUSE_BETWEEN_ATTEMPTS max (sec)", default=settings.get("PAUSE_BETWEEN_ATTEMPTS", [3, 10])[1])
    settings["PAUSE_BETWEEN_ATTEMPTS"] = [pause_min, pause_max]

    config["SETTINGS"] = settings
    if save_config(config):
        console.print("[bold green]Settings saved.[/bold green]")

    Prompt.ask("[yellow]Press Enter to return[/yellow]", default="")


def action_configure_tasks() -> None:
    """Configure task presets in tasks.py"""
    show_logo()
    console.rule("[bold magenta]Configure Tasks[/bold magenta]", style="magenta")

    table = Table(title="Available Task Presets", box=box.ROUNDED, border_style="magenta")
    table.add_column("#", style="bold yellow", width=3)
    table.add_column("Preset", style="cyan")

    for i, preset in enumerate(TASK_PRESETS, 1):
        table.add_row(str(i), preset)
    console.print(table)
    console.print()

    console.print("[bold]Select presets (comma-separated numbers, e.g. 1,3,5):[/bold]")
    choice = Prompt.ask("Presets", default="1")

    try:
        indices = [int(x.strip()) for x in choice.split(",")]
        selected = [TASK_PRESETS[i - 1] for i in indices if 1 <= i <= len(TASK_PRESETS)]
        if not selected:
            selected = ["CAMPAIGNS"]
    except (ValueError, IndexError):
        selected = ["CAMPAIGNS"]

    tasks_content = f'''"""
Somnia-Auto — Task Configuration
"""

TASKS = {selected}
'''
    TASKS_PATH.write_text(tasks_content, encoding="utf-8")
    console.print(f"[green]Tasks updated: {selected}[/green]")

    Prompt.ask("[yellow]Press Enter to return[/yellow]", default="")


def action_data_management() -> None:
    """Manage data files (view/edit)"""
    show_logo()
    console.rule("[bold blue]Data Management[/bold blue]", style="blue")

    table = Table(title="Data Files", box=box.ROUNDED, border_style="blue")
    table.add_column("#", style="bold yellow", width=3)
    table.add_column("File", style="cyan")
    table.add_column("Description", style="white")
    table.add_column("Status", style="dim")

    for key, (fname, desc) in DATA_FILES.items():
        filepath = DATA_DIR / fname
        status = "[green]exists[/green]" if filepath.exists() else "[red]missing[/red]"
        table.add_row(key, fname, desc, status)
    table.add_row("0", "Back", "Return to main menu", "")
    console.print(table)
    console.print()

    choice = Prompt.ask("Select file to view/edit", default="0")
    if choice == "0":
        return

    if choice not in DATA_FILES:
        console.print("[red]Invalid option.[/red]")
        Prompt.ask("[yellow]Press Enter[/yellow]", default="")
        return

    fname, _ = DATA_FILES[choice]
    path = DATA_DIR / fname

    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("# Add entries, one per line\n", encoding="utf-8")

    content = path.read_text(encoding="utf-8")
    console.print(Panel(content, title=f"data/{fname}", border_style="blue"))
    console.print("\n[dim]Edit file directly in data/ folder, or enter new content (empty = keep):[/dim]")
    new_content = Prompt.ask("New content (multiline: paste and end with empty line)")
    if new_content.strip():
        path.write_text(new_content, encoding="utf-8")
        console.print("[green]File updated.[/green]")

    Prompt.ask("[yellow]Press Enter to return[/yellow]", default="")


def action_run_bot() -> None:
    """Run the Somnia-Auto bot"""
    show_logo()
    console.rule("[bold bright_green]Run Bot[/bold bright_green]", style="green")

    config = load_config()
    console.print(Panel(
        "[bold]Launching Somnia-Auto...[/bold]\n\n"
        "The bot will execute tasks from tasks.py using config.yaml.\n"
        "Ensure data files are configured (private_keys.txt, proxies.txt, etc.)\n\n"
        "[dim]Note: Full bot logic requires the Somnia-Auto repository.\n"
        "Clone: git clone https://github.com/Dcurig/Somnia-Auto[/dim]",
        title="Run Bot",
        border_style="green",
    ))

    if Confirm.ask("\nProceed with run?", default=True):
        bot_runner = BASE_DIR / "run_bot.py"
        if bot_runner.exists():
            subprocess.run([sys.executable, str(bot_runner)], cwd=BASE_DIR)
        else:
            console.print("\n[cyan]Simulating bot start...[/cyan]")
            with console.status("[bold green]Processing wallets...[/bold green]", spinner="dots"):
                import time
                time.sleep(2)
            console.print("[green]Bot would process wallets according to tasks.py and config.yaml.[/green]")
            console.print("[dim]Add run_bot.py or integrate with Somnia-Auto source for full automation.[/dim]")

    Prompt.ask("[yellow]Press Enter to return[/yellow]", default="")


def action_about() -> None:
    """About project and hashtags"""
    show_logo()
    console.rule("[bold yellow]About Somnia-Auto[/bold yellow]", style="yellow")

    about_text = ""
    if README_PATH.exists():
        about_text = README_PATH.read_text(encoding="utf-8")
    elif ABOUT_SOMNIA.exists():
        about_text = ABOUT_SOMNIA.read_text(encoding="utf-8")
    else:
        about_text = (
            "Somnia-Auto — Retrodrop Automation Bot for Somnia Network.\n"
            "Multi-threaded, proxy support, campaigns, NFT minting, Quills messaging.\n"
            "SUPPORT: @jackthedevv"
        )

    console.print(Panel(about_text, title="About", border_style="yellow"))
    console.print()

    hashtags_text = ""
    if ABOUT_HASHTAGS.exists():
        hashtags_text = ABOUT_HASHTAGS.read_text(encoding="utf-8")
    else:
        hashtags_text = "#Somnia #Retrodrop #Airdrop #Automation #Blockchain"

    console.print(Panel(hashtags_text, title="about/hashtags.txt", border_style="magenta"))

    Prompt.ask("[yellow]Press Enter to return[/yellow]", default="")


@ensure_env
def main() -> None:
    os.chdir(BASE_DIR)

    actions = {
        "1": action_install_dependencies,
        "2": action_settings,
        "3": action_configure_tasks,
        "4": action_data_management,
        "5": action_run_bot,
        "6": action_about,
    }

    while True:
        show_logo()
        choice = show_main_menu()

        if choice == "0":
            console.print("\n[bold red]Exiting Somnia-Auto. Goodbye![/bold red]")
            break

        if choice in actions:
            actions[choice]()
        else:
            console.print("[red]Invalid option. Try again.[/red]")
            Prompt.ask("[yellow]Press Enter[/yellow]", default="")


if __name__ == "__main__":
    main()
