#!/usr/bin/python

import boto.ec2
import argparse
import xlsxwriter
import datetime

REGIONS = {"ap-northeast-1":"Tokyo",
            "ap-southeast-1":"Singapore",
            "ap-southeast-2":"Sydney",
            "eu-central-1":"Frankfurt",
            "eu-west-1":"Ireland",
            "sa-east-1":"Sao Paulo",
            "us-east-1":"N.Virginia",
            "us-west-1":"Northern California",
            "us-west-2":"Oregon"}

def get_options():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-o', '--output',
        dest = 'output_file',
        nargs = '?',
        default = './ec2_instances.xlsx',
        required = False,
        type = str,
        help = 'Output file path. default: ec2_instances.xlsx'
    )
    return parser.parse_args()

def format_output_data(instances):
    rows = []
    headers = ["id", "tags.Name", "state", "instance_type", "ip_address", "private_ip_address", \
            "placement", "vpc_id", "subnet_id", "image_id", "monitored", "launch_time", "key_name"]
    rows.append(headers)
    for instance in instances:
        for i in instance.instances:
            row = [i.id, i.tags["Name"], i.state, i.instance_type, i.ip_address, i.private_ip_address, \
                    i.placement, i.vpc_id, i.subnet_id, i.image_id, i.monitored, i.launch_time, i.key_name]
        rows.append(row)
    return rows

def write_excel(sheet, data):
    sheet.set_column(0, len(data[0]), 23.0)
    sheet.write(0, 0, "Last updated: ")
    sheet.write(1, 0, "The number of instances: ")

    # time
    now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    sheet.write(0, 1, now)
    # total instances
    sheet.write(1, 1, len(data))
    # data
    start_row = 3
    for i, row in enumerate(data):
        for j, val in enumerate(row):
            sheet.write(i+start_row, j, val)

if __name__ == '__main__':
    opts = get_options()
    excel = xlsxwriter.Workbook(opts.output_file)
    
    print("start")
    for region_code, region_name in REGIONS.items():
        print("processing %s region") % region_name
        con = boto.ec2.connect_to_region(region_code)
        instances = con.get_all_instances()
        if len(instances) == 0:
            continue
    
        data = format_output_data(instances)
        sheet = excel.add_worksheet(region_name)
        write_excel(sheet, data)
    
    excel.close()
    print("finish")
