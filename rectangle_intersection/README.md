# Rectangle Intersection  
  
Problem:  
Write a program which tests if two rectangles have a nonempty intersection. If the intersection is nonempty, return the rectangle formed by their intersection.  

The Rectangle is defined by the parameters [x, y, width, height]. The (x, y) coordinate corresponds to the bottom-left corner of the rectangle.   
  
Examples:  
```
 Input: R1 = [36, 65, 69, 5]
        R2 = [99, 83, 99, 61]
Output: Rectangle(x=0, y=0, width=-1, height=-1)
Conclusion: No Intersection

 Input: R1 = [26, 12, 76, 62]
        R2 = [68, 59, 77, 28]
Output: Rectangle(x=68, y=59, width=34, height=15)
Conclusion: Nonempty Intersection

 Input: R1 = [17, 77, 58, 67]
        R2 = [5, 19, 32, 60]
Output: Rectangle(x=17, y=77, width=20, height=2)
Conclusion: Nonempty Intersection
```  
  
Solution - from [rectangle-intersection-mysol.py](rectangle-intersection-mysol.py):  
```python
def intersect_rectangle(R1, R2):
    # TODO - you fill in here.
    return Rectangle(0, 0, 0, 0)
```  
  
Explanation:   
  