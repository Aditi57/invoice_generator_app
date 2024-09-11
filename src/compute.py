from num2words import num2words

def compute_item_parameters(data):
    total=0;
    total_tax_value=0
    for item in data["item_values"]:
        item_values= calculate_item_values(item, data["place_of_supply"],data["place_of_delivery"])

        item["net_amount"] = item_values["net_amount"]
        item["tax_type"] = item_values["tax_type"]
        item["cgst"] = item_values["cgst"]
        item["sgst"] = item_values["sgst"]
        item["igst"] = item_values["igst"]
        item["total_tax"] = item_values["total_tax"]
        item["total_amount"] = item_values["total_amount"]

        total=total+item_values["total_amount"]
        total_tax_value=total_tax_value+item_values["total_tax"]
    data["total_invoice_amount"] = round(total, 2)
    data["total_tax_value"]=round(total_tax_value,2)
    total=round(total,2)
    data["total_in_words"]=num2words(total).upper()
    return data

def calculate_item_values(item, place_of_supply, place_of_delivery):
    # Calculate Net Amount
    net_amount = item['unit_price'] * item['quantity'] - item['discount']
    # Initialize tax variables
    tax_type = ""
    cgst = 0
    sgst = 0
    igst = 0
    # Determine Tax Type (CGST + SGST or IGST)
    if place_of_supply == place_of_delivery:
        # Apply CGST and SGST (9% each)
        tax_type = "CGST + SGST"
        cgst = net_amount * 0.09  # 9% CGST
        sgst = net_amount * 0.09  # 9% SGST
    else:
        # Apply IGST (18%)
        tax_type = "IGST"
        igst = net_amount * 0.18  # 18% IGST
    
    # Calculate total tax
    total_tax = cgst + sgst + igst
    
    # Calculate total amount
    total_amount = net_amount + total_tax
    
    # Return the calculated values in a dictionary
    return {
        "net_amount": round(net_amount, 2),
        "tax_type": tax_type,
        "cgst": round(cgst, 2),
        "sgst": round(sgst, 2),
        "igst": round(igst, 2),
        "total_tax": round(total_tax, 2),
        "total_amount": round(total_amount, 2)
    }

