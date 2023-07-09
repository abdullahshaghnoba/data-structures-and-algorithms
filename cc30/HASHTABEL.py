class Hashtable:
    def __init__(self):
        self.size = 3  
        self.table = [[] for _ in range(self.size)]  # List of lists (buckets)

    def hash(self, key):
        """
        takes a key and returns the hashed value of the key as the index
        Args:key
        returns the index 
        """
        sum_of_asccii = 0
        # print(key)
        for ch in str(key):
            asccii_of_ch = ord(ch)
            sum_of_asccii += asccii_of_ch
        temp = sum_of_asccii*599
        indx = temp%self.size
        return indx

    def set(self, key, value):
        """
        takes a key and a value and adds the key value pair to the hash table
        args:key , value
        returns nothing
        """
        hash_value = self.hash(key)
        bucket = self.table[hash_value]


        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:

                bucket[i] = (key, value)
                return


        bucket.append((key, value))

    def get(self, key):
        """
        takes a key and returns the value associated with the key
        args: key
        returns the value associated with the key
        """
        hash_value = self.hash(key)
        bucket = self.table[hash_value]


        for existing_key, value in bucket:
            if existing_key == key:
                return value


        return(f"Key '{key}' does not exist.")

    def has(self, key):
        """
        takes a key and returns True if the key exists in the hash table and False otherwise
        args: key
        returns True or False
        """
        hash_value = self.hash(key)
        bucket = self.table[hash_value]


        for existing_key, _ in bucket:
            if existing_key == key:
                return True

        return False

    def keys(self):
        """
        takes no arguments and returns a list of keys in the hash table
        args: none
        returns a list of keys
        """
        keys = []
        for bucket in self.table:
            for key, _ in bucket:
                keys.append(key)
        return keys


# hashtable1 = Hashtable()
# hashtable1.set(str(150), 0)
# hashtable1.set("E", 90)
# hashtable1.set("A", 70)
# hashtable1.set("B", 90)
# hashtable1.set("C", 80)
# print(hashtable1.table)
# print(hashtable1.keys())
# print(hashtable1.has("A"))
# print(hashtable1.has("B"))
# print(hashtable1.has("C"))
# print(hashtable1.has("E"))
# print(hashtable1.has("N"))
# print(hashtable1.get("N"))
# print(hashtable1.get("A"))
# print(hashtable1.get("B"))
# print(hashtable1.get("C"))
# print(hashtable1.get("E"))
# print(hashtable1.get("F"))