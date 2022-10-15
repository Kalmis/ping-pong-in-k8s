echo "Building with tag $1"
docker build -t kalmis-local-registry:2000/log-output:$1 log-output
docker build -t kalmis-local-registry:2000/ping-pong:$1 ping-pong
echo "Pushing with tag $1"
docker push kalmis-local-registry:2000/log-output:$1
docker push kalmis-local-registry:2000/ping-pong:$1
echo "Done with tag $1"
