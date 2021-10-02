data = """
INDIA
Runs:231, Wickets:3, Overs:50
ENGLAND
Runs:187, Wickets:10, Overs:50
BANGLADESH
Runs:220, Wickets:8,Overs:50
AUSTRALIA
Runs:250,Wickets:9, Overs:50
"""
COUNTRY_NAME : {"Runs":int, "Wickets":int,"Overs":int}
d1 = {"Runs": 231, "Wickets": 3, "Overs": 50}
d2 = {"Runs": 187, "Wickets": 10, "Overs": 50}
d3 = {"Runs": 220, "Wickets": 8, "Overs": 50}
d4 = {"Runs": 250, "wickets": 9, "Overs": 50}
name = input("Enter Country Name:")
if name == "INDIA":
    print(d1)
elif name == "ENGLAND":
    print(d2)
elif name == "BANGLADESH":
    print(d3)
else:
    print(d4)

