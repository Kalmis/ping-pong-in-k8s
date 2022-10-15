echo "Building with tag $1"
docker build -t kalmis-local-registry:2000/log-output:$1 log-output
echo "Pushing with tag $1"
docker push kalmis-local-registry:2000/log-output:$1
echo "Done with tag $1"
