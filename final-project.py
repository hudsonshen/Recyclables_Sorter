#!/usr/bin/env python3

import argparse
import sys
from jetson_inference import imageNet
from jetson_utils import videoSource, videoOutput, cudaFont, Log

# parse the command line
parser = argparse.ArgumentParser()
parser.add_argument("input", type=str, default="", nargs='?', help="URI of the input stream")
parser.add_argument("output", type=str, default="", nargs='?', help="URI of the output stream")
parser.add_argument("--topK", type=int, default=1, help="show the topK number of class predictions (default: 1)")
args = parser.parse_args()


net = imageNet(model="resnet18.onnx",labels="labels.txt",input_blob="input_0", output_blob="output_0")

# create video sources & outputs
input = videoSource(args.input, argv=sys.argv)
output = videoOutput(args.output, argv=sys.argv)
font = cudaFont()

while True:
    img = input.Capture()

    if img is None:
        continue

    predictions = net.Classify(img, topK=args.topK)

    for n, (ClassID, confidence) in enumerate(predictions):
        classlabel = net.GetClassLabel(ClassID)
        confidence *= 100

        print(f"imagenet:  {confidence:05.2f}% class #{ClassID} ({classlabel})")

        font.OverlayText(img, text=f"{confidence:05.2f}% {classlabel}",
                        x=5, y=5 + n * (font.GetSize() + 5),
                        color=font.White, background=font.Gray40)
    
    output.Render(img)

    output.SetStatus("{:s} | Network {:.0f} FPS".format(net.GetNetworkName(), net.GetNetworkFPS()))

    net.PrintProfilerTimes()

    if not input.IsStreaming() or not output.IsStreaming():
        break


