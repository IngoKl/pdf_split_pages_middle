# pdf_split_pages_middle

*This is a very simple Python tool that splits the pages of PDF documents in the middle in order to create single-page PDFs from scans.*

![Visualization](https://user-images.githubusercontent.com/16179317/63167497-cd314700-c031-11e9-9347-c09484794ebe.png)

Often, documents and books are being scanned two pages at a time. This tool allows you to easily split these dual-page scans into individual pages. In order for this to work properly, every page of the documents needs to be, more or less, scanned with the same orientation and positioning.

## Installation

- via Python (3.x): clone this repository, install the dependencies in `requirements.txt`, and run `cli.py` (see Usage)
- Windows: you can find a (semi-)current stand-alone binary under "Releases."

## Usage

`python cli.py input.pdf --pdf_output_path output.pdf --skip_pages 0,1 --shift_middle_percentage 0`
`pdf_split_middle.exe input.pdf --pdf_output_path output.pdf --skip_pages 0,1 --shift_middle_percentage 0`
  
Technically, you only have to provide the path for the input file. The tool will then split every page into two halves.
You can skip pages (comma-separated list) and shift the 'line' at which to cut. Positive values (0.1 to 49) will shift the line to the right (percentages of the width of the document), and negative values (-0.1 to -49) will shift the line to the left.

### Directory splitting

`python cli.py my_pdf_folder --recursive --recursive_suffix my_suffix --skip_pages 0,1 --shift_middle_percentage 0`

To walk through a given directory and split every PDF within it and its subfolders, use the `--recursive` parameter. Since providing a specific output path is not possible here, you can define a custom suffix with `--recursive_suffix`. The output directory of the PDF will be the same as the input PDF.

## Creating a Binary

The Windows binary was created using `pyinstaller` on Windows 10. If you want to create your own binary:

- New environment conda create --name splitpdfmiddle python=3.7
- activate splitpdfmiddle
- pip install pyinstaller
- pip install -r requirements.txt
- pyinstaller --onefile cli.py
