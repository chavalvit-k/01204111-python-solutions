# level-2/01.py

def calculate_roi(amount, expected):
    if amount == 0:
        return 0

    roi = (expected - amount) / amount * 100

    return roi

def classify_roi(roi):
    if roi < 10:
        return "Low Return"
    elif roi <= 30:
        return "Moderate Return"
    else:
        return "High Return"

print("""
--- Financial ROI Calculator ---
1. Enter Data
2. Calculate ROI and Categorize
q. Quit
""")

projects, amounts, returns = [], [], []

while True:
    option = input("Select an option: ")

    if option == "1":
        while True:
            project = input("Project name: ")

            if project == "":
                print()
                break

            amount = float(input("Investment amount: (THB): "))
            expected = float(input("Expected return: (THB): "))

            projects.append(project)
            amounts.append(amount)
            returns.append(expected)

    elif option == "2":
        print("\n--- ROI Summary ---")
        print(f"{'Project':<20} {'Investment':>15} {'Return':>15} {'ROI (%)':>10} {'Category':>20}")

        for project, amount, expected in zip(projects, amounts, returns):
            roi = calculate_roi(amount, expected)
            category = classify_roi(roi)
            print(f"{project:<20} {amount:>15.2f} {expected:>15.2f} {roi:>10.2f} {category:>20}")

        print()

    elif option == "q":
        print("Bye\n")
        break
