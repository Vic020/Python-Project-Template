# -*- encoding: utf-8 -*-

import os
import logging
import logging.config
import json

import click


def read_config(ctx, param, value):
    if not value:
        return {}

    def underline_dict(d):
        if not isinstance(d, dict):
            return d
        return dict((k.replace('-', '_'), underline_dict(v)) for k, v in d.items())

    config = underline_dict(json.load(value))
    ctx.default_map = config
    return config


@click.group()
@click.option('-c', '--config', default=os.path.join(os.path.dirname(__file__), "config.json"), callback=read_config,
              type=click.File('r'), help="config file, support json file")
@click.option('--logging-config', default=os.path.join(os.path.dirname(__file__), "logging.conf"),
              help="logging config file for built-in python logging module", show_default=True)
@click.pass_context
def cli(ctx, **kwargs):
    logging_config = kwargs.pop('logging_config')
    logging.config.fileConfig(logging_config)
    config = kwargs.pop('config')
    kwargs.update(config)
    ctx.obj = kwargs
    return ctx


@cli.command()
@click.pass_context
def Web(ctx):
    from Project.webserver import WebServer
    g = ctx.obj
    g['logger'] = 'webserver'
    webserver = WebServer(**g)
    webserver.run()


if __name__ == '__main__':
    cli()