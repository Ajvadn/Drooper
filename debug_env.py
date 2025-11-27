import sys
import os

print(f"Python Executable: {sys.executable}")
print(f"Python Version: {sys.version}")
print("Sys Path:")
for p in sys.path:
    print(f"  {p}")

try:
    import pyngrok
    print(f"Pyngrok found: {pyngrok.__file__}")
except ImportError:
    print("Pyngrok NOT found.")

try:
    import rich
    print(f"Rich found: {rich.__file__}")
except ImportError:
    print("Rich NOT found.")
