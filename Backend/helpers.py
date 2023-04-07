def retrieveHelperVal(key, filename):
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            if len(parts) == 2 and parts[0].strip() == key:
                return parts[1].strip()