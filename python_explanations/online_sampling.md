# Sample Online Data
This problem is motivated by the design of a packet sniffer that provides a uniform sample of packets for a network session.  
  
Design a program that takes as input a size _k_, and reads packets, continuously maintaining a uniform random subset of size _k_ of the read packets.  
  
## Examples
```
BLANK
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
* BLANK  
  
## Code Dissection
1. BLANK  