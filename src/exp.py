import compute

data={
    "seller": {
        "name": "Varasiddhi Silk Exports",
        "address": "75, 3rd Cross, Lalbagh Road, IN",
        "city":"BENGALURU",
        "state":"KARNATAKA",
        "pincode":"560027",
        "pan": "AACFV3325K",
        "gst": "29AACFV3325K1ZY"
    },
    "buyer": {
        "billing":{
                "name": "Madhu B",
                "address": "75, 3rd Cross, Lalbagh Road, IN",
                "city":"BENGALURU",
                "state":"KARNATAKA",
                "pincode":"560027",
                "state_code":"29"
        },
        "shipping":{
            
                "name": "Madhu B",
                "address": "75, 3rd Cross, Lalbagh Road, IN",
                "city":"BENGALURU",
                "state":"KARNATAKA",
                "pincode":"560027",
                "state_code":"29"
        }
    },
    "order_detail": {
        "order_number": "403-3225714-7676307",
        "order_date": "28.10.2019"
    },
    "invoice_details":{
        "invoice_number": "IN-761",
        "invoice_date": "28.10.2019",
        "invoice_detail":"Xgsjkshi3koie93i"
    },
    "place_of_supply":"KARNATAKA",
    "place_of_delivery":"KARNATAKA",
    "items": [
        {
            "description": "Varasiddhi Silks Men's Formal Shirt (SH-05-42, Navy Blue, 42)",
            "unit_price": 338.10,
            "quantity": 1,
            "discount":5,
            "net_amount": 338.10,
            "tax_rate":2.5
        },
        {
            "description": "Shipping Charges",
            "unit_price": 30.96,
            "quantity": 1,
            "discount":2,
            "net_amount": 30.96,
            "tax_rate": 2.5
        }
    ],
    "reverse_charge": "No"
}

data=compute.compute_item_parameters(data)
print(data)
data['items']
