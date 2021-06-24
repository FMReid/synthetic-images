# Changes:

create.py:

Change for .png alpha-layer mask in line 150:"bkg_w_obj.paste(new_obj, (x, y), new_obj)" takes mask argument as 3rd positional argument in PIL.Image.paste() allowing transparent background from object.

Change for bounding box: line 157: "ann = [{'coordinates': {'h': h, 'w': w, 'x': x + (0.0), 'y': y + (0.0)},"

Thus x&y are no longer adjusted from centroid but from lower bounds.

JSON Convert.py:

A script that allows you to convert the output from create.py (by default called annotations.json) into structured data (.csv file) which is easier to work with.

# Creating Synthetic Image Datasets
This tool helps create synthetic data for object detection modeling. Given
a folder of background images and object images, this tool iterates through each
background and superimposes objects within the frame in random locations,
automatically annotating as it goes. The tool also resizes the icons to help the
model generalize better to the real world.

## Setup
Clone this repo. Then create and activate the conda environment provided:
```bash
$ conda env create -f environment.yml
$ conda activate images
```

Place background images in the `Backgrounds/` subfolder and objects in
the `Objects/` subfolder.

## Create
Run the `create.py` script to generate hundreds/thousands of synthetic training
images for object detection models.

```bash
$ python create.py
```

Output images will be placed in the `TrainingData/` subfolder once done.

### Args
These are the available entrypoint arguments that you can supply at runtime. More will be added in the future.

- `--backgrounds`: Path to folder of background images.
- `--objects`    : Path to folder of object images.
- `--output`     : Path to folder of output images.
- `--groups`     : Whether or not to place groups of objects together.
- `--annotate`   : Whether or not to create and save annotations for the new images.
- `--sframe`     : Whether or not to create a Turi Create SFrame for modeling.
- `--mutate`    : Perform mutatuons to objects (rotation, brightness, shapness, contrast)
