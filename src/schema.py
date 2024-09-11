schema={
    "seller": {
        "name": str,
        "address": str,
        "city": str,
        "state": str,
        "pincode": str,
        "pan": str,
        "gst": str
    },
    "buyer": {
        "billing": {
            "name": str,
            "address": str,
            "city": str,
            "state": str,
            "pincode": str,
            "state_code": str
        },
        "shipping": {
            "name": str,
            "address": str,
            "city": str,
            "state": str,
            "pincode": str,
            "state_code": str
        }
    },
    "order_detail": {
        "order_number": str,
        "order_date": str
    },
    "invoice_details": {
        "invoice_number": str,
        "invoice_date": str,
        "invoice_detail": str
    },
    "place_of_supply": str,
    "place_of_delivery": str,
    "item_values": [{
        "description": str,
        "unit_price": float,
        "quantity": int,
        "discount": int,
        "net_amount": float,
        "tax_rate": float
    }],
    "reverse_charge": str
}