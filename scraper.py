from bing_image_downloader import downloader  

downloader.download(
    'orang pakai jam tangan', 
    limit=50, 
    output_dir='D:/fashion-object-detection/images',  # Use forward slashes
    adult_filter_off=True
)