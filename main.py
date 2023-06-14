#install dependency
#pyTorch, transformers, sentencepiece
import os
import tempfile
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import readimage

# Load tokenizer
tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum")

# Load model 
model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")



with tempfile.TemporaryDirectory() as tmp_dir:
    model.save_pretrained(tmp_dir, max_shard_size="200MB")
#    print(sorted(os.listdir(tmp_dir)))

#text = readimage.text

def pegasus_summary(text):
    # Create tokens - number representation of our text
    tokens = tokenizer(text, truncation=True, padding="longest", return_tensors="pt")

    # Summarize 
    summary = model.generate(**tokens)

    # Decode summary
    reut = tokenizer.decode(summary[0])
    return reut
#pegasus_summary(text)