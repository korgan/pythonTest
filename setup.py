import sys
from setuptools import setup

try:
    from semantic_release import setup_hook
    setup_hook(sys.argv)
except ImportError:
    message = "Unable to locate 'semantic_release', releasing won't work"
    print(message, file=sys.stderr)


version = '1.0.0'


install_requires = [
    'requests',
]


tests_require = [
    'pytest-runner',
    'pytest',
    'pylama',
    'responses',
    'mock',
    'coveralls',
    'pytest-cov',
]
release_requires = [
    'python-semantic-release',
]

setup(
   name='pythontest',
   version=version,
   description='Python Travis Heroku Test',
   long_description=open('README.md').read(),
   author='Nicolas Brieger',
   author_email='git@xtmp.de',
   py_modules=('fiobank',),
   install_requires=install_requires,
   tests_require=tests_require,
   extras_require={
       'tests': tests_require,
       'release': release_requires,
    }
)
