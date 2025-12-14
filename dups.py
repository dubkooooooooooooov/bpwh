seen = set()
duplicates = set()

with open("whitelist.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line in seen:
            duplicates.add(line)
        else:
            seen.add(line)

with open("whitelist2.txt", "w", encoding="utf-8") as f:
    for line in seen:
        f.write(line + "\n")
