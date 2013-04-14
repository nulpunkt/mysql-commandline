clean:
	find . -name "*.pyc" -exec rm {} \;
env:
	export PYTHONPATH="$PYTHONPATH:$PWD" 
