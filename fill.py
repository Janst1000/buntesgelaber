from transformers import AutoTokenizer, AutoModelForMaskedLM
from transformers import pipeline

tokenizer = AutoTokenizer.from_pretrained("Janst1000/buntesgelaber")

model = AutoModelForMaskedLM.from_pretrained("Janst1000/buntesgelaber")
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--input", type=str, required=True)
parser.add_argument("--tokens", type= int, required=False, default=1)
parser.add_argument("--m", type=bool, required=False, default=False)

def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])

if __name__ == "__main__":
    args = parser.parse_args()
    fill_mask = pipeline(
        "fill-mask",
        model= model,
        tokenizer=tokenizer
    )
    # checking if input has <mask> token
    if "<mask>" not in args.input:
        input = args.input + " <mask>"
    else:
        input = args.input
    if args.tokens == 1:
        try:
            output = fill_mask(input)
        except Exception as e:
            print(e)
            print(type(input))
        if args.m:
            output = flatten(output)[0]
            while "<mask>" in output["sequence"]:
                output = fill_mask(output["sequence"])
                output = flatten(output)[0]
            print(output["sequence"])
        else:
            for item in output:
                print(item["sequence"], item["score"])
    elif args.tokens > 1:
        for i in range(args.tokens):
            output = fill_mask(input)
            input = output[0]["sequence"] + " <mask>"
        print(output[0]["sequence"])
    