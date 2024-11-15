"""
This script trains a YOLO model on a custom dataset using the Ultralytics YOLO library.

Functions:
    parse_args(): Parses command-line arguments for training configuration.

Command-line Arguments:
    --model (str): Name or path of the YOLO model. Default is "yolo11n.pt".
    --data (str): Path to the dataset's YAML configuration file. Default is "eggs-dataset/data.yaml".
    --epochs (int): Number of training epochs. Default is 100.
    --imgsz (int): Image size for training. Default is 640.
    --device (str): Device to use for training: 'cpu', 'cuda', 'mps', or 'auto'. Default is 'auto'.
    --batch_size (int): Batch size for training. Default is 8.
    --cache (bool): Whether to cache images for faster training. Default is True.

Usage:
    Run the script from the command line with the desired arguments to start training the YOLO model.
    python3 train.py --model yolo11n.pt --data eggs-dataset/data.yaml --epochs 100 --imgsz 640 --device cpu --batch_size 8 --cache True
"""
import argparse
from ultralytics import YOLO  # Import YOLO for model training
from os.path import *  # Import path utilities

# Parse command-line arguments
def parse_args():
    parser = argparse.ArgumentParser(description="Train a YOLO model on a custom dataset.")
    parser.add_argument('--model', type=str, default="yolo11n.pt", help="Name or path of the YOLO model.")
    parser.add_argument('--data', type=str, default="./src/eggs-dataset/data.yaml", help="Path to the dataset's YAML configuration file.")
    parser.add_argument('--epochs', type=int, default=2, help="Number of training epochs.")
    parser.add_argument('--imgsz', type=int, default=640, help="Image size for training.")
    parser.add_argument('--device', type=str, default='cpu', help="Device to use: 'cpu', 'cuda', 'mps'.")
    parser.add_argument('--batch_size', type=int, default=8, help="Batch size for training.")
    parser.add_argument('--cache', type=bool, default=True, help="Whether to cache images for faster training.")
    return parser.parse_args()

# Main function
if __name__ == "__main__":
    # Collect arguments
    args = parse_args()

    # Print the parsed arguments for verification
    print("Training configuration:")
    print(f"  Model: {args.model}")
    print(f"  Data YAML: {args.data}")
    print(f"  Epochs: {args.epochs}")
    print(f"  Image Size: {args.imgsz}")
    print(f"  Device: {args.device}")
    print(f"  Batch Size: {args.batch_size}")
    print(f"  Cache Images: {args.cache}")

    # Load the YOLO model
    model = YOLO(args.model)  # Load the specified model (pretrained recommended for training)

    # Train the model with the parsed parameters
    data = abspath(args.data)  # Get the absolute path to the dataset YAML file
    results = model.train(
        data=data,
        epochs=args.epochs,
        imgsz=args.imgsz,
        device=args.device,
        batch=args.batch_size,
        cache=args.cache
    )

    # Print training results summary
    print("Training completed!")
