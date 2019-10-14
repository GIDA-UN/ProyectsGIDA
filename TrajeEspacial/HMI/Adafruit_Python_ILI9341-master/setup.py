# Workaround for issue in Python 2.7.3
# See http://bugs.python.org/issue15881#msg170215
try:
    import multiprocessing
except ImportError:
    pass

try:
    # Try using ez_setup to install setuptools if not already installed.
    from ez_setup import use_setuptools
    use_setuptools()
except ImportError:
    # Ignore import error and assume Python 3 which already has setuptools.
    pass

from setuptools import setup, find_packages


classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: System :: Hardware']

setup(name              = 'Adafruit_ILI9341',
      version           = '1.5.1',
      author            = 'Tony DiCola',
      author_email      = 'tdicola@adafruit.com',
      description       = 'Library to control an ILI9341 TFT LCD display.',
      license           = 'MIT',
      classifiers       = classifiers,
      url               = 'https://github.com/adafruit/Adafruit_Python_ILI9341/',
      dependency_links  = ['https://github.com/adafruit/Adafruit_Python_GPIO/tarball/master#egg=Adafruit-GPIO-0.6.5'],
      install_requires  = ['Adafruit-GPIO>=0.6.5'],
      packages          = find_packages())
