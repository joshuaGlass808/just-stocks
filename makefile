build:
	echo "Building $(service):$(tag)"
	docker image build -t $(service):$(tag) -f src/$(service)/dockerfile src/
