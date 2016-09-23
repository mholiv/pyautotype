from setuptools import setup

setup(name='pyautotype',
    version='0.1',
    description='Reads in a file and types it out simulating key presses',
    url='https://github.com/mholiv/pyautotype',
    author='Caitlin Campbell',
    author_email='',
    license='AGPL',
    packages=['pyautotype'],
    zip_safe=False,
    entry_points = {
    'console_scripts': ['pyautotype=pyautotype.pyautotype:main'],
    },
    install_requires=[
        'pyobjc',
        'pillow',
        'PyAutoGUI',
        'click'
    ],
    setup_requires= [
        'pyobjc-core',
    ]
    )
