def analyze_logs(input_file='log.txt', output_file='rapport.txt'):
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    
    with open(input_file, 'r') as file:
        for line in file:
            for level in counts:
                if level in line:
                    counts[level] += 1

    with open(output_file, 'w') as file:
        for level, count in counts.items():
            file.write(f"{level}: {count}\n")

    print("Rapport généré dans rapport.txt")

if __name__ == "__main__":
    analyze_logs()