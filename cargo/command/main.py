# -*- encoding: utf-8 -*-

import click
import logging

from cargo.data import People
from cargo import __version__


@click.group()
@click.version_option(version=__version__)
@click.option('--debug', default=False, is_flag=True,
              help="enable debugging")
@click.pass_context
def cargo(ctx, debug):
    """
    Cargo global command
    """
    level = debug and logging.DEBUG or logging.INFO
    logging.basicConfig(level=level)

    ctx.obj = {
        'people': People()
    }
