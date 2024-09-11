from flask import Flask, render_template, request, send_file ,jsonify
from weasyprint import HTML
from io import BytesIO
import compute
from schema import schema
from dataValidation import validate_json_structure
import os
import json


app = Flask(__name__)

@app.route('/generate_invoice', methods=['POST'])
def generate_invoice():

    if 'signature' not in request.files:
        return jsonify({"error": "Signature file is missing"}), 400
    
    signature_file = request.files['signature']
    # Saveing  the image file to server
    signature_path = os.path.join("static", "signature.png")
    signature_file.save(signature_path)
    # Retrieve the JSON data sent as string json_data field
    json_data_str = request.form.get('json_data')
    if not json_data_str:
        return jsonify({"error": "JSON data is missing"}), 400
    try:
        invoice = json.loads(json_data_str)
        is_valid, message=validate_json_structure(invoice,schema)
        #insert the derived value 
        if is_valid:
            invoice=compute.compute_item_parameters(invoice)
            invoice['signature_path'] = signature_path
            # Rendering  the invoice HTML template with the data
            html_content = render_template('invoice.html', invoice=invoice)
            
            # Convert the HTML to PDF
            pdf_file = BytesIO()
            HTML(string=html_content,base_url=request.base_url).write_pdf(pdf_file)
            pdf_file.seek(0)
            # Send the PDF as a response
            return send_file(pdf_file, as_attachment=True, download_name='invoice.pdf', mimetype='application/pdf')
        else:
            error={
                "type":"schema error",
                "message":message
            }
            return jsonify(error=error),422
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON data"}), 400


if __name__ == '__main__':
    app.run(debug=True)