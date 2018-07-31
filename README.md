# tranmon-api
An API that pulls together various other crypto currency APIs.

## HACKS
Using this branch of the env lib. Should switch back to the "real" one if this ever gets merged:
`pip install git+git://github.com/slavaGanzin/python-dotenv.git@e821e2fee436a9761e985cb15201f96b4441d76a`

# Deployment
tranmon is deployed to AWS Lambda using Zappa.

## Deploy staging
To deploy staging, use `make deploy_staging`,

The staging service is located [here](https://185ebay4e9.execute-api.us-east-1.amazonaws.com/staging/api/v1/currencies/btg/wallet/GadstVMuHyhcw4hpn5z3m9LD7FhefAMunB).


## Deploy production
To deploy production, use `make deploy_production`.

The production service is located [here](https://smsyuwkzfd.execute-api.us-east-1.amazonaws.com/production/api/v1/currencies/btg/wallet/GadstVMuHyhcw4hpn5z3m9LD7FhefAMunB).

# Custom domain
https://stackoverflow.com/questions/47604237/can-i-move-an-aws-lambda-site-to-a-private-domain
