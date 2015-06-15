# -*- encoding: utf-8 -*-

import json
import logging
import click

from cargo.command.main import cargo as cli
from cargo.click import pass_people


@cli.group()
@click.argument('data', type=click.File('r'))
@click.pass_context
def social(ctx, data):
    """
    Social related command
    """
    ctx.obj['people'].load(json.load(data))


@social.command()
@click.argument('person_id', type=int)
@pass_people
def direct(people, person_id):
    """
    Retrieve direct friends for a specific user
    """
    log = logging.getLogger('social')

    person = people.get(person_id)
    friends = people.friends_of(person_id)

    log.info('%s friend(s) found for %s', len(friends), person.fullname())
    for friend in friends:
        log.info('- %s', friend.fullname())


@social.command()
@click.argument('person_id', type=int)
@click.option('--steps', '-s', default=2, type=int,
              help="Number of steps to reach the person")
@pass_people
def steps(people, person_id, steps):
    """
    Retrieve people separated with a number of steps from a person
    """
    log = logging.getLogger('social')

    person = people.get(person_id)
    relation = person.friends_level(steps)

    log.info('%s relation with %s steps for %s',
             len(relation), steps, person.fullname())
    for person in relation:
        log.info('- %s', person.fullname())


@social.command()
@click.argument('person_id', type=int)
@pass_people
def suggest(people, person_id):
    """
    Retrieve people not friends but with at least 2 common friends
    """
    log = logging.getLogger('social')

    person = people.get(person_id)
    suggestion = people.suggestion(person_id)

    log.info('%s friend(s) suggestion for %s',
             len(suggestion), person.fullname())
    for person in suggestion:
        log.info('- %s', person.fullname())
