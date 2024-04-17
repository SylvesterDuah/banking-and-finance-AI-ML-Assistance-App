from setuptools import setup, find_packages

setup(
    name='Finance_Advice',
    version='0.1',
    author='Sylvester Duah',
    author_email='duahsylvester24@gmail.com',
    description='A banking assistance application for managing and analyzing financial data.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/SylvesterDuah/banking-and-finance-AI-ML-Assistance-App.git',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.0.0',
        'numpy>=1.18.0',
        'scikit-learn>=0.22.0',
        'matplotlib>=3.1.0',
        'seaborn>=0.10.0',
    ],
    scripts=['path/to/app.py'], 
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Financial and Insurance Industry',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License', 
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.6',
    include_package_data=True,
)
