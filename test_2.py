


"""
The program is meant to display the number of grades.
Also the number of grades that are above average.
There will be two functions two functions working in this program.
Function1 will be to kickstart the program and Function2 will be to calculate the percentage of grades that are above average.

Function1 will Kickstart the application
Function2 will output(Number of grades,average grade, and percentage of grades above average)

Number of Grades: 24
Average Grade: 83.25
Percentage of grades above average: 54.17%
"""

"""
#Main Function
def main():
    f = open('Final.txt')
    grades = []
    for line in f:
        grades.append(int(line.strip()))
    print("Number of grades:", len(grades))
    avg = 0
    for grade in grades:
        avg += grade
    avg /= len(grades)
    print("Average grade:", avg)
    print("Percentage of grades above average: {:.2f}%".format(calculate_percent_above_average(grades, avg)))
    f.close()


main()
#calculate_percent_above_average function
def calculate_percent_above_average(grades, avg):
    count = 0
    for grade in grades:
        if grade > avg:
            count += 1
    return (count * 100) / len(grades)

"""
def calculate_percent_above_average(grades, avg):
    count = 0
    for grade in grades:
        if grade > avg:
            count += 1
    return (count * 100) / len(grades)
def main():
    f = open('Final.txt')
    grades = []
    for line in f:
        grades.append(int(line.strip()))
    print("Number of grades:", len(grades))
    avg = 0
    for grade in grades:
        avg += grade
    avg /= len(grades)
    print("Average grade:", avg)
    print("Percentage of grades above average: {:.2f}%".format(calculate_percent_above_average(grades, avg)))
    f.close()

