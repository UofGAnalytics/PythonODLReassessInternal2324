
Installing the Package
========================

To install this package you can use `pip`, if you wish to use an alternative
package installation method then please adjust the commands appropriately, but
we cannot provide support for all package managers/installation methods. 

We can install the package using the following command using ssh::

     pip install git+ssh://git@github.com/UofGAnalytics/PythonODLReassessInternal2324

You can also install via https using the following command::

     pip install git+https://github.com/UofGAnalytics/PythonODLReassessInternal2324


In a terminal window for your current version of python. Note this will
install/update all of the dependencies of our package. You can see the
dependences on `this page`_.

.. _this page: https://github.com/UofGAnalytics/PythonODLReassessInternal2324/blob/main/pyproject.toml

It is likely that many of the routines will work with earlier versions of these
libraries but installing this is more advanced than the installation proposed here.  
If you wish to do this we unfortunately cannot support all possible python installations, and therefore it is your responsibility to make sure that the package has been well installed. 

If you are in a Colab/Jupyter you can use an `!` in front of the command in the
first cell which will install the package.

If you are working with conda or virtualenv or otherwise you may wish to make a
new environment for this project to avoid having our assessment library in your
standard install. 

Although it might be worth exploring installing packages yourself if you have
not done this before in Python. 

