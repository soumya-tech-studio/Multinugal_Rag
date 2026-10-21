from Chunking.Semantic import SemanticChunking
def test_chunk_text():
    chunker = SemanticChunking()

    pages = [
        {
            "metadata": {
                "document_id": "doc1",
                "page_no": 1,
                "language": "en"
            },
            "Content": {
                "text": (
                    "Artificial Intelligence is transforming industries. "
                    "Machine Learning is a branch of Artificial Intelligence. "
                    "Deep Learning is used in computer vision, natural language processing, "
                    "speech recognition, robotics, and many other real-world applications."
                )
            }
        }
    ]
    chunks=chunker.chunk_text(pages)
    

    assert isinstance(chunks, list)
    assert len(chunks) > 0

    first_chunk = chunks[0]

    assert first_chunk.metadata["document_id"] == "doc1"
    assert first_chunk.metadata["page_no"] == 1
    assert first_chunk.metadata["language"] == "en"

    assert isinstance(first_chunk.page_content, str)
    assert len(first_chunk.page_content) > 0
    