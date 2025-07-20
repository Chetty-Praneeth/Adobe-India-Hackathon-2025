FROM --platform=linux/amd64 python:3.10

WORKDIR /app

COPY heading_classifier.py heading_classifier.py
COPY heading_extractor.py heading_extractor.py
COPY json_writer.py json_writer.py
COPY pdf_loader.py pdf_loader.py
COPY process_pdf.py process_pdf.py
COPY title_detector.py title_detector.py
COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p sample_dataset/pdfs sample_dataset/output

CMD ["python", "process_pdf.py"]
