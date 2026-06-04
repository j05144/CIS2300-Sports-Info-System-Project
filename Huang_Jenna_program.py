import pandas as pd
import matplotlib.pyplot as plt
import wikipediaapi as wk
%matplotlib inline

# load file
df = pd.read_csv("sports.csv")
df = df.set_index("SPORT")

# Wikipedia object (required user agent)
wiki = wk.Wikipedia(
    language="en",
    user_agent="CIS2300-Project (student@example.com)"
)

print("CIS2300 Sports Project")

# menu variable
op = ""

while op != "X":
    print("\n--- MAIN MENU ---")
    print("A - Show all data")
    print("S - Show selected sports/countries")
    print("N - Add a new sport")
    print("D - Delete a sport")
    print("W - Save changes")
    print("I - Wikipedia information")
    print("X - Exit")

    op = input("Choose an option: ").upper()

    # A - All data
    if op == "A":
        print("\n--- FULL DATA ---")
        print(df)
        g = input("Show chart? (y/n): ").upper()
        if g == "Y":
            df.plot(kind="bar")
            plt.show()

    # S - Selected
    elif op == "S":
        countries = input("Enter countries (comma): ").upper().split(",")
        countries = [c.strip() for c in countries]

        sports = input("Enter sports (comma): ").upper().split(",")
        sports = [s.strip() for s in sports]

        try:
            selected = df.loc[sports, countries]
            print("\n--- SELECTED DATA ---")
            print(selected)

            g = input("Show chart? (y/n): ").upper()
            if g == "Y":
                selected.plot(kind="bar")
                plt.show()
        except:
            print("Invalid sport or country entered.")

    # N - New sport
    elif op == "N":
        new_sport = input("Enter new sport name: ").upper()
        scores = []

        for c in df.columns:
            value = int(input(f"Enter score for {c}: "))
            scores.append(value)

        df.loc[new_sport] = scores
        print("Sport is successfully added.")

    # D - Delete sport
    elif op == "D":
        remove_sport = input("Enter sport to delete: ").upper()
        if remove_sport in df.index:
            df = df.drop(remove_sport)
            print("Sport successfully deleted.")
        else:
            print("Sport not found.")

    # W - Save to CSV
    elif op == "W":
        df.to_csv("sports.csv")
        print("Saved to sports.csv.")

    # I - Wikipedia information
    elif op == "I":
        term = input("Search term: ")
        page = wiki.page(term)
        if page.exists():
            print("\n--- INFORMATION ---")
            print(page.summary[:600])
        else:
            print("No information found.")

    # X - Exit
    elif op == "X":
        print("Goodnight!")

    else:
        print("Uh oh! Try again.")