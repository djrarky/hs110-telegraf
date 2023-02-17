# Telegraf Importer for TP Link Smart plugs

For a full compatibility list, see the API maintainers list here: https://github.com/python-kasa/python-kasa#plugs

> This is a first draft

## API Installation

### PIP (pip3 on some distros)
`pip install -r requirements.txt`
 
## Configure

### Telegraf Setup
```
[[inputs.exec]]
  ## Commands array
  commands = ["python3 location/telegraf-tplink-hs110.py plugName1 IPAddress1 plugName2 IPAddress2"]

  ## measurement name suffix (for separating different commands)
  name_suffix = "_mycollector"

  ## Data format to consume.
  data_format = "influx"
