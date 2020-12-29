#python_version == '3.7'

def get_average_grades(filename):
    with open(filename) as file:
        list_of_lists = [[float(i) for i in line.split(',')] for line in file]
        student_num, lab_num = len(list_of_lists), len(list_of_lists[0])
        lab_submit_num, score = [student_num for n in range(lab_num)], [0 for n in range(lab_num)]
        for y in range(student_num):
            for x in range(lab_num):
                if float(list_of_lists[y][x]) == -1: lab_submit_num[x] -= 1
                else: score[x] += float(list_of_lists[y][x])
        average_grades_list = [score[lab]/lab_submit_num[lab] for lab in range(lab_num)]
        average_grades_list = [int(i) if i%1 == 0 else i for i in average_grades_list]
    return average_grades_list

# print(get_average_grades('grades.csv'))