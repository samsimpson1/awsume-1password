from setuptools import setup

setup(
    name='awsume-onepassword-plugin',
    version='0.0.1',
    description='Fetches AWS access keys and MFA from 1Password',
    entry_points={
        'awsume': [
            'onepassword = onepassword'
        ]
    },
    author='Sam Simpson',
    author_email='pypi@sams.wtf',
    url='https://github.com/samsimpson1/awsume-onepassword-plugin',
    py_modules=['onepassword'],
)
