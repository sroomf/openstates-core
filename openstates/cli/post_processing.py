import click
import json
import os
import sys



@click.group()
def main():
    pass

@main.command(help="run specified post processes on raw data")
@click.argument("state")
@click.option('--post-process-type',
              type=click.Choice(['clean-whitespace', 'classify-actions'], case_sensitive=False), required=True, multiple=True)
@click.option("--session", default=None)
def post_process(state,post_process_type,session):
    #gets the data for that state and that session

    # TODO (this is a placeholder until we can interface with scraped bills)
    # use the filepath to your _data directory
    fp = "../../../openstates-scrapers/_data/" + state.lower()

    for filename in os.listdir(fp):
        this_bill = os.path.join(fp, filename)
        bill_loaded = open(this_bill)
        data = json.load(bill_loaded)

        if "clean-whitespace" in post_process_type:
            clean_whitespace(data)

        '''
        if "actions" in data:
            for action in data["actions"]:
                if "classify-actions" in post_process_type:
                    action["classification"] = classify_actions(action, state)
        '''
        if session:
            click.echo(session)
    pass


def clean_whitespace(_data):
    click.echo('initialized whitespace cleaning')
    click.echo('finished whitespace cleaning')





def classify_actions(_data,state):
    click.echo('initialized action classification')
    '''
    fp = "../../../openstates-scrapers/scrapers"
    sys.path.append(fp)
    sys.path.append("../../../openstates-core/")
    sys.path.append("../../../")
    from ak import actions
    '''
    '''
    action, classification = clean_action(_data['actions'])
    return classification
    '''


if __name__ == '__main__':
    main()

