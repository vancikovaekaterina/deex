class RollingHash:
    def __init__(self, string, window_size):
        self.string = string
        self.window_size = window_size
        self.base = 256
        self.mod = 101

        self.hash_value = 0
        for i in range(window_size):
            self.hash_value = (self.hash_value * self.base + ord(string[i])) % self.mod

    def update_hash(self, old_char, new_char):
        self.hash_value = (self.hash_value * self.base - ord(old_char) * pow(self.base, self.window_size - 1, self.mod) + ord(new_char)) % self.mod

    def get_hash(self):
        return self.hash_value
