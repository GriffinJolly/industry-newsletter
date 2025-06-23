# Hybrid Sector Intelligence Newsletter Generator

A modular Python app to generate sector-specific newsletters as PowerPoint presentations, using open-source APIs, local NLP models, and a Streamlit GUI.

## Features
- Sector/region/date selection via Streamlit UI
- Fetches news and filings (GNews, EDGAR, etc.)
- Cleans, parses, and clusters articles locally
- Summarizes and classifies insights (M&A, Innovation, etc.)
- Generates professional PPTX newsletters

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Configure `config.yaml` with API keys and paths
3. Run the app: `streamlit run streamlit_app/app.py`

## Folder Structure
```
newsletter_generator/
│
├── data/
│   ├── raw_articles/
│   ├── processed/
│   └── logos/
│
├── models/
│   ├── summarizer/
│   ├── classifier/
│   └── NER/
│
├── scrapers/
│   ├── news_api_fetcher.py
│   ├── sec_scraper.py
│   └── pdf_downloader.py
│
├── nlp_pipeline/
│   ├── cleaner.py
│   ├── summarizer.py
│   ├── clusterer.py
│   └── insight_extractor.py
│
├── ppt_generator/
│   ├── slide_templates.pptx
│   └── build_ppt.py
│
├── streamlit_app/
│   ├── app.py
│   └── utils.py
│
├── main.py
└── config.yaml
```

## Requirements
Python 3.10+

## License
Open Source, MIT License.
