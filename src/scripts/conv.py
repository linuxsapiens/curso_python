import json
import xmltodict
import argparse
import os

def json_a_xml(json_data, xml_file):
    # Cargar el JSON
    with open(json_data, 'r') as json_file:
        data = json.load(json_file)
    
    # Convertir a XML
    xml_data = xmltodict.unparse(data, pretty=True)
    
    # Guardar el XML
    with open(xml_file, 'w') as xml_output:
        xml_output.write(xml_data)

def xml_a_json(xml_data, json_file):
    # Cargar el XML
    with open(xml_data, 'r') as xml_file:
        data = xmltodict.parse(xml_file.read())
    
    # Convertir a JSON
    json_data = json.dumps(data, indent=4)
    
    # Guardar el JSON
    with open(json_file, 'w') as json_output:
        json_output.write(json_data)

def main():
    parser = argparse.ArgumentParser(description='Convierte entre archivos JSON y XML.')
    parser.add_argument('input_file', help='Archivo de entrada (JSON o XML)')
    parser.add_argument('output_file', help='Archivo de salida (JSON o XML)')
    args = parser.parse_args()

    input_ext = os.path.splitext(args.input_file)[1].lower()
    output_ext = os.path.splitext(args.output_file)[1].lower()

    if input_ext == '.json' and output_ext == '.xml':
        json_a_xml(args.input_file, args.output_file)
        print(f"Conversión completada: {args.input_file} -> {args.output_file}")
    elif input_ext == '.xml' and output_ext == '.json':
        xml_a_json(args.input_file, args.output_file)
        print(f"Conversión completada: {args.input_file} -> {args.output_file}")
    else:
        print("Error: Los archivos deben ser .json o .xml y la conversión debe ser de JSON a XML o de XML a JSON.")

if __name__ == "__main__":
    main()

'''
pip install xmltodict
python script.py entrada.json salida.xml
python script.py entrada.xml salida.json
'''