# Levenshtein distance

Print the values in a column of a table that are at some given Levenshtein distance to a given word. 
Also check if the implementation in utils gives the same answer as the implementation in pyenchant, http://pyenchant.github.io/pyenchant/

Run the script as follow:
./levenshtein_distance.py <csv file path> <column of interest> <target word> <wanted distance>

For docker run:
docker build -t my-app .
docker run -v /local/path/file_name.csv:/image/path/file_name.csv --rm my-app python3 levenshtein_distance.py /image/path/file_name.csv column_of_interest target_word wanted_distance
