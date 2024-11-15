set -e

cd "$(dirname "$0")" || exit

# Read the model_name and img_size from arguments
if [ "$#" -le 2 ]; then
    echo "Usage: $0 <model_name> <img_size> <classes>"
    exit 1
fi

model_name="$1" # exampples: yolov5su, yolov8n, yolov8s, ../custom-model.pt
img_size="$2"   # examples: 320, 416, 512, 608
classes="${@:3}"    # examples: person car truck bus
echo "Model name: $model_name"
echo "Image size: $img_size"
echo "Classes: $classes"

# Remove old onnx files
rm -rf *.onnx

onnx_path=$(realpath $model_name-$img_size.onnx)
complete_onnx_path=$(realpath $model_name-$img_size-complete.onnx)

bash export-to-onnx.sh "$model_name" "$onnx_path" "$img_size"
python3 complete_onnx.py \
    --onnx_path "$onnx_path" \
    --output_onnx_path "$complete_onnx_path" \
    --classes $classes

python3 test_onnx.py "$complete_onnx_path"
