#!/usr/bin/python3
from stem.control import Controller

#connect to the tor control port

with Controller.from_port(port=9051) as controller:
	controller.authenticate()    #add password

	bytes_read=controller.get_info("traffic/read")
	bytes_written=controller.get_info("traffic/written")
	print(f"My Tor relay has read {bytes_read} bytes and written {bytes_written} bytes.")
