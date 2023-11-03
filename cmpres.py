import gzip

input_file = "input.txt"
output_file = "compressed.gz"

with open(input_file, "rb") as f_in, gzip.open(output_file, "wb") as f_out:
    f_out.writelines(f_in)

print(f"File '{input_file}' has been compressed to '{output_file}'.")
