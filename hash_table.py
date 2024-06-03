class HashTable:
    def __init__(self):
        """
        Constructor function for HashTable
        Creates 31 blank spaces in a list
        """
        self.hash_data = 31 * [None]
        self.rehash_attempt = 1
        self.total_collisions = 0



    def __str__(self):
        """
        String method for HashTable
        :return: A string containing the amount of slots, amount occupied, and load factor
        """

        slots = len(self.hash_data)
        occupied = self.occupied()
        load_factor = self.load_factor()

        return str(slots) + " slots, " + str(occupied) + " occupied, " + "load factor = " + str(load_factor)

    def store(self, word, tuple):
        """
        Takes a word and song details (tuple) and stores it into the hash table
        :param word: Word that is to be searched throughout the song list
        :param tuple: Tuple that contains (number, name, artist)
        :return: Nothing
        """
        load_factor_maximum = .7
        self.rehash_attempt = 1                   # Reset rehash attempt counter

        index = self.hash_function(word)
        slot = self.hash_data[index]

        if slot is None:
            self.hash_data[index] = [word, tuple]
        else:
            while slot is not None and slot[0] != word:
                index = self.rehash(index)
                slot = self.hash_data[index]
                self.total_collisions += 1
            if slot is None:
                self.hash_data[index] = [word, tuple]
            else:
                slot.append(tuple)

        # Write progress to logfile.txt
        logfile = open("logfile.txt", "a")
        if self.load_factor() > load_factor_maximum:    # Check load factor
            logfile.write("   " + str(self.occupied()) + " keys read, HashTable expansion needed\n")
            logfile.write("       Before expansion: " + str(self) + "\n")
            self.remap()
            logfile.write("       After expansion: " + str(self) + "\n")

        logfile.close()



    def get(self, word):
        """
        Accepts a word before returning a corresponding list of songs with said word
        :param word: Word being used to search songs
        :return: Hashed list of songs that are obtained from the hashmap
        """
        index = self.hash_function(word)
        self.rehash_attempt = 1
        # slot = self.hash_data[index]

        while self.hash_data[index] is not None:
            slot = self.hash_data[index]
            if slot[0] == word:
                return slot[1:]
            index = self.rehash(index)




    def hash_function(self, word):
        """
        Hashes the word so that it can be stored to the hash table
        :param word: Specific word that is to be hashed
        :return: The value that comes from hashing the word
        """
        # Hashing algorithm rationale:
        # I chose to use the unicode value of only alphanumeric values and then taking the modulo
        # of the value by the length of the hash table because I thought it would allow for a more accurate
        # Hashing value, since storing the words only considers lowercase values without special characters
        word = word.lower()
        total = 0
        for c in str(word):
            if c.isalnum():
                total += ord(c)
        return total % len(self.hash_data)


    def rehash(self, hash_value):
        """
        Employs quadratic probing on the item in order to rehash
        :param hash_value: The initial hash obtained from hash_function
        :return: A rehashed value
        """
        # Reason for choosing quadratic probing:
        # I chose quadratic probing because I think it can be more efficient in collision resolution
        # by allowing for there to be more space in the hash table between each collision without
        # data becoming too clustered in one location
        rehashed = (hash_value + self.rehash_attempt ** 2) % len(self.hash_data)
        self.rehash_attempt += 1
        return rehashed



    def remap(self):
        """
        Increases the size of the hash table and reallocates the occupied spots to their proper hash location
        :return: None
        """
        old_data = self.hash_data
        new_data = self.next_prime(len(self.hash_data) * 2)
        self.hash_data = new_data * [None]

        for data in old_data:                          # Loop through original Hash Table
            if data is not None:
                word = data[0]
                for tuple in data[1:]:
                    self.store(word, tuple)



    def load_factor(self):
        """
        Keeps track of the current load factor by dividing occupied amount by the amount of slots in the data
        :return: The load factor of the hash table
        """
        return self.occupied() / len(self.hash_data)


    def occupied(self):
        """
        Tracks the amount of slots in the hash table that is not None
        :return: The amount of occupied slots in the hash table
        """
        occupied = 0
        for item in self.hash_data:
            if item is not None:
                occupied += 1
        return occupied

    def is_prime(self, n):
        """
        Checks whether a specified value is a prime number. Helper function for next_prime()
        :param n: Number to be checked
        :return: Boolean. True if the value is prime, False otherwise
        """
        for i in range(2, n):
            if (n % i) == 0:
                return False
        return True

    def next_prime(self, num):
        """
        Finds the next prime number of a value
        :param num: The value being checked for prime
        :return: Incremented value once it reaches a prime number
        """
        if num % 2 == 0:
            num += 1
        while not self.is_prime(num):
            num += 2
        return num





