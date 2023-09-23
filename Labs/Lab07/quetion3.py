import numpy as np

# Question-3

homeworks = np.loadtxt("lab2-hw.txt", skiprows=1, usecols=(1, 2, 3, 4, 5))
#gets lab2-hw.txt and skips row 1, uses col 1-5
avg_hw = homeworks.mean(axis=1)
hw_percentiles = avg_hw*30/50
# print(hw_percentiles)

#gets lab2-project.txt and skips row 1, uses col
project = np.loadtxt("lab2-project.txt", skiprows=1, usecols=1)
project_percentiles = project*20/100
# print(project_percentiles)

quiz = np.loadtxt("lab2-quiz.txt", skiprows=1, usecols=(1, 2, 3, 4, 5))
#gets lab2-quiz.txt and skips row 1, uses col 1-5
avg_quiz = quiz.mean(axis=1)
quiz_percentiles = avg_quiz*10/10
# print(quiz_percentiles)

#gets lab2-test.txt and skips row 1, uses col 1-2
tests = np.loadtxt("lab2-test.txt", skiprows=1, usecols=(1, 2))
avg_tests = tests.mean(axis=1)
tests_percentile = avg_tests*40/100


# print(tests_percentile)
total_marks = hw_percentiles + quiz_percentiles + project_percentiles + tests_percentile
#print("total marks= ",total_marks)
print("A's final score =",round(total_marks[0],2))
print("B's final score =",round(total_marks[1],2))
print("C's final score =",round(total_marks[2],2))
print("D's final score =",round(total_marks[3],2))
print("E's final score =",round(total_marks[4],2))
print("F's final score =",round(total_marks[5],2))