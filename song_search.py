from hash_table import HashTable

def build_hash_table(filename):
    """
    Builds hash table using hash_table module and class
    :param filename: File to pull data from to build hash_table
    :return: The built hash table containing data
    """
    # The following code begins writing in logfile.txt until hash_table building begins
    print("Building hash table using data in ", filename)
    hash_table = HashTable()

    logfile = open("logfile.txt", "w")  # Logfile for assignment
    logfile.write("Program start\n")
    logfile.write("HashTable details: " + str(hash_table) + "\n")
    logfile.write("Start reading songs from file " + str(filename) + "\n")
    logfile.close()

    #code for reading song titles from filename
    #and indexing the words in the song title in hash_table

    infile = open(filename, "r")
    line_count = 0                      # Line counter to track the line in the text file
    for line in infile:
        line_count += 1                 # Increment line counter
        song, artist = line.strip().split(" :: ")

        index_gone = False              # Make variable to track getting rid of numbers in the text file
        counter = 0                     # Counter for the index of the song string (number and song title)
        while index_gone is False:
            counter += 1
            if song[counter] == " ":          # Checks for space after line number
                song = song[counter + 1:]     # Replaces song variable with a new string that contains the song title WITHOUT the line number
                index_gone = True

        song_words = song.split(" ")          # Separate each word in the song
        tuple = (line_count, song, artist)

        for word in song_words:
            new_word = ''
            for char in word:
                if char.isalnum():            # If the character is alphanumeric, concatenate the string to the new word
                    new_word += char

            new_word = new_word.lower()
            hash_table.store(new_word, tuple)

    infile.close()

    # Continue writing in logfile.txt
    logfile = open("logfile.txt", "a")
    logfile.write("End reading songs from file " + str(filename) + "\n")
    logfile.write("HashTable details: " + str(hash_table) + "\n")
    logfile.write("Number of unique keys inserted into HashTable = " + str(hash_table.occupied()) + "\n")
    logfile.write("Number of key conflicts encountered = " + str(hash_table.total_collisions) + "\n" + "\n")
    logfile.write("Now starting search of songs")

    logfile.close()
    return hash_table


def find_words(hash_table, filename):
    """
    Looks for songs with the specified word in the hash table
    :param hash_table: The built hash_table to be searched through
    :param filename: File of words to check for in the songs of the hash table
    :return: None, but print the found songs.
    """
    print("Searching for words listed in ", filename)
    infile = open(filename, "r")

    for line in infile:
        word = line.strip()
        result = (hash_table.get(word))     # Get word from hash_table
        num_songs = len(result)

        print(str(num_songs) + ' songs contain the word "' + str(word) + '" in their title')
        number = 1
        print()


        for word in result:
            index = word[0]
            song_name = word[1]
            artist = word[2]
            print("   ", str(number) + ". " + str(index) + ", " + str(song_name) + ", " + str(artist))
            number += 1
        print()
        print("This search examined " + str(hash_table.rehash_attempt) + " slot(s) in the hash table")
        print("-----------------------------------------------------------")
        print()



    infile.close()
    return None

def find_phrases(hash_table, filename):
    try:
        infile = open(filename, "r")
    except IOError:
        print("Could not open file: ", filename)
        return None

    print("Searching for phrases listed in ", filename)

    for line in infile:
        line = line.strip()
        phrase = line.lower()  # Convert phrase to lower case
        songs_with_phrase = set()  # Use a set to eliminate duplicates

        slots_examined = 0
        for word in phrase.split():
            result = hash_table.get(word)
            slots_examined += hash_table.rehash_attempt
            for item in result:
                song_title = item[1].lower()  # Convert song title to lower case
                if phrase in song_title:
                    songs_with_phrase.add(item)

        song_amount = len(songs_with_phrase)
        print(str(song_amount) + ' songs contain the phrase "' + phrase + '" in their title')

        number = 1
        for item in songs_with_phrase:
            index = item[0]
            song_name = item[1]
            artist = item[2]
            print("   ", str(number) + ". " + str(index) + ", " + str(song_name) + ", " + str(artist))
            number += 1
        print()
        print("This search examined " + str(slots_examined) + " slot(s) in the hash table")
        print("-----------------------------------------------------------")
        print()

    infile.close()
    return None

def main():

    hash_table = build_hash_table("resources/songs.txt")

    find_words(hash_table, "words.txt")

    find_phrases(hash_table, "phrases.txt")


main()




