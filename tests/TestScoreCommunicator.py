from ui.ScoreCommunicator import ScoreCommunicator


communicator = ScoreCommunicator('../db/test_scores_db.csv')

# Test if communicator is reading database
# (must return whatever was previously written to the file)
communicator.read_csv_file()
print(communicator.scores_table)

# Test if communicator is storing score in the wright way
rows = [["CHRIS", 2140],
        ["CHRIS", 2140],
        ["CHRIS", 2500],
        ["GREG", 2300],
        ["ROCHEL", 700],
        ["JULIUS", 3000],
        ["DREW", 1900],
        ["TONYA", 1940]]

for row in rows:
    communicator.write_csv_file(row[0], row[1])

print(communicator.scores_table)

# Test again if communicator is reading score database
# (must print same as last time)
communicator.read_csv_file()
print(communicator.scores_table)

# Test if communicator can clear the database
# communicator.clear_db()
# print(communicator.scores_table)
