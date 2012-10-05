from setuptools import setup, find_packages

#from https://github.com/cburgmer/pdfserver/blob/master/setup.py
def parse_requirements(file_name):
    requirements = []
    for line in open(file_name, 'r').read().split('\n'):
        if re.match(r'(\s*#)|(\s*$)', line):
            continue
        if re.match(r'\s*-e\s+', line):
            # TODO support version numbers
            requirements.append(re.sub(r'\s*-e\s+.*#egg=(.*)$', r'\1', line))
        elif re.match(r'\s*-f\s+', line):
            pass
        else:
            requirements.append(line)

    return requirements

def parse_dependency_links(file_name):
    dependency_links = []
    for line in open(file_name, 'r').read().split('\n'):
        if re.match(r'\s*-[ef]\s+', line):
            dependency_links.append(re.sub(r'\s*-[ef]\s+', '', line))

    return dependency_links


setup(
    name = "fabric-config",
    version = "0.1",
    packages = find_packages(),

    install_requires = parse_requirements('requirements.txt'),
    dependency_links = parse_dependency_links('requirements.txt'),


    # metadata for upload to PyPI
    author = "George Erickson",
    author_email = "george@kyruus.com",
    description = "Helper functions for fabric, based on a config file",
    keywords = "fabric django",
    url = "https://github.com/GeorgeErickson/fabric-config",
)