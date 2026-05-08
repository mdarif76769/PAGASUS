import os, base64, zlib, sys, hashlib, hmac
from colorama import Fore, Style, init
init(autoreset=True)

# -------- Screen clear --------
os.system("cls" if os.name == "nt" else "clear")

# -------- SAME SECRET used in encryptor.py --------
SECRET = b"secret!"

# -------- Paste your BLOB here --------
BLOB = "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"   # your encrypted payload blob (same as before)

import base64
import sys
import zlib
import time
import os
import platform
import random
from datetime import datetime
from colorama import Fore, Style, init

# কালার ইনিশিয়ালাইজেশন
init(autoreset=True)

# আপনার নাম (ARIF) এখানে Hex ফরম্যাটে এনকোড করা আছে
# সরাসরি 'ARIF' লেখা নেই, তাই সোর্স কোড দেখে চেনা অসম্ভব।
SECRET_HEX = "41524946" 

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(text, speed=0.02, color=Fore.WHITE):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(speed)
    print(Style.RESET_ALL)

def loading_bar(duration=1.5, task_name="Loading"):
    for i in range(21):
        percent = i * 5
        bar = "█" * i + "░" * (20 - i)
        sys.stdout.write(f"\r{Fore.WHITE}[*] {task_name}: {Fore.RED if 'Critical' in task_name else Fore.CYAN}|{bar}| {percent}%")
        sys.stdout.flush()
        time.sleep(duration/20)
    print(f" {Fore.GREEN}DONE")

def check_auth(u_in):
    try:
        # ইনপুটকে Hex-এ কনভার্ট করে ম্যাচ করানো হচ্ছে
        target = bytes.fromhex(SECRET_HEX).decode().upper()
        return u_in.strip().upper() == target
    except: return False

# --- শুরু হচ্ছে মেইন ইন্টারফেস ---
clear_screen()

# একটি ছোট ম্যাট্রিক্স গ্লিচ ইফেক্ট
def glitch_init():
    chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    for _ in range(15):
        print(Fore.GREEN + "".join(random.choice(chars) for _ in range(60)), end='\r')
        time.sleep(0.05)
    print(" " * 60, end='\r')

glitch_init()

print(f"""{Fore.RED}
    ▓█████▄  ▄▄▄       ███▄    █   ▄████ ▓█████  ██▀███   █    ██   ██████ 
    ▒██▀ ██▌▒████▄     ██ ▀█   █  ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒ ██  ▓██▒▒██    ▒ 
    ░██   █▌▒██  ▀█▄   ▓██  ▀█ ██▒▒██░▄▄▄░▒███   ▓██ ░▄█ ▒▓██  ▒██░░ ▓██▄   
    ░▓█▄   ▌░██▄▄▄▄██  ▓██▒  ▐▌██▒░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄  ▓▓█  ░██░  ▒   ██▒
    ░▒████▓  ▓█   ▓██▒ ▒██░   ▓██░░▒▓███▀▒░▒████▒░██▓ ▒██▒▒▒█████▓ ▒██████▒▒
     ▒▒▓  ▒  ▒▒   ▓▒█░ ░ ▒░   ▒ ▒  ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░
     ░ ▒  ▒   ▒   ▒▒ ░ ░ ░░   ░ ▒░  ░   ░  ░ ░  ░  ░▒ ░ ▒░░░▒░ ░ ░ ░ ░▒  ░ ░
""")

print(f"{Fore.CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(f"{Fore.WHITE} HOST: {platform.node()} | {Fore.WHITE}SYSTEM: {platform.system()} | TIME: {datetime.now().strftime('%H:%M:%S')}")
print(f"{Fore.CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

typewriter(">> BOOTING SECURE ENVIRONMENT...", 0.03, Fore.YELLOW)
loading_bar(1.0, "Integrity Check")
loading_bar(0.8, "Encrypted Tunnel")
print()

# অথোরাইজেশন ইনপুট
key = input(f"{Fore.WHITE}┌──({Fore.RED}root@cyber-lab{Fore.WHITE})-[{Fore.YELLOW}/dev/null{Fore.WHITE}]\n└─{Fore.CYAN}$ {Fore.WHITE}ENTER MASTER KEY: ")

if not check_auth(key):
    print(f"\n{Fore.RED}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"{Fore.RED}[!] ACCESS VIOLATION: INVALID KEY")
    print(f"{Fore.RED}[!] ALERTING SYSTEM ADMINISTRATOR...")
    print(f"{Fore.RED}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    time.sleep(2)
    sys.exit(1)

# অথোরাইজেশন সফল
print(f"\n{Fore.GREEN}[√] IDENTITY CONFIRMED. ACCESS GRANTED.")
loading_bar(1.5, "Decrypting Payload")
loading_bar(0.5, "Executing Stream")
print()

try:
    # আপনার ডিক্রিপশন লজিক এখানে (BLOB এবং SECRET আগে থেকে ডিফাইন করা থাকতে হবে)
    raw = base64.b64decode(BLOB)
    decrypted = bytes([b ^ SECRET[i % len(SECRET)] for i, b in enumerate(raw)])
    code = zlib.decompress(decrypted).decode("utf-8")
    
    typewriter(">> PAYLOAD DEPLOYED SUCCESSFULLY...", 0.04, Fore.GREEN)
    print(f"{Fore.YELLOW}="*75)
    
    namespace = {}
    exec(code, namespace)
    
    if "run" in namespace: namespace["run"]()
    elif "main" in namespace: namespace["main"]()
        
    print(f"{Fore.YELLOW}="*75)
    input(f"\n{Fore.CYAN}[*] Session Active. Press Enter to wipe traces...")
    
except NameError:
    print(f"{Fore.RED}[X] ERROR: Missing encryption components (BLOB/SECRET).")
except Exception as e:
    print(f"\n{Fore.RED}[X] KERNEL PANIC: {e}")
    input(f"{Fore.YELLOW}Press Enter to exit...")
