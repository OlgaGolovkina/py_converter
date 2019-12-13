import argparse
import json

import requests


def _get_arguments():
    parser = argparse.ArgumentParser(description='Currency converter client')
    parser.add_argument('-t', '--target', choices=("USD", "JPY", "EUR"), help='Target currency', required=True)
    parser.add_argument('-i', '--inputfile', help='Path to input JSON file', required=True)
    parser.add_argument('-o', '--outputfile', help='Path to output JSON file', required=True)
    return parser.parse_args()


def _get_inputdata(arguments):
    with open(arguments.inputfile) as f:
        data = json.load(f)
    return data


def _get_outputdata(arguments, i_data):
    data = []
    for item in i_data:
        url = f"http://127.0.0.1:5000/?from={item['currency']}&to={arguments.target}&amount={item['price']}"
        r = requests.get(url)
        if r.status_code == 200:
            value = float(r.text)
        else:
            value = None
        data.append({'item': item['item'], 'price': value, 'currency': arguments.target})
    return data


def _write_output_file(arguments, o_data):
    with open(args.outputfile, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    args = _get_arguments()
    input_data = _get_inputdata(args)
    output_data = _get_outputdata(args, input_data)
    _write_output_file(args, output_data)

