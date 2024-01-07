# PDF Merger

## Description

This project provides a simple Python script to merge multiple PDF files from a specified folder into a single PDF file.

## Requirements

- Python
- PyPDF2

## Installation

Install the required package using pip:

```sh
pip install requirements.txt
```

## Usage

Run the script with the name of the output PDF file and the path to the folder containing the PDFs to merge:

```sh
python main.py "output.pdf" "path/to/folder"
```

The script will merge all PDF files in the specified folder into the single output PDF file.

## Note

- Ensure the folder path contains only PDF files.
- The output file must end with `.pdf`, and it should not already exist.
