#!/bin/bash
set -e

# Get model path from arguments
if [ "$#" -le 3 ]; then
    echo "Usage: $0 <model_path> <img_size> <classes>"
    exit 1
fi

model_path=$(realpath "$1")
img_size="$2"
classes="${@:3}"
echo "Model path: $model_path"
echo "Image size: $img_size"
echo "Classes: $classes"

# convert to ONNX
bash src/ultralytics-to-onnx/ultralytics-to-onnx.sh "$model_path" "$img_size" "$classes"

echo "ONNX conversion successful"
echo "ONNX file can be found in: $(dirname $model_path)"