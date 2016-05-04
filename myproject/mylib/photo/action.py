print '__name__:', __name__
# You cannot directly execute this script.
# Use this script as a module, a library element.
# So if you want to test this module, use a kind of testing method to do it.

# import the same python module inside the same directory
import libofphoto
# import the same python module inside the same directory
# we call a dot as 'father', so . means father, .. means father's father
from . import libofphoto2
# go to father's father, until we land in 'mylib' package, then find the son of it, 'user' package
from .. import user
# go to father's father, until we land in 'mylib' package, then find the son package 'user', inside it, module 'libofuser'
from ..user import libofuser 
# But: from .. import user.libofuser is wrong expression, wrong syntax.