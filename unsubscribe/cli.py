import click
import re
import webbrowser
import subprocess
import requests
from os import path
from concurrent import futures
from tqdm import tqdm
from .utils import collect_mails
from .patterns import UNSUBSCRIBE_PATTERNS

MAIL_DIR = path.join(path.expanduser('~'), 'Library/Mail/V3/')
pool = futures.ProcessPoolExecutor()


@click.command()
@click.option(
    '--auto/--no-auto',
    default=False,
    help='automatically unsubscribe from everything'
)
@click.option(
    '--view/--no-view',
    default=False,
    help='open email in Apple Mail'
)
@click.option(
    '--browse/--no-browse',
    default=False,
    help='open unsubscribe page in the browser'

)
def main(auto, view, browse):
    mails = tqdm(collect_mails(MAIL_DIR), unit=' mails')
    for mail in mails:
        with open(mail, 'r', encoding='utf-8', errors='ignore') as mailfile:
                content = mailfile.read()
                for pattern in UNSUBSCRIBE_PATTERNS:
                    match = re.search(pattern, content, re.IGNORECASE)
                    if match:
                        if auto:
                            pool.submit(requests.get, match.group(1))
                        if view:
                            subprocess.call(("open", mail))
                        if browse:
                            webbrowser.open(match.group(1))
                        continue


if __name__ == '__main__':
    main()
