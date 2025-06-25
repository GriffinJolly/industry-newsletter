from setuptools import setup, find_packages

setup(
    name="newsletter_generator",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'streamlit',
        'python-pptx',
        'pyyaml',
        'requests',
    ],
    python_requires='>=3.7',
)
