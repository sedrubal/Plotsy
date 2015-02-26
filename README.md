Plotsy
======

ASCII plotting module for python

Files:
------
 - [plotsy.py](plotsy.py) - the actual module
 - [plotsy_color.py](plotsy_color.py) - colors
 - [plotsy_example.py](plotsy_example.py) - an example
 - [__init__.py](__init__.py) - for using this as a library

Documentation
-------------

See the [example](plotsy_example.py) and the documentation comments in [plotsy.py](plotsy.py)

Example Plot
------------

This is a black and white output of [plotsy_example.py](plotsy_example.py). It might be a bit confusing. Please inspect the script anyway. It's quite simple ;)

```bash

example 1: Print Chaos
----------------------

––––––––––––––––––––––––––––––
|                            |
|                            |
|   +–––––––––––+            |
|   |HELLO WORLD|            |
|   +–––––––––––+            |
|                            |
|                            |
|                            |
|                            |
|                            |
| supported colors:          |
| fffffffffffffffff          |
| bbbbbbbbbbbbbbbbb    max=15|
|––––––––––––––––––––––––––––|
|   1311. .                  |
|  1.1..   12                |
| 1. .     .    11           |
|1.         10 1.            |
|.          .99. 9           |
|  x         ..  .           |
|                 77         |
|                 ..6x       |
|                   .5x      |
|                    . x @   |
| x             @     33x    |
|        @            .. x   |
|   @                   1 x  |
|x                      .0000|
–––––––––––––––––––––––––....–

example 2: Plot a sqrt function
-------------------------------

^sqrt(x)                                                                                                                                                           x
|                                                                                                                                        xxxxxxxxxxxxxxxxxxxxxxxxxx 
–14.0                                                                                                            xxxxxxxxxxxxxxxxxxxxxxxx                           
|                                                                                           xxxxxxxxxxxxxxxxxxxxx                                                   
–11.0                                                                   xxxxxxxxxxxxxxxxxxxx                                                                        
|                                                      xxxxxxxxxxxxxxxxxx                                                                                           
–9.0                                     xxxxxxxxxxxxxx                                                                                                             
|                           xxxxxxxxxxxxx                                                                                                                           
–6.0              xxxxxxxxxxx                                                                                                                                       
|         xxxxxxxx                                                                                                                                                  
–3.0xxxxxx                                                                                                                                                          
|xxx  12.0    25.0    37.0    49.0    61.0    74.0    86.0    98.0    111.0   123.0   135.0   148.0   160.0   172.0   184.0   197.0   209.0   221.0   234.0   246.0x
x–––––––|–––––––|–––––––|–––––––|–––––––|–––––––|–––––––|–––––––|–––––––|–––––––|–––––––|–––––––|–––––––|–––––––|–––––––|–––––––|–––––––|–––––––|–––––––|–––––––|––>
```

Contribute
----------

If you find a bug or can make a small change to make the module better, please fork this repo and commit your idea!

License
-------

[MIT](LICENSE.md)
