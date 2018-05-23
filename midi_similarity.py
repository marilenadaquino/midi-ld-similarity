import rdflib, csv , sys , os , hashlib , midi
from rdflib import Graph, Namespace, RDF, RDFS , XSD , Literal, URIRef
from rdflib.namespace import SKOS
from werkzeug.urls import url_fix

# MD5 to identify the input MIDI file
filename = sys.argv[1]
md5_id = hashlib.md5(open('data/'+filename, 'rb').read()).hexdigest()

# Namespaces
midi = Namespace("http://purl.org/midi-ld/midi#")
m_uri = URIRef(url_fix("http://purl.org/midi-ld/pattern/"))
m = Namespace(m_uri)

piece = m[md5_id]

# initialize rdf graph
g = Graph()
g.bind('midi', midi)

# open match.tsv 
with open('match.tsv','rb') as tsvin:
	tsvin = csv.reader(tsvin, delimiter='\t')
	for row in tsvin:

		# generate MD5 for each MIDI
		matchMIDIname = str('data/'+row[0].strip())
		matchPiece_md5_id = hashlib.md5(open(matchMIDIname, 'rb').read()).hexdigest()
		matchPiece = m[matchPiece_md5_id]

		# add triples to the graph: similarity between input MIDI and each similar MIDI 
		if piece != matchPiece and float(row[1]) >= 0.60000000:
			g.add((piece, SKOS.closeMatch, matchPiece))
			g.add((matchPiece, SKOS.closeMatch, piece))

			# reification and similarity score
			hashMatch = hashlib.md5(piece+matchPiece).hexdigest()
			statementId = URIRef(m+str(hashMatch))
			g.add((statementId, RDF.type, RDF.Statement))
			g.add((statementId, RDF.subject, piece ))
			g.add((statementId, RDF.predicate, RDFS.label))
			g.add((statementId, RDF.object, matchPiece ))
			g.add((statementId, midi.melodyShapeScore, Literal(row[1],datatype=XSD.float)  ))

print g.serialize(format='nt')