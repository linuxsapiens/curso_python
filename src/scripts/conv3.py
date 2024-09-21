import json
import xmltodict
import csv
import argparse
import os

def json_a_xml(json_data, xml_file):
    with open(json_data, 'r') as json_file:
        data = json.load(json_file)
    xml_data = xmltodict.unparse({'root': data}, pretty=True)
    with open(xml_file, 'w') as xml_output:
        xml_output.write(xml_data)

def xml_a_json(xml_data, json_file):
    with open(xml_data, 'r') as xml_file:
        data = xmltodict.parse(xml_file.read())
    json_data = json.dumps(data, indent=4)
    with open(json_file, 'w') as json_output:
        json_output.write(json_data)

def csv_a_json(csv_data, json_file):
    data = []
    with open(csv_data, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    with open(json_file, 'w') as json_output:
        json.dump(data, json_output, indent=4)

def json_a_csv(json_data, csv_file):
    with open(json_data, 'r') as json_input:
        data = json.load(json_input)
    if data and isinstance(data, list):
        keys = data[0].keys()
        with open(csv_file, 'w', newline='') as csv_output:
            writer = csv.DictWriter(csv_output, fieldnames=keys)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
    else:
        print("Error: El JSON debe contener una lista de objetos.")

def csv_a_xml(csv_data, xml_file):
    data = []
    with open(csv_data, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    xml_data = xmltodict.unparse({'root': {'row': data}}, pretty=True)
    with open(xml_file, 'w') as xml_output:
        xml_output.write(xml_data)

def xml_a_csv(xml_data, csv_file):
    with open(xml_data, 'r') as xml_input:
        data = xmltodict.parse(xml_input.read())
    if 'root' in data and 'row' in data['root']:
        rows = data['root']['row']
        if isinstance(rows, dict):
            rows = [rows]
        keys = rows[0].keys()
        with open(csv_file, 'w', newline='') as csv_output:
            writer = csv.DictWriter(csv_output, fieldnames=keys)
            writer.writeheader()
            for row in rows:
                writer.writerow(row)
    else:
        print("Error: El XML debe tener una estructura root/row.")

def main():
    parser = argparse.ArgumentParser(description='Convierte entre archivos JSON, XML y CSV.')
    parser.add_argument('input_file', help='Archivo de entrada (JSON, XML o CSV)')
    parser.add_argument('output_file', help='Archivo de salida (JSON, XML o CSV)')
    args = parser.parse_args()

    input_ext = os.path.splitext(args.input_file)[1].lower()
    output_ext = os.path.splitext(args.output_file)[1].lower()

    conversions = {
        ('.json', '.xml'): json_a_xml,
        ('.xml', '.json'): xml_a_json,
        ('.csv', '.json'): csv_a_json,
        ('.json', '.csv'): json_a_csv,
        ('.csv', '.xml'): csv_a_xml,
        ('.xml', '.csv'): xml_a_csv
    }

    if (input_ext, output_ext) in conversions:
        conversions[(input_ext, output_ext)](args.input_file, args.output_file)
        print(f"Conversión completada: {args.input_file} -> {args.output_file}")
    else:
        print("Error: Conversión no soportada. Las conversiones válidas son entre JSON, XML y CSV.")

if __name__ == "__main__":
    main()

'''
python script.py entrada.csv salida.json
python script.py entrada.json salida.csv
python script.py entrada.csv salida.xml
python script.py entrada.xml salida.csv
'''