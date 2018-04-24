import csv
import os


class ScoreCommunicator(object):
    MAX_TABLE_ROWS = 50

    def __init__(self, db_file_name):
        self.db_file_name = os.path.join(os.path.dirname(__file__), os.pardir, db_file_name)
        self.scores_table = []

    def read_csv_file(self):
        self.scores_table = []
        try:
            csv_readable_file = open(self.db_file_name, 'r')
        except FileNotFoundError:
            return

        score_reader = csv.reader(csv_readable_file)
        for row in score_reader:
            if len(row) == 2:
                self.scores_table.append([row[0], int(row[1])])

        csv_readable_file.close()

    def write_csv_file(self, name, score):
        self.read_csv_file()

        csv_writable_file = open(self.db_file_name, 'w+')
        score_writer = csv.writer(csv_writable_file)
        was_written = False

        for row in self.scores_table:
            if not was_written and name == row[0] and score == row[1]:
                was_written = True

            elif not was_written and score >= row[1]:
                score_writer.writerow([name, score])
                was_written = True

            score_writer.writerow(row)

            if len(self.scores_table) == self.MAX_TABLE_ROWS:
                break

        if len(self.scores_table) < self.MAX_TABLE_ROWS:
            if not was_written:
                score_writer.writerow([name, score])

        else:
            print("Maximum number of score table rows ({}) was reached".format(self.MAX_TABLE_ROWS))

        csv_writable_file.close()

        self.read_csv_file()

    def clear_db(self):
        self.scores_table = []

        csv_writable_file = open(self.db_file_name, 'w')
        csv_writable_file.close()
