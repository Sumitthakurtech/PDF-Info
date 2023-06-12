#Made by github.com/itz-harshit

import streamlit as st
from PyPDF2 import PdfReader

def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

    txt = f"""
    Information about {pdf_path}: 

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
        information, txt = extract_information(uploaded_file)

        st.write(txt)
        st.write(information) 

if __name__ == '__main__':
    main()
