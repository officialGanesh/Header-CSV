# Import the required module
import os ,csv

def Remove_header():
    ''' Main program to remove headers from csv files '''

    current_working_dir = os.getcwd()
    dir_contents = os.listdir()
    print(f'Your current working directory --> {current_working_dir} \n Contents --> {dir_contents}' )

    def search_removeheader_csv():
        '''Searhing for csv files'''

        csv_header_rows = []

        for file in dir_contents:
            try:
                if file.endswith('.csv'):
                    print(f'Removing header from --> {file}')
                    with open(file,'r') as csv_file:
                        csv_reader = csv.reader(csv_file)
                        for row in csv_reader:
                            if csv_reader.line_num == 1:
                                continue
                            csv_header_rows.append(row)
                    
            except Exception as e:
                print('Something Went Wrong ',e)

    search_removeheader_csv()
      



if __name__ == "__main__":

    Remove_header()
    print('Code Completed 🔥')