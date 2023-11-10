import nox

locations = "src", "noxfile.py"


@nox.session(python=["3.10.4"])
def tests(session):
    args = session.posargs or ["--cov"]
    session.run("poetry", "install", external=True)
    session.run("pytest", *args)


@nox.session(python=["3.10.4"])
def format(session):
    args = session.posargs or locations
    session.run("poetry", "install", external=True)
    session.run("black", *args)


@nox.session(python=["3.10.4"])
def lint(session):
    args = session.posargs or locations
    session.run("poetry", "install", external=True)
    session.run("flake8", *args)


@nox.session(python=["3.10.4"])
def mypy(session):
    args = session.posargs or locations
    session.run("poetry", "install", external=True)
    session.run("mypy", *args)
