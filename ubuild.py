import os
import subprocess
from uranium import task_requires

ROOT = os.path.dirname(os.path.realpath("__file__"))
GITHUB_ACCOUNT = "yunstanford"
WEB_BRANCH = "patch-logging-refactor"

def main(build):
    build.packages.install(".", develop=True)
    # build.packages.install("git+https://github.com/channelcat/sanic.git#sanic")
    # build.packages.install("aiohttp")
    build.packages.install("pip")
    build.executables.run([
        "{0}/bin/pip".format(ROOT), "install",
        "https://github.com/{0}/sanic/tarball/{1}".format(GITHUB_ACCOUNT, WEB_BRANCH)
    ])


@task_requires("main")
def test(build):
    build.packages.install("pytest", version="==3.2.1")
    build.packages.install("pytest-cov")
    build.packages.install("sanic")
    # build.packages.uninstall("transmute-core")
    # build.packages.uninstall("sanic")
    # build.packages.install("aiohttp")
    # build.packages.install("git+https://github.com/channelcat/sanic.git#sanic")
    build.packages.install("pytest-sanic")
    # build.packages.install("pytest-flake8")
    # build.packages.install("pytest-aiohttp")
    build.packages.install("pymongo")
    build.packages.install("motor")
    build.packages.install("aioredis")
    build.packages.install("radon")
    build.executables.run([
        "pytest", "./tests",
        "--cov", "py_benchmarks",
        "--cov-report", "term-missing",
    ] + build.options.args)
