from rembg import remove

input_path = 'img/input.webp'
output_path = 'img/output.png'

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input_data = i.read()
        output_data = remove(input_data)
        o.write(output_data)

print(f"Background removed from {input_path} and saved as {output_path}")
