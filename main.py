import requests
import json
import os
import time

class Colors:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    PURPLE = '\033[35m'
    RESET = '\033[0m'

print("https://discord.gg/Zn2VBmb3ak")

print("\n" * 4)

os.system('title Virtuous Webhook Spammer')


def send_webhook_message(webhook_url, message):
    data = {
        "content": message,
    }

    try:
        response = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})

        if response.status_code == 204:
            print(f"{Colors.GREEN}[+] Message sent successfully!{Colors.RESET}")
        else:
            print(f"{Colors.RED}[-] Rate Limited. Status Code: {response.status_code}{Colors.RESET}")

    except requests.exceptions.RequestException as e:
        print(f"{Colors.RED}An error occurred: {str(e)}{Colors.RESET}")


def main():
    webhook_url = input(f"[?]{Colors.PURPLE} Enter Webhook URL >>> {Colors.RESET}")
    print("\n" * 1)
    message = input(f"[?]{Colors.PURPLE} Message >>> {Colors.RESET}")

    if not webhook_url or not message:
        print("\n" * 1)
        print(f"{Colors.RED}[!] Both Webhook URL and Message are required!{Colors.RESET}")
        return
    print("\n" * 1)
    try:
        iterations = int(input(f"[?]{Colors.PURPLE} Iterations >>> {Colors.RESET}"))
        if iterations <= 0:
            print(f"{Colors.RED}[!] Please enter a positive number for iterations.{Colors.RESET}")
            return
    except ValueError:
        print(f"{Colors.RED}[-] Invalid input! Please enter a valid number.{Colors.RESET}")
        return


    delay = 0.05  

    for i in range(iterations):
        send_webhook_message(webhook_url, message)
        if i < iterations - 1: 
            time.sleep(delay)


if __name__ == "__main__":
    main()

    input(f"\n{Colors.PURPLE}Press Enter to Exit → {Colors.RESET}")