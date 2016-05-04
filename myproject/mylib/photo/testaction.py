print '__name__:', __name__

import action
# If you go back to top directory /myproject, and execute command 'python -m mylib.photo.testaction'
# things go well as the output will be:
# >> in mylib package
# >> in photo package
# __name__: __main__
# __name__: mylib.photo.action
# __name__: mylib.photo.libofphoto
# __name__: mylib.photo.libofphoto2
# >> in user package
# __name__: mylib.user.libofuser
#
# What happens?
# Python interpreter now starts to find all the modules/package on the way inside /test folder where
# we type the command 'python'. It will try to find out mylib/photo/testaction.py as we instructed by 
# command line 'python -m mylib.photo.testaction'
# Ok, it will import and recognize all the package on the way down sub folders till 'testaction.py'.
# So you see:
# >> in mylib package
# >> in photo package
# Ok, as we are executing 'testaction.py' directly, then it is renamed as '__main__'
# So you see:
# __name__: __main__
# Then Python interpreter find out a statement 'import action' inside 'testaction.py', it will start to import a module 'action'
# on the same level as the 'testaction.py', which happens to be the file 'action.py'. It takes in this file and start
# to execute it. It hits the first line in 'action.py' as `print '__name__:', __name__`
# So you see:
# __name__: mylib.photo.action
# Ok, then inside 'action.py', are some other lines of execution, python starts to execute them one by one
# These relateive imports demanded by the 'action.py' is totally up to the intention of 'action.py', it imports
# module on the same level, and even from father's father level and import from other packages:
# So you see:
# __name__: mylib.photo.libofphoto
# __name__: mylib.photo.libofphoto2
# >> in user package
# __name__: mylib.user.libofuser

# However:
# If you change into this directory /myproject/mylib/photo
# and execute the command 'python testaction.py'
# Then things go wrong, out put is:
# __name__: __main__
# __name__: action
# __name__: libofphoto
# Traceback (most recent call last):
#   File "testaction.py", line 3, in <module>
#     import action
#   File "/Users/Jefferson/test/mylib/photo/action.py", line 9, in <module>
#     from . import libofphoto2
# ValueError: Attempted relative import in non-package
#
# What happens?
# Ok, as we are executing 'testaction.py' directly by 'python testaction.py', then 'testaction.py' is renamed as '__main__'
# Now when 'testaction.py' tries to 'import action', python finds the file 'action.py' on the same level, import it.
# But now the module name is simply 'action' not 'mylib.photo.action', it lost all the dots. It becomes naked.
# So if you try to refer to the father level of 'action.py', it will pop through the roof and referes to nothing.
