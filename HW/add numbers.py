# Template
def count_department():
    """ 
    input:
        -
    output:
        number_of_dept- list (key: majors, values: number of people who have the major)
                        ex：[['Engineering', 10], ['Nursing', 17], ... ]
    
    """
    from glob import glob
    filenames = glob('rosters/*txt') #list of file names in the folder
    number_of_dept = []
    for file_name in filenames:
        with open(file_name, 'r') as f:
            for line in f:
                if line.startswith('Department'):
                    dept = line.split(':')[1].strip()
                    number_of_dept.append([dept, 0])
                    break