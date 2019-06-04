# Knapsack-memes
Knapsack-memes help you earn more money in dark times. When memes are illegal.

## General info
Function `calculate` in main.py, solve knapsack problem wich set of memes should we save on USB stick, that we can sell it for the highest price. Pendrive is represented by capacity in GiB. 

Every meme has:
* name
* size in MiB
* market price  

Computation is based on [Google OR-Tools](https://developers.google.com/optimization/). The package is written in C++, so the script is faster than the normal implementation in Python. 
  
Solver use Branch and Bound algorithm which in more cases are the most efficient and return optimum value. There where few cases when Dynamic Programming solver works better. Everything depends on a number of items, weights, values and capacity of storage. Some algorithm are more efficient, but return local optimum (sometimes is better to calculate approximately, but in this decade).


Example of use:
```python
>>>from main import calculate
>>>
>>>
>>>usb_size = 1     # capacity in GiB, non negative integer
>>>memes = [
>>>     ('roolsafe.jpg', 205, 6),    # (name, capacity in MiB, value)
>>>     ('sad_pepe_compilation.gif', 410, 10),
>>>     ('yodeling_kid.avi', 605, 12)
>>>       ]
>>>    
>>>calculate(usb_size, memes)   # Return (max price, {set of memes})
(22, {'yodeling_kid.avi', 'sad_pepe_compilation.gif'})
```  

If some meme name apears more than once function raise error. Because returned set of memes always has unique items, so is hard to guess wich memes we have to sell. There is not enough information. 

## Requirements
Python 3.7.2 (should work on 3.5+)

Packages:
* ortools==7.1.6722
* protobuf==3.8.0
* six==1.12.0
