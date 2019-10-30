# Sample Online Data
This problem is motivated by the design of a packet sniffer that provides a uniform sample of packets for a network session.

Design a program that takes as input a size _k_, and reads packets, continuously maintaining a uniform random subset of size _k_ of the read packets.

## Examples
```
stream = [1, 2, 3, 4]
k = 1

[1]
[3]
[1]
[3]
[3]
[4]
[3]
[2]
[2]
[2]
[1]
[4]
[2]
[1]
[2]
[4]
[4]
[3]
[3]
[4]
```

## Solution
```python
def online_random_sample(stream, k):
    sample = list(itertools.islice(stream, k))
    num_read = k
    for packet in stream:
        num_read += 1
        r_num = random.randrange(num_read)
        if r_num < k:
            sample[r_num] = packet
    return sample
```

## Explanation
The algorithm works like this:
1. The first _n_ packets are read into a running sample list, which will be used as a continous random subset of size _k_
2. When we read the (_n_ + 1)th packet, it should belong to the new subset with the probability _k_ / (_n_ + 1)
3. We choose a random packet in the existing subset (the sample list) to replace with the (_n_ + 1)th packet
4. The resulting collection will be a random subset of the _n_ + 1 packets
* The induction hypothesis is that all _k_-sized subsets are equally likely after _n_ >= _k_ packets have been read

## Code Dissection
1. Read in the first _n_ packets of the specified size _k_, store those packets into a list, and set a variable to keep track of the number of packets read so far
    ```python
    sample = list(itertools.islice(stream, k))
    num_read = k
    ```
2. Loop through the packets in the stream and increment the number of packets read so far
    ```python
    for packet in stream:
        num_read += 1
    ```
3. Generate a uniform random number ranging from 0 to (_n_ + 1) &mdash; this will be used to select which packet to replace in the sample list
    ```python
    r_num = random.randrange(num_read)
    ```
4. Check to make sure that the generated random number is less than _k_, because we want to make sure we replace a number within the index range of the sample list
    ```python
    if r_num < k:
        sample[r_num] = packet
    ```
5. Return the sample list
    ```python
    return sample
    ```