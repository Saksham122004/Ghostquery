import webbrowser
import urllib.parse
import sys
import time
import os



GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

os.system("")


def type_writer(text, delay=0.02):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def loading_animation(text="Initializing"):
    for i in range(3):
        print(GREEN + f"{text}{'.' * (i+1)}", end="\r")
        time.sleep(0.4)
    print(" " * 50, end="\r")


# NEW ANIMATED BANNER
def animated_banner():

    banner_text = r"""

 ████████╗███████╗ ██████╗██╗  ██╗███╗   ██╗██╗ ██████╗ █████╗ ██╗     
 ╚══██╔══╝██╔════╝██╔════╝██║  ██║████╗  ██║██║██╔════╝██╔══██╗██║     
    ██║   █████╗  ██║     ███████║██╔██╗ ██║██║██║     ███████║██║     
    ██║   ██╔══╝  ██║     ██╔══██║██║╚██╗██║██║██║     ██╔══██║██║     
    ██║   ███████╗╚██████╗██║  ██║██║ ╚████║██║╚██████╗██║  ██║███████╗
    ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝

            ███████╗ █████╗ ███╗   ███╗
            ██╔════╝██╔══██╗████╗ ████║
            ███████╗███████║██╔████╔██║
            ╚════██║██╔══██║██║╚██╔╝██║
            ███████║██║  ██║██║ ╚═╝ ██║
            ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝

                >>> GHOSTQUERY <<<
    """

    for line in banner_text.split("\n"):
        print(GREEN + line)
        time.sleep(0.03)

    print(GREEN + "=" * 65)
    print(GREEN + "     GHOSTQUERY - OSINT SEARCH CONSTRUCTOR TERMINAL")
    print(GREEN + "=" * 65 + RESET)


def banner():
    os.system("cls" if os.name == "nt" else "clear")
    animated_banner()


def boot_sequence():
    banner()
    type_writer(GREEN + "[+] Booting GhostQuery Engine")
    loading_animation("Loading Search Modules")
    loading_animation("Establishing OSINT Interface")
    loading_animation("Preparing Query Constructor")
    type_writer(GREEN + "[+] System Ready\n")
    time.sleep(0.5)



def build_query():
    print(CYAN + "-" * 60)
    print(CYAN + "BUILD SEARCH QUERY")
    print(CYAN + "-" * 60 + RESET)

    keyword = input(GREEN + "Keyword (optional): " + RESET).strip()
    exact = input(GREEN + "Exact phrase (optional): " + RESET).strip()
    site = input(GREEN + "Site (example.com) [optional]: " + RESET).strip()
    filetype = input(GREEN + "Filetype (pdf, txt, docx) [optional]: " + RESET).strip()
    inurl = input(GREEN + "InURL keyword [optional]: " + RESET).strip()
    intitle = input(GREEN + "InTitle keyword [optional]: " + RESET).strip()
    exclude = input(GREEN + "Exclude keyword (without '-') [optional]: " + RESET).strip()

    query_parts = []

    if keyword:
        query_parts.append(keyword)
    if exact:
        query_parts.append(f'"{exact}"')
    if site:
        query_parts.append(f"site:{site}")
    if filetype:
        query_parts.append(f"filetype:{filetype}")
    if inurl:
        query_parts.append(f"inurl:{inurl}")
    if intitle:
        query_parts.append(f"intitle:{intitle}")
    if exclude:
        query_parts.append(f"-{exclude}")

    if not query_parts:
        print(RED + "\nError: At least one field must be provided." + RESET)
        time.sleep(1)
        return

    final_query = " ".join(query_parts)

    print(YELLOW + "\n[+] Generated Query:")
    print(YELLOW + "-" * 60)
    print(final_query)
    print(YELLOW + "-" * 60 + RESET)

    open_choice = input(GREEN + "Open in browser? (y/n): " + RESET).strip().lower()

    if open_choice == "y":
        encoded_query = urllib.parse.quote(final_query)
        url = f"https://www.google.com/search?q={encoded_query}"
        webbrowser.open(url)


def main():
    boot_sequence()

    while True:
        print(GREEN + "\n[1] Build Search Query")
        print("[2] Clear Screen")
        print("[3] Exit" + RESET)

        option = input(GREEN + "\nSelect option: " + RESET).strip()

        if option == "1":
            build_query()

        elif option == "2":
            banner()

        elif option == "3":
            print(GREEN + "\nShutting down GhostQuery...\n" + RESET)
            time.sleep(1)
            sys.exit()

        else:
            print(RED + "Invalid selection." + RESET)


if __name__ == "__main__":
    main()
