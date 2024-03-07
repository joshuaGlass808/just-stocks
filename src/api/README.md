API - will be a dedicated API service, that could be consumed by Webby or any other service to get data we are storing.


building app locally by running (from root of repo):
```
make service=api tag=0.0.2 build
```

running app locally by:
```
docker run -p 5000:5000 api:0.0.1 
```

To pull things from ghcr.io:
```
docker login ghcr.io -u $GITHUB_USERNAME -p $GITHUB_TOKEN 
docker pull ghcr.io/joshuaglass808/just-stocks/api:main
docker run -p 5000:5000 ghcr.io/joshuaglass808/just-stocks/api:main
```
