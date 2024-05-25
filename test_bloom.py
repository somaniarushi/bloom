from bloom import BloomFilter

class TestBloom:
    def test_basic(self) -> None:
        bloom = BloomFilter(expected_items_count=100, acceptable_false_pos_prob=0.05)
        bloom.add("hello")
        assert bloom.check("hello"), f"Expected 'hello' to be in bloom filter"
        assert not bloom.check("world"), f"Expected 'world' to not be in bloom filter"
        bloom.add("world")
        assert bloom.check("world"), f"Expected 'world' to be in bloom filter"
        assert not bloom.check("python"), f"Expected 'python' to not be in bloom filter"
    
    def test_false_positive_find(self) -> None:
        bloom = BloomFilter(expected_items_count=10, acceptable_false_pos_prob=0.7)
        # Create 10 random strings
        random_strings = [str(i) for i in range(10)]
        # Add them to bloom filter
        for s in random_strings:
            bloom.add(s)
    
        # Create ten more random strings
        more_random_strings = [str(i) for i in range(10, 20)]

        # Check if they are in bloom filter, at least one of them should be a false positive
        assert any(bloom.check(s) for s in more_random_strings), f"Expected at least one false positive"