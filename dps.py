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


def process_grid(package_list):
	'''
	Function `process_grid` is responsible for representing the relevant list.
	It gets the name of the grid and returns the packages within that grid. 
	'''
	url = 'https://www.djangopackages.com/api/v1/grid/' + package_list
	response = requests.get(url)
	data = simplejson.loads(response.content)
	
	for item in data.get('packages'):
		print item.rsplit('/', 2)[1]


def process_package(package):
	'''
	Function `process_package` gets the package name as the input and 
	returns some useful information about the founded package.
	'''
	url = 'https://www.djangopackages.com/api/v1/package/' + package
	response = requests.get(url)
	data = simplejson.loads(response.content)
	print 'Package: \t', data.get('title')
	print 'Description: \t', data.get('repo_description')
	print 'PyPI URL: \t', data.get('pypi_url')
	print 'Repository URL: ', data.get('repo_url')
	print 'PyPI downloads: ', data.get('pypi_downloads')
	print 'Last modified: ', data.get('modified')[:10]



if __name__ == '__main__':
	parser = optparse.OptionParser()
	parser.add_option('-l', '--list', dest='grid', help='listing packages among the favorite list')
	parser.add_option('-p', '--package', dest='package', help='getting the required information about the package')
	options, args = parser.parse_args()
	if options.grid:
		try:
			process_grid(options.grid)
		except:
			print "Sorry! I can't find such a list"
	if options.package:
		try:
			process_package(options.package)
		except:
			print "Sorry! I can't find this package.."


