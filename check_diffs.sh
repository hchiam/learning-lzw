input_plaintext="example_text.txt"
output_plaintext="example_text_decoded.txt"

if [ ! -f "$output_plaintext" ]; then
    echo "MISSING FILE: $output_plaintext"
    echo "TRY RUNNING PYTHON CODE TO ENCODE AND DECODE."
else
  DIFF=$(diff $input_plaintext $output_plaintext) 
  if [ "$DIFF" != "" ] 
  then
    echo "Difference found! Something went wrong with either encoding or decoding."
  else
    echo "The plaintext input and plaintext output are the same"
  fi
fi
