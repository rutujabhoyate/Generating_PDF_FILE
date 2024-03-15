   
############################ GENERATE PDF FROM HTML TO PDF THROUGH PYTHON #########################################

from flask import Flask, render_template, send_file
from weasyprint import HTML
import os

app = Flask(__name__)

# Set the download path on the server
#Define the path where the generated PDF will be saved (download_path). Also, specify the path to the WeasyPrint binary (weasyprint_binary_path).
download_path = 'D:/NOV/Python_PDF'
os.makedirs(download_path, exist_ok=True)

weasyprint_binary_path = 'C:/Program Files/GTK3-Runtime Win64/bin/weasyprint.exe'

@app.route('/')
def index():
    # Render HTML template with Flask's render_template function
    rendered_template = render_template('index.html')

    # Generate PDF from rendered HTML using WeasyPrint
    pdf_path = os.path.join(download_path, 'output.pdf')
    #HTML(string=rendered_template).write_pdf(pdf_path)
    
    '''Combine the rendered HTML with WeasyPrint to generate a PDF. The HTML class from WeasyPrint is used to create an HTML object
    from the rendered template, and then the write_pdf method is called to write the PDF to the specified path (pdf_path)'''
    HTML(string=rendered_template).write_pdf(pdf_path, weasyprint=weasyprint_binary_path)


    # Send the saved PDF as a response
    return send_file(pdf_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
    
    

 
