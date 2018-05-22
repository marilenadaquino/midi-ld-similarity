# swmiditp-similarity.sh
name=$1

if [ $# -lt 2 ]
	  then
	    echo "Usage: swmiditp-similarity.sh <midi-file> <named-graph-uri>"
	    exit 0
	fi

# print bash results in csv :  TODO change data/0A2A.mid with a parameter (the midi file produced by the user)
java -jar melodyshape-1.4.jar -q data/$1 -c data/ -a 2015-shapeh -k 10 | paste -s -d '\n' - > match.tsv

# call a python script to convert to rdf 
python midi_similarity.py $1 > match.nt

# curl send the .nt file to MIDI LOD Cloud
curl -s -o /dev/null -X POST -H'Content-Type: application/sparql-update' -d"INSERT DATA { GRAPH <http://virtuoso-midi.amp.ops.labs.vu.nl/none> { $(cat match.nt) } }" $2