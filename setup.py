from setuptools import setup

setup(
    name='ambient_api',
    version='1.0.3',
    packages=['ambient_api'],
    url='https://github.com/avryhof/ambient_api',
    license='MIT',
    author='Amos Vryhof',
    author_email='amos@vryhofresearch.com',
    description='A Python class for accessing the Ambient Weather API.',
    classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3'
      ],
    install_requires=[
        "requests",
        "urllib3",
    ],
)
