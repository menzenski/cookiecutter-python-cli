"""
{{ cookiecutter.project_short_description }}
"""
import os
import os.path
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(here, '{{ cookiecutter.package_name }}', '__about__.py')) as about_file:
    exec(about_file.read(), about)

setup(
    name='{{ cookiecutter.pypi_name }}',
    version=about['__version__'],
    url=about['__version__'],
    license=about['__license__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    maintainer=about['__maintainer__'],
    maintainer_email=about['__maintainer_email__'],
    description=about['__description__'],
    long_description=__doc__,
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.script_name }} = {{ cookiecutter.package_name }}.cli:main',
        ],
    },
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    setup_requires=['pytest-runner'],
    tests_requires=['pytest'],
)
