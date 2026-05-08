import os
import time
from colorama import Fore, Style, init

# কালার ইনিশিয়ালাইজেশন
init(autoreset=True)

def create_ultra_license():
    # একদম পরিষ্কার এবং বোল্ড ARIF ASCII Art (Block Style)
    # এটি টার্মিনালে বা টেক্সট ফাইলে খুব সুন্দরভাবে ফুটে উঠবে
    arif_neon = f"""
{Fore.GREEN}      █████╗ ██████╗ ██╗███████╗
{Fore.GREEN}     ██╔══██╗██╔══██╗██║██╔════╝
{Fore.CYAN}     ███████║██████╔╝██║█████╗  
{Fore.CYAN}     ██╔══██║██╔══██╗██║██╔══╝  
{Fore.WHITE}     ██║  ██║██║  ██║██║██║     
{Fore.WHITE}     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝     
    """

    arif_plain = """
      █████╗ ██████╗ ██╗███████╗
     ██╔══██╗██╔══██╗██║██╔════╝
     ███████║██████╔╝██║█████╗  
     ██╔══██║██╔══██╗██║██╔══╝  
     ██║  ██║██║  ██║██║██║     
     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝     
    """

    license_content = f"""
============================================================
     {Fore.RED}SYSTEM  PAGASUS AUTHORIZATION LICENSE{Fore.RESET}
============================================================
{arif_neon}
{Fore.YELLOW}------------------------------------------------------------
{Fore.WHITE}  HACKER LICENSE ID  : {Fore.GREEN}ARIF
{Fore.WHITE}  STATUS             : {Fore.RED}CERTIFIED WHITE-HAT
{Fore.WHITE}  ACCESS             : {Fore.CYAN}ROOT_LEVEL_ENABLED
{Fore.YELLOW}------------------------------------------------------------

{Fore.WHITE}[!] THIS PRIVILEGED DATA IS ENCRYPTED.
[!] UNAUTHORIZED MODIFICATION WILL TRIGGER KERNEL PANIC.
[!] PROPERTY OF ARIF SECURITY LABS.

{Fore.YELLOW}------------------------------------------------------------
{Fore.RED}        (c) 2026 CYBER-LAB | SECURED BY ARIF
============================================================
    """

    try:
        # ১. টার্মিনালে সুন্দর কালারফুল প্রিভিউ দেখানো
        os.system('cls' if os.name == 'nt' else 'clear')
        print(license_content)
        
        # ২. 'LICENSE' ফাইল তৈরি করা (ভিতরে plain art থাকবে যাতে ফাইল নষ্ট না হয়)
        with open("LICENSE", "w", encoding="utf-8") as f:
            # ফাইলের ভেতরে কালার কোড ছাড়াই আর্টটি সেভ হবে যাতে টেক্সট ফাইলে সুন্দর দেখায়
            f.write(license_content.replace(Fore.GREEN, "").replace(Fore.CYAN, "").replace(Fore.WHITE, "").replace(Fore.YELLOW, "").replace(Fore.RED, "").replace(Fore.RESET, ""))
            
        print(f"{Fore.GREEN}✅ 'LICENSE' file generated successfully in your folder!")
        
    except Exception as e:
        print(f"{Fore.RED}❌ Error: {e}")

if __name__ == "__main__":
    create_ultra_license()
