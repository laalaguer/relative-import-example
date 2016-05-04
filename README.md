# Python Relative Import
Discuss the question about 'relative import' in python.

## Question
Very simple folder structure represents a common problem in daily programming. How do I import a 'sibling project' as foundation library when I am developing several new libraries? Except from copy-paste the foundation library into every new library (as a child folder), using `relative import` feature in python gives me a convenient way.

## Typical Folder Structure
```
/myproject
  
  myapp.py
  
  /mylib
    __init__.py
    
    /user
      __init__.py
      action.py
      libofuser.py
    
    /photo
      __init__.py
      action.py
      libofphoto.py
      libofphoto2.py
      testaction.py
    
```

## Explain
`myapp.py` is the actual running script of your application. `/user` folder is the foundation library that every other custom library wants to refer. So `/photo` library needs some function/module inside `/user` package. But `/photo` and `/user` are siblings, so if any module inside `/photo` wants to refer to any thing inside `/user`, it needs `relative import` feature in Python since 2.5

## Details
See the code of `/photo/action.py`, `/photo/testaction.py` and `myapp.py` for details.

## Thanks
Inspired by two questions and explanation

1. [https://docs.python.org/2.5/whatsnew/pep-328.html](https://docs.python.org/2.5/whatsnew/pep-328.html)
2. [http://stackoverflow.com/questions/14132789/python-relative-imports-for-the-billionth-time](http://stackoverflow.com/questions/14132789/python-relative-imports-for-the-billionth-time)
