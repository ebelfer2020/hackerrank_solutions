if __name__ == '__main__':
    
    students = []
    second_lowest_grades = []
    grades =set()
    
    for _ in range(int(input())):
        name = input()
        grade= float(input())
        students.append([name, grade])
        grades.add(grade)
        
    second_lowest = sorted(grades)[1]
    
    for name, grade in students:
        if grade == second_lowest:
            second_lowest_grades.append(name)
            
    for name in sorted (second_lowest_grades):
        print (name, end='\n')
