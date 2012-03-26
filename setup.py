from setuptools import setup, find_packages
import sys

readme_file = 'README.mkd'
try:
    long_description = open(readme_file).read()
except IOError, err:
    sys.stderr.write("[ERROR] Cannot find file specified as "
        "``long_description`` (%s)\n" % readme_file)
    sys.exit(1)

setup(name='bootstrap-breadcrumbs',
      version=0.1,
      description='Bootstrap breadcrumbs for django',
      long_description=long_description,
      zip_safe=False,
      author='Rich Atkinson',
      author_email='rich@piran.com.au',
      url='https://github.com/piran/bootstrap-breadcrumbs',
      download_url='https://github.com/piran/bootstrap-breadcrumbs/downloads',
      packages = find_packages(exclude=['demo_project', 'demo_project.*']),
      include_package_data=True,
      install_requires = [
        'Django>=1.2.1',
      ],
      classifiers = ['Development Status :: 4 - Beta',
                     'Environment :: Web Environment',
                     'Framework :: Django',
                     'Intended Audience :: Developers',
                     'License :: OSI Approved :: BSD License',
                     'Operating System :: OS Independent',
                     'Programming Language :: Python',
                     'Topic :: Utilities'],
      )

