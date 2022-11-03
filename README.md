# buntesgelaber

This is a natural language processing model trained on german laws taken from the bundestag/gesetze repository.

## Setup

In order to set everything up correctly, you should download the model files from https://huggingface.co/Janst1000/buntesgelaber/tree/main

Make sure to place config.json, pytorch_model.bin and training_args.bin in a subfolder of this directory called buntesgelaber

Place merges.txt and vocab.json in a subfolder called tokenizer

Your file structure should look like this

```
│   .gitignore
│   fill.py
│   README.md
│
├───buntesgelaber
│       config.json
│       pytorch_model.bin
│       training_args.bin
│
└───tokenizer
        merges.txt
        vocab.json
```

Once this is done you will be able to run the fill.py script

It is also recommended to install a conda evironment with all the necessary python modules

```
conda create -n buntesgelaber transformers
```

## How to use it

There are mutiple flags and arguments that can be provided to the script in order to do different things.

However we should first activate our conda environment:

```
conda activate buntesgelaber
```

### Case 1 Tokens provided

In this case we provide some text and how many token we are supposed to generate. Here is an example

```
python3 fill.py --input "Das Gesetz besagt, dass " --tokens 25
```

This is the resulting output:

> Das Gesetz besagt, dass die erforderlichen Unterlagen zur Verfügung zu. Die in § 1 Absatz 1 Satz 1, § 2a Absatz 1aa 1 Satz

Just be aware that this generates a lot of gibberish very fast

### Case 2 Single mask provided (or automatically add one token at the end)

We can also provide a single `<mask>` or have a single mask added at the end of our sequence

```
python3 fill.py --input "Das <mask> Gesetzt besagt, dass"
python3 fill.py --input "Das Gesetz besagt, dass"
```

In this case the 5 best sequences will be output with it's score behind

> Das zuständige Gesetzt besagt, dass 0.027889449149370193
> Das Nähere Gesetzt besagt, dass 0.022903546690940857
> Das folgende Gesetzt besagt, dass 0.012660632841289043
> Das gleiche Gesetzt besagt, dass 0.011971857398748398
> Das oberste Gesetzt besagt, dass 0.00967432465404272

### Case 3 Multiple masks in single line

In this case we can provide a sequence with multiple masks in them. The script will automatically fill in all masks with tokens

```
python3 fill.py --input "Das <mask> Gesetz besagt, dass <mask> nicht <mask> kann" --m True
```

The output will look like this:

> Das folgende Gesetz besagt, dass sie nicht verlangen kann
