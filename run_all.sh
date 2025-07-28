for i in 1 2 3
do
  COLLECTION="Challenge_1b/Collection $i"
  echo "Running for $COLLECTION"
  docker run --rm -v "$PWD/$COLLECTION:/app/$COLLECTION" pdf-outline-1b python Challenge_1b/analyze_collection.py "$COLLECTION"
done
