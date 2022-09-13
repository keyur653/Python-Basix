if __name__== '__main__':
    students_info=[]
    for _ in range (int(input())):
        name=input()
        score=float(input())
        students_info.append([name, score])
        sorted_scores=sorted(list(set([x[1] for x in students_info])))
    second_lowest=sorted_scores[1]
    final_list=[]
    for student in students_info:
        if second_lowest == student[1]:
            final_list.append(student[0])
            for student in sorted(final_list):
                print(student)
