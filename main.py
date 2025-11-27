#!/usr/bin/env python3
import sys
from app.ui.cli import main_menu

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n[!] Exiting...")
        sys.exit()
