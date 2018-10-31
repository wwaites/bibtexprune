import argparse
import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
from sys import stdout
import re

def _citations(auxfile):
    cite = re.compile(r'^\\citation{(.*)}$')
    with open(auxfile) as fp:
        for line in fp.readlines():
            m = cite.match(line)
            if m is None: continue
            citations, = m.groups()
            for citation in citations.split(","):
                yield citation 
def citations(auxfile):
    return list(set(_citations(auxfile)))

def main():
    parser = argparse.ArgumentParser(prog='bibtexprune')
    parser.add_argument('auxfile', help='.aux file generated by latex')
    parser.add_argument('bibfile', help='full bibliography')
    parser.add_argument('outfile', help='pruned bibliography')

    args = parser.parse_args()

    with open(args.bibfile) as bibfile:
        full = bibtexparser.load(bibfile)

    pruned = BibDatabase()
    pruned.entries = []

    for citation in citations(args.auxfile):
        entry = list(e for e in full.entries if e["ID"] == citation)
        if len(entry) == 0:
            pruned.commends.append("%s not found in full database" % citation)
        elif len(entry) == 1:
            pruned.entries.append(entry[0])
        else:
            raise ValueError("multiple entries for %s" % citation)

    writer = BibTexWriter()
    with open(args.outfile, "w") as fp:
        fp.write(writer.write(pruned))
