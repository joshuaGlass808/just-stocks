capture service - responsible for  getting and caching results from public API (stock data) to some local db/cache to get pulled quicker. 
This service will be configured to only keep X days amount of data

building app locally by running:
```
cd src/capture
docker image build -t capture:0.0.2 .
```

running app locally by:
```
docker run --rm -p 5000:5000 -v /just-stocks/db:/db -e ALPHAVANTAGE_API_TOKEN=demo --user $(id -u):$(id -g) capture:0.0.2 
```

To pull things from ghcr.io:
```
docker login ghcr.io -u $GITHUB_USERNAME -p $GITHUB_TOKEN 
docker pull ghcr.io/joshuaglass808/just-stocks/capture:main
docker run --rm -p 5000:5000 -v /just-stocks/db:/db -e ALPHAVANTAGE_API_TOKEN=demo --user $(id -u):$(id -g) ghcr.io/joshuaglass808/just-stocks/capture:main
```