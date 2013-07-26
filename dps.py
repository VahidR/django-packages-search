#!/usr/bin/env python
''' 
Copyright (C) 2013  Vahid Rafiei (@vahid_r)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


import requests
import simplejson
import optparse
import sys


class DPS(object):
	'''
	Class `DPS` is the main logic with some relevant methods. 
	'''

	def __init__(self):
		self._url = 'https://www.djangopackages.com/api/v1/'
		self._response = ''
		self._data = ''
		self._grids = ''
		

	def grid_list(self):
		'''
		Method `grid_list` is responsible for getting the main list of Grid names. 
		OBS. Apparently there is a bug in the main API that leads to fetching a partial list.
		I have opened an isue, and still waiting for a proper answer!
		Don't use this particular function until further notice..
		'''
		self._url = self._url +  'grid/'
		self._response = requests.get(self._url)
		self._data = simplejson.loads(self._response.content)
		self._grids = [item.get('absolute_url') for item in self._data.get('objects')]
		for grid_item in self._grids:
			print grid_item.rsplit('/', 2)[1]


	def process_grid(self, package_list):
		'''
		Method `process_grid` is responsible for representing the relevant list.
		It gets the name of the grid and returns the packages within that grid. 
		'''
		self._url =  self._url + 'grid/' + package_list
		self._response = requests.get(self._url)
		self._data = simplejson.loads(self._response.content)
		
		print 'Here is the list of packages: '
		for item in self._data.get('packages'):
			print item.rsplit('/', 2)[1]


	def process_package(self, package):
		'''
		Method `process_package` gets the package name as the input and 
		returns some useful information about the founded package.
		'''
		self._url = self._url + 'package/' + package
		self._response = requests.get(self._url)
		self._data = simplejson.loads(self._response.content)
		print 'Here is the detailed info about the package: '
		print 'Name: \t\t\t', self._data.get('title')
		print 'Description: \t\t', self._data.get('repo_description')
		print 'PyPI URL: \t\t', self._data.get('pypi_url')
		print 'Repository URL: \t', self._data.get('repo_url')
		print 'Repository forks: \t', self._data.get('repo_forks')
		print 'Repository watchers:\t', self._data.get('repo_watchers')
		print 'Last modified: \t\t', self._data.get('modified')[:10]



if __name__ == '__main__':
	
	help_message = "usage: python dps.py [options] arg"
	parser = optparse.OptionParser(help_message)
	parser.add_option('-l', '--list', dest='grid', help='listing packages among the favorite list')
	parser.add_option('-p', '--package', dest='package', help='getting the required information about the package')
	options, args = parser.parse_args()
	
	DPS = DPS()
	if options.grid:
		try:
			DPS.process_grid(options.grid)
		except:
			print "Sorry! I can't find such a list"
	
	if options.package:
		try:
			DPS.process_package(options.package)
		except:
			print "Sorry! I can't find this package.."
	
	
	try:
		if sys.argv[1] and sys.argv[1] == 'galaxy':
			DPS.grid_list()
	except:
		print help_message

