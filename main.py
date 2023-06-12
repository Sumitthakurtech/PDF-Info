import streamlit as st
from PyPDF2 import PdfFileReader
from io import BytesIO

def extract_information(file_contents):
    pdf = PdfFileReader(BytesIO(file_contents))
    information = pdf.getDocumentInfo()
    number_of_pages = pdf.getNumPages()

    txt = f"""
    Information about the uploaded PDF: 

    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {number_of_pages}
    """

    return information, txt

def main():
    st.title("PDF Information Extractor")
    st.write("Upload a PDF file to extract information.")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        information, txt = extract_information(uploaded_file.read())

        st.write(txt)
        st.write(information)  # Debug statement to display the information object

if __name__ == '__main__':
    main()
