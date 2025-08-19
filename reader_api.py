import requests
import json


def read_receipt(image): 
    receipt_ocr_endpoint = 'https://ocr.asprise.com/api/v1/receipt' 

    r = requests.post(receipt_ocr_endpoint, data = {
    'api_key': 'TEST',        # Use 'TEST' for testing purpose 
    'recognizer': 'GB',       # language 
    'ref_no': 'Lorem Ipsum', # optional ref code 
    }, files = {"file": open(image, "rb")})

    print(r.text) # result in JSON
    return r.json()


if __name__ == "__main__":
    image = "example2.jpg"
    
    receipt_dict = dict(read_receipt(image))
