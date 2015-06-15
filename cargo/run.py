# -*- encoding: utf-8 -*-

from cargo.command.main import cargo as cli

import cargo.command.social

# import commands
# avoid IDE warning and ensure module availablility
assert cargo.command.social

# used for debugging
if __name__ == '__main__':
    cli(obj={})
