# Song Search Project

This project involves building a hash table to store and search for songs and their respective artists based on words or phrases found in song titles. The implementation leverages a custom `HashTable` class to store song data and allows for efficient searching.

## Files

- `song_search.py`: Main script for building the hash table and searching for songs based on words or phrases.
- `hash_table.py`: (not included) Contains the `HashTable` class definition and relevant methods for storing and retrieving data.
- `resources/songs.txt`: (not included) File containing song data in the format `song_title :: artist`.
- `words.txt`: (not included) File containing words to search for in song titles.
- `phrases.txt`: (not included) File containing phrases to search for in song titles.
- `logfile.txt`: Log file generated during the execution of the script.

## Usage

1. **Building the Hash Table**: The script reads song data from a file and builds a hash table.
2. **Searching for Words**: The script searches for individual words in song titles and prints the results.
3. **Searching for Phrases**: The script searches for phrases in song titles and prints the results.