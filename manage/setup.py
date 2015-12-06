from setuptools import setup

setup_args = dict(
    name='Contestify',
    install_requires=[
        # web framework
        'Flask>=0.9',
        'Flask-Login>=0.2.7',
        'flask-mongoengine==0.7.0',
        'pymongo==2.8.0',
        'mongoengine==0.8.6',
        'Flask-WTF==0.12',
        'gunicorn==19.3.0'],

    entry_points=dict(
        console_scripts=[
            ],
    ),
)

if __name__ == '__main__':
    setup(**setup_args)
