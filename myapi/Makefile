.PHONY: build

FILE=./metadata.yml
VERSION = `cat $(FILE) | grep -i version | awk -F  ':' '{print $2}'`
DESC = `cat $(FILE) | grep -i Description | awk -F  ':' '{print $2}'`

build:
	 sed -i -e "s/VersionNumber/${VERSION}/g"  -e "s/VersionDescription/${DESC}/" -e "s/VersionCommit/${TRAVIS_COMMIT}/" myapp.py

