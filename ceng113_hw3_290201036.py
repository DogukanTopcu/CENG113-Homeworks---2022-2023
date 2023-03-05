def scores():
    termScore = int(input("Please enter your 1th mid-term score: "))
    finalScore = int(input("Please enter your final score: "))
    quiz1Score = int(input("Please enter your 1th quiz score: "))
    quiz2Score = int(input("Please enter your 2th quiz score: "))
    quiz3Score = int(input("Please enter your 3th quiz score: "))
    quiz4Score = int(input("Please enter your 4th quiz score: "))
    homework1Score = int(input("Please enter your 1th homework score: "))
    homework2Score = int(input("Please enter your 2th homework score: "))
    homework3Score = int(input("Please enter your 3th homework score: "))
    homework4Score = int(input("Please enter your 4th homework score: "))

    return [termScore, finalScore, quiz1Score, quiz2Score, quiz3Score, quiz4Score, homework1Score, homework2Score, homework3Score, homework4Score]


def TotalScore(scores):
    total = scores[0]*0.25 + scores[1]*0.35 + (scores[2]+scores[3]+scores[4]+scores[5])*0.2 + (
        scores[6]+scores[7]+scores[8]+scores[9])*0.2

    print("Your total score is:", total)
    return total


def AbsenceNum():
    absence = int(input("Enter your absence number: "))
    absenteeismRate = (absence/14)

    return absenteeismRate


def Grade(total, absence):
    if absence > 0.25:
        grade = "NA"
    else:
        if total >= 90:
            grade = "AA"
        elif total >= 85:
            grade = "BA"
        elif total >= 80:
            grade = "BB"
        elif total >= 75:
            grade = "CB"
        elif total >= 70:
            grade = "CC"
        elif total >= 65:
            grade = "DC"
        elif total >= 60:
            grade = "DD"
        elif total >= 50:
            grade = "FD"
        else:
            grade = "FF"

    return grade


def main():
    print("Your grade is:", Grade(TotalScore(scores()), AbsenceNum()))


if __name__ == "__main__":
    main()
