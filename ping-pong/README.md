# Ping-pong

Implements one endpoint GET `/pingpong` which returns the number of times the endpoint has been called, e.g. `{"pong":39165}`. A new row is inserted into a postgres database for each execution of the endpoint, and then count of rows is returned.