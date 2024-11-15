from os.path import dirname, abspath

from utils import add_pre_post_processing_to_onnx, simplify_onnx

import argparse

HERE = dirname(abspath(__file__))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process ONNX file.')
    parser.add_argument('--onnx_path', type=str, help='Path to the input ONNX file')
    parser.add_argument('--output_onnx_path', type=str, help='Path to the output ONNX file')
    parser.add_argument('--classes', nargs='+', type=str, help='List of class names')

    args = parser.parse_args()

    onnx_path = args.onnx_path
    output_onnx_path = args.output_onnx_path
    classes = args.classes
    
    add_pre_post_processing_to_onnx(onnx_path, output_onnx_path, classes)
    simplify_onnx(output_onnx_path, output_onnx_path)
