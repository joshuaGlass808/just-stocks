# just-stocks
Exploring stock data with free api - doing some POC exploratory stuff.

> The point of this repo is just to have fun building things. Ill try to update the readme as I go along to keep instructions on how to build / run things on your own. At some point parts may require you to pay for a cloud provider account, unless its built via KIND. - Which is possible - not sure that my current computer would hang though :).
>
>If you'd like to contribute - go ahead, I would recommend you'd reach out to me though to discuss any planning.
>
>Thanks.

building app locally by running:
```
cd src/capture
docker image build -t capture:0.0.1 .
```

running app locally by:
```
docker run --rm -it -e ALPHAVANTAGE_API_TOKEN=demo capture:0.0.1 
```

To pull things from ghcr.io:
```
docker login ghcr.io -u $GITHUB_USERNAME -p $GITHUB_TOKEN 
docker pull ghcr.io/joshuaglass808/just-stocks/capture:main
docker run -it -e ALPHAVANTAGE_API_TOKEN=demo ghcr.io/joshuaglass808/just-stocks/capture:main
```

I was plotting graphs with matplotlib, but I am going to explore rendering a small local webpage with the data.

Once I start getting a bit more serious the above wont matter and the below will be more of the path to follow:

Im thinking for fun that I should make it a micro-service based system.

1) A service can be used to capture a list of stocks periodically and then storing the data into a DB (probably sqlite for now since its free/light weight) and make sure we can use different DB - dealers choice. (docker container)

2) A service that just acts as an API server listening for requests on which stock(s) a user wants to see thats only reading from the DB. (docker container)

3) A frontend website (docker container)

4) add a section in this repo for spinning up a simple k8s cluster with TF in either Linode or GCP. (make sure to git-ignore any config/cred files)

5) github actions to "publish" docker images so they can be consumed.

6) add a section in this repo for k8s manifest that will use the docker images.
