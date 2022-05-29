test:
	pytest tests -s

create-dirs:
	mkdir LOGS
	mkdir FILES

clear-logs:
	rm LOGS/*
