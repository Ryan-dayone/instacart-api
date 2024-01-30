# Instacart api

instacart-api is a Python library for dealing with token authentication and requests for the instacart advertising api

## Installation

TODO

```bash
pip install git+https://github.com/Ryan-dayone/instacart-api
```

## Usage

```python
from instacart_api import auth
from instacart_api import instacart_reports_api as iapi
import json
from os import environ as env

# application credentials (follow instructions in instacart documentation)
env.__setitem__(key='instacart_client_id', value='Your Client Id')
env.__setitem__(key='instacart_client_secret', value='Your Client Secret')


# use this only once to print the refresh token within 5 mins of authorizing the app. Follow instacart api documentation to get authorization code
auth.get_token(authorization_code='Your App Authorization Code')

# set the refresh token to what was printed above
env.__setitem__(key='instacart_refresh_token', value='Your Client Refresh Token')

# get your access token
auth.refresh_token()
# set start and end date
start_date = '20240-01-01'
end_date = '20240-01-02'

# request daily report
response = iapi.request_report(report_type='product', start_date=start_date, end_date=end_date)
# get the report id from the response
report_id = response['data']['id']
# check to see if the report is generated
if iapi.is_generated(report_id=report_id):
    # download the report as a pandas dataframe
    df = iapi.download_report(report_id=report_id)

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)