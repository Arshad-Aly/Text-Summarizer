import setuptools

with open("README.md", "r", encoding="utf-8") as f: ## To publish as PYPI package, add a README.md file
    long_description = f.read()

__version__= "0.0.0"

REPO_NAME = 'Text-Summarizer'
AUTHOR_USER_NAME = 'Arshad-Aly'
SRC_REPO = 'TextSummarizer'
AUTHOR_EMAIL = 'syedarshadali188@gmail.com'


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Python package for text summarization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)