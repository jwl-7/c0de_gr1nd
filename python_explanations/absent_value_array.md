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
* An array of 2<sup>16</sup> integers filled with zeroes will be referred to as a 'block'
* The block will be used to represent the IP addresses without using up too much storage/memory
1. First pass of the block: For every IP address, its leading 16 bits (MSBs) are used to index into the block and increment that spot by 1
2. Second pass of the block: Find the first entry in the array less than 2<sup>16</sup> and get the index of that spot
3. First pass of block2: Find all the IP addresses whose first 16 bits (LSBs) are equal to the entry retrieved in Step 2
4. Second pass of block2: Find the first entry in block2 that is zero and return the index
    * This means that some combination of the first 16 bits (LSBs) is missing

## Code Dissection
1. BLANK