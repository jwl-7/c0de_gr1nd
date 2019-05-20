# Swap Bits

"A 64-bit integer can be viewed as an array of 64 bits, with the bit at index 0 corresponding to the least significant bit (LSB), and the bit at index 63 corresponding to the most significant bit (MSB)." - EPI

Problem:  
Write code that swaps the bits of a 64-bit integer at indices i and j.</p>

Example:  
Let x = 1234 (decimal value)  

1234 in binary:  

|MSB | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |LSB|  
|---:|---|---|---|---|---|---|---|---|---|---|
|  1 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | 0 |   
  
Let i = 3 and j = 7  
```swap_bits(x, i, j)```  
  
Bits 3 (0) and 7 (1) will be swapped resulting in:  

|MSB | 9 | 8 |   7   | 6 | 5 | 4 |   3   | 2 | 1 |LSB|  
|---:|---|---|-------|---|---|---|-------|---|---|---|
|  1 | 0 | 0 | **0** | 1 | 0 | 1 | **1** | 0 | 1 | 0 | 
  
The swapped number in decimal would be: 1114