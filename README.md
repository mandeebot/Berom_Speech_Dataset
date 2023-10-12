# Berom_Speech_Dataset
this repo is a work in progress and contains Berom Speech data for ML Speech Applications


## Downloading

Go to your terminal and enter;

```git
git clone https://github.com/mandeebot/Berom_Speech_Data.git
```

This adds a folder called "Berom_Speech_Data" which contains the files to your local directory.

## Statistics

- 212 recordings of an average of 20 word length per recording
- total recording hours

## Data Collection
Recording and text Data were collected from a single Berom Male speaker via WhatsApp, hopefully, this is a baseline for berom speech data and as the project grows, 
the [Lig-Aikuma](https://lig-aikuma.imag.fr/tutorial/) Android app will be used in crowd-sourcing for more Berom Data. It is an easy-to-use app with a good interface for recording and elicitation. It offers 6 modes of usage;

- Recording
- Respeaking
- Translating
- Elicitation
- Check
- Share


## Data Preprocessing

Preprocessing involved;

- validating data for errors and removing corrupt files

One main dataset directory with subdirectories;

- `wav` contains the unprocessed recorded files and metadata
- 



## Application

The dataset can be used majorly for low-resource speech model experiments or for cross-lingual ASR.

## Problems Encountered
-Berom is a low resource language, meaning there is a very very low amount of resources online to supplement this, actively working towards generating more Berom speech data to add to this repo
- so far the text transcriptions collected **D0 NOT** have their  tonal descriptions represented(diacritcs), this sets this dataset at some disadvantage, as it is very common in the Berom Language to have one word with different meanings, the different meanings of such a word is often indicated by the tone present in the word. Working towards updating this repo with data that have their tonal descriptions represented
- Recording speech takes time and can become uninteresting to perform quickly.

## Contributing

If you would like to contribute to this project by recording more audio files and transcriptions, You can make a pull request and I will be happy to add you to the project.

## Original Author

[Mandieng Bot](https://www.linkedin.com/in/mandiengbot/)

## License
