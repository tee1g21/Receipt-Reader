import requests
import json
from pprint import pprint
import sys
import os


def read_receipt(filename): 
    
    image = f"{filename}.jpg"
    
    receipt_ocr_endpoint = 'https://ocr.asprise.com/api/v1/receipt' 

    r = requests.post(receipt_ocr_endpoint, data = {
    'api_key': 'TEST',        # Use 'TEST' for testing purpose 
    'recognizer': 'GB',       # language 
    'ref_no': 'Lorem Ipsum', # optional ref code 
    }, files = {"file": open(image, "rb")})

    with open(f"{filename}.json", "w") as f:
        json.dump(r.json(), f) 
        

def output_to_csv(d, filename):
    
    
    items = d["receipts"][0]["items"]

    with open(f"{filename}.csv", "w") as f: 
        
        out = "description, qty, amount\n"        
        f.write(out)
        print(out, end="\r")
        
        for i in items: 
            out = f"{i["description"]},{i["qty"]},{i["amount"]}\n"
            f.write(out)
            print(out, end="\r")
        
if __name__ == "__main__":
    
    filename = os.path.splitext(sys.argv[1])[0]
    
    if (sys.argv[2] == "T"):
        print("Reading receipt")
        read_receipt(filename)
    
    with open(f"{filename}.json") as f: 
        d = json.load(f)
        output_to_csv(d, filename)
