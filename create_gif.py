import  imageio.v3 as iio
from pathlib import Path
import datetime
import re

today=datetime.date.today()

filenames=['naruto1.jpg','naruto2.jpg','naruto3.jpg',
           'naruto4.jpg','naruto5.jpg','naruto6.jpg']

input_dir=Path("images")
output_dir=Path("gif_generate")
output_dir.mkdir(exist_ok=True)

images=[]

for filename in filenames:
    input_path=input_dir/filename
    try:
        images.append(iio.imread(input_path))
    except FileNotFoundError:
        print(f"❌ File not found: {input_path}")
    except Exception as e:
        print(f"⚠️ Error reading {input_path}: {e}")

name_gif=input("Give me the name you want for your gif : ").strip().replace(" ","_")
name_gif=re.sub(r'[\\/:*?"<>|]',"_",name_gif)

if not name_gif:
    name_gif="default_name"

if images:
    output_path=output_dir/"{}_{}.gif".format(name_gif,today)
    iio.imwrite(output_path, images, duration=600, loop=0)
    print(f"✅ GIF generated successfully at: {output_path}")
else:
    print("🚫 No images to process. GIF not created.")
