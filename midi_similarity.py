import rdflib, csv , sys , os , hashlib , midi
from rdflib import Graph, Namespace, RDF, Literal, URIRef
from rdflib.namespace import SKOS
from werkzeug.urls import url_fix

# MD5 to identify the input MIDI file
filename = sys.argv[1]
md5_id = hashlib.md5(open('data/'+filename, 'rb').read()).hexdigest()

# Namespaces
midi_r = Namespace("http://purl.org/midi-ld/")
midi = Namespace("http://purl.org/midi-ld/midi#")
m_uri = URIRef(url_fix("http://purl.org/midi-ld/pattern/"))
m = Namespace(m_uri)

piece = m[md5_id]

# initialize rdf graph
g = Graph()
g.bind('midi-r', midi_r)
g.bind('midi', midi)

# open match.tsv 
with open('match.tsv','rb') as tsvin:
    tsvin = csv.reader(tsvin, delimiter='\t')
    for row in tsvin:

    	# generate MD5 for each MIDI
    	matchMIDIname = str('data/'+row[0].strip())
    	matchPiece_md5_id = hashlib.md5(open(matchMIDIname, 'rb').read()).hexdigest()
    	matchPiece = m[matchPiece_md5_id]

    	# add triples to the graph
    	if piece != matchPiece and row[1] > 0.6:
	    	g.add((piece, SKOS.closeMatch, matchPiece))

print g.serialize(format='nt')