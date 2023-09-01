import pandas as pd

def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def find_similarities(list1, list2):
    return set(list1).intersection(list2)

def main():
    file1_path = 'file1.txt'
    file2_path = 'file2.txt'
    output_excel_path = 'similarities.xlsx'

    file1_lines = read_file(file1_path)
    file2_lines = read_file(file2_path)

    similarities = find_similarities(file1_lines, file2_lines)

    if similarities:
        df = pd.DataFrame({'Similar Lines': list(similarities)})
        df.to_excel(output_excel_path, index=False)
        print(f'Similarities found. Check "{output_excel_path}" for results.')
    else:
        print('There were no similarities found.')

if __name__ == "__main__":
    main()
