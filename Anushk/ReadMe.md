## Query Embeddings
To use the query_encoder.py script:

  ```
    from query_encoder.py import DistilBertQueryEncoder

    encoder = DistilBertQueryEncoder(embed_dim=128)

    # this is what you'd get after speech-to-text
    sample_queries = [
        "Play me some upbeat rock music",
        "I want chill acoustic vibes from the 90s",
        "Suggest me some classical piano songs"
    ]

    # Forward pass
    with torch.no_grad():  # We don't need gradients in this test
        embeddings = encoder(sample_queries)

    print("Embeddings shape:", embeddings.shape)
    print("First embedding:", embeddings[0])
  ```
