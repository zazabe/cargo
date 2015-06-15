# -*- encoding: utf-8 -*-

import click
from functools import update_wrapper


def pass_people(f):
    @click.pass_context
    def new_func(ctx, *args, **kwargs):
        return ctx.invoke(f, ctx.obj['people'], *args, **kwargs)
    return update_wrapper(new_func, f)
