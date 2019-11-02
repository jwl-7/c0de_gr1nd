# Find the Missing IP Address
Suppose you were given a file containing roughly one billion IP addresses, each of which is a 32-bit quantity. How would you programmatically find an IP address that is not in the file? Assume you have unlimited drive space but only a few megabytes of RAM at your disposal.

## Solution
```python
def find_missing_element(stream):
    block_size = 1 << 16
    stream, stream_copy = itertools.tee(stream)

    count_block = [0] * block_size
    for ip in stream:
        count_block[ip // block_size] += 1

    block_idx = 0
    for i, val in enumerate(count_block):
        if val < block_size:
            block_idx = i
            break

    block = [0] * block_size
    stream = stream_copy
    for ip in stream_copy:
        if ip // block_size == block_idx:
            block[ip % block_size] = 1

    for i, val in enumerate(block):
        if not val:
            return block_idx * block_size + i
```

## Explanation
* BLANK

## Code Dissection
1. BLANK