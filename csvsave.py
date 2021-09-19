import csv
import os.path

def csv_save(title, price, area, floor):
    if os.path.isfile("ss.csv"):
        with open('ss.csv', 'a', encoding = "utf-8",  newline = '') as csv_ss:           
            fieldnames = ["Title", "Price", "Area", "Floor"]
            content = {"Title" : title,
                            "Price" : price,
                            "Area" : area,
                            "Floor" : floor}
                            
            writer = csv.DictWriter(csv_ss, fieldnames = fieldnames)
            writer.writerow(content)

    else:
        with open('ss.csv', 'w', encoding = "utf-8",  newline = '') as csv_ss:
            
            fieldnames = ["Title", "Price", "Area", "Floor"]
            content = {"Title" : title,
                            "Price" : price,
                            "Area" : area,
                            "Floor" : floor}                          
            writer = csv.DictWriter(csv_ss, fieldnames = fieldnames)
            writer.writeheader()
            writer.writerow(content)