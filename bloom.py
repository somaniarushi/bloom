import math
import mmh3
from bitarray import bitarray

class BloomFilter:

    def __init__(self, expected_items_count, acceptable_false_pos_prob):
        self.acceptable_false_pos_prob = acceptable_false_pos_prob

        # Size of bit array to use
        self.size = self.get_size(
            expected_items_count=expected_items_count,
            acceptable_false_pos_prob=acceptable_false_pos_prob
        )

        # number of hash functions to use
        self.hash_count = self.get_hash_count(
            optimal_size=self.size, 
            expected_items_count=expected_items_count
        )

        self.bit_array = bitarray(self.size)
        self.bit_array.setall(0) # TODO: Unnecesary?

    def add(self, item):
        for i in range(self.hash_count):
            bucket = mmh3.hash(item, i) % self.size
            self.bit_array[bucket] = 1

    def check(self, item):
        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size
            if not self.bit_array[digest]:
                return False
        return True

    @staticmethod
    def get_size(*, expected_items_count, acceptable_false_pos_prob):
        """
        Return the size of bit array(m) to use.
        TODO(Arushi): Explain formula
        """
        optimal_size = -(expected_items_count * math.log(acceptable_false_pos_prob)) / (math.log(2) ** 2)
        return int(optimal_size)

    @staticmethod
    def get_hash_count(*, optimal_size, expected_items_count):
        """
        Return the hash function(k) to use
        """
        num_hash_funcs = (optimal_size / expected_items_count) * math.log(2)
        return int(num_hash_funcs)
