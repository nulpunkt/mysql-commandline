clean:
	find . -name "*.pyc" -exec rm {} \;
evn:
	export PYTHONPATH="$PYTHONPATH:$PWD" 
