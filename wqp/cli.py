import click
from wqp import __version__

@click.group(name='wqp', help='Wine quality predictor - a packaged machine learning algorithm to predict wine quality')
@click.version_option(__version__)
def wqp():
    pass

