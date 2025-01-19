class HashTable:
    def __init__(self, size):
        """Initialize the hash table with a fixed size and empty buckets."""
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        """Generate a hash for the given key."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value  # Update existing key
                return
        self.table[index].append([key, value])

    def retrieve(self, key):
        """Retrieve the value associated with a given key."""
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None  # Key not found

    def delete(self, key):
        """Delete a key-value pair from the hash table."""
        index = self.hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
        return False  # Key not found

    def display(self):
        """Print the current state of the hash table."""
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")

# Example: Content Recommendation System
def main():
    # Create a hash table to store user recommendations
    user_recommendations = HashTable(size=10)

    # Insert user-specific recommendations
    user_recommendations.insert("user1", ["Post A", "Post B", "Post C"])
    user_recommendations.insert("user2", ["Post D", "Post E"])
    user_recommendations.insert("user3", ["Post F", "Post G", "Post H", "Post I"])

    # Retrieve and display recommendations for a specific user
    print("Recommendations for user1:", user_recommendations.retrieve("user1"))

    # Update recommendations for a user
    user_recommendations.insert("user1", ["Post X", "Post Y"])
    print("Updated recommendations for user1:", user_recommendations.retrieve("user1"))

    # Delete recommendations for a user
    user_recommendations.delete("user2")
    print("Recommendations for user2 after deletion:", user_recommendations.retrieve("user2"))

    # Display the current state of the hash table
    print("\nCurrent state of the hash table:")
    user_recommendations.display()

if __name__ == "__main__":
    main()
