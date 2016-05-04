print '__name__:',__name__

import mylib.photo.action
# If you are now inside '/myproject' folder and tries to execute 'python myapp.py'
# The output is like this:
#
# __name__: __main__
# >> in mylib package
# >> in photo package
# __name__: mylib.photo.action
# __name__: mylib.photo.libofphoto
# __name__: mylib.photo.libofphoto2
# >> in user package
# __name__: mylib.user.libofuser
# __name__: mylib.photo.testaction

import mylib.photo.testaction
# Since all the modules needed are imported,
# Python will not import them again.
# So the import of 'testaction.py' will simply import
# __name__: mylib.photo.testaction
