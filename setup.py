# Copyright 2014 The University of Melbourne
#
# This file is part of Karaage-User.
#
# Karaage-User is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Karaage-User is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Karaage-User If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages
import ast

path = "kgterms/__init__.py"
with open(path, 'rU') as file:
    t = compile(file.read(), path, 'exec', ast.PyCF_ONLY_AST)
    for node in (n for n in t.body if isinstance(n, ast.Assign)):
        if len(node.targets) == 1:
            name = node.targets[0]
            if isinstance(name, ast.Name) and \
                    name.id in ('__version__', '__version_info__', 'VERSION'):
                v = node.value
                if isinstance(v, ast.Str):
                    version = v.s
                    break
                if isinstance(v, ast.Tuple):
                    r = []
                    for e in v.elts:
                        if isinstance(e, ast.Str):
                            r.append(e.s)
                        elif isinstance(e, ast.Num):
                            r.append(str(e.n))
                    version = '.'.join(r)
                    break

tests_require = [
    "mock",
]

setup(
    name="karaage-terms",
    version=version,
    url='https://github.com/NeCTAR-RC/karaage-terms',
    author='Russell Sim',
    author_email='russell.sim@unimelb.edu.au',
    description='Karaage user terms and conditions.',
    packages=find_packages(),
    license="GPL3+",
    include_package_data=True,
    tests_require=tests_require,
    extras_require={
        'tests': tests_require},
)
