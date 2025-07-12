import requests
import json
import os
import time
import sys
import re
import random

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

def get_rotating_usernames():
    try:
        with open("names.txt", "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"{RED}[!] names.txt not found in current directory.{RESET}")
        return []
    except Exception as e:
        print(f"{RED}[!] Error reading names.txt: {e}{RESET}")
        return []
    
def get_rotating_messages():
    try:
        with open("messages.txt", "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"{RED}[!] messages.txt not found in current directory.{RESET}")
        return []
    except Exception as e:
        print(f"{RED}[!] Error reading messages.txt: {e}{RESET}")
        return []
    
def update_progress(current, total):
    print(f"\rSent {current} / {total}\n", end="", flush=True)

clear_screen()
set_console_title("VirtuousVellum@WebhookSpammer")

# TODO: Move away from Command Prompt and move to a real GUI | LOW PRIOR

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
                                         Current Version: 1.6

                                        [1] Send Normal Message
                                        [2] Send Embed Message
"""
Slow(Colorate.Horizontal(Colors.purple_to_red, banner_art, 1))

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
    print(f"[?]{PURPLE} Choose your option for the Name >>> {RESET}")
    print("\n" * 1)
    print(f"{PURPLE}[1] Custom Name{RESET}")
    print(f"{PURPLE}[2] Random Name{RESET}")
    print(f"{PURPLE}[3] Default Name{RESET}")
    print("\n" * 1)
    name_choice = input(f"[?]{PURPLE} Choose an option (1/3) >>> {RESET}")

    if name_choice not in ['1', '2', '3']:
        print(f"{RED}[-] Invalid choice. Please enter 1, 2, or 3.{RESET}")
        return

    if name_choice == '1':
        username = input(f"[?]{PURPLE} Name >>> {RESET}")
        if not username:
            print(f"{GREEN}[!] No Name given, using default {PURPLE}Virtuous{GREEN} Name.{RESET}")
            username = "Virtuous Webhook Spammer 1.6 | .gg/virtuoustools"
        usernames = username
    elif name_choice == '2':
        usernames = get_rotating_usernames()
        if not usernames:
            print(f"{GREEN}[!] No usernames found in names.txt, using default {PURPLE}Virtuous{GREEN} Name.{RESET}")
            usernames = "Virtuous Webhook Spammer 1.6 | .gg/virtuoustools"
        else:
            print(f"{GREEN}[!] Using rotating usernames from names.txt{RESET}")
    else:
        print(f"{GREEN}[!] Using default {PURPLE}Virtuous{GREEN} Name.{RESET}")
        usernames = "Virtuous Webhook Spammer 1.6 | .gg/virtuoustools"

    print("\n" * 1)
    avatarurl = input(f"[?]{PURPLE} Avatar URL (OPTIONAL) >>> {RESET}")
    print("\n" * 1)

    if not webhook_url:
        print("\n" * 1)
        print(f"{RED}[!] Webhook URL is required!{RESET}")
        return
    print("\n" * 1)

    avatarurl = get_avatar_url(avatarurl)
    if avatarurl is None:
        pass
    else:
        print(f"{GREEN}[!] Using Avatar: {avatarurl}!{RESET}")
    print("\n" * 1)

    # TODO: Maybe make a multi webhook tool

    if choice == '1':
        print(f"[?]{PURPLE} Choose your option for the Message >>> {RESET}")
        print("\n" * 1)
        print(f"{PURPLE}[1] Custom Message{RESET}")
        print(f"{PURPLE}[2] Random Message{RESET}")
        print("\n" * 1)
        message_choice = input(f"[?]{PURPLE} Choose an option (1/2) >>> {RESET}")

        if message_choice not in ['1', '2']:
            print(f"{RED}[-] Invalid choice. Please enter 1, or 2.{RESET}")
            return
        
        if message_choice == '1':
            message = input(f"[?]{PURPLE} Message >>> {RESET}")
            if not message:
                print(f"{GREEN}[!] No Message given, using default {PURPLE}Virtuous{GREEN} message.{RESET}")
                message = "# Virtuous Webhook Spammer 1.6 | Get more at .gg/virtuoustools"
                messages = message
        elif message_choice == '2':
            messages = get_rotating_messages()
            if not messages:
                print(f"{GREEN}[!] No messages found in messages.txt, using default {PURPLE}Virtuous{GREEN} message.{RESET}")
                messages = "# Virtuous Webhook Spammer 1.6 | .gg/virtuoustools"
            else:
                print(f"{GREEN}[!] Using rotating messages from messages.txt{RESET}")
        else:
            print(f"{GREEN}[!] Using default {PURPLE}Virtuous{GREEN} message.{RESET}")
            messages = "# Virtuous Webhook Spammer 1.6 | .gg/virtuoustools"

        try:
            iterations = int(input(f"[?]{PURPLE} Iterations >>> {RESET}"))
            if iterations <= 0:
                print(f"{RED}[!] Please enter a positive number for iterations.{RESET}")
                return
        except ValueError:
            print(f"{RED}[-] Invalid input! Please enter a valid number.{RESET}")
            return

        min_delay = 0.05
        max_delay = 0.5

        for i in range(iterations):
            username = random.choice(usernames)
            message = random.choice(messages)
            custom_prefix = "Virtuous Webhook Spammer 1.6 | .gg/virtuoustools "
            full_message = f"{message}\n\n{custom_prefix}\n\n## Made with :heart:"
            send_webhook_message(webhook_url, full_message, username, avatarurl)
            update_progress(i + 1, iterations)

            if i < iterations - 1:
                delay = random.uniform(min_delay, max_delay)
                time.sleep(delay)

        print()

    elif choice == '2':
        title = input(f"[?]{PURPLE} Embed Title >>> {RESET}")
        if not title:
            print(f"{RED}[!] Title is required for embeds!{RESET}")
            return

        description = input(f"[?]{PURPLE} Embed Description (OPTIONAL) >>> {RESET}")
        if not description:
            print(f"{GREEN}[!] No Message given, using default {PURPLE}Virtuous{GREEN} description.{RESET}")
            description = "Virtuous Webhook Spammer 1.6 | Get more at .gg/virtuoustools"

        default_footer = "Sent via Virtuous Webhook Spammer 1.6 | .gg/virtuoustools"
        default_color_hex = "7F00FF"
        default_color = int(default_color_hex, 16)

        color_input = input(f"[?]{PURPLE} Embed Color (6-digit Hex, e.g. 7289DA) (Optional) >>> {RESET}")

        if not color_input:
            print(f"{GREEN}[!] No Color given, using default {PURPLE}Virtuous{GREEN} color.")
            color = default_color
        else:
            stripped_color = color_input.strip('#')  # Remove '#' if present
            if len(stripped_color) == 6 and all(c in '0123456789abcdefABCDEF' for c in stripped_color):
                try:
                    color = int(stripped_color, 16)
                except ValueError:
                    print(f"{RED}[!] Invalid hex color format. Using default {PURPLE}Virtuous{RED} color.")
                    color = default_color
            else:
                print(f"{RED}[!] Invalid hex color format. Using default {PURPLE}Virtuous{RED} color.")
                color = default_color

        username = random.choice(usernames)

        # TODO: Add more input stuff for own color.

        embed_data = {
            "embeds": [
                {
                    "title": title,
                    "description": description,
                    "footer": {
                        "text": default_footer
                    },
                    "color": color,
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

        min_delay = 0.05
        max_delay = 0.5

        for i in range(iterations):
            response = requests.post(
                webhook_url,
                data=json.dumps(embed_data),
                headers={'Content-Type': 'application/json'}
            )
            update_progress(i + 1, iterations)

            if response.status_code == 204:
                print(f"{GREEN}[+] Embed sent successfully!{RESET}")
            elif response.status_code == 429:
                print(f"{RED}[-] Rate Limited.")
            else:
                print(f"{RED}[-] Failed. Status Code: {response.status_code}{RESET}")

            if i < iterations - 1:
                delay = random.uniform(min_delay, max_delay)
                time.sleep(delay)

        print()

if __name__ == "__main__":
    main()

    input(f"\n{PURPLE}Press Enter to Exit → {RESET}")
    clear_screen()