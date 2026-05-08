import os, base64, zlib, sys, hashlib, hmac
from colorama import Fore, Style, init
init(autoreset=True)
# -------- Screen clear --------
os.system("cls" if os.name == "nt" else "clear")
# -------- SAME SECRET used in encryptor.py --------
SECRET = b"secret!"
# -------- Paste your BLOB here --------
BLOB = "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"  # Replace with the output from encrypt_pegasus.py
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
