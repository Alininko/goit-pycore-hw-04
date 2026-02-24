from pathlib import Path


def get_cats_info(path) -> Path:
    """Function reading the text file, converting the lines
    into a list of dictionaries by:
        - going through each line
        - splitting each line into elements split by a comma
        - creating dictionary with the elements
        - adding disctionaries to the empty list"""

    all_cats = []

    try: #going through the file if it exists

        with open(path) as file: #opening given file

            for line in file: #going trhough each line in the file

                id, name, age = line.strip().split(",") #removeing extra signs, splitting into separate elements after each comma
                cats = {"id":id, "name":name, "age":age} #creating a disctionary with all elements from the line
                all_cats.append(cats) # adding the dictionary to the list

    except FileNotFoundError: #returning error message if the file is not found
        print("File not found")

    return all_cats
    


if __name__ == "__main__": #testing function with given data
    cats_info = get_cats_info("cats_file.txt")
    print(cats_info)