APP_NAME='tranmon-api'
CWD=$(shell pwd)

include ops/common.mk

deps:: common_jq_binary
	virtualenv env
	-mkdir -p ./build/currencies
	-mkdir -p ./build/lib
	./env/bin/pip install -r requirements.txt --target=./build

package:
	cd ./build && zip -r9 ../${APP_NAME}.zip *

release: aws_lambda_deploy

clean::
	-rm ${APP_NAME}.zip
	-rm -rf build

test:
	@echo 'TODO: Actually test something, dude.'

build: clean deps
	cp ./currencies/*.py ./build/currencies/
	cp ./lib/*.py ./build/lib/
	cp ./lib/*.json ./build/lib/
	cp ./*.py ./build/
