# Write a String Sinusoidally
The string "Hello_World!" written in sinusoidal fashion is:
```
  e       _       l
H   l   o   W   r   d
      l       o       !
```
(Here _ denotes a blank.)  
  
Define the snakestring of _s_ to be the left-right top-to-bottom sequence in which characters appear when _s_ is written in sinusoidal fashion. For example, the snakestring for "Hello_World!" is "e_lHloWrdlo!".  
  
Write a program which takes as input a string _s_ and returns the snakestring of _s_.
  
## Examples
```
 Input: 'Python_is_fun!'
Output: 'yn_!Pto_sfnhiu'

 Input: 'White_Board'
Output: 'h_rWieBadto'
```
  
## Pythonic Solution
```python
def snake_string(s):
    return s[1::4] + s[::2] + s[3::4]
```
  
## Explanation
* BLANK
  
## Code Dissection
1. BLANK