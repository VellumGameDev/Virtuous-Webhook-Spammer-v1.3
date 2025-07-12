import requests
import json
import os
import time
import sys
import re

from        pystyle         import      Write, Colors, Colorate

RED = '\033[91m'
GREEN = '\033[92m'
GREY = '\033[90m'
PURPLE = '\033[38;2;108;0;172m'
RESET = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def set_console_title(title):
    if os.name == 'nt':
        os.system(f'title {title}')
    else:
        sys.stdout.write(f"\033]0;{title}\007")
        sys.stdout.flush()

def ErrorModule(e):
    print(f"{RED}Error: {e}{RESET}")

def Slow(text):
    for line in text.splitlines():
        print(line)
        time.sleep(0.03)

def get_avatar_url(avatarurl=None):
    valid_image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.webp', '.bmp', '.tiff')

    default_avatar_url = "https://imgur.com/yAw5nxU.png"

    if not avatarurl:
        print("\n" * 1)
        print(f"{GREEN}[!] No Avatar URL given, using default {PURPLE}Virtuous{GREEN} Avatar.{RESET}")
        return default_avatar_url

    if not re.match(r'^https?:\/\/.*\.(?:png|jpg|jpeg|gif|webp|bmp|tiff)$', avatarurl, re.IGNORECASE):
        print("\n" * 1)
        print(f"{RED}[!] Invalid Avatar URL provided. Must end in a valid image extension (.png, .jpg, etc.).{RESET}")
        return default_avatar_url
    return avatarurl

clear_screen()
set_console_title("VirtuousVellum@WebhookSpammer")

# TODO: Move away from Command Prompt and move to a real GUI

banner_art = r"""

            __      _________  __          ________ ____  _    _  ____   ____  _  __
            \ \    / /__   __| \ \        / /  ____|  _ \| |  | |/ __ \ / __ \| |/ /
             \ \  / /   | |_____\ \  /\  / /| |__  | |_) | |__| | |  | | |  | | ' / 
              \ \/ /    | |______\ \/  \/ / |  __| |  _ <|  __  | |  | | |  | |  <  
               \  /     | |       \  /\  /  | |____| |_) | |  | | |__| | |__| | . \ 
                \/      |_|        \/  \/   |______|____/|_|  |_|\____/ \____/|_|\_\

                                    Made by Virtuous.m2k & Vellum__
                                       Educational Purposes Only
                                    https://discord.gg/virtuoustools
                                         Current Version: 1.5

                                        [1] Send Normal Message
                                        [2] Send Embed Message
"""
Slow(Colorate.Horizontal(Colors.purple_to_blue, banner_art, 1))

def send_webhook_message(webhook_url, message, username, avatarurl):
    data = {
        "content": message,
        "username": username,
        "avatar_url": avatarurl,
    }

    try:
        response = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})

        if response.status_code == 204:
            print(f"{GREEN}[+] Text sent successfully!{RESET}")
        elif response.status_code == 429:
            print(f"{RED}[-] Rate Limited.")
        else:
            print(f"{RED}[-] Failed. Status Code: {response.status_code}{RESET}")

    except requests.exceptions.RequestException as e:
        print(f"{RED}An error occurred: {str(e)}{RESET}")

def main():
    choice = input(f"\n[?]{PURPLE} Choose an option (1/2) >>> {RESET}")

    if choice not in ['1', '2']:
        print(f"{RED}[-] Invalid choice. Please enter 1 or 2.{RESET}")
        return

    webhook_url = input(f"[?]{PURPLE} Enter Webhook URL >>> {RESET}")
    print("\n" * 1)
    username = input(f"[?]{PURPLE} Name (OPTIONAL) >>> {RESET}")
    print("\n" * 1)
    avatarurl = input(f"[?]{PURPLE} Avatar URL (OPTIONAL) >>> {RESET}")
    print("\n" * 1)

    if not webhook_url:
        print("\n" * 1)
        print(f"{RED}[!] Webhook URL is required!{RESET}")
        return
    print("\n" * 1)

    if not username:
        print("\n" * 1)
        print(f"{GREEN}[!] No Name given, using default {PURPLE}Virtuous{GREEN} Name.{RESET}")
        username = "Virtuous Webhook Spammer 1.5 | .gg/virtuoustools"
    print("\n" * 1)

    avatarurl = get_avatar_url(avatarurl)
    if avatarurl is None:
        pass
    else:
        print(f"{GREEN}[!] Using Avatar: {avatarurl}!{RESET}")
    print("\n" * 1)

    # TODO: Maybe make a multi webhook tool

    if choice == '1':
        message = input(f"[?]{PURPLE} Message >>> {RESET}")
        if not message:
            print(f"{RED}[!] Message is required!{RESET}")
            return
        print("\n" * 1)

        custom_prefix = "Virtuous Webhook Spammer 1.5 | .gg/virtuoustools "
        full_message = f"{message}\n\n{custom_prefix}"
        message = full_message

        try:
            iterations = int(input(f"[?]{PURPLE} Iterations >>> {RESET}"))
            if iterations <= 0:
                print(f"{RED}[!] Please enter a positive number for iterations.{RESET}")
                return
        except ValueError:
            print(f"{RED}[-] Invalid input! Please enter a valid number.{RESET}")
            return

        delay = 0.05

        for i in range(iterations):
            send_webhook_message(webhook_url, message, username, avatarurl)

            if i < iterations - 1:
                time.sleep(delay)

    elif choice == '2':
        title = input(f"[?]{PURPLE} Embed Title >>> {RESET}")
        if not title:
            print(f"{RED}[!] Title is required for embeds!{RESET}")
            return

        description = input(f"[?]{PURPLE} Embed Description >>> {RESET}")
        if not description:
            print(f"{RED}[!] Description is required for embeds!{RESET}")
            return

        default_footer = "Sent via Virtuous Webhook Spammer 1.5 | .gg/virtuoustools"
        default_color = 8323327

        # TODO: Add more input stuff for own color.

        embed_data = {
            "embeds": [
                {
                    "title": title,
                    "description": description,
                    "footer": {
                        "text": default_footer
                    },
                    "color": default_color,
                }
            ],
            "username": username,
            "avatar_url": avatarurl,
        }

        try:
            iterations = int(input(f"[?]{PURPLE} Iterations >>> {RESET}"))
            if iterations <= 0:
                print(f"{RED}[!] Please enter a positive number for iterations.{RESET}")
                return
        except ValueError:
            print(f"{RED}[-] Invalid input! Please enter a valid number.{RESET}")
            return

        delay = 0.05

        for i in range(iterations):
            response = requests.post(
                webhook_url,
                data=json.dumps(embed_data),
                headers={'Content-Type': 'application/json'}
            )

            if response.status_code == 204:
                print(f"{GREEN}[+] Embed sent successfully!{RESET}")
            elif response.status_code == 429:
                print(f"{RED}[-] Rate Limited.")
            else:
                print(f"{RED}[-] Failed. Status Code: {response.status_code}{RESET}")

            if i < iterations - 1:
                time.sleep(delay)

if __name__ == "__main__":
    main()

    input(f"\n{PURPLE}Press Enter to Exit → {RESET}")
    clear_screen()