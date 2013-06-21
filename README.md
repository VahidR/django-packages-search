django-packages-search
=====================

A command line tool for searching within djangopackages.com

Introduction
------------
Imagine that you are in the middle of a project, and would like to search for a third-party django app that suits your
current need. You live in Terminal and do all of your stuff within your favorite editor like Vim or Emacs. 
one way to search for such apps is to fire your web browser and visit `djangopackages.com` and browse the packages 
comprehensively. Another way is using this tool. You can search for a *list* of packages within a certain area like
`cms` and `profiles`, or you can get the vital information about a *specific* package. The details come later.
This tool is under active development and lots of improvements could be added gradually..


How to use it
-------------
Let's imagine that we would like to see what packages are available in a *grid* of `profiles`. 
We have heard that there is a package called `django-profiles`, but we want to see all of the apps that people has created.
Within the terminal, enter this :
```bash
$ python dps.py -l profiles
or
$ python dps.py --list=profiles
```
Oh... we have lots of apps:
```
django-easy-profiles
django-modeltranslation
django-primate
django-profile
django-profilebase
django-profiles
django-profiletools
django-userena
django-userprofiles
idios
pinax
```

Now, let's get some information about one of those packages:

```bash
$ python dps.py -p django-userena
or
$ python dps.py --package=django-userena
```
Here is the result for such searching:
```bash
Package:      django-userena
Description: 	Accounts for Django made beautifully simple
PyPI URL: 	  http://pypi.python.org/pypi/django-userena/
Repository URL:  https://github.com/bread-and-pepper/django-userena
PyPI downloads:  27525
Last modified:  2013-06-21
```
