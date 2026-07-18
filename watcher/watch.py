import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from Ingestion_pipeline.pipeline import IngestionPipeline 
class PDFHANBLER(FileSystemEventHandler):
    def on_created(self,event):
        print("New File Detected:")
        pipeline=IngestionPipeline()
        with open(event.src_path,"rb") as file:
            pipeline.ingest(file)
            
        

folder="uploads"
observer=Observer()
observer.schedule(
      PDFHANBLER(),
      folder,
    
    
    recursive=False
)
observer.start()
print("Watching uploads folder...")
try:
  while True:
    time.sleep(1)
except KeyboardInterrupt: 
    observer.stop()
observer.join()

