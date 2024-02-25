import streamlit as st 
from nbconvert import PDFExporter
from nbformat import read,NO_CONVERT

def convert_to_pdf(ipynb_file): 
    pdf_exporter = PDFExporter() 
    pdf_data, resources = pdf_exporter.from_notebook_node(ipynb_file) 
    return pdf_data 
def main():
    st.title('Jupyter Notebook to PDF Converter: ') 
    #upload button 
    ipynb_file = st.file_uploader('Upload the .ipynb file: ')#,type=['ipynb']) 
    print(ipynb_file)
    if ipynb_file: 
        ipynb_file_content = read(ipynb_file,NO_CONVERT) 
        pdf_data = convert_to_pdf(ipynb_file_content) 
        st.download_button(label='Download PDF',
                           data=pdf_data,
                           key="pdf_download",
                           file_name="output.pdf",
                           mime='application/pdf')
if __name__ == "__main__": 
    main() 