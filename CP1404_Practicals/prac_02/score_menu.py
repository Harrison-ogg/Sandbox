
def main():
    """Get a numeric score and display its status."""
    score = float(input("Enter score: "))
    print(determine_status(score))


def determine_status(score):
    """Determine the status of a given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()


number_of_stars = int(input("Number of stars: "))
for i in range(number_of_stars):
    print('*', end=' ')
print()

for i in range(1, number_of_stars + 1):
    print('*' * i)
print()