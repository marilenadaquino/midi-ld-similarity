
## MIDI LD Similarity matching

* Given an input MIDI file, ``MelodyShape`` algorithm matches similar pieces in the ``data`` folder. 
* Writes file names of similar pieces and related similarity scores in a .tsv file
* Uses MD5 to identify MIDI pieces
* Creates RDF triples about similarity using ``skos:closeMatch`` 
* Reifies statements about similarity to link the similarity score (but discards MIDI whose similarity score is below 0.6)
* Writes triples in a .nt file
* Uploads the triples on MIDI LD Cloud

### Usage

``swmiditp-similarity.sh <midi-file> <named-graph-uri>``