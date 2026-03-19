import argparse
import pandas as pd

def clean_csv(input_file, output_file):
    """
    Clean the CSV file and save to output_file.
    """
    try:
        # Read the CSV file
        df = pd.read_csv(input_file)

        # Remove duplicate rows
        df = df.drop_duplicates()

        # Fill missing values with empty strings
        df = df.fillna('')

        # Strip whitespace from string columns
        for col in df.select_dtypes(include=['object']):
            df[col] = df[col].astype(str).str.strip()

        # Save the cleaned data
        df.to_csv(output_file, index=False)
        print(f"Cleaned data saved to {output_file}")

    except Exception as e:
        print(f"Error cleaning CSV: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean a CSV file")
    parser.add_argument("input_file", help="Path to the input CSV file")
    parser.add_argument("output_file", help="Path to the output CSV file")

    args = parser.parse_args()
    clean_csv(args.input_file, args.output_file)
