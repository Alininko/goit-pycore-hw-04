from pathlib import Path
import re



def total_salary(path):
    """Function filtering the list, getting the salaries in integer, 
    number of people and calculating total and average salaries."""

    salaries = []
    total = 0 #initializing total so the function works in case of exception
    average = 0 #initializing average so the function works in case of exception

    
    try:
    
        with open(path, encoding="utf8") as file:


            for line in file: #splitting lines of strings into elements based on comma
                element_list = line.split(",")
            
                for element in element_list: #removing all unnecessary signs from the elements
                    element = element.strip()

                    if re.match(r"\d+", element): #searching elements only with numbers
                        salaries.append(int(element)) #adding elements with numbers to the list "salaries"
       
    
        total = sum(salaries) #calculating a sum
        average = total/len(salaries) # calculating an average

    
    
    except FileNotFoundError:
        print("File not found")


    return total, average
            


if __name__ == "__main__": #testing the function the given data in the text file
    total, average = total_salary("salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")