
<h1 align="center">
  <br>
  <img src="readme_images\logo_spectra.png" alt="Spectra logo" width="500">
  <br>
  <br>
</h1>

<h4 align="center">A Python-based graphical interface for analyzing bacterial inhibition and generating customizable graphs.</h4>

<h1 align="center">
  <img src="readme_images\gui_screenshot.png" alt="Spectra GUI screenshot" width="1000">
</h1>

## Overview

This project is part of my undergraduate thesis in Biomedicine, titled *"Comparative Analysis Between the Use of Oxyreductive Dye and Automated Reading in the Determination of the Minimum Inhibitory Concentration in Bacteria of Medial Importance"*. It is a Python-based graphical user interface (GUI) designed to optimize experiments aimed at determining the percentage of bacterial inhibition and the Minimum Inhibitory Concentration (MIC) in 96-well microplate experiments. The data obtained is represented through customizable graphs, which can be saved in various formats. This project builds upon the findings of a previously published article, **"[Comparative Analysis Between the Use of Oxidoreductant Revealers and Automated Reading in Determining the Minimum Inhibitory Concentration in Medically Important Bacteria](https://doi.org/10.46311/2318-0579.60.eUJ4398)"**  

## Features

### Key Features:
- **Bacterial Inhibition Calculation**: Automatically calculates the percentage of bacterial inhibition based on absorbance values.
- **Customizable Graphs**: Generates graphs that can be personalized (colors, titles, axes, etc.).
- **File Export**: Allows saving graphs in formats such as `.jpg`, `.png`, `.pdf`, and `.svg`, and exporting data as `.csv`.
- **Interactive Table**: Allows easy input of absorbance values.
- **Dynamic Graph Generation**: Graphs are generated dynamically based on input data.
- **Data Processing**: Handles absorbance data and calculates inhibition percentages.
- **Graph Customization**: Supports customization of graph elements (e.g., colors, titles, axes).

## How to Use?

This project was designed based on experiments conducted with *Staphylococcus aureus* and *Escherichia coli*, where each dye occupies two rows (duplicates), and the positive and negative controls occupy the last two columns of the microplate. However, it is possible to configure the position of the controls, the bacteria used, and the antibiotic concentration corresponding to the experiment. The microplate line-up used in the experiments can be found in the mentioned article.

### Steps:
1. **Select the Bacteria**: Choose the bacteria used in the experiment from the options provided.
2. **Input Absorbance Values**: Enter the absorbance values into the table provided in the interface. (You don’t need to fill the entire table if the experiment used fewer dyes and duplicates.)
3. **Select Duplicates**: For each duplicate, select the two rows and press the button corresponding to the dye used in the duplicate.
4. **Generate Graph**: After completing the input, click "Generate Graph." The corresponding graph will automatically appear in the "Graph" tab. The graph can be customized (colors, titles, axes) and saved.

## Setup

To run the application locally, you'll need [Git](https://git-scm.com) and [Python](https://www.python.org/downloads/) installed.

```bash
# Clone this repository
$ git clone https://github.com/luizreinert/Spectra

# Install dependencies
$ pip install -r requirements.txt

# Run the application
$ python Spectra.py
```

## Tech Stack

- [Python](https://www.python.org/): Main programming language.
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter): For building the graphical user interface.
- [Matplotlib](https://matplotlib.org/): For generating and customizing graphs.
- [Pillow](https://python-pillow.org/): For image processing.
- [TkSheet](https://github.com/ragardner/tksheet): For handling table data.
- [mplcursors](https://github.com/anntzer/mplcursors): For interactive graph annotations.
- [CTkColorPicker](https://github.com/Akascape/CTkColorPicker): For color customization in the GUI.

## License

This project is licensed under the MIT License.

---
<p align='center'>
  <span>Made with 💙 by <a href='https://github.com/luizreinert'>Luiz Reinert</a></span>
</p>


