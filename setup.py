from setuptools import setup

# Extract version
def get_version():
    with open('gwdet/gwdet.py') as f:
        for line in f.readlines():
            if "__version__" in line:
                return line.split('"')[1]

setup(
    name='gwdet3',
    version=get_version(),
    description='Fork of gwdet - Detectability of gravitational-wave signals from compact binary coalescences',
    long_description="For original description, see: `github.com/dgerosa/gwdet <https://github.com/dgerosa/gwdet>`_." ,
    classifiers=[
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='gravitational-wave, black-hole binary',
    url='https://github.com/dgerosa/gwdet',
    author='Davide Gerosa',
    author_email='dgerosa@caltech.edu',
    license='MIT',
    packages=['gwdet'],
    install_requires=['numpy','scipy','scipy','matplotlib','astropy','pathos','requests'],
    include_package_data=True,
    zip_safe=False,
)