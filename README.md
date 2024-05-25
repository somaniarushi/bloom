# Bloom Filter
I have seen bloom filters used in a bunch of cases recently — most relevantly, in a large-scale distributed web crawler, a Bloom filter is used as a model of probabilistically checking that a value is in a set.

While it’s completely fine to black box them, it’s important to me to understand a bunch of parts of the stack that I use at a slightly deeper level!

The core principle behind a bloom filter is using hashes instead of exact matches to some data. The cost of this is some false positives, because of hash collisions. However, bloom filters never create a false negative result.

As the number of elements in the bloom filter get larger, the false positive rate increases. As the size of the bloom filter increases, false positives decrease— at the cost of higher latency.

Full Logbook: https://dailyink.notion.site/Making-a-Bloom-Filter-3146563f3c864edfa1f30277d7bb7a36