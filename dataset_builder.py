import os
from icrawler.builtin import GoogleImageCrawler
from PIL import Image

def scrape_and_clean(query, num_images=20, save_root="data", min_size=(200,200), target_size=(224,224)):
    # 1. Set up directories
    save_dir = os.path.join(save_root, query)
    os.makedirs(save_dir, exist_ok=True)

    # 2. Crawl with icrawler
    crawler = GoogleImageCrawler(
        feeder_threads=1,
        parser_threads=2,
        downloader_threads=4,
        storage={"root_dir": save_dir},
        log_level='INFO'
    )
    crawler.crawl(
        keyword=query,
        max_num=num_images,
        min_size=min_size,        # only download if at least this big
        file_idx_offset=0
    )

    # 3. Clean up: remove any images Pillow can’t open/verify
    for fname in os.listdir(save_dir):
        fpath = os.path.join(save_dir, fname)
        try:
            with Image.open(fpath) as img:
                img.verify()  # will raise if corrupted
                # Optionally also enforce a minimum resolution:
                img = Image.open(fpath)  # reopen for size check
                if img.size[0] < min_size[0] or img.size[1] < min_size[1]:
                    raise ValueError("Too small")
        except Exception as e:
            print(f"Removing bad image {fname}: {e}")
            os.remove(fpath)

    downloaded = len(os.listdir(save_dir))

    print(f"Done. {downloaded}/{num_images} valid images in {save_dir}")
    # 4) Normalize: resize all remaining images to target_size
    for fname in os.listdir(save_dir):
        fpath = os.path.join(save_dir, fname)
        try:
            with Image.open(fpath) as img:
                # Convert to RGB (in case of PNG with alpha, etc.)
                img = img.convert("RGB")
                # Resize—this will ignore aspect ratio and stretch:
                img = img.resize(target_size, Image.LANCZOS)
                img.save(fpath, format="JPEG", quality=90)
        except Exception as e:
            print(f"Failed to resize {fname}: {e}")
            # Optionally remove bad files here

    final_count = len(os.listdir(save_dir))
    print(f"Done. {final_count}/{num_images} images (resized to {target_size}) in {save_dir}")

if __name__ == "__main__":
    scrape_and_clean(
        query="Gyeongbokgung Palace close up",
        num_images=20,
        save_root="data",
        min_size=(200,200),
        target_size=(224,224)
    )
