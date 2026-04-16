import os
import requests
import time
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

class SpyE_IG:
    def __init__(self):
        self.api_url = "https://i.instagram.com/api/v1/users/lookup/"
        self.headers = {
            'accept-language': 'en-US;q=1.0',
            'content-type': 'application/x-www-form-exists-urlencoded; charset=UTF-8',
            'user-agent': 'Instagram 337.0.3.23.54 (iPhone12,1; iOS 16_6; en_US; en; scale=2.00; 828x1792; 577210397) AppleWebKit/420+',
        }
        self.version = "1.0.0"

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def banner(self):
        self.clear_screen()
        banner_text = f"""
{Fore.RED}  ██████  ██████  ██    ██      ███████ 
{Fore.RED} ██       ██   ██  ██  ██       ██      
{Fore.WHITE}  █████   ██████    ████        █████   
{Fore.WHITE}      ██  ██         ██         ██      
{Fore.RED} ██████   ██         ██         ███████ 
                                        
{Fore.WHITE}        [ Instagram Recon Tool ]
{Fore.RED}          Branding: SPY E
{Fore.WHITE}      Developer: Rolandino (123Tool)
        """
        print(banner_text)
        print(f"{Fore.YELLOW}{Style.BRIGHT} v{self.version} | Modded for OSINT Research Purposes")
        print("-" * 50)

    def fetch_data(self, username):
        payload = {"q": username}
        try:
            print(f"{Fore.CYAN}[*] Searching target: @{username}...")
            response = requests.post(self.api_url, headers=self.headers, data=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"{Fore.RED}[!] Network Error: {e}")
            return None

    def display_results(self, data):
        if not data or data.get('status') != 'ok':
            print(f"{Fore.RED}[!] Target not found or API rate limited.")
            return

        user = data.get('user', {})
        
        print(f"\n{Fore.GREEN}[ RESULT FOR @{user.get('username')} ]")
        print(f"{Fore.WHITE}Full Name      : {Fore.YELLOW}{user.get('full_name')}")
        print(f"{Fore.WHITE}User ID        : {Fore.YELLOW}{user.get('pk')}")
        print(f"{Fore.WHITE}Is Verified    : {Fore.YELLOW}{user.get('is_verified')}")
        
        print(f"\n{Fore.CYAN}[ SECURITY DATA ]")
        print(f"{Fore.WHITE}Obfuscated Email : {Fore.YELLOW}{data.get('email', 'Not Linked')}")
        print(f"{Fore.WHITE}Obfuscated Phone : {Fore.YELLOW}{data.get('obfuscated_phone', 'Not Linked')}")
        print(f"{Fore.WHITE}WhatsApp Reset   : {Fore.YELLOW}{data.get('can_wa_reset')}")
        print(f"{Fore.WHITE}SMS Reset        : {Fore.YELLOW}{data.get('can_sms_reset')}")
        print(f"{Fore.WHITE}FB Login Linked  : {Fore.YELLOW}{data.get('fb_login_option')}")
        
        print(f"\n{Fore.CYAN}[ LOG INFO ]")
        print(f"{Fore.WHITE}Lookup Source    : {Fore.YELLOW}{data.get('lookup_source')}")
        print(f"{Fore.WHITE}Status           : {Fore.GREEN}{data.get('status')}")
        print("-" * 50)

    def run(self):
        self.banner()
        target = input(f"{Fore.WHITE}Enter Target Username: {Fore.RED}")
        if not target:
            print(f"{Fore.RED}[!] Username cannot be empty.")
            return
        
        result = self.fetch_data(target)
        if result:
            self.display_results(result)
        
        print(f"\n{Fore.WHITE}Press Enter to exit...")
        input()

if __name__ == "__main__":
    app = SpyE_IG()
    app.run()
