def read_names_from_csv(input_filepath):
    """this method creates a list of names read from a csv file line by line by adding them one by one to the list"""
    names = []
    with open(input_filepath, "r", encoding="utf-8") as f:
        for line in f:
            #remove whitespacess with strip and adds a name to the list
            name = line.strip()
            if name:
                names.append(name)
    return names