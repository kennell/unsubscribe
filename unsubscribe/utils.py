from os import path
try:
    from os import scandir
except ImportError:
    from scandir import scandir


def scantree(path):
    for entry in scandir(path):
        if entry.is_dir():
            yield from scantree(entry.path)
        else:
            yield entry


def collect_mails(dir):
    mails = []
    for f in scantree(dir):
        if f.is_file and f.name.endswith('.emlx'):
            mails.append(f.path)
    return mails