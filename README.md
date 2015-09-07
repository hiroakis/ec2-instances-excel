# ec2-instances-excel

Output EC2 instances to Excel on all regions.

## Installation

```
git clone git@github.com:hiroakis/ec2-instances-excel.git
cd ec2-instances-excel
pip install -r requirements.txt
```

Note: I did testing only Python 2.7.

## AWS Credentials

Set AWS credential by environment variable or create `~/.boto`.

* environment variable

```
export AWS_ACCESS_KEY_ID=xxxxx
export AWS_SECRET_ACCESS_KEY=xxxxx
```

* ~/.boto

```
[Credentials]
aws_access_key_id=xxxxx
aws_secret_access_key=xxxxx
```

## Usage

```
python ec2_instances_excel.py
```

* option
  - -h: show helps
  - -o: The output excel file. default: ./ec2_instances.xlsx

## Output example

![](output.png?raw=true)

## License

MIT
