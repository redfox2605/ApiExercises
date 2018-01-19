loadtest:
	time xargs -n 4 curl -s  < queries.txt > /dev/null
test:
	python -m doctest -v app.py DB.py
run:
	./app.py
