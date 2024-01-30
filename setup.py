import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='instacart-api',
    version='1.0.0',
    author='Ryan Morlando',
    author_email='ryan@dayonedigital.com',
    description='Instacart API access',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Ryan-dayone/instacart-api',
    license='MIT',
    packages=['instacart_api'],
    install_requires=['requests', 'pandas', 'numpy'],
)