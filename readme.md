## MIDI LD Similarity matching

* Given an input MIDI file, ``MelodyShape`` algorithm matches similar pieces in the ``data`` folder. 
* Writes file names of similar pieces and scores in a .tsv file
* Uses MD5 to identify MIDI pieces
* Writes RDF triples in a .nt file
* upload triples on MIDI LD Cloud

### Usage

``swmiditp-similarity.sh <midi-file> <named-graph-uri>``