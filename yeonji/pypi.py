import setuptools
import importlib
import sys
import os
import shutil
import glob
from doreah.control import mainfunction

@mainfunction({},shield=True)
def main(packagename,test=False):

	assert os.path.exists(packagename)
	sys.argv = (sys.argv[0],"sdist","bdist_wheel")

	# use local package!
	sys.path.insert(0,".")

	pkginfo = importlib.import_module(".__pkginfo__",package=packagename)
	pkginfo = pkginfo.__dict__
	print(pkginfo)


	# extract info

	readmelocs = [
		packagename + "/README.md",
		"README.md"
	]

	for rml in readmelocs:
		if os.path.exists(rml):
			with open(rml, "r") as fh:
			    long_description = fh.read()
			break

	setuptools.setup(
	    name=pkginfo.get("links",{}).get("pypi") or pkginfo["name"],
	    version=".".join(str(n) for n in pkginfo["version"]),
	    author=pkginfo["author"]["name"],
	    author_email=pkginfo["author"]["email"],
	    description=pkginfo["desc"],
		license=pkginfo.get("license") or "GPLv3",
	    long_description=long_description,
	    long_description_content_type="text/markdown",
	    url="https://github.com/" + pkginfo["author"]["github"] + "/" + (pkginfo.get("links",{}).get("github") or pkginfo.get("name")),
	    packages=[packagename],
	    classifiers=[
	        "Programming Language :: Python :: 3",
	        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
	        "Operating System :: OS Independent",
	    ],
		python_requires=pkginfo.get("python_version"),
		install_requires=pkginfo.get("requires",[]),
		package_data={'': pkginfo.get("resources",[])},
		include_package_data=True,
		entry_points = {
			"console_scripts":[
				cmd + " = " + pkginfo["name"] + "." + pkginfo["commands"][cmd]
				for cmd in pkginfo.get("commands",[])
			],
			**{k:pkginfo["entrypoints"][k] for k in pkginfo.get("entrypoints",{})}
		}
	)


	os.system("git tag v" + ".".join(str(n) for n in pkginfo["version"]))

	uploadcmd = "python3 -m twine upload --skip-existing dist/*"
	if test:
		uploadcmd += " --repository-url https://test.pypi.org/legacy/"
	os.system(uploadcmd)

	shutil.rmtree("build")
	shutil.rmtree("dist")
	for d in glob.glob("*.egg-info"):
		shutil.rmtree(d)
