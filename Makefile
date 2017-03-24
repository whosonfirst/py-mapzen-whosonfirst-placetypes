spec:
	utils/mk-spec.py > mapzen/whosonfirst/placetypes/spec.py

install:
	sudo pip install -r requirements.txt .

upgrade:
	sudo pip install --upgrade -r requirements.txt .
