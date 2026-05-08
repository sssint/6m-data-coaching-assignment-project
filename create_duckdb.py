import duckdb
import os

if os.path.exists("SGJobData.db"):
    print('There is already a file created. Exiting program.')
    print('To repeat the process delete the file test_duck.db')
    exit(0)


con = duckdb.connect("SGJobData.db")

# download csv file with the name "Resale flat prices based on registration date from Jan-2017 onwards"
# from the data.gov.sg website
# https://beta.data.gov.sg/datasets/189/resources/d_8b84c4ee58e3cfc0ece0d773c8ca6abc/view
# then store the file (ResaleflatpricesbasedonregistrationdatefromJan2017onwards.csv) in this folder

con.sql(
    "CREATE TABLE SGJobData AS SELECT * FROM read_csv_auto('SGJobData.csv', HEADER=TRUE);"
)
