bri@extrahops.com
Bri Hatch

bri@ifokr.org, personal email

_internal_method_or_data
__double_underscore_means_it_is_private
__python_builtins__

pep8 styleguide, google style guide
False, True, None (capitals)

***no ++ ***

print r'http://github.com' -- prints without needing escaping
 dir(object) will return a list of all operations allowed on that object

print foo.get('key_that_doesn't_exist')
returns None

print foo.get('key_that_doesn't_exist', 'default_value')
returns default_value

foo.extend(will take the string you put in here and split into characters and push them onto the existing list)

def diehorribly():
  """anything you put here at the very top will help document automagically"""
  sys.exit(2)

print diehorribly.__doc__
    will print out your doc string up above

ipython go-to choice for interpreter


def my_method(arg1, arg2="default_for_2", arg3="default_for_3"):
    """Print the args that were sent"""
    print 'You send %s/%s/%s' % (arg1, arg2, arg3)

def argfunc (arg1, *mylist):
    """Print the args you get"""
    print 'You sent %s and "%s" % (arg, ','.join(mylist))

def newfunc(arg1, foo=None, *args, **kwargs)

newfunc(100, 12, "about", "now", "pete"="seager")

DON"T USE TABS

python is 4 spaces

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print [x in xin nums if x % 2 == 0]
[0, 2, 4, 6]

pylint and pychecker are great tools

