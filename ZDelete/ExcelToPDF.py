import pandas as pd
import json
from fpdf import FPDF

def excel_to_pdf(excel_file, output_folder):
    """
    Extract each record from an Excel file and create individual PDF files with data in JSON format.

    Args:
        excel_file (str): Path to the Excel file.
        output_folder (str): Folder where the PDF files will be saved.
    """
    # Read the Excel file
    df = pd.read_excel(excel_file)

    # Iterate through each record in the DataFrame
    for index, row in df.iterrows():
        # Convert the row to a dictionary (JSON format)
        record_json = row.to_dict()

        # Create a PDF file
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Add JSON data to the PDF
        pdf.cell(200, 10, txt="Record in JSON Format", ln=True, align='C')
        pdf.ln(10)  # Add a line break
        json_data = json.dumps(record_json, indent=4)
        for line in json_data.splitlines():
            # Ensure each line fits within the PDF width
            pdf.multi_cell(0, 10, txt=line)

        # Save the PDF file
        pdf_file_name = f"{output_folder}/record_{index + 1}.pdf"
        pdf.output(pdf_file_name)
        print(f"PDF created: {pdf_file_name}")

# Example usage
if __name__ == "__main__":
    excel_file_path = "/Users/daisymanikabaleeswaran/Library/CloudStorage/OneDrive-MavericSystemsLimited/Impact/LendingUseCase/Sample Data Set.xlsx"  # Replace with the path to your Excel file
    output_folder_path = "/Users/daisymanikabaleeswaran/Library/CloudStorage/OneDrive-MavericSystemsLimited/Impact/LendingUseCase/pdf"  # Replace with the path to your output folder
    excel_to_pdf(excel_file_path, output_folder_path)
