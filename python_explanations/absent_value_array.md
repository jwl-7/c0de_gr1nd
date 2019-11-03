# Find the Missing IP Address
You're given a file with 1 billion IP addresses in 32-bit. Find the missing IP address. Assume you do not have much RAM.

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
1. First pass, First block: for every IP address, its leading 16 bits (MSBs) are used to index into the block and increment that spot by 1
2. Second pass, First block: find the first entry in the array less than 2<sup>16</sup> and get the index of that spot
3. First pass, Second block: find all the IP addresses whose first 16 bits (LSBs) are equal to the entry retrieved in Step 2
4. Second pass, Second block: find the first entry in block2 that is zero and return the index
    * This means that some combination of the first 16 bits (LSBs) is missing

## Code Dissection
1. Define the size of the block to be 2<sup>16</sup> and create two iterators to use on the IP addresses
    ```python
    block_size = 1 << 16
    stream, stream_copy = itertools.tee(stream)
    ```
2. Block 1, Pass 1: for every IP in the stream, use its leading 16 bits (MSBs) to index into the block and increment that spot by 1
    ```python
    count_block = [0] * block_size
    for ip in stream:
        count_block[ip // block_size] += 1
    ```
3. Block 1, Pass 2: look for an entry in *count_block* that is less than 2<sup>16</sup> and return that index
    ```python
    block_idx = 0
    for i, val in enumerate(count_block):
        if val < block_size:
            block_idx = i
            break
    ```
4. Block 2, Pass 1: find an IP address whose first 16 bits (LSBs) are equal to *block_idx*
    ```python
    block = [0] * block_size
    stream = stream_copy
    for ip in stream_copy:
        if ip // block_size == block_idx:
            block[ip % block_size] = 1
    ```
5. Block 2, Pass 2: find an entry equal to zero and return the index
    ```python
    for i, val in enumerate(block):
        if not val:
            return block_idx * block_size + i
    ```