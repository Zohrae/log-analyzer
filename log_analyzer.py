from colorama import Fore, Style, init

def analyze_logs(input_file='log.txt', output_file='rapport.txt'):
    init(autoreset=True)  # Pour réinitialiser les couleurs automatiquement
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}

    with open(input_file, 'r') as file:
        for line in file:
            for level in counts:
                if level in line:
                    counts[level] += 1

    with open(output_file, 'w') as file:
        for level, count in counts.items():
            file.write(f"{level}: {count}\n")

    # Affichage coloré dans le terminal
    print(Fore.GREEN + f"INFO: {counts['INFO']}" + Style.RESET_ALL)
    print(Fore.YELLOW + f"WARNING: {counts['WARNING']}" + Style.RESET_ALL)
    print(Fore.RED + f"ERROR: {counts['ERROR']}" + Style.RESET_ALL)

    print(Fore.CYAN + "✅ Rapport généré dans rapport.txt" + Style.RESET_ALL)

if __name__ == "__main__":
    analyze_logs()
