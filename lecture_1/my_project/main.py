from colorama import init, Fore, Back, Style

init()

print(f"{Fore.RED}{Back.YELLOW}Hello World!{Style.RESET_ALL}")
print(f"{Fore.GREEN}{Back.WHITE}Hello World!{Style.RESET_ALL}")
print(f"{Fore.BLUE}{Back.WHITE}Hello World in Bright Blue!{Style.RESET_ALL}")
print(f"{Fore.MAGENTA}{Back.CYAN}Hello World with Magenta text and Cyan background!{Style.RESET_ALL}")

