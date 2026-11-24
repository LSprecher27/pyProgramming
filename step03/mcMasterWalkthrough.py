score = int(input("Score: "))
study = input("Did you study? (y/n)")

if score >= 90:
    grade = "A"
    print("Great job, dude!")
elif score <= 50:
    grade = "F"
    print("Hit the road dude!")
if score >= 80 and score < 90:
    grade = "B"
    print("Not too shabby")
else:
    if score >= 60 and score < 70:
        grade = "D"
        print("ehh whatever")
    elif score >= 70 and score < 80:
            grade = "C"
            print("ehh whatever")



if study.lower() == "y" and score >= 80:
    print("Good effort!")
elif study.lower() == "y" and score < 80:
    print("Rough go, pal!")

if study.lower() == "n" and score >= 80:
    print("Lucky duck!")
elif study.lower() == "n" and score < 80:
    print("Try harder next time!")


print(f"Grade: {grade}")
