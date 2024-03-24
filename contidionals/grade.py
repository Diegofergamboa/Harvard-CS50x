# Program to check the score of grade

def checkGradeScore(score):
    if score <= 100 and score >= 0:
        if score >= 90:
            print('Grade A')
        elif score >= 80:
            print('Grade B')
        elif score >= 70:
            print('Grade C')
        elif score >= 60:
            print('Grade D')
        elif score >= 50:
            print('Grade E')
        else:
            print('Grade F')
    else:
        return print('Invalid Score Format')


scoreInput = int(input('Score: '))

# Main init
def main():
    checkGradeScore(scoreInput)    

main()