run: gui.py database.py
	python main.py


setup:requirements.txt
	pip3 install -r requirements.txt
	sudo apt-get install python-tk