"""
=============
 Hello World
=============


This is a test.
"""

def HelloWorld(first, arg=0):
 """

 A dummy function.

 :param str first: A dummy parameter
 :param int arg: A dummy argument.
 :return: None
 """
 return None

def NumpyWorld(param, arg=0):
 """A dummy function

 Parameters
 ----------
 param : str
     A dummy parameter.
 arg : int
     A dummy argument.

 Returns
 -------
 None
 """
 return None

"""
So I have Kite installed but whatever is automatically creating
docstrings for my code is creating reStructured Text style docstrings
as opposed to Google or Numpy styles.

Figured this out! I needed to go to the settings (under Preferences on a Mac)
and under Tools find Python Integrated Tools where I can change the Docstring
format to any one of five different styles.
"""
