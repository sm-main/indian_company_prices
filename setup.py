from setuptools import setup, find_packages

setup(
        name='indian_company_prices',
        versions='0.1',
        scripts=['indian_company_price'],
        description='Function to get eod pricing data of all indian companies',
        author='Sumant Mann',
        author_email='sumantmann@yahoo.com',
        url='https://github.com/sumantmann/indian_company_prices',
        download_url='https://github.com/sumantmann/indian_company_prices/tarball/0.1',
        keywords=['Finance', 'Indian Company Pricing'],
        classifiers=['Development Status :: 3 - Alpha', 'Programming Language :: Python'],
#        packages=find_packages(exclude=['bs4', 'html5lib']),
        install_requires=['bs4', 'html5lib'],
        entry_points={
                'console_scripts': [
                            'indian_company_prices=indian_company_prices:indian_company_prices',
                                    ],
                },
)
