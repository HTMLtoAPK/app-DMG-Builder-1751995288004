
import certifi
from setuptools import setup

# The app is now the LAUNCHER script
APP = ['launcher.py']

# We bundle the user's script AND the SSL certs as data files
DATA_FILES = [
    ('', ['app.py']),
    ('', [certifi.where()])
]

OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'icon.icns',
    'includes': ["tkinter","certifi","psutil"],
    'plist': {
        'CFBundleName': 'app',
        'CFBundleDisplayName': 'app',
        'CFBundleIdentifier': 'com.htmltoapk.app',
        'CFBundleVersion': '0.1.0',
        'CFBundleShortVersionString': '0.1.0',
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)
