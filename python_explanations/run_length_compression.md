# Implement Run-Length Encoding
Run-length encoding (RLE) compression offers a fast way to do efficient on-the-fly compression and decompression of strings. The idea is simple --- encode successive repeated characters by the repetition count and the character. For example, the RLE of "aaaabcccaa" is "4a1b3c2a". The decoding of "3e4f2e" returns "eeeffffee".  
  
Implement run-length encoding and decoding functions. Assume the string to be encoded consists of letters of the alphabet, with no digits, and the string to be decoded is valid encoding.
  
## Examples
```
Decoding:
    Input: '5a12z6n21y3d3p'
   Output: 'aaaaazzzzzzzzzzzznnnnnnyyyyyyyyyyyyyyyyyyyyydddppp'

Encoding:
    Input: 'vvvkkkkkkkkwwwwwwwwwwwwwwwwwffffffffffmmmmmmm'
   Output: '3v8k17w10f7m'
```
  
## Solution
```python
def decoding(s):
    decoded = ''
    count = ''
    for char in s:
        if char.isdigit():
            count += char
        else:
            decoded += int(count) * char
            count = ''
    return decoded

def encoding(s):
    encoded = ''
    prev = s[0]
    count = 0
    for char in s:
        if char == prev:
            count += 1
        else:
            encoded += str(count) + prev
            prev = char
            count = 1    
    encoded += str(count) + char
    return encoded
```
  
## Explanation
* BLANK
  
## Code Dissection
1. BLANK