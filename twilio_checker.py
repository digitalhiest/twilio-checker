import argparse
import requests
from colorama import init, Fore
from art import text2art

def display_logo():
    logo_art = text2art("Twilio", font='small')
    print(Fore.GREEN + logo_art)

def display_usage():
    usage = """
    Usage:
    python script_name.py your_account_sid your_auth_token
    """
    print(Fore.RED + usage)

def check_twilio_account(account_sid, auth_token):
    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}.json"
    response = requests.get(url, auth=(account_sid, auth_token))

    if response.status_code == 200:
        account_info = response.json()
        print("Account SID:", account_info["sid"])
        print("Account Status:", Fore.GREEN + account_info["status"])
        #print("Balance:", account_info["balance"])
        #print("Date Created:", account_info["date_created"])
        if "balance" in account_info:
            #print("Balance:", account_info["balance"])
            print("Balance:", Fore.GREEN + account_info["balance"])
        else:
            #print("Balance information not available")
            #print("Date Created:", account_info["date_created"])
            print("Date Created:", account_info["date_created"]) 
    elif response.status_code == 401:
        print(Fore.RED + "[+] Account Not Valid")
    else:
        print("Failed to fetch account information. Status code:", response.status_code)
        #print("Error message:", response.text)

if __name__ == "__main__":
    init(autoreset=True)  # Initialize colorama
    display_logo()
    #display_usage()

    parser = argparse.ArgumentParser(description="Twilio Account Checker")
    parser.add_argument("account_sid")
    parser.add_argument("auth_token")
    args = parser.parse_args()
    check_twilio_account(args.account_sid, args.auth_token)
