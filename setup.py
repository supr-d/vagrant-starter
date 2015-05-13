from setuptools import setup

APP = ['app.py']
DATA_FILES = ['ui/app.ui']
OPTIONS = {
    'argv_emulation': True,
    'includes': ['sip', 'PyQt4']
}

setup(
    app=APP,
    data_files=DATA_FILES,
    py_modules=['workers'],
    options={
        'py2app': OPTIONS
    },
    setup_requires=['py2app']
)